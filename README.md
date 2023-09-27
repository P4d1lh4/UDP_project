# Objetivo geral: Desenvolver uma aplicação cliente-servidor capaz de, na camada de
# aplicação, fornecer um transporte confiável de dados considerando um canal com
# perdas de dados e erros.

import socket

# the way servers know which data to serve to what computer, even though they have reserved the same port for that process, is by a bunch of numbers
# known as `sockets`, and this is what makes each connection unique.
# 
# Source IP address, port number (client-server)
# Destination IP address, port number (server-client)
# 
# at the ent, a socket is just a communication endpoint
# the socket endpoint for internet communication is the AF_INET --> ipv4 and AF_INET6 --> ipv6 

# the sockets types can be SOCK_STREAM for TCP(transmission control protocol) and SOCK_DGRAM for UDP (user datagram protocol)  


# SOMA DE VERIFICAÇÃO

# the Internet Protocol Suite (TCP/IP)
# uses a method called checksum to verify the
# integrity of the data packets.

# The idea is that if the data is changed in any way, 
# even by a single bit, the checksum value will also change.
# by comparing the checksum values of the original and the received
#  data, you can detect if there was any error or tampering during transmission

# TCP/IP checksum is based on the concept of ones' complement arithmetic,
# which is a way of representing negative numbers by flipping all 
# the bits of the positive number.

# To calculate the TCP/IP checksum, you add up all the 16-bit words
# in the data, and then take the ones' complement of the sum. The result
# is a 16-bit value that is appended to the data as the checksum field. 
# The receiver performs the same calculation on the received data 
# and compares it with the checksum field.