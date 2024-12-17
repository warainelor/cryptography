from itertools import cycle
import ast


def xor_cipher(text: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(text, cycle(key)))


if bool(input("cipher (0) or decipher (1): ") == "0"):
    plaintext = input("input text: ").encode('utf-8')
    key = input("input key: ").encode('utf-8')
    ciphertext = xor_cipher(plaintext, key)
    print(f"ciphered text: {ciphertext}")
else:
    plainbytes = input("input bytes in format b'\\x05\\t\\x17\\x1e\\x12': ")
    try:
        byte_data = ast.literal_eval((plainbytes))
    except ValueError:
        print("bad input")
    key = input("input key: ").encode('utf-8')
    deciphertext = xor_cipher(byte_data, key)
    print(f"deciphered text: {deciphertext}")