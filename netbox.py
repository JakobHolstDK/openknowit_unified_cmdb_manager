import pynetbox
import os

api = os.getenv("NETBOX_URL")
token = os.getenv("NETBOXTOKEN")

nb = pynetbox.api(
    api,
    token=token
)

devices = nb.dcim.devices.all()
for device in devices:
  print(device.name)
  print(device.primary_ip.address)
  print(device.primary_ip.assigned_object.name)
  print(device.primary_ip.assigned_object.device_role.name)
  