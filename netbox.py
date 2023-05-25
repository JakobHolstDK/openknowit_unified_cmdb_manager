import pynetbox
import os

api = os.getenv("NETBOX_URL")
token = os.getenv("NETBOXTOKEN")

nb = pynetbox.api(
    api,
    token=token
)
