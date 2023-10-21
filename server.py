import socket as s
import time
import threading

def checksum(data):
    byte_count = len(data)
    print(f"N. bytes: {byte_count}")
    return

def timer(event):
    while True:
        time.sleep(1)
        event.set()

if __name__ == "__main__":
    
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080
    server = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server.bind((HOST, PORT))

    event = threading.Event()
    timer_thread = threading.Thread(target=timer, args=(event,))
    timer_thread.start()

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")

        print("Client: {data}")
        data = data.upper()
        data = data.encode("utf-8")
        checksum(data)
        server.sendto(data, addr)

        event.wait()
        event.clear()
        print("Timer tick")