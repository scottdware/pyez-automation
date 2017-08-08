#!/usr/bin/env python3
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import csv

USER = "admin"
PW = "starwars"
CSV_FILE = "config-values.csv"
CONFIG_FILE = "config.txt"

with open(CSV_FILE) as f:
    csvfile = csv.DictReader(f)

    for row in csvfile:
        fw = row['firewall']
        values = {
            'dns_server': row['dns_server'],
            'ntp_server': row['ntp_server'],
            'snmp_location': row['snmp_location'],
            'snmp_contact': row['snmp_contact'],
            'snmp_community': row['snmp_community'],
            'snmp_trap_recvr': row['snmp_trap_recvr']
        }

        dev = Device(host=fw, user=USER, password=PW).open()
        with Config(dev) as cu:
            cu.load(template_path=CONFIG_FILE, template_vars=values, format='set', merge=True)
            cu.commit(timeout=30)
        dev.close()
