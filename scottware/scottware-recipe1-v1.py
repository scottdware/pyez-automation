#!/usr/bin/env python3
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

USER = "admin"
PW = "starwars"
CONFIG_VARS = {
	'dns_server': '8.8.8.8',
	'ntp_server': '24.56.178.140',
	'snmp_location': 'Data center core rack',
	'snmp_contact': 'IT Security',
	'snmp_community': 'snmprw',
	'snmp_trap_recvr': '192.168.1.10'
}
CONFIG_FILE = 'config.txt'
HOSTS = 'firewalls.txt'

with open(HOSTS, 'r') as f:
	firewalls = f.readlines()
	firewalls = [x.strip() for x in firewalls]

	for fw in firewalls:
		dev = Device(host=fw, user=USER, password=PW).open()
		with Config(dev) as cu:
			cu.load(template_path=CONFIG_FILE, template_vars=CONFIG_VARS, format='set', merge=True)
			cu.commit(timeout=30)
		dev.close()