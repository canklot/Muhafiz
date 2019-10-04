# Muhafiz
Python easy to use password storage


The password is expanded to two 256 bit keys using PBKDF2 with a 256 bit random salt (increased from 128 bits in release 3.0.0), SHA256, and 100,000 iterations (increased from 10,000 in release 4.0.0).

AES256 CTR mode is used to encrypt the data with one key. The first 64 bits of the salt are used as a message nonce (of half the block size); the incremental part of the counter uses the remaining 64 bits (see section B.2 of http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf).

An encrypted messages starts with a 4 byte header ("sc" in ASCII followed by two bytes containing version data).

An SHA256 HMAC (of header, salt, and encrypted message) is calculated using the other key.

The final password consists of the header, salt, encrypted data, and HMAC, concatenated in that order.

On decryption, the header is checked and the HMAC validated before decryption.
