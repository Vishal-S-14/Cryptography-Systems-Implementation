def prime_check(p):
    if p < 2:
        return False
    for i in range(2, int(pow(p, 0.5)) + 1):
        if p % i == 0:
            return False
    return True

def primitive_check(g, p, L):
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return False
        return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(p):
    count = 0
    for i in range(1, p + 1):
        if gcd(i, p) == 1:
            count += 1
    return count

def factors(s):
    factor = []
    for i in range(1, s + 1):
        if s % i == 0:
            factor.append(i)
    return factor
 
l = []

while True:
    P = int(input("Enter the Prime Number(P): "))
    if not prime_check(P):
        print("Number is not a Prime, Please Enter the Correct Prime Number")
        continue
    break

while True:
    g = int(input(f"Enter The Primitive Root Of {P} : "))
    if not primitive_check(g, P, l):
        print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
        continue
    break

while True:
    a = int(input("Enter the Private Key(a): "))
    if(a>P):
        print("It should be lesser than Prime. Because of Key Space")
        continue
    break

while True:
    b = int(input("Enter the Private Key(b): "))
    if(b>P):
        print("It should be lesser than Prime. Because of Key Space")
        continue
    break

search_capacity = phi(P)
print(f"Search Capacity: {search_capacity}")
s = factors(search_capacity)
print(f"The Factors of {search_capacity} is {s}")

k = int(input("Enter the Value of k: "))
l = []
T= phi(P)//k

for i in range(0,T):
    val = pow(g,k*i,P)
    l.append(val)
    set1 = set(l)
print("Possible search space is : ",set1)

x = pow(g, (k*a), P)

y = pow(g, (k*b), P)

print("Alice Public Key:", x)
print("Bob Public Key:", y)

k1 = pow(y, (k*a), P)
k2 = pow(x, (k*b), P)

print("Alice Retrieved Key: ", k1)
print("Bob Retrieved Key: ",k2)

if k in s:
    print("Small Subgroup Attack Possible")
else:
    print("Small Subgroup Attack Not possible")

if k1 == k2 and k1 in set1:
    print("Shared Key is in the search space.")
else:
    print("Shared Key is not in the search space.")