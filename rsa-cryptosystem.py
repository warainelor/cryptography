import random

def is_prime(num):
    if num <= 1 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def generate_large_prime():
    while True:
        num = random.randint(10_000_000_000, 99_999_999_999)
        if is_prime(num):
            return num

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def multiplicative_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("modular inversion does not exist")
    else:
        return x % phi

def generate_keys():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(3, phi - 1)
        if greatest_common_divisor(e, phi) == 1:
            break
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

public_key, private_key = generate_keys()
print(f"public key: {public_key}")
print(f"private key: {private_key}")

message = input("input a message: ")

encrypted_msg = encrypt(public_key, message)
print(f"encrypted message: {encrypted_msg}")

decrypted_msg = decrypt(private_key, encrypted_msg)
print(f"decrypted message: {decrypted_msg}")
