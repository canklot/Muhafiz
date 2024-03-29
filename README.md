
# Muhafiz
Easy to use password manager written in Python

The password is expanded to two 256 bit keys using PBKDF2 with a 256 bit random salt , SHA256, and 100,000 iterations 

AES256 CTR mode is used to encrypt the data with one key. The first 64 bits of the salt are used as a message nonce (of half the block size); the incremental part of the counter uses the remaining 64 bits (see section B.2 of http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf).

An encrypted messages starts with a 4 byte header ("sc" in ASCII followed by two bytes containing version data).

An SHA256 HMAC (of header, salt, and encrypted message) is calculated using the other key.

The final password consists of the header, salt, encrypted data, and HMAC, concatenated in that order.

On decryption, the header is checked and the HMAC validated before decryption.

Site names and usernames are stored as just hashed with sha256 (without salt)


# Usage
Just run the code with: `python muhafiz.py`

The program will ask you about which mode you want to use it. Choose `s` for storage , `d` for decryption mode

Then the program will ask you about your login credentials `website`, `e-mail` and `masterpassword`

After credentials have submitted the encrypted data will be saved in a file named `kasa` in the same folder.



