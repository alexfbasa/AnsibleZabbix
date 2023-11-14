import sys
from pyzabbix import ZabbixAPI, ZabbixAPIException

ZABBIX_SERVER = "http://172.17.8.103:8080/"
ZABBIX_USER = "Admin"
ZABBIX_PASSWORD = "zabbix"


zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login(ZABBIX_USER, ZABBIX_PASSWORD)

new_host_name = "Zabbix Test"
new_host_ip = "192.168.1.1"

existing_hosts = zapi.host.get(filter={"host": new_host_name}, selectInterfaces=["interfaceid"])


if existing_hosts:
    print(f"Host with name {new_host_name} already exists.")
    sys.exit()

try:
    new_host = zapi.host.create(
        host=new_host_name,
        interfaces=[{"type": 1, "main": 1, "useip": 1, "ip": new_host_ip, "dns": "", "port": "10050"}],
        groups=[{"groupid": "Linux"}],
        template={"templateid": "Linux by Zabbix agent active"},
    )
except ZabbixAPIException as e:
    print(e)
    sys.exit()

print(f"Created new host with ID: {new_host['hostids'][0]}")
