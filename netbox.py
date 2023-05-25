import pynetbox
import os

api = os.getenv("NETBOX_URL")
token = os.getenv("NETBOXTOKEN")

nb = pynetbox.api(
    api,
    token=token
)


def get_device_by_name(name):
    return nb.dcim.devices.get(name=name)
def list_devices():
    return nb.dcim.devices.all()
def add_device():

def add_organization(name):
    return nb.dcim.organizations.create(name=name)
def list_organizations():
    return nb.dcim.organizations.all()
def get_organization_by_name(name):
    return nb.dcim.organizations.get(name=name)
def add_site(name,slug,organization):
    return nb.dcim.sites.create(name=name,slug=slug,organization=organization)
def list_sites():
    return nb.dcim.sites.all()
def get_site_by_name(name):
    return nb.dcim.sites.get(name=name)
def add_device_role(name,slug,color):
    return nb.dcim.device_roles.create(name=name,slug=slug,color=color)
def list_device_roles():
    return nb.dcim.device_roles.all()
def get_device_role_by_name(name):
    return nb.dcim.device_roles.get(name=name)
def add_device_type(manufacturer,model,slug,part_number,height,display_color):
    return nb.dcim.device_types.create(manufacturer=manufacturer,model=model,slug=slug,part_number=part_number,height=height,display_color=display_color)
def list_device_types():
    return nb.dcim.device_types.all()
def get_device_type_by_name(name):
    return nb.dcim.device_types.get(name=name)
def add_platform(name,slug):
    return nb.dcim.platforms.create(name=name,slug=slug)
def list_platforms():
    return nb.dcim.platforms.all()
def get_platform_by_name(name):
    return nb.dcim.platforms.get(name=name)


def add_device(name,device_type,device_role,platform,serial,site):
    return nb.dcim.devices.create(name=name,device_type=device_type,device_role=device_role,platform=platform,serial=serial,site=site)
def list_devices():
    return nb.dcim.devices.all()
def get_device_by_name(name):
    return nb.dcim.devices.get(name=name)
def add_interface(device,name,type,enabled):
    return nb.dcim.interfaces.create(device=device,name=name,type=type,enabled=enabled)
def list_interfaces():
    return nb.dcim.interfaces.all()
def get_interface_by_name(name):
    return nb.dcim.interfaces.get(name=name)
def add_ip_address(address,interface):
    return nb.ipam.ip_addresses.create(address=address,interface=interface)
def list_ip_addresses():
    return nb.ipam.ip_addresses.all()
def get_ip_address_by_address(address):
    return nb.ipam.ip_addresses.get(address=address)
def add_vlan(name,vid,site):
    return nb.ipam.vlans.create(name=name,vid=vid,site=site)
def list_vlans():
    return nb.ipam.vlans.all()
def get_vlan_by_name(name):
    return nb.ipam.vlans.get(name=name)
def add_prefix(prefix,vlan):
    return nb.ipam.prefixes.create(prefix=prefix,vlan=vlan)
def list_prefixes():
    return nb.ipam.prefixes.all()
def get_prefix_by_prefix(prefix):
    return nb.ipam.prefixes.get(prefix=prefix)
def add_rir(name,slug):
    return nb.ipam.rirs.create(name=name,slug=slug)
def list_rirs():
    return nb.ipam.rirs.all()
def get_rir_by_name(name):
    return nb.ipam.rirs.get(name=name)
def add_aggregate(prefix,rir):
    return nb.ipam.aggregates.create(prefix=prefix,rir=rir)
def list_aggregates():
    return nb.ipam.aggregates.all()
def get_aggregate_by_prefix(prefix):
    return nb.ipam.aggregates.get(prefix=prefix)
def add_vrf(name,rd,tenant):
    return nb.ipam.vrfs.create(name=name,rd=rd,tenant=tenant)
def list_vrfs():
    return nb.ipam.vrfs.all()
def get_vrf_by_name(name):
    return nb.ipam.vrfs.get(name=name)
def add_service(name,protocol,port):
    return nb.ipam.services.create(name=name,protocol=protocol,port=port)
def list_services():
    return nb.ipam.services.all()
def get_service_by_name(name):
    return nb.ipam.services.get(name=name)
def add_ip_address(address,interface):
    return nb.ipam.ip_addresses.create(address=address,interface=interface)
def list_ip_addresses():
    return nb.ipam.ip_addresses.all()
def get_ip_address_by_address(address):
    return nb.ipam.ip_addresses.get(address=address)
def add_circuit_provider(name,slug):
    return nb.circuits.providers.create(name=name,slug=slug)
def list_circuit_providers():
    return nb.circuits.providers.all()
def get_circuit_provider_by_name(name):
    return nb.circuits.providers.get(name=name)
def add_circuit_type(name,slug):
    return nb.circuits.circuit_types.create(name=name,slug=slug)
def list_circuit_types():
    return nb.circuits.circuit_types.all()
def get_circuit_type_by_name(name):
    return nb.circuits.circuit_types.get(name=name)
def add_circuit_termination(device,interface,circuit,term_side):
    return nb.circuits.circuit_terminations.create(device=device,interface=interface,circuit=circuit,term_side=term_side)
def list_circuit_terminations():
    return nb.circuits.circuit_terminations.all()
def get_circuit_termination_by_device(device):
    return nb.circuits.circuit_terminations.get(device=device)
def add_circuit(cid,provider,type,tenant):
    return nb.circuits.circuits.create(cid=cid,provider=provider,type=type,tenant=tenant)
def list_circuits():
    return nb.circuits.circuits.all()
def get_circuit_by_cid(cid):
    return nb.circuits.circuits.get(cid=cid)
def add_circuit_termination(device,interface,circuit,term_side):
    return nb.circuits.circuit_terminations.create(device=device,interface=interface,circuit=circuit,term_side=term_side)
def list_circuit_terminations():
    return nb.circuits.circuit_terminations.all()
def get_circuit_termination_by_device(device):
    return nb.circuits.circuit_terminations.get(device=device)
def add_circuit_termination(device,interface,circuit,term_side):
    return nb.circuits.circuit_terminations.create(device=device,interface=interface,circuit=circuit,term_side=term_side)
def list_circuit_terminations():
    return nb.circuits.circuit_terminations.all()
def get_circuit_termination_by_device(device):
    return nb.circuits.circuit_terminations.get(device=device)
def add_circuit_termination(device,interface,circuit,term_side):
    return nb.circuits.circuit_terminations.create(device=device,interface=interface,circuit=circuit,term_side=term_side)
def list_circuit_terminations():
    return nb.circuits.circuit_terminations.all()
def get_circuit_termination_by_device(device):
    return nb.circuits.circuit_terminations.get(device=device)


add_organization("knowit","knowit")



  