import random
import math

def generate_private_key():
    superincreasing_set = [1]  # Start with 1 as the first element
    for i in range(1, 5):
        y = random.randint(1,10)
        superincreasing_set.append(sum(superincreasing_set) + y)
    return superincreasing_set

def generate_random_number_greater_than(limit):
    return random.randint(limit + 1, limit * 2)

def generate_coprime(number):
    while True:
        candidate = random.randint(2, number - 1)
        if math.gcd(candidate, number) == 1 and candidate>1:
            return candidate

def generate_public_key(pkey,n,m):
    pubkey = []
    for i in pkey:
        x = (i*n)%m
        pubkey.append(x)
    return pubkey

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(n, m):
    gcd, x, y = extended_gcd(n, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {n} mod {m}")
    else:
        return (x % m + m) % m

def knapsack_encrypt(pubkey,message):
    m1 = bin(message)[2:]
    x = len(pubkey)
    b = len(m1)
    n = b%x
    if n == 0:
        y = b//x
        binary_list = [m1[i:i+x] for i in range(0, len(m1), x)]
        l = []
        for i in binary_list:
            sum = 0
            for j in range(x):
                p = int(i[j]) * pubkey[j]
                sum += p
            l.append(sum)
    else:
        y = b%x
        y = x - y
        m1 = '0' * y + m1
        len_of_padded_binary = len(m1)
        n = len_of_padded_binary//x
        binary_list = [m1[i:i+x] for i in range(0, len(m1), x)]
        l = []
        for i in binary_list:
            sum = 0
            for j in range(x):
                p = int(i[j]) * pubkey[j]
                sum += p
            l.append(sum)
    return l

def knapsack_decrypt(pkey,cipher,m,n):
    n_inverse = mod_inverse(n,m)
    pt1 = []
    for i in cipher:
        str = ""
        x = (i * n_inverse) % m
        rev = sorted(pkey, reverse = True)
        for i in rev:
            if i<=x:
                x = x - i
                str += '1'
            else:
                str += '0'
        pt1.append(str[::-1])
    str2 = ""
    for i in pt1:
        str2 += i
    return int(str2,2)

def main():
    pkey = generate_private_key()
    print("Private key = ",pkey)

    m = generate_random_number_greater_than(sum(pkey))
    n = generate_coprime(m)
    print("Randomly generated m value: ",m)
    print("Randomly generated n value: ",n)
    pubkey = generate_public_key(pkey,n,m)
    print("Public Key: ",pubkey)

    message = int(input("Enter the Message Here(in Decimal): "))
    cipher = knapsack_encrypt(pubkey,message)
    print("Encrypted message : ",cipher)

    plaintext = knapsack_decrypt(pkey,cipher,m,n)
    print("Decrypted Message: ",plaintext)

if __name__ == "__main__":
    main()

    