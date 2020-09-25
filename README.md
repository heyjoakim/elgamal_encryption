# elgamal_encryption
ElGamal encryption public-key cryptosystem

**1. Alice wants to send 2000 DKK to Bob through a confidential message. A decision to use the ElGamal public key method is chosen. The keyring material used to send the message to Bob is as follows:**
 
* The shared base <img src="https://render.githubusercontent.com/render/math?math=g = 666">
* The shares prime <img src="https://render.githubusercontent.com/render/math?math=p = 6661">
* Bob's public key <img src="https://render.githubusercontent.com/render/math?math=PK = g^{x} mod p = 227">


Send the message '2000' to Bob.

**2. Eve intercept Alice’s encrypted message. Find Bob’s private key and reconstruct Alice’s message.**

**2. Mallory intercept Alice’s encrypted message. However, you run on a constrained device and are unable to find Bob’s private key.
Modify Alice’s encrypted message so that when Bob decrypts it, he will get the message ’6000’.**
