import socket
import sys

#Specify the target host and port range
host = input("Enter target (iP) address sent:")
start_port = int(input("Enter start port number:"))
end_port = int(input("Enter end port number:"))

print(f"Scanning started on ports {host} from {start_port} to {end_port}")

#prot scanning loop
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is open")
        s.close()