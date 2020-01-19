team_list = \
    {
        0:
        {
            'title': 'Team0_abc',  # ae
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:()',  # container
            'labels': '<labels>'  # labels
        },
        1:
        {
            'title': 'TDS_monitoring_for_drinking_water',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(TDS_Sensor)',  # container
            'labels': '<labels>'  # labels
        },
        2:
        {
            'title': 'Water_flow_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Water_flow_sensor)',  # container
            'labels': '<labels>'  # labels
        },
        3:
        {
            'title': 'Ambient_classroom_Small_class',
            'num_of_nodes': '10',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'node_7', 'node_8', 'node_9', 'node_10'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Temp, Humidity, Air Pressure,Light,Sound),\
								 node_2:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_3:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_4:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_5:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_6:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_7:(Temp, Humidity, Air Pressure,Light,Sound),\
							     node_8:(Temp, Humidity, Air Pressure,Light,Sound),\
								 node_9:(Temp, Humidity, Air Pressure,Light,Sound, CO2),\
								 node_10:(Temp, Humidity, Air Pressure,Light,Sound, CO2)',  # container
            'labels': '<labels>'  # labels
        },
        4:
        {
            'title': 'Water_Level_Monitoring_in_Overhead_Tanks',  # ae
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            # container
            'node_description': 'node_1:(photo_electric_fluid_level)',
            'labels': '<labels>,water'  # labels
        },
        5:
        {
            'title': 'Audio_volume_control_based_on_distance_of_students',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            # container
            'node_description': 'node_1:(ultrasonic_sensor)',
            'labels': '<labels>,audio,indoor,classroom'  # labels
        },
        6:
        {
            'title': 'Outdoor_air_pollution_mobile',
            'num_of_nodes': '2',  # container
            'nodes': ['node_1', 'node_2'],  # container
            'project_description': 'abc',  # container
            # container
            'node_description': 'node_1:(turbidity,photo_electric_fluid_level),\
								 node_2:(turbidity,photo_electric_fluid_level)',
            'labels': '<labels>'  # labels
        },
        7:
        {
            'title': 'Turbidity_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(turbidity)',  # container
            'labels': '<labels>,water,turbidity'  # labels
        },
        8:
        {
            'title': 'IOT_Wireless_Control',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(distance, temperature, speed)',  # container
            'labels': '<labels>'  # labels
        },
        9:
        {
            'title': 'Pumps_performance_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['pr_4_esp32_1'],  # container
                                        'project_description': 'abc',  # container
                                        'node_description': 'pr_4_esp32_1:(oe_1_temperature, oe_1_rh, #Sensor - Outdoor Env\
															em_1_watts_total, #Sensor - Energy Meter 1\
															em_1_watts_r_phase,\
															em_1_watts_y_phase,\
															em_1_watts_b_phase,\
															em_1_var_total,\
															em_1_var_r_phase,\
															em_1_var_y_phase,\
															em_1_var_b_phase,\
															em_1_pf_avg,\
															em_1_pf_r_phase,\
															em_1_pf_y_phase,\
															em_1_pf_b_phase,\
															em_1_va_total,\
															em_1_va_r_phase,\
															em_1_va_y_phase,\
															em_1_va_b_phase,\
															em_1_vll_avg,\
															em_1_v_ry_phase,\
															em_1_v_yb_phase,\
															em_1_v_br_phase,\
															em_1_vln_avg,\
															em_1_v_r_phase,\
															em_1_v_y_phase,\
															em_1_v_b_phase,\
															em_1_current_total,\
															em_1_current_r_phase,\
															em_1_current_y_phase,\
															em_1_current_b_phase,\
															em_1_frequency,\
															fm_1_pump_type,#Sensor - Flow Meter 1\
															fm_1_pump_capacity,\
															fm_1_pump_flowrate)',  # container
                                        'labels': '<labels>'  # labels
        },
        10:
        {
            'title': 'Indoor_air_pollution_Mobile',
            'num_of_nodes': '2',  # container
            'nodes': ['node_1', 'node_2'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2),\
							     node_2:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2)',  # container
            'labels': '<labels>,water,turbidity'  # labels
        },
        11:
        {
            'title': 'Outdoor_Air_Pollution_Mobile',
            'num_of_nodes': '2',  # container
            'nodes': ['node_1', 'node_2'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(DHT, Gas, Particulate_Matter),\
								 node_2:(DHT, Gas, Particulate_Matter)',  # container
            'labels': '<labels>'  # labels
        },
        12:
        {
            'title': 'Water_pH_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(pH_sensor)',  # container
            'labels': '<labels>'  # labels
        },
        13:
        {
            'title': 'GPS_base_stations',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1', 'node_2'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(lat,long),node_2:(lat,long)',  # container
            'labels': '<labels>'  # labels
        },
        14:
        {
            'title': 'Indoor_air_pollution_Mess',
            'num_of_nodes': '4',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2),\
								 node_2:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2),\
                        		 node_3:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2),\
  								 node_4:(Multichannel_gas_sensor, SDS011_dust_sensor, DHT22_sensor, Grove_VOC,eCo2)',  # container
            'labels': 'Mess'  # labels
        },
        15:
        {
            'title': 'Hostel_washing_machine_automation',
            'num_of_nodes': '1',  # container
            'nodes': ['pr_3_esp32_1'],  # container
                                        'project_description': 'abc',  # container
                                        'node_description': 'pr_3_esp32_1:(oe_1_temperature, oe_1_rh, #Sensor - Outdoor Env\
															em_1_watts_total, #Sensor - Energy Meter 1\
															em_1_watts_r_phase,\
															em_1_watts_y_phase,\
															em_1_watts_b_phase,\
															em_1_var_total,\
															em_1_var_r_phase,\
															em_1_var_y_phase,\
															em_1_var_b_phase,\
															em_1_pf_avg,\
															em_1_pf_r_phase,\
															em_1_pf_y_phase,\
															em_1_pf_b_phase,\
															em_1_va_total,\
															em_1_va_r_phase,\
															em_1_va_y_phase,\
															em_1_va_b_phase,\
															em_1_vll_avg,\
															em_1_v_ry_phase,\
															em_1_v_yb_phase,\
															em_1_v_br_phase,\
															em_1_vln_avg,\
															em_1_v_r_phase,\
															em_1_v_y_phase,\
															em_1_v_b_phase,\
															em_1_current_total,\
															em_1_current_r_phase,\
															em_1_current_y_phase,\
															em_1_current_b_phase,\
															em_1_frequency,\
															fm_1_pump_type,#Sensor - Flow Meter 1\
															fm_1_pump_capacity,\
															fm_1_pump_flowrate,\
															ss_1_control_signal, #Acutuator - Supply Switch 1\
															ss_1_current_status)',  # container
                                        'labels': '<labels>'  # labels
        },
        16:
        {
            'title': 'IOT_Wireless_Control',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(distance, speed)',  # container
            'labels': '<labels>'  # labels
        },
        17:
        {
            'title': 'Water_Level_Monitoring_in_Overhead_Tanks',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(photo_electric_fluid_level)',  # container
            'labels': '<labels>'  # labels
        },
        18:
        {
            'title': 'Ambient_classroom-1_Large_class',
            'num_of_nodes': '10',  # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'node_7', 'node_8', 'node_9', 'node_10'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Temp, Humidity, Air Pressure, Sound),\
								 node_2:(Temp, Humidity, Air Pressure, Sound),\
								 node_3:(Temp, Humidity, Air Pressure, Sound),\
								 node_4:(Temp, Humidity, Air Pressure, Sound),\
								 node_5:(Temp, Humidity, Air Pressure, Sound),\
								 node_6:(Temp, Humidity, Air Pressure, Sound),\
								 node_7:(Temp, Humidity, Air Pressure, Sound),\
								 node_8:(Temp, Humidity, Air Pressure, Light, CO2),\
								 node_9:(Temp, Humidity, Air Pressure, Light, CO2),\
								 node_10:(Temp, Humidity, Air Pressure, Light, CO2)',  # container
            'labels': '<labels>'  # labels
        },
        19:
        {
            'title': 'Lighting_dim_control_based_on_speaker_presentation',
            'num_of_nodes': '4',  # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(LDR)',  # container
            'labels': '<labels>'  # labels
        },
        20:
        {
            'title': 'Outdoor_air_pollution_2',
            'num_of_nodes': '4',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:([DHT_temp,dht_humdity], [SDS_Pm_2p5,SDS_Pm_2p10], [grove_multichanel]),\
								 node_2:(),\
								 node_3:(),\
								 node_4:()',  # container
            'labels': '<labels>'  # labels
        },
        21:
        {
            'title': 'Sensing_soil_moisture_changes_with_garden_watering',
            'num_of_nodes': '4',  # container
            'nodes': ['node_1,node_2,node_3,node_4'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(moisture_sensor),\
							     node_2:(moisture_sensor),\
								 node_3:(moisture_sensor),\
								 node_4:(moisture_sensor)',  # container
            'labels': '<labels>'  # labels
        },
        22:
        {
            'title': 'Water_Level_Monitoring_in_Overhead_Tanks',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(photo_electric_fluid_level)',  # container
            'labels': '<labels>'  # labels
        },
        23:
        {
            'title': 'Leakage_detection_and_Water_Flow_Meter',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Water_flow_sensor_1, Water_flow_sensor_2)',  # container
            'labels': '<labels>'  # labels
        },
        24:
        {
            'title': 'Audio_volume_control_based_on_distance_of_students',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(HCSR04)',  # container
            'labels': '<labels>'  # labels
        },
        25:
        {
            'title': 'Lighting_dim_control_based_on_speaker_presentation',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(HCSR04)',  # container
            'labels': '<labels>,indoor,classroom'  # labels
        },
        26:
        {
            'title': 'Indoor-air_pollution-3_Washrooms',
            'num_of_nodes': '1',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(gas_sensor,dust_sensor,dht_temperature,dht_humidity,grove_eco2,grove_voc),\
							     node_2:(gas_sensor,dust_sensor,dht_temperature,dht_humidity,grove_eco2,grove_voc),\
						    	 node_3:(gas_sensor,dust_sensor,dht_temperature,dht_humidity,grove_eco2,grove_voc),\
							  	 node_4:(gas_sensor,dust_sensor,dht_temperature,dht_humidity,grove_eco2,grove_voc)',  # container
            'labels': '<labels>,water'  # labels
        },
        27:
        {
            'title': 'Water_flow_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Water Flow Sensor)',  # container
            'labels': '<labels>'  # labels
        },
        28:
        {
            'title': 'Abnormal_activity_detection_outside_classroom',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(acoustic_sensor)',  # container
            'labels': '<labels>,water'  # labels
        },
        29:
        {
            'title': 'classroom_lighting_and_AC_control_based_on_presence',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(ir_sensor)',  # container
            'labels': '<labels>,water'  # labels
        },
        30:
        {
            'title': 'classroom_lighting_and_AC_control_based_on_presence',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(ir_sensor)',  # container
            'labels': '<labels>,water'  # labels
        },
        31:
        {
            'title': 'Street_lighting_And_building_entrances_based_on_daylight',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(LDR)',  # container
            'labels': '<labels>'  # labels
        },
        32:
        {
            'title': 'Campus_energy_and_demand_dashboard',
            'num_of_nodes': '1',  # container
            'nodes': ['pr_1_esp32_1'],  # container
            'project_description': 'Campus energy and demand management',  # container
            'node_description': 'pr_1_esp32_1:(oe_1_temperature, oe_1_rh, #Sensor - Outdoor Env\
															em_1_watts_total, #Sensor - Energy Meter 1\
															em_1_watts_r_phase,\
															em_1_watts_y_phase,\
															em_1_watts_b_phase,\
															em_1_var_total,\
															em_1_var_r_phase,\
															em_1_var_y_phase,\
															em_1_var_b_phase,\
															em_1_pf_avg,\
															em_1_pf_r_phase,\
															em_1_pf_y_phase,\
															em_1_pf_b_phase,\
															em_1_va_total,\
															em_1_va_r_phase,\
															em_1_va_y_phase,\
															em_1_va_b_phase,\
															em_1_vll_avg,\
															em_1_v_ry_phase,\
															em_1_v_yb_phase,\
															em_1_v_br_phase,\
															em_1_vln_avg,\
															em_1_v_r_phase,\
															em_1_v_y_phase,\
															em_1_v_b_phase,\
															em_1_current_total,\
															em_1_current_r_phase,\
															em_1_current_y_phase,\
															em_1_current_b_phase,\
															em_1_frequency)',  # container
            'labels': '<labels>'  # labels
        },
        33:
        {
            'title': 'Indoor-air_pollution-3_Houses',
            'num_of_nodes': '4',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(gas,dust,dht_temperature,dht_humdity,grove_eco2,grove_voc),\
								 node_2:(gas,dust,dht_temperature,dht_humdity,grove_eco2,grove_voc),\
								 node_3:(gas,dust,dht_temperature,dht_humdity,grove_eco2,grove_voc),\
								 node_4:(gas,dust,dht_temperature,dht_humdity,grove_eco2,grove_voc)',  # container
            'labels': '<labels>,water'  # labels
        },
        34:
        {
            'title': 'Abnormal_activity_detection_outside_of_classroom',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(acoustic_sensor)',  # container
            'labels': '<labels>,water'  # labels
        },
        35:
        {
            'title': 'Street_lighting_And_building_entrances_based_on_daylight',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(LDR)',  # container
            'labels': '<labels>'  # labels
        },
        36:
        {
            'title': 'TDS_monitering_for_drinking_water',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(TDS_Sensor)',  # container
            'labels': '<labels>'  # labels
        },
        37:
        {
            'title': 'Soil_Moisture_Sensing',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(moisture)',  # container
            'labels': '<labels>'  # labels
        },
        38:
        {
            'title': 'Sound_Noise_around_the_campus',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(sound_level)',  # container
            'labels': '<labels>'  # labels
        },
        39:
        {
            'title': 'Outdoor_Air_Pollution',
            'num_of_nodes': '4',  # container
            # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4'],
            'project_description': 'abc',  # container
            # container
            'node_description': 'node_1:(multichannel_gas_sensor,dust_sensor,dht_temperature,dht_humidity,GPS),\
								 node_2:(multichannel_gas_sensor,dust_sensor,dht_temperature.dht_humidity,GPS),\
								 node_3:(multichannel_gas_sensor,dust_sensor,dht_temperature,dht_humidity,GPS),\
								 node_4:(multichannel_gas_sensor,dust_sensor,dht_temperature,dht_humidity,GPS)',
            'labels': '<labels>,water'  # labels
        },
        40:
        {
            'title': 'DG_performance_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['pr_2_esp32_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'pr_2_esp32_1:(oe_1_temperature, oe_1_rh, #Sensor - Outdoor Nnv\
															em_1_watts_total, #Sensor - Energy Meter 1\
															em_1_watts_r_phase,\
															em_1_watts_y_phase,\
															em_1_watts_b_phase,\
															em_1_var_total,\
															em_1_var_r_phase,\
															em_1_var_y_phase,\
															em_1_var_b_phase,\
															em_1_pf_avg,\
															em_1_pf_r_phase,\
															em_1_pf_y_phase,\
															em_1_pf_b_phase,\
															em_1_va_total,\
															em_1_va_r_phase,\
															em_1_va_y_phase,\
															em_1_va_b_phase,\
															em_1_vll_avg,\
															em_1_v_ry_phase,\
															em_1_v_yb_phase,\
															em_1_v_br_phase,\
															em_1_vln_avg,\
															em_1_v_r_phase,\
															em_1_v_y_phase,\
															em_1_v_b_phase,\
															em_1_current_total,\
															em_1_current_r_phase,\
															em_1_current_y_phase,\
															em_1_current_b_phase,\
															em_1_frequency,\
															fg_1_fuel_type,#Sensor Fuel Guage\
															fg_1_fuel_capacity,\
															fg_1_fuel_current_level)',  # container
            'labels': '<labels>'  # labels
        },
        41:
        {
            'title': 'Street_lightning_based_on_daylight',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            # container
            'node_description': 'node_1:(LDR, proximity_1,proximity_2,proximity_3,proximity_4)',
            'labels': '<labels>'  # labels
        },
        42:
        {
            'title': 'Ambient_classroom-2_Large_class',
            'num_of_nodes': '10',  # container
            'nodes': ['node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'node_7', 'node_8', 'node_9', 'node_10'],
            'project_description': 'abc',  # container
            'node_description': 'node_1:(Temp, Humidity, Air Pressure, Sound),\
								 node_2:(Temp, Humidity, Air Pressure, Sound),\
								 node_3:(Temp, Humidity, Air Pressure, Sound),\
								 node_4:(Temp, Humidity, Air Pressure, Sound),\
								 node_5:(Temp, Humidity, Air Pressure, Sound),\
								 node_6:(Temp, Humidity, Air Pressure, Sound),\
								 node_7:(Temp, Humidity, Air Pressure, Sound),\
								 node_8:(Temp, Humidity, Air Pressure, Light, CO2),\
								 node_9:(Temp, Humidity, Air Pressure, Light, CO2),\
								 node_10:(Temp, Humidity, Air Pressure, Light, CO2)',  # container
            'labels': '<labels>'  # labels
        },
        43:
        {
            'title': 'UPS_performance_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['pr_5_esp32_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'pr_5_esp32_1:(oe_1_temperature, oe_1_rh, #Sensor - Outdoor Env\
															em_1_watts_total, #Sensor - Energy Meter 1\
															em_1_watts_r_phase,\
															em_1_watts_y_phase,\
															em_1_watts_b_phase,\
															em_1_var_total,\
															em_1_var_r_phase,\
															em_1_var_y_phase,\
															em_1_var_b_phase,\
															em_1_pf_avg,\
															em_1_pf_r_phase,\
															em_1_pf_y_phase,\
															em_1_pf_b_phase,\
															em_1_va_total,\
															em_1_va_r_phase,\
															em_1_va_y_phase,\
															em_1_va_b_phase,\
															em_1_vll_avg,\
															em_1_v_ry_phase,\
															em_1_v_yb_phase,\
															em_1_v_br_phase,\
															em_1_vln_avg,\
															em_1_v_r_phase,\
															em_1_v_y_phase,\
															em_1_v_b_phase,\
															em_1_current_total,\
															em_1_current_r_phase,\
															em_1_current_y_phase,\
															em_1_current_b_phase,\
															em_1_frequency,\
															em_2_watts_total, #Sensor - Energy Meter 2\
															em_2_watts_r_phase,\
															em_2_watts_y_phase,\
															em_2_watts_b_phase,\
															em_2_var_total,\
															em_2_var_r_phase,\
															em_2_var_y_phase,\
															em_2_var_b_phase,\
															em_2_pf_avg,\
															em_2_pf_r_phase,\
															em_2_pf_y_phase,\
															em_2_pf_b_phase,\
															em_2_va_total,\
															em_2_va_r_phase,\
															em_2_va_y_phase,\
															em_2_va_b_phase,\
															em_2_vll_avg,\
															em_2_v_ry_phase,\
															em_2_v_yb_phase,\
															em_2_v_br_phase,\
															em_2_vln_avg,\
															em_2_v_r_phase,\
															em_2_v_y_phase,\
															em_2_v_b_phase,\
															em_2_current_total,\
															em_2_current_r_phase,\
															em_2_current_y_phase,\
															em_2_current_b_phase,\
															em_2_frequency)',  # container
            'labels': '<labels>'  # labels
        },
        44:
        {
            'title': 'GPS_base_stations',
            'num_of_nodes': '2',  # container
            'nodes': ['node_1,node_2'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(lat,lon),node_2:(lat,lon)',  # container
            'labels': '<labels>'  # labels
        },
        45:
        {
            'title': 'Outdoor_air_pollution-3',
            'num_of_nodes': '2',  # container
            'nodes': ['node_1', 'node_2'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(multichannel_gas_sensor,dust_sensor,dht_temperature,dht_humidity,GPS), \
								 node_2:(multichannel_gas_sensor,dust_sensor,dht_temperature,dht_humidity,GPS)',  # container
            'labels': '<labels>,water'  # labels
        },
        46:
        {
            'title': 'Water_pH_monitoring',
            'num_of_nodes': '1',  # container
            'nodes': ['node_1'],  # container
            'project_description': 'abc',  # container
            'node_description': 'node_1:(pH Sensor)',  # container
            'labels': '<labels>'  # labels
        }
    }
