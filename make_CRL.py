#!/usr/bin/env python
'''
This script is for making a Certificate Revocation List that we can use to test scurl
'''

import OpenSSL
import socket

crlfile = "crl.pem"
urls = ['www.facebook.com', 'www.google.com', 'www.stanford.edu']
method = OpenSSL.SSL.TLSv1_2_METHOD
port = 443

# Instantiate a Certificate Revocation List object
crl = OpenSSL.crypto.CRL()

# Instantiate a Connection Object
context = OpenSSL.SSL.Context(method)

for url in urls:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = OpenSSL.SSL.Connection(context, sock)
    # Open a connection
    connection.connect((url, port))
    connection.do_handshake()

    certificate = connection.get_peer_certificate()
    print "Recieved certificate: %s" % certificate

    serial = certificate.get_serial_number()
    hex_serial = hex(serial)
    print "%s Serial: %s" % (url, hex_serial)

    revoked = OpenSSL.crypto.Revoked()
    revoked.set_serial(hex_serial)

    crl.add_revoked(revoked)

    connection.shutdown()
    connection.close()


# Just kidding this only works in pyOpenSSL 16+
crl_dump = OpenSSL.crypto.dump_crl(OpenSSL.crypto.FILETYPE_PEM, crl)

open(crlfile, 'w').write(crl_dump)