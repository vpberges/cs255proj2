#!/usr/bin/env python
'''
This script is supposed to be for making a Certificate Revocation List that we can use
to test out out scurl
'''

import OpenSSL
import socket

crlfile = "crl.pem"
urls = ['www.facebook.com', 'www.google.com', 'www.stanford.edu']
method = OpenSSL.SSL.TLSv1_2_METHOD
port = 443

# Make a Certificate Revocation List object
crl = OpenSSL.crypto.CRL()

# Make a Connection Object
context = OpenSSL.SSL.Context(method)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = OpenSSL.SSL.Connection(context, sock)

for url in urls:
    # Open a connection
    connection.connect((url, port))
    connection.do_handshake()
    certificate = connection.get_peer_certificate()
    serial = certificate.get_serial_number()
    print "Serial: %d" % serial
    revoked = OpenSSL.crypto.Revoked()
    revoked.set_serial(serial)
    crl.add_revoked(revoked)

    connection.shutdown()
    connection.close()

crl_dump = OpenSSL.crypto.dump_crl(OpenSSL.crypto.FILETYPE_PEM, crl)
open(crlfile, 'w').write(crl_dump)