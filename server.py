import socket as s

def checksum(data):
    byte_count = len(data)
    print(f"N. bytes: {byte_count}")
    return

if __name__ == "__main__":
    
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080
    server = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server.bind((HOST, PORT))

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")

        print("Client: {data}")
        data = data.upper()
        data = data.encode("utf-8")
        checksum(data)
        server.sendto(data, addr)
