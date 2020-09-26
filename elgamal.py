g = 666
p = 6661  # generator

x = 37  # Bob secret key
y = 144  # Alice secret key

B = g**x % p  # Message send to Alice
A = g**y % p  # Message send to Bob
print("Bob sends (g^x mod p) to Alice", B)
print("Alice computes (g^y mod p) ", A)

s_Bob = A**x % p  # Bob computes secret
s_Alice = B**y % p  # Alice computes secret

assert s_Alice == s_Bob
#print("Alice computes (g^y mod p) ", s_Alice)
#print("Bob computes the secret", s_Bob)

# Messages intercepted
A_message = 820
B_message = 5333

print("-"*20)


def bruteforce(A, B):
    for i in range(1, p):
        if g**i % p == A:
            x_key = i
        if g**i % p == B:
            y_key = i

    print("Alice secret was", x_key)
    print("Bob secret was", y_key)

    assert B**x_key % p == A**y_key % p
    s = A**x_key % p
    print("Adversary computes secret", s)


bruteforce(A_message, B_message)

