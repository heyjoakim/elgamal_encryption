"""
Alice & Bob agreed on base g = 666 with a generator p = 6661
Bob then sends his Public-key (g^x mod p) = 2227 to Alice
"""
g = 666
p = 6661  # generator
B = 2227  # Message send to Alice

print("Bob sends PK (" + str(B) + ") to alice ")

y = 144 # Alice random key
Alice_PK = g**y % p  # Alice PK
Key = B**y % p  # Alice computes secret
print(Key)
c = Key * 2000  # Alice compute her secret message c
print(c)

print("Alice sends PK with encrypted message (" + str(Alice_PK) + "," +  str(c) + ") to Bob." )


""" Eve intercepts Alice's message (AlicePK, c) """

# Messages intercepted
A_message, c = (Alice_PK, c)
B_message = B

print("-"*66)
print("Eve intercepts the messages and bruteforces")
print("-"*66)

def bruteforce(A, B):
    for i in range(1, p):
        if g**i % p == A:
            y_key = i
        if g**i % p == B:
            x_key = i

    print("Alice secret was", y_key)
    print("Bob secret was", x_key)

    try:
        assert B**y_key % p == A**x_key % p
        secret = B**y_key % p
        message = c // secret
        print("Message was", message)
    except AssertionError:
        print("Bruteforce failed, the shared secrets were not the same")


bruteforce(A_message, B_message)

""" 
Mallory intercepts the messages and modifies the message to '6000'
M knows Alice's message and her secret key and acts like Alice
"""
M_Key = B_message**y % p # Bob's PK, Alices secret key
malory_c = M_Key * 6000 # Corrupting c
modified_message = Alice_PK, malory_c  # An easier solution would be to multiply c by 3

print("-"*66)
print("Mallory intercepts and modifies the message")
print("-"*66)

print("Mallory sends Bob the message modified", modified_message)

# Bob decrypting
PK, corrupted_message = modified_message

B_Key = PK**66 % p # Bob should know his secret key 66
decrypted_message = corrupted_message // B_Key 
print("Bob decrypts the modified message", decrypted_message) 