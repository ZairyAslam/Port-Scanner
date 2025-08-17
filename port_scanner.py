"""
Simple Port Scanner
Author: Zairy Izzul Aslam
Last Updated: 2025-08-17

Description:
    A basic Python TCP port scanner that checks a list of common ports 
    on a specified host to determine if they are open or closed. 
    Measures the total time taken for the scan.
"""

import socket
from datetime import datetime

# Introductory message for the user
print("This tool scans a target host for common TCP ports and reports "
      "which are open or closed.")

# Prompt user for target IP or hostname
target = input("Enter target IP or hostname: ")

# Attempt to resolve the hostname to an IP address
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved")
    exit()

# Define a list of common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

# Record the start time of the scan
start_time = datetime.now()

# Loop through each port and check its status
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket
    socket.setdefaulttimeout(1)  # Set 1-second timeout to avoid hanging
    result = sock.connect_ex((target_ip, port))  # Attempt connection

    # Report port status
    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")

    sock.close()  # Close socket to free resources

# Record the end time and print total scan duration
end_time = datetime.now()
print(f"Scanning completed in: {end_time - start_time}")