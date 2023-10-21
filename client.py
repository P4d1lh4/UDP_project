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
    client = s.socket(s.AF_INET, s.SOCK_DGRAM)
    addr = (HOST, PORT)
    next_seq_num = 0

    while True:
        data = input("Enter a word: ")
        data = data.encode("utf-8")
        send_packet(next_seq_num, data, addr, client)
        next_seq_num += 1