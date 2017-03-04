#!/usr/bin/env python
'''
This script is supposed to be for making a Certificate Revocation List that we can use
to test out out scurl
'''

import OpenSSL

crlfile = "crl.pem"
urls = ['www.facebook.com', 'www.google.com', 'www.stanford.edu']

crl = OpenSSL.crypto.CRL()

crl.add_revoked()

crl_dump = OpenSSL.crypto.dump_crl(OpenSSL.crypto.FILETYPE_PEM, crl)
open(crlfile, 'w').write(crl_dump)