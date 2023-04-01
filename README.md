cisco.py:
This script connects to Cisco devices and pulls information using Netmiko library. It requires Python version 3.6 or higher and the installation of Netmiko library in the system.


This script imports necessary libraries: 'getpass', 'openpyxl', 'netmiko' and 'datetime'. It loads an excel file 'Cisco.xlsx' and assigns the contents of 'Sheet1' to a variable named 'sheet'. Prompt for username and password using getpass. The script then iterates through each row in the sheet to create device_list for each device. The dictionaries created for each device in the device_list contains device_type, host, username, password and secret. 


The script then loops through each device in device_list and tries to connect to it. If the connection is successful, it creates an output file handle for the device with the name 'device_hostname_current_time.txt'. It writes the time of connection and some basic device information to the output file. It uses Netmiko library to send commands and writes the output of these commands to the output file. It disconnects from the device when done. 


If the connection fails or an error occurs during run time, it prints out an error message for the particular device and moves on to the next device. If everything runs without errors, it prints out a message indicating that the connection was closed to the device.


To use this script, install the required version of Python, necessary libraries (getpass, openpyxl and netmiko) and run the script. Update the Excel file with the necessary device information and provide the username and password when prompted. The script will create the output files with the information requested from each device.


