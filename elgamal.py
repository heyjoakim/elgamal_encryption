"""Alice & Bob agreed on base g = 666 with a generator p = 6661 """
print("--- Key exchange & Encryption ---")
g = 666
p = 6661  # generator
B = 2227  # Message send to Alice

print("Bob sends PK ({0}) to Alice".format(B)) # Bob then sends his Public-key (g^x mod p) = 2227 to Alice

y = 144 # Alice random key
Alice_PK = g**y % p  # Alice PK
Key = B**y % p  # Alice computes secret
c = Key * 2000  # Alice compute her secret message c

print("Alice sends PK with encrypted message ({0},{1}) to Bob".format(Alice_PK, c))


""" Eve intercepts Alice's message (AlicePK, c) """
print(" --- Eve intercepting ---")

# Messages intercepted
A_message, c = (Alice_PK, c)
B_message = B

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

""" Mallory intercepts the messages and modifies the message to '6000' """
print(" --- Mallory intercepting ---")

M_Key = B_message**y % p # Secret computes with Bob's PK, Alices secret key
malory_c = M_Key * 6000 # Corrupting c
modified_message = Alice_PK, malory_c  # An easier solution would be to multiply c by 3

print("Mallory sends Bob the message modified", modified_message)

# Bob decrypting
PK, corrupted_message = modified_message

B_Key = PK**66 % p # Bob should know his secret key 66
decrypted_message = corrupted_message // B_Key 
print("Bob decrypts the modified message", decrypted_message) 