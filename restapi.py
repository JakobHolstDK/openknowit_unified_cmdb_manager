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
try:
    devices_url = api_url + 'dcim/devices/'
    vm_url = api_url + 'virtualization/virtual-machines/'
    cluster_url = api_url + 'virtualization/clusters/'
    tenant_url = api_url + 'tenancy/tenants/'
    role_url = api_url + 'dcim/device-roles/'
    site_url = api_url + 'dcim/sites/'
    ipam_url = api_url + 'ipam/ip-addresses/'
    prefix_url = api_url + 'ipam/prefixes/'
    vlan_url = api_url + 'ipam/vlans/'
except:
    print("Error in URL")
    print("You need to set the NETBOX_URL environment variable to the URL of your NetBox instance")
    exit(1)


token = os.getenv("NETBOXTOKEN")
if token == None:
    print("Error in NETBOXTOKEN")
    print("You need to set the NETBOXTOKEN environment variable to the API token for your NetBox instance")
    exit(1)
    

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

