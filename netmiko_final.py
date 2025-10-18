from netmiko import ConnectHandler
from pprint import pprint

device_ip = "<!!!REPLACEME with router IP address!!!>"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "<!!!REPLACEME with device type for netmiko!!!>",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show ip interface brief", use_textfsm=True)
        parts = []
        for row in result:
            intf = row.get("interface") or row.get("intf")
            status = row.get("status")
            if intf and intf.startswith("GigabitEthernet"):
                parts.append(f"{intf} {status}")
                if status == "up":
                    up += 1
                elif status == "down":
                    down += 1
                elif status == "administratively down":
                    admin_down += 1
        ans = ", ".join(parts) + f" -> {up} up, {down} down, {admin_down} administratively down"
        pprint(ans)
        return ans
