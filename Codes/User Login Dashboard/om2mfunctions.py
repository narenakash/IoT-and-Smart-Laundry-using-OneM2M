# coding=utf-8

import requests
import json
import time


# def delete_ae(uri, data_format="json"):
#     """
#         Method description:
#         Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
#         under the specified CSE

#         Parameters:
#         uri_cse : [str] URI of parent CSE
#         ae_name : [str] name of the AE
#         fmt_ex : [str] payload format
#     """
#     headers = {
#         'X-M2M-Origin': 'admin:admin',
#         'Content-type': 'application/{}'.format(data_format)}

#     response = requests.delete(uri, headers=headers)
#     print('Return code : {}'.format(response.status_code))
#     print('Return Content : {}'.format(response.text))
#     return


# def register_ae(uri_cse, ae_name, labels="", fmt_ex="json"):
#     """
#         Method description:
#         Registers an application entity(AE) to the OneM2M framework/tree
#         under the specified CSE

#         Parameters:
#         uri_cse : [str] URI of parent CSE
#         ae_name : [str] name of the AE
#         labels : [str] labels for the AE
#         fmt_ex : [str] payload format
#     """

#     headers = {
#         'X-M2M-Origin': 'admin:admin',
#         'Content-type': 'application/{};ty=2'.format(fmt_ex)}

#     payload = {
#         "m2m:ae": {
#             "rn": "{}".format(ae_name),
#             "api": "tap",
#             "rr": "true",
#             "lbl": labels
#         }
#     }

#     try:
#         response = requests.post(uri_cse, json=payload, headers=headers)
#     except TypeError:
#         response = requests.post(uri_cse, data=json.dumps(payload), headers=headers)

#     print('Return code : {}'.format(response.status_code))
#     print('Return Content : {}'.format(response.text))


# def create_cnt(uri_ae, cnt_name="", fmt_ex="json"):
#     """
#         Method description:
#         Creates a container(CON) in the OneM2M framework/tree
#         under the specified AE

#         Parameters:
#         uri_ae : [str] URI for the parent AE
#         cnt_name : [str] name of the container (DESCRIPTOR/DATA)
#         fmt_ex : [str] payload format
#     """

#     headers = {
#         'X-M2M-Origin': 'admin:admin',
#         'Content-type': 'application/{};ty=3'.format(fmt_ex)}

#     payload = {
#         "m2m:cnt": {
#             "rn": "{}".format(cnt_name),
#             "mni": 200000    
#         }
#     }

#     try:    
#         response = requests.post(uri_ae, json=payload, headers=headers)
#     except TypeError:
#         response = requests.post(uri_ae, data=json.dumps(payload), headers=headers)

#     print('Return code : {}'.format(response.status_code))
#     print('Return Content : {}'.format(response.text))


# def create_descriptor_cin(uri_con, fmt_ex="json"):
#     """
#         Method description:
#         Creates a descriptor content instance(desc_CIN) in the OneM2M framework/tree
#         under the specified DESCRIPTOR CON

#         This holds the detailed description for an specific AE

#         Parameters:
#         uri_con : [str] URI for the parent DESCRIPTOR CON
#         fmt_ex : [str] payload format
#     """

#     headers = {
#         'X-M2M-Origin': 'admin:admin',
#         'Content-type': 'application/{};ty=4'.format(fmt_ex)}

#     data = {
#         "m2m:cin": {
#             "con": {
#                 "obj": {
#                     "str": [{"@name": "type", "@val": "Temperature_Sensor"},
#                             {"@name": "location", "@val": "Home"},
#                             {"@name": "appId", "@val": "DHT"}],
#                     "op": {
#                         "@name": "getValue",
#                         "@href": "/in-cse/in-name/DHT/DATA/la",
#                         "@in": "obix:Nil",
#                         "@out": "obix:Nil",
#                         "@is": "retrieve"
#                     }
#                 }
#             }
#         }
#     }

#     try:
#         response = requests.post(uri_con, json=payload, headers=headers)
#     except TypeError:
#         response = requests.post(uri_con, data=json.dumps(payload), headers=headers)
#     print('Return code : {}'.format(response.status_code))
#     print('Return Content : {}'.format(response.text))


def create_data_cin(uri_cnt, value, fmt_ex="json"):
    """
        Method description:
        Creates a data content instance(data_CIN) in the OneM2M framework/tree
        under the specified DATA CON

        Parameters:
        uri_cnt : [str] URI for the parent DATA CON
        fmt_ex : [str] payload format (json/XML)
    """

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=4'.format(fmt_ex)}

    payload = {
        "m2m:cin": {
            "con": "{}".format(value)
        }
    }

    try:
        response = requests.post(uri_cnt, json=payload, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(payload), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

# ====================================================

# ====================================================


def get_data(uri, format="json"):
    """
        Method description:
        Gets data from the specified container(data_CIN)
        in the OneM2M framework/tree

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json'}

    response = requests.get(uri, headers=headers)
    # print('Return code : {}'.format(response.status_code))
    # print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:cin"]["con"]

# ====================================================


def discovery(uri, format="json"):
    """
        Method description:
        Returns a string of URIs separated by space
        from the OneM2M framework/tree

        Parameters:
        uri : [str] URI for the server appended by filter parameters
        fmt_ex : [str] payload format (json/XML)
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json'}

    response = requests.get(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:uril"]

# ====================================================


def get_filtered_uri(uri, filter=""):
    """
        Method description:
        Splits the string into a list of URIs

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """
    _, filtered_uri = discovery(uri)
    filtered_uri_list = filtered_uri.split(" ")
    print(filtered_uri_list)
    return filtered_uri_list


# def create_group_ae(cse_uri, group_name, uri_list):
#     """
#         Method description:
#         Creates an AE that groups various other specifies AEs in the OneM2M framework/tree
#         under the specified DATA CON

#         Parameters:
#         uri : [str] URI for the parent DATA CON appended by "la" or "ol"
#         fmt_ex : [str] payload format (json/XML)
#     """

#     headers = {
#         'X-M2M-Origin': 'admin:admin',
#         'Content-type': 'application/json;ty=9'
#     }

#     payload = {
#         "m2m:grp":
#             {
#                 "rn": group_name,
#                 "mt": 3,
#                 "mid": uri_list,
#                 "mnm": 10
#             }
#     }

#     try:
#         response = requests.post(uri_cse, json=payload, headers=headers)
#     except TypeError:
#         response = requests.post(uri_cse, data=json.dumps(payload), headers=headers)

#     print('Return code : {}'.format(response.status_code))
#     print('Return Content : {}'.format(response.text))


if __name__ == "__main__":
    # server = "http://192.168.1.233:8080"
    server = "http://127.0.0.1:8080"
    server = "http://139.59.42.21:8080"

    cse = "/~/in-cse/in-name/"
