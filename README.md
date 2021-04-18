# CryptoWail
A very simple script for encrypting/decrypting text content with Caesar, Vigenere, Vernam ciphers (decrypting Caesar ciphre with frequency analysis included).

## Usage
Currently this script supports only english characters. Any non-english alphabet character will be ignored!
### Encoding/Decoding
Use the following command to encode/decode the content of a file using available ciphers and write it to the output file.<br />
`python crypto.py encode/decode [OPTIONS]`

Required options:<br />
`-c, --cipher [vernam|vigenere|caesar]` Cipher type. <br />
`-k, --key KEY` Cipher key (a positive integer for Caesar, string for Vigenere/Vernam ciphers). <br />
`-i, --input FILE` File to read from. <br />
`-o, --output FILE` File to write to. <br />

### Attack
Use the following command to decode the content of a file encrypted by Caesar cipher through frequency analysis.<br />
`python crypto.py attack [OPTIONS]`

Required options:<br />
`-n` A positive integer parameter choosing the size of n-grams to be analyzed (results vary due to the size of text; one may try n from 1 to 8 to get desired result). <br />
`-i, --input FILE` File to read from. <br />
`-o, --output FILE` File to write to. <br />

