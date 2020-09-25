g = 666
p = 6661  # generator

a = 37  # Alice secret key
b = 144  # Bob secret key

A = g**a % p  # Message send to Bob
B = g**b % p  # Message send to Alice
print("Alice sends to Bob ", A)
print("Bob sends to Alice", B)

s_Alice = B**a % p  # Alice computes secret
s_Bob = A**b % p  # Bob computes secret

assert s_Alice == s_Bob
print("Alice computes the secret ", s_Alice)
print("Bob computes the secret", s_Bob)

# Messages intercepted
A_message = 820
B_message = 5333

print("-"*20)


def bruteforce(A, B):
    for i in range(1, p):
        if g**i % p == A:
            a_key = i
        if g**i % p == B:
            b_key = i

    print("Alice secret was", a_key)
    print("Bob secret was", b_key)

    assert B**a % p == A**b % p
    s = A**b % p
    print("Adversary computes secret", s)


bruteforce(A_message, B_message)

