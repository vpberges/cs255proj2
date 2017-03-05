# CS 255: Proejct 2 – Secure CURL
This is the second project in CS 255, "Introduction to Cryptography" taught by Dan Boneh at Stanford University. In this project we implement a secure version of the curl command line utility which is used for fetching HTTP content from a URL. This project is implemented in PYthon 2.7 and makes use of the pyOpenSSL library.

## Authors
Jon Deaton: jdeaton@stanford.edu
Vincent-Pierre Berges: vpberges@stanford.edu

## Installation
Run `pip pyopenssl` in terminal to install the OpenSSL library

Give permission to `scurl` by running  `chmod +x scurl`

## How to use
Just like how you would use curl:

`$ ./scurl [options] [URL...]`

for example

`$ ./scurl --ciphers DHE-DSS-AES256-SHA:DH-RSA-AES256-SHA https://www.stanford.edu/`


## Project TODO list
1. Verify Hostname matches in certificate verification
2. Stop listening/timeout when no content end it sent
3. Make --cacert override --crlfile
4. Test everything extensively