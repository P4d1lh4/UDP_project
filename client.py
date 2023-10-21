import socket as s
import time

def checksum(data):
    byte_count = len(data)
    print(f"N. bytes: {byte_count}")
    return


if __name__ == "__main__":
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080
    client = s.socket(s.AF_INET, s.SOCK_DGRAM)
    addr = (HOST, PORT)

    while True:
        data = input("Enter a word: ")
        data = data.encode("utf-8")
        checksum(data)
        client.sendto(data, addr)
        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(len(data))
        time.sleep(1)