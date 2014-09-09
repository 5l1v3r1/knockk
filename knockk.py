#!/usr/bin/env python
import socket
import sys

def knockTCP(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.send("hello")
    except: pass
    s.close()

def knockUDP(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))
    s.send("hello")
    s.close()

def usage():
    print("Usage: {0:s} IP PROTOCOL PORT1 [PORT2...]".format(sys.argv[0]))

def main():
    if len(sys.argv) < 4:
        usage()
        return 1
    IP = sys.argv[1]
    PROTO = sys.argv[2]
    PORTS = []
    for i in range(3, len(sys.argv)):
        try:
            PORTS.append(int(sys.argv[i]))
        except:
            print("Port argument \"{0}\" is invalid".format(sys.argv[i]))
            usage()
            return 1

    validoctets = 0
    if len(IP.split('.')) == 4:
        for octet in IP.split('.'):
            try:
                if int(octet) < 256 and int(octet) >= 0:
                    validoctets += 1
            except: pass
    else:
        print("Invalid IP address given: {0}".format(IP))
        usage()
        return 1

    if validoctets != 4:
        print("Invalid IP address given: {0}".format(IP))
        usage()
        return 1


    if PROTO.upper() == 'TCP':
        for port in PORTS:
            knockTCP(IP, port)
    elif PROTO.upper() == 'UDP':
        for port in PORTS:
            knockUDP(IP, port)
    else:
        print("TCP or UDP... not \"{0:s}\"", PROTO)
        usage()
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
