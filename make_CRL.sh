#!/bin/bash
# This script converts the CRL file given into PEM format

crl_file="gsorganizationvalsha2g2.crl"
crl_pem="crl.pem"

openssl crl -in $crl_file -inform DER -out $crl_pem