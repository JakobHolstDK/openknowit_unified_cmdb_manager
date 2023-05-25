from flask import Flask, jsonify, request
import requests
import random
import string

from pymongo import MongoClient
import os

MONGO = os.getenv("MONGO")
DNSTOKEN = os.getenv("DNSTOKEN")


import requests
import json

# NetBox API endpoint URLs

api_url = os.getenv("NETBOX_URL")
try:
    if api_url[-1] == "/":
        api_url = api_url[:-1]

    devices_url = api_url + '/dcim/devices/'
    vm_url = api_url + '/virtualization/virtual-machines/'
    cluster_url = api_url + '/virtualization/clusters/'
    tenant_url = api_url + '/tenancy/tenants/'
    role_url = api_url + '/dcim/device-roles/'
    site_url = api_url + '/dcim/sites/'
    ipam_url = api_url + '/ipam/ip-addresses/'
    prefix_url = api_url + '/ipam/prefixes/'
    vlan_url = api_url + '/ipam/vlans/'
    users_url = api_url + '/users/'
    config_context_url = api_url + '/circuits/circuit-terminations/'
    circuit_url = api_url + '/circuits/circuits/'
    provider_url = api_url + '/circuits/providers/'
    interface_url = api_url + '/dcim/interfaces/'
    interface_connection_url = api_url + '/dcim/interface-connections/'
    device_type_url = api_url + '/dcim/device-types/'
    manufacturer_url = api_url + '/dcim/manufacturers/'
    platform_url = api_url + '/dcim/platforms/'
    rack_url = api_url + '/dcim/racks/'
    rack_group_url = api_url + '/dcim/rack-groups/'
    rack_role_url = api_url + '/dcim/rack-roles/'
    region_url = api_url + '/dcim/regions/'
    site_group_url = api_url + '/dcim/site-groups/'
    virtual_chassis_url = api_url + '/dcim/virtual-chassis/'
    device_role_url = api_url + '/dcim/device-roles/'
    

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


def generate_password(length=12):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for _ in range(length))
def create_user(username, email):
  # User data
  user_data = {
    'username': username,
    'password': generate_password(),
    'email': 'newuser@example.com',
    # Include other attributes as needed
  }

  # Create a new user
  try:
    response = requests.post(users_url, headers=headers, json=user_data)
    response.raise_for_status()  # Raise an exception for any HTTP error
    new_user = response.json()
    print('User created successfully.')
    print('Username:', new_user['username'])
    print('Email:', new_user['email'])
    print('Password:', user_data['password'])
  except requests.exceptions.RequestException as e:
    print('Error creating user:', e)













def create_virtualmachine(vmdata):
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


vm_data = {
    'name': 'MyVM',
    'status': 1,
    'cluster': 1,  # Replace with the cluster ID
    'role': 1,  # Replace with the role ID
    'tenant': 1,  # Replace with the tenant ID
    # Include other attributes as needed
}
create_user("jhp","jakob.holst@knowit.dk")
create_virtualmachine(vm_data)

