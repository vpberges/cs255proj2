# CS 255: Proejct 2 – Secure CURL
### Winter 2017

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
