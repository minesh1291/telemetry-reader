import socket
import sys
import json
import struct
import binascii

UDP_IP = "192.168.43.213"
UDP_PORT = 5555

server_address = (UDP_IP, UDP_PORT)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) #
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(f"received message: {data}")

    # data = json.loads(data)
    # data = str(data)
    # output = str(struct.unpack_from('>i', bytearray(data)))
    # b = bytearray(data)
    # output  = binascii.hexlify(b)

    # with open('textfile.txt', 'a') as f:
        # for ch in data:
            # f.write('{}\n'.format(ord(ch)))
