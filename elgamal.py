""" ElGamal encryption public-key cryptosystem"""
g = 666
p = 6661
PK_bob = 2227  # Message send to Alice

print("Bob sends PK ({0}) to Alice".format(PK_bob)) # Bob then sends his Public-key (g^x mod p) = 2227 to Alice

# Assignment 1.

message = 2000
y = 144 # Alice random key
PK_alice = pow(g,y,p)  # Alice PK (g**y) mod p
gxy = pow(PK_bob,y,p) # Shared key

c = (gxy * message) % p  # Alice compute her secret message c, using mod to stay within group

print("Alice sends PK with encrypted message ({0},{1}) to Bob".format(PK_alice, c))

# Bob recovers message by calculateing c / g^yx (we actualy need c*(g^yx)^-1 (multiplicative inverse)
gxy_1 = pow(gxy, -1, p) # Multiplicative inverse
message_reconstructed = (c*gxy_1) % p
print("Bob recovers message", message_reconstructed)


# Assignment 2.

def bruteforce(PK_bob):
    for i in range(1, p+1):
        if pow(g,i,p) == PK_bob:
            x_key = i
            print("Bobs secret was", x_key)
            break

    try:
        assert pow(PK_alice, x_key,p) == pow(PK_bob,y,p)
        eve_gxy = pow(PK_alice,x_key,p)
        eve_gxy_1 = pow(eve_gxy, -1, p)
        message = (c*eve_gxy_1) % p
        print("Message was", message)
    except AssertionError:
        print("Bruteforce failed, the shared secrets were not the same")


bruteforce(PK_bob)

# Assignment 3.

malory_gxy = pow(PK_bob,y,p) # Secret computes with Bob's PK, Alices secret key
malory_c = malory_gxy * 6000 # Corrupting c
modified_message = PK_alice, malory_c  # An easier solution would be to multiply c by 3

print("Mallory sends Bob the message modified", modified_message)

# Bob decrypting
PK, corrupted_message = modified_message
decrypted_message = (corrupted_message*gxy_1) % p
print("Bob is decrypting message ", decrypted_message)
