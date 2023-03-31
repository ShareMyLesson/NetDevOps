import getpass
from netmiko import ConnectHandler
from datetime import datetime

# Get username and password
username = input("Enter username: ")
password = getpass.getpass("Enter Password: ")

# Loop through each row in the Excel sheet to create device list
device_list = []
for x in range(99, 101):
    for y in range(1, 11):
        device = {
            "device_type": "hp_procurve",
            "host": f"10.{x}.5.{y}",
            "username": username,
            "password": password,
        }
        device_list.append(device)

# Loop through each device in device_list
for each_device in device_list:
    try:
        # Connect to device
        connection = ConnectHandler(**each_device)
        connection.enable()

        # Create output file handle for the device
        device_name = each_device['host']
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'{device_name}_{current_time}.txt'
        with open(file_name, "w") as f:
            f.write(f'Connecting to {each_device["host"]} on {current_time}\n')
            # Send commands and write output to file
            output1 = connection.send_command('show run')
            f.write(output1+"\n")
            output2 = connection.send_command('show IP route')
            f.write(output2+"\n")
            output3 = connection.send_command('sh system')
            f.write(output3+"\n")
            output4 = connection.send_command('sh vlan')
            f.write(output4+"\n")
            output5 = connection.send_command('sh cdp n')
            f.write(output5+"\n")
            output6 = connection.send_command('sh cdp n d')
            f.write(output6+"\n")
            output7 = connection.send_command('sho lldp info remote-device')
            f.write(output7+"\n")
            output8 = connection.send_command('sho mac-address')
            f.write(output8+"\n")
            output9 = connection.send_command('show arp')
            f.write(output9+"\n")
            output10 = connection.send_command('show log -r')
            f.write(output10+"\n")

    except ConnectionError as e:
        print(
            f'Error connecting to device {each_device["host"]}. Error message: {e}\n')
        continue
    except Exception as e:
        print(
            f'Error occurred while connecting {each_device["host"]}: {str(e)}')
        continue

    else:
        # Disconnect from device
        print(f'Closing connection to {each_device["host"]}\n')
        connection.disconnect()
