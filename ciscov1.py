import getpass
import openpyxl
from netmiko import ConnectHandler
from datetime import datetime

# Open Excel file containing devices
wb = openpyxl.load_workbook('Cisco.xlsx')
sheet = wb['Sheet1']

# Get username and password
username = getpass.getpass("Enter username: ")
password = getpass.getpass("Enter Password: ")

# Loop through each row in the Excel sheet to create device list
device_list = []
for row in sheet.iter_rows(min_row=1, values_only=True):
    device = {
        "device_type": "cisco_ios",
        "host": row[0],
        "username": username,
        "password": password,
        "secret": password,
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
            output3 = connection.send_command('sh inventory')
            f.write(output3+"\n")
            output4 = connection.send_command('sh vlan')
            f.write(output4+"\n")
            output5 = connection.send_command('sh cdp n')
            f.write(output5+"\n")
            output6 = connection.send_command('sh cdp n d')
            f.write(output6+"\n")
            output7 = connection.send_command('sho lldp neighbors')
            f.write(output7+"\n")
            output8 = connection.send_command('show mac address-table')
            f.write(output8+"\n")
            output9 = connection.send_command('show arp')
            f.write(output9+"\n")
            output10 = connection.send_command('show log')
            f.write(output10+"\n")

    except ConnectionError as e:
        print(
            f'Error connecting to device {each_device["host"]}. Error message: {e}\n')
        continue
    except Exception as e:
        print(f'Error occurred while connecting {each_device["host"]}: {str(e)}')
        continue

    else:
        # Disconnect from device
        print(f'Closing connection to {each_device["host"]}\n')
        connection.disconnect()
