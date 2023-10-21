import socket as s
import time

def checksum(data):
    byte_count = len(data)
    print(f"N. bytes: {byte_count}")
    return

def send_packet(seq_num, data, addr, client_socket):
    packet = str(seq_num).encode() + b"|" + data
    checksum(packet)
    client_socket.sendto(packet, addr)

if __name__ == "__main__":
    
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080
    server = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server.bind((HOST, PORT))
    server.bind((HOST, PORT))
    expected_seq_num = 0

    while True:
        data, addr = server.recvfrom(1024)
        seq_num, data = data.split(b"|", 1)
        seq_num = int(seq_num)
        data = data.decode("utf-8")

        print("Client: {data}")
        data = data.upper()
        data = data.encode("utf-8")
        checksum(data)
        server.sendto(data, addr)
        if seq_num == expected_seq_num:
            print(f"Received from Client: {data}")
            data = data.upper()
            data = data.encode("utf-8")
            checksum(data)
            server.sendto(data, addr)
            expected_seq_num += 1
        else:
            print(f"Received out-of-order packet with seq_num {seq_num}. Ignoring.")