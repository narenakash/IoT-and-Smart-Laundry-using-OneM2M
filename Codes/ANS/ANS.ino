
//------------------------------------------------------------------------------------
/*
      HOSTEL-WASHING MACHINE MONITORING AND AUTOMATION

*/
//  -----------------------------------------------------------------------------------------------------



#include "WiFi.h"
#include "HTTPClient.h"
#include "ArduinoJson.h"

//  =======================================================================================================
#define RELAY 15


// Initialising string values to 0
String pushCurrent = "0 ";
String pushVoltage = "0 ";
String pushPower = "0 ";
String pushTemp = "0 ";
String pushRH = "0 ";
String pushFlow = "0 ";
String pushEnergy = "0";
String pushTotflow = "0";

//  =======================================================================================================
//  ---------------------------------------------- Energy Meter -------------------------------------------
//  =======================================================================================================

#include <Arduino.h>
#include "esp32ModbusRTU.h"
#include <algorithm>  // for std::reverse

String energyBuff = "NULL-Value";
esp32ModbusRTU modbus(&Serial1, 25);  // use Serial1 and pin 16 as RTS

/*
 *
  SUCCESS                = 0x00,
  ILLEGAL_FUNCTION      = 0x01,
  ILLEGAL_DATA_ADDRESS  = 0x02,
  ILLEGAL_DATA_VALUE    = 0x03,
  SERVER_DEVICE_FAILURE = 0x04,
  ACKNOWLEDGE           = 0x05,
  SERVER_DEVICE_BUSY    = 0x06,
  NEGATIVE_ACKNOWLEDGE  = 0x07,
  MEMORY_PARITY_ERROR   = 0x08,
  TIMEOUT               = 0xE0,
  INVALID_SLAVE         = 0xE1,
  INVALID_FUNCTION      = 0xE2,
  CRC_ERROR             = 0xE3,  // only for Modbus-RTU
  COMM_ERROR            = 0xE4  // general communication error
 */



// This function obtains values from the Energy meter by reading its holding registers through Modbus protocol.
// These are then assigned to separate strings, which will be later pushed into OneM2M.
String energyMeasure() {
    String retstr = "";
    retstr += "Power: ";
    modbus.readHoldingRegisters(0x01, 100, 2);
    delay(3000);
    retstr += energyBuff + "W\n";
    pushPower = energyBuff;
    Serial.println(retstr);

    retstr += "Current: ";
    modbus.readHoldingRegisters(0x01, 148, 2);
    delay(3000);
    retstr += energyBuff + "A\n";
    pushCurrent = energyBuff;
    Serial.println(retstr);

    retstr += "Voltage: ";
    modbus.readHoldingRegisters(0x01, 140, 2);
    delay(3000);
    retstr += energyBuff + "V\n";
    pushVoltage = energyBuff;
    Serial.println(retstr);

    retstr += "Energy: ";
    modbus.readHoldingRegisters(0x01, 158, 2);
    delay(3000);
    retstr += energyBuff + "Wh\n";
    pushEnergy = energyBuff;
    Serial.println(retstr);

    energyBuff = "NULL-Value";
    return retstr;
}

//  -------------------------------------------------------------------------------------------------------
//  =======================================================================================================

//  =======================================================================================================
//  ---------------------------------------------- Temp sensor --------------------------------------------
//  =======================================================================================================
#include <Wire.h>;

// sda 21
// scl 22

#define si7021Addr 0x40
String tempStr;

void tempMeasure()
{
  unsigned int data[2];

  Wire.beginTransmission(si7021Addr);
  //Send humidity measurement command
  Wire.write(0xF5);
  Wire.endTransmission();
  delay(500);

  // Request 2 bytes of data
  Wire.requestFrom(si7021Addr, 2);
  // Read 2 bytes of data to get humidity
  if(Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data
  float humidity  = ((data[0] * 256.0) + data[1]);
  humidity = ((125 * humidity) / 65536.0) - 6;

  Wire.beginTransmission(si7021Addr);
  // Send temperature measurement command
  Wire.write(0xF3);
  Wire.endTransmission();
  delay(500);

  // Request 2 bytes of data
  Wire.requestFrom(si7021Addr, 2);

  // Read 2 bytes of data for temperature
  if(Wire.available() == 2)
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
  }

  // Convert the data
  float temp  = ((data[0] * 256.0) + data[1]);
  float celsTemp = ((175.72 * temp) / 65536.0) - 46.85;
  float fahrTemp = celsTemp * 1.8 + 32;

  tempStr = "Humidity : " + (String)humidity + " % RH" + "\n";
  tempStr += "Celsius : " + (String)celsTemp + " C" + "\n" + "Fahrenheit : " + (String)fahrTemp + " F" + "\n";
  pushRH = (String)humidity;
  pushTemp = (String)celsTemp;
}
//  -------------------------------------------------------------------------------------------------------
//  ========================================================================================================



//  ========================================================================================================
//  ---------------------------------------------- Flow meter ----------------------------------------------
//  ========================================================================================================
#define SENSOR  13

float calibrationFactor = 4.5;
volatile byte pulseCount;
byte pulse1Sec = 0;
float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;

void IRAM_ATTR pulseCounter()
{
  pulseCount++;
}

int flowMeasure()
{
    pulseCount = 0;
    delay(1000);
    flowRate = ( pulse1Sec / calibrationFactor);

    // Divide the flow rate in litres/minute by 60 to determine how many litres have
    // passed through the sensor in this 1 second interval, then multiply by 1000 to
    // convert to millilitres.
    flowMilliLitres = (flowRate / 60) * 1000;

    // Add the millilitres passed in this second to the cumulative total
    totalMilliLitres += flowMilliLitres;

    // Print the flow rate for this second in litres / minute
    Serial.print("Flow rate: ");
    Serial.print(int(flowRate));  // Print the integer part of the variable
    Serial.print("L/min");
    Serial.print("\t");       // Print tab space

    // Print the cumulative total of litres flowed since starting
    Serial.print("Output Liquid Quantity: ");
    Serial.print(totalMilliLitres);
    Serial.print("mL / ");
    Serial.print(totalMilliLitres / 1000);
    Serial.println("L");
//    flowStr = "Flow rate: " + (String)((float)(flowRate)) + "L/min" + "\t";
//    Serial.printf("flow : %.2f\n",pushFlow);
    pushFlow = (String)((float)(flowRate));
    pushTotflow = (String)((float)(totalMilliLitres));
//    flowStr += "Output Liquid Quantity: " + (String)totalMilliLitres + "mL / " + (String)(totalMilliLitres / 1000) + "L" + "\n";
  return 1;
}

//  -------------------------------------------------------------------------------------------------------
//  =======================================================================================================
//-------------------------------------------WiFi and server connections-----------------------------------
//  =======================================================================================================

char* wifi_ssid="esw-m19@iiith";
char* wifi_pwd="e5W-eMai@3!20hOct";

String cse_ip = "onem2m.iiit.ac.in";
String cse_port = "443";

//  =======================================================================================================
//  ---------------------------------------------- One M2M ------------------------------------------------
//  =======================================================================================================

StaticJsonBuffer<200> jsonBuffer;


String server = "http://"+cse_ip+":"+cse_port+"/~/in-cse/in-name/";

String createCI(String server, String ae, String cnt, String val)
{
  HTTPClient http;
  http.begin(server + ae + "/" + cnt + "/");
  http.addHeader("X-M2M-Origin", "admin:admin");
  http.addHeader("Content-Type", "application/json;ty=4");
  http.addHeader("Content-Length", "100");
  http.addHeader("Connection", "close");
  int code = http.POST("{\"m2m:cin\": {\"cnf\": \"text/plain:0\",\"con\": "+ String(val) +"}}");
  http.end();
  Serial.println(code);
  if(code==-1){
    Serial.println("UNABLE TO CONNECT TO THE SERVER");
  }
  delay(300);
}

//This function calls createCI to push data into the container of the onem2m resource tree that is specified
void pushMyData(String pathh, String val){
  val = "\"" + val + "\"";
  pathh = "pr_3_esp32_1/"+pathh;
  createCI(server, "Team15_Hostel_washing_machine_automation", pathh, val);
}


// sendGet() is used for obtaining the value of the latest instance in a container from the OneM2M resource tree.
String sendGET(String url)
{
    StaticJsonBuffer<300> jsonBuffer;
    HTTPClient http;  //Declare an object of class HTTPClient
    http.begin(url);  //Specify request destination
    http.addHeader("X-M2M-Origin", "admin:admin");
    http.addHeader("Content-Type", "application/json");
    int httpCode = http.GET();                                                                  //Send the request
    String payload = "";
    char json[300];
    const char* value = 0;

    if (httpCode > 0)
    {
      payload = http.getString();   //Get the request response payload
      Serial.printf("Payload\n");
      Serial.print(payload);
      payload.toCharArray(json, 300);
      JsonObject& root = jsonBuffer.parseObject(json);
//    Test if parsing /succeeds.
      if (!root.success())
      {
        Serial.println("parseObject() failed");
      }
      const char* state = root["m2m:cin"]["con"];
      Serial.printf("State\n");
      Serial.print(state);
//      Serial.println(value);
      http.end();   //Close connection
      return state;
    }
    http.end();   //Close connection
}



//  -------------------------------------------------------------------------------------------------------
//  =======================================================================================================
//  --------------------------------------------Connecting to WiFi-----------------------------------------
//  =======================================================================================================

void connect_to_WIFI(){
  WiFi.mode(WIFI_STA);// Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.disconnect();
  delay(100);
  WiFi.begin(wifi_ssid, wifi_pwd);
  Serial.println("Connecting to WiFi..");
  while (WiFi.status() != WL_CONNECTED || WiFi.status()==WL_CONNECT_FAILED){
    delay(500);
    Serial.print(".");
  }
  if(WiFi.status()==WL_CONNECTED){
    Serial.println("Connected to the WiFi network");
  }
  else{

  }
  Serial.println("Connected to the WiFi network");
}

void setup()
{
  Serial.begin(115200);
  connect_to_WIFI();

  pinMode(RELAY,OUTPUT);
  digitalWrite(RELAY, HIGH);
  Serial.println("Setup done");

//  ========================================================================================================
//  ---------------------------------------------- Energy Meter --------------------------------------------
//  ========================================================================================================

  Serial1.begin(9600, SERIAL_8E1, 26, 27);  // Modbus connection

  modbus.onData([](uint8_t serverAddress, esp32Modbus::FunctionCode fc, uint8_t* data, size_t length) {
//    Serial.printf("id 0x%02x fc 0x%02x len %u: 0x", serverAddress, fc, length);

    for (size_t i = 0; i < length; ++i) {
      //Serial.printf("%02x", data[i]);
//      Serial.printf("\n/%.2f\n",data[i]);
    }

    uint8_t data2[4];
    data2[0] = data[1];
    data2[1] = data[0];
    data2[2] = data[3];
    data2[3] = data[2];

//    Serial.printf("\nval: %.2f", *reinterpret_cast<float*>(data2));
    energyBuff = (String)(*reinterpret_cast<float*>(data2));
  });
  modbus.onError([](esp32Modbus::Error error) {
    Serial.printf("Got error: 0x%02x\n\n", static_cast<uint8_t>(error));
  });
  modbus.begin();

//  -------------------------------------------------------------------------------------------------------


//  ========================================================================================================
//  ---------------------------------------------- Flow meter ----------------------------------------------
//  ========================================================================================================

  pinMode(SENSOR, INPUT_PULLUP);

  pulseCount = 0;
  flowRate = 0.0;
  flowMilliLitres = 0;
  totalMilliLitres = 0;

  attachInterrupt(digitalPinToInterrupt(SENSOR), pulseCounter, RISING);

//  -------------------------------------------------------------------------------------------------------


//  =======================================================================================================
//  ---------------------------------------------- Temp sensor --------------------------------------------
//  =======================================================================================================
  Wire.begin();
  Wire.beginTransmission(si7021Addr);
  Wire.endTransmission();
  delay(300);
//  -------------------------------------------------------------------------------------------------------
//  =======================================================================================================

}

void loop()
{
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connection lost.. trying to reconnect");
    connect_to_WIFI();
  }

pushCurrent = "NULL-Value";
pushVoltage = "NULL-Value";
pushPower = "NULL-Value";
pushTemp = "NULL-Value";
pushRH = "NULL-Value";
pushFlow = "NULL-Value";
pushTotflow = "NULL-Value";
pushEnergy = "NULL-Value";

tempMeasure();
Serial.println(tempStr);

flowMeasure();

String energyStr = energyMeasure();

Serial.printf("Printing energyStr\n");
Serial.print(energyStr);

Serial.printf("Flowrate: ");
Serial.println(pushFlow);


  //We push the values into oneM2M by keeping a 10-second delay between each parameter. During the time in between, we keep checking
  //the status of the washing machine, as to whether clicked "On" or "Off".


  pushMyData("em/em_1_watts_total", pushPower);
  delay(10000);

  String value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");


  pushMyData("em/em_1_var_total", pushEnergy);
  delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

  pushMyData("fm/fm_1_pump_flowrate", pushFlow);
  delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

  pushMyData("fm/fm_1_pump_capacity",pushTotflow);
  delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

  pushMyData("oe/oe_1_temperature", pushTemp);
  delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

  pushMyData("oe/oe_1_rh", pushRH);
  delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

 pushMyData("em/em_1_vll_avg", pushVoltage);
 delay(10000);

  value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");
  if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");

  pushMyData("em/em_1_current_total", pushCurrent);
  delay(10000);

  Serial.printf("\nPushed\n");


     value = sendGET(server + "Team15_Hostel_washing_machine_automation" + "/pr_3_esp32_1/ss/ss_1_control_signal/la");


    if(value=="1")
    {
      digitalWrite(RELAY, HIGH);
      Serial.printf("\nActuator on\n");
    }
    else if(value=="0")
    {
      digitalWrite(RELAY, LOW);
      Serial.printf("\nActuator off\n");
    }
    else
    {
      Serial.println("Invalid");
    }
     Serial.printf("\nActuator used\n");


  delay(10000); // DO NOT CHANGE THIS LINE 10 sec delay

}
