# -*- coding: utf-8 -*-
"""Covid19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ddVrGcICzv3_O7M_deAdZg0lNgKN9oUf
"""

import requests       #requesting API to send covid data       # importing request & Json libraries
import json           #importing data in json format

response = requests.get('https://api.covid19india.org/state_district_wise.json')        #received data is stored in response

print(response_API.status_code)

data = response.text        #received data being converted in text format and stored in data

parsed = json.loads(data)

print(json.dumps(parsed, indent=4))

parse_json = json.loads(data)       #loading the text data

active_case = parse_json['Delhi']['districtData']['North East Delhi']['active']        #passing the location and checking active cases in a location

print("Active cases in North East Delhi:", active_case)        #printing the active cases

