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

while True:
    o1 = int(input("Enter the Private Key(o1): "))
    if(o1>P):
        print("It should be lesser than Prime. Because of Key Space")
        continue
    break

while True:
    o2 = int(input("Enter the Private Key(o2): "))
    if(o2>P):
        print("It should be lesser than Prime. Because of Key Space")
        continue
    break
    

x = pow(g,a,P)

w1 = pow(g,o1,P)
w2 = pow(g,o2,P)

y = pow(g, b, P)

print("Alice Public Key:", x)
print("Bob Public Key:", y)
print("Oscar 1st Public Key: ",w1)
print("Oscar 2nd Public Key: ",w2)

k1 = pow(w2,a,P)
k2 = pow(x,o2,P)

print("Alice Retrieved Key: ", k1)
print("Oscar Retrieved Key: ", k2)

k3 = pow(y,o1,P)
k4 = pow(w1,b,P)

print("Oscar Retrieved Key: ", k3)
print("Bob Retrieved Key: ", k4)
