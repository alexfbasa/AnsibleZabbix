from pyzabbix import ZabbixAPI

zabbix_url = "http://172.17.8.103:8080"
zabbix_user = "Admin"
zabbix_password = "zabbix"

new_host_name = "postgres.dev2"
new_host_ip = "192.168.0.50"
template_name = "Linux by Zabbix agent"
group_name = "Linux servers"

zabbix = ZabbixAPI(zabbix_url)
zabbix.login(zabbix_user, zabbix_password)

template = zabbix.template.get(filter={"host": [template_name]}, output=["templateid"])
template_id = template[0]["templateid"]

group = zabbix.hostgroup.get(filter={"name": [group_name]}, output=["groupid"])
group_id = group[0]["groupid"]

new_host = zabbix.host.create(
    host=new_host_name,
    interfaces=[
        {
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": new_host_ip,
            "dns": "",
            "port": "10050",
        }
    ],
    groups=[{"groupid": group_id}],
    templates=[{"templateid": template_id}],
)

if "hostids" in new_host:
    print(f"Host '{new_host_name}' successfully created in group '{group_name}' with template '{template_name}'.")
else:
    print(f"Failed to create host: {new_host['error']['data']}")

zabbix.user.logout()
