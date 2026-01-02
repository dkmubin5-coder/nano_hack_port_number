#This is a simple conditional script
port = int(input("Enter port number:"))
if port == 8080:
    print("This HTTP port This is commonly used for web servers: 8080")

elif port == 443:
    print("This HTTPS port This is commonly used for secure web servers: 443")

else:
    print("This port is not specifically recognized by the port number:", port)
