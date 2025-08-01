def primeCheck(p):
    for i in range(2, int(p**0.5) + 1):
        if p < 2 or p % i == 0:
            return False
    return True

def prime4check(p):
    return p % 4 == 3

def checkRabin(n, m, dec):
    for i in range(len(dec)):
        if n == dec[i] and m == n:
            return True
    return False

def generate_rabin_key():
    p = int(input("Enter the Prime Number p: "))
    while not (primeCheck(p) and prime4check(p)):
        print("Invalid Input. Enter the Correct Prime Number, and it should be in the form 4k+3")
        p = int(input("Enter the Prime Number p: "))

    q = int(input("Enter the Prime Number q: "))
    while not (primeCheck(q) and prime4check(q)):
        print("Invalid Input. Enter the Correct Prime Number, and it should be in the form 4k+3")
        q = int(input("Enter the Prime Number q: "))


    n = p * q
    print(f"Public Key: {n}")

    return p, q, n

def add_padding(n):
    str1 = str(n)
    str2 = "1" + str1 + "1"
    str3 = int(str2)
    return str3

def remove_padding(n):
    str3 = str(n)
    str4 = str3[1:-1]
    message = int(str4)
    return message

def encrypt_decrypt_message(p, q, n, m):
    M = add_padding(m)
    c = pow(M, 2, n)
    print(f"Cipher Text ≅ {c} (mod {n})")

    a1 = pow(c, (p + 1) // 4, p)
    a2 = p - a1
    b1 = pow(c, (q + 1) // 4, q)
    b2 = q - b1

    print("The Possible Values are:")
    print(f"a1 ≅ {a1} (mod {p})\na2 ≅ {a2} (mod {p})\nb1 ≅ {b1} (mod {q})\nb2 ≅ {b2} (mod {q})")
    m1 = (p * q) // p
    m2 = (p * q) // q

    y1 = pow(m1, -1, p)
    y2 = pow(m2, -1, q)

    x1 = ((a1 * m1 * y1) + (b1 * m2 * y2)) % n
    x2 = ((a2 * m1 * y1) + (b1 * m2 * y2)) % n
    x3 = ((a1 * m1 * y1) + (b2 * m2 * y2)) % n
    x4 = ((a2 * m1 * y1) + (b2 * m2 * y2)) % n

    print("The Values of x are:")
    print(f"x1 ≅ {int(x1)} (mod {n})\nx2 ≅ {int(x2)} (mod {n})\nx3 ≅ {int(x3)} (mod {n})\nx4 ≅ {int(x4)} (mod {n})")

    l = [int(x1), int(x2), int(x3), int(x4)]
    print(l)
    dec = []
    for i in range(len(l)):
        dec.append(remove_padding(l[i]))
    print(dec)

    while True:
        num = int(input("Enter the Number to Check: "))
        if not checkRabin(num, m, dec):
            print(f"{num} is not a valid result.")
            continue
        else:
            print(f"{num} is a valid result.")
            break

p, q, n = generate_rabin_key()
m = int(input("Enter the Message: "))
encrypt_decrypt_message(p, q, n, m)
