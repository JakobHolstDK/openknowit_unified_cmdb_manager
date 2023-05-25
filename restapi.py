from flask import Flask, jsonify, request
import requests
import requests

from pymongo import MongoClient
import os

MONGO = os.getenv("MONGO")
DNSTOKEN = os.getenv("DNSTOKEN")


import requests
import json

# NetBox API endpoint URLs

api_url = os.getenv("NETBOX_URL")
devices_url = api_url + 'dcim/devices/'
vm_url = api_url + 'virtualization/virtual-machines/'

token = os.getenv("NETBOXTOKEN")

# Headers containing the API token
headers = {
    'Authorization': 'Token {}'.format(token),
    'Content-Type': 'application/json',
}

# Virtual machine data
vm_data = {
    'name': 'MyVM',
    'status': 1,
    'cluster': 1,  # Replace with the cluster ID
    'role': 1,  # Replace with the role ID
    'tenant': 1,  # Replace with the tenant ID
    # Include other attributes as needed
}

# Create a virtual machine
try:
    response = requests.post(devices_url, headers=headers, data=json.dumps(vm_data))
    response.raise_for_status()  # Raise an exception for any HTTP error
    vm = response.json()
    print('Virtual machine created successfully:')
    print('ID:', vm['id'])
    print('Name:', vm['name'])
    # Print other relevant information
except requests.exceptions.RequestException as e:
    print('Error creating virtual machine:', e)

