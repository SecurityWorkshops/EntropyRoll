# EntropyRoll
Workshop for rolling your own entropy for creating key pairs. Key pairs are used for encryption/decryption 




## Install 

pip install pycryptodome



base58
pycryptodome
ecdsa




## Steps 

### 1

Example 1 has a series of rolls but the rolls do not have enouogh entropy. 


Entropy required for an rsa key is 256 bytes (2048 bits) 

How much entropy is there in a dice roll?

Dice Rolls: Each roll of a 6-sided die provides about 2.58 bits of entropy (since log2(6) ≈ 2.58).

For 256 bytes (2048 bits) of entropy, you would need about 795 dice rolls (2048 / 2.58 ≈ 795).


**Q How do we get more entropy without rolling that many times? ** 


A you can reduce the number of dice rolls needed while still obtaining sufficient entropy by using a key stretching function. Key stretching allows you to take a smaller amount of initial entropy and "stretch" it to produce a larger amount of output that appears random and is difficult to predict



### 2 - Key stretch functions 

Example #2 


One common method for key stretching is the PBKDF2 (Password-Based Key Derivation Function 2) algorithm. PBKDF2 works by repeatedly hashing the input entropy along with a salt value to generate a longer, more complex output.


This example is one used in the bitcoin world to stretch initial randomness into a proper secure key. 



### 3 - how much entropy is enough?


Rsa key is a 256 bit (32 bytes) derived key. This means that we should target the entropy to the key size. 


 The desired derived key is 256 bits.
 
 Each roll of a 6-sided die gives approximately 2.58 bits of entropy.
 
 256 bits / 2.58 bits/roll is around 99.22 rolls or 100 
 
 100 rolls would product 256 bits of intial entropy 
 
 
 
 ** Activity ** 
 
 Please roll 100 dice rolls and place them in your rolls.py file. Be sure to place a comma between the values. 
 
 
 
 ### 4 - Create an rsa key pair 
 
 The provided 4.py should run correctly. But it is still giving a not enough entorpy error. 
The rsa key creation appears to be exchausting the entorpy pool that we provided. Instead of stretching it further we are going to use the original derrrived_key as a seed for a rng. 


 
### 5 - add rng 



 In line 49 we created a random number generator and seeded it with the derived key. This creates a near endless supply of numbers created deterministically from the original entropy source. 
 
 
 You should see output with the following format 
 
 ```
 
 Size of derived_key: 32 bytes
Number of dice rolls: 100
Entropy: b'75182a65d460a9975182a65d460a9975182a65d460a9975182a65d460a9975182a65d460a990'
Derived Key: b'fe3b4fb4e046d215e224a343605b59bc16f307e1d8c07d959cd64af001f93169'
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxLf8F7z4IUQB1CJ5px+r9rpIaPVam94gKo+PbtsScNPl9Yow
ITB6UoVwdoS4f5mHlmKxaOOrfJHMo+kkjIXZrgf1j3iAFkqWHWr+YWl7OppZq/PB
ygjwHGeCWKOkgEcL7rCDU4f/hz7Kv179Nm0IhtDKlEhhdXWOduP/byddr1RuPa5A
qX5DWXnZ+sFl/jvEFfWavNl2EhZO6tIIiCpN2dkRfnKVgYFJI8FwvjLol3mY/RGw
MwHUTs6xFchyMYIZesjcTk6Dbebs+4g4UDFenP4M8+wr9XDH/E1A9/lDZoD+/u/c
pjNNpMAewD7bjjQ7Q9Tyz1Gg+HOo/6t1QQZanQIDAQABAoIBAAZFHZEAug4bYNok
ho9ov15aX4j2FJ8ZSrN4k56Gd07z0T8Zs+eDtOTKi1D0ixavRTOD1HpB0wf7jXpG
KdIcL3NwN84zGpTU6A+qrTSovBLPc4WH+/iaMm1nvWKUX3k8N0ZMFEXjDll+vmkW
y4gCz43QFVWtFrgiJbomq1AdND7GKiSTrX+4hmVqtcREpOnyFsl4v3ilgNja+kqN
lttq3CCoQpryJLPlxcplRqhTjmK0d/ReLYJkmNDsY5X09zQzuDTeAm8fFE6PxWE+
H9Hes1/bT25dirOh+5y1wd/fq0ZZtoxYzs3lglwT1yTUte5GBXdBLSPzvXKTiOVd
3Lgy77kCgYEAzz/3hq22k0S/WOOPjp3iolR2tyC2Kw6T6atAe4BBNaJIPVQrMLF0
6Gy6dgdQmpil0sCGcZ3KxTmmygbKR4lJCKThGhix/gwqHNWLoga2ty6mEUkh6spq
it68vn3qAIR3Bjtz0Eron4i2YdaxstjdLcXGww78+iQ6iy/h9wiT1GUCgYEA8v3b
up1nPA110e/fFoMWDzMbPwl3ck9f0R++SEt6ulZj0ypjrHQfXPNEcli8NoS/zYMH
GhCfHRBQdhAboK0GMrSUnFeVB4fa4hOaU6E7ggz7OnxmZoBnj4de0LmDdM9G9i0s
+B20uHFMxFxvMVm3okPz7GpzywYUskTht8PafdkCgYEAyJ5TLbvakJRr5c/il1ue
lyTMBllT/joOVJPBx8tPVGvTIgroBCrD0HnvxXEvRXeejXRwsGrebixwmAAar0Tl
vchdXrWpFxMPcPoGQMHe/VPazcDNZEqs9+DFNGEOs5GG5jGG2oqoxEXCxtLdERN8
h2J8FTXdDQck5LdlNYzIDUECgYBsdSrSTNd7Una4Udy9a505A5KxvEP4Xb1i1kxU
cHxDF7RO2KjMnLgzANIYR8saen4x+L3+wFSE4HdJez8ZpKETmM6MSftW9SiZqC5G
Db1F+w1XuZbrQXz373A+sc8fIDWIQ/nCdV/ow4mES83FtUnlv3bsm0c742bxexVU
tLKdYQKBgQCN+OW7F78iofqRTrOtYfSlHKd6biyEmWnIcvCythPozzxLllCQWzi2
qbmqWKBiRTPYwKF3VenKcoqDHK8S5J2VULBvaQkQdqKC+1zN/tYQ3EkBwKkEsAGm
jcSLn5M4JhfiR2mdXug41WWSt2+xACzOib/05Ox+TPg+m4zdrDJ9FA==
-----END RSA PRIVATE KEY-----
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxLf8F7z4IUQB1CJ5px+r
9rpIaPVam94gKo+PbtsScNPl9YowITB6UoVwdoS4f5mHlmKxaOOrfJHMo+kkjIXZ
rgf1j3iAFkqWHWr+YWl7OppZq/PBygjwHGeCWKOkgEcL7rCDU4f/hz7Kv179Nm0I
htDKlEhhdXWOduP/byddr1RuPa5AqX5DWXnZ+sFl/jvEFfWavNl2EhZO6tIIiCpN
2dkRfnKVgYFJI8FwvjLol3mY/RGwMwHUTs6xFchyMYIZesjcTk6Dbebs+4g4UDFe
nP4M8+wr9XDH/E1A9/lDZoD+/u/cpjNNpMAewD7bjjQ7Q9Tyz1Gg+HOo/6t1QQZa
nQIDAQAB
-----END PUBLIC KEY-----

```


You know have a public and private RSA key. You can use this to sign and encrypt messages. 


The public key can be given to another user. Now any message you sencrypt to that public key can only be decrypted by the user. 


After running this file you will have the file named "private_key.pem" in your directory. This file is a exported private key that will be utilized by the following scripts. 


### 6 - Encrytping messages 

Let's enrypt a message to somebody's public key. 

For the following exersizes make sure you ran 5.py and have a private_key.pem file. 

Running 6.py will encrypt a message to the public key derived from the private key. Then it will decrypt the message. 


This is a great proof of concept but how edo we use it to send messages to other users?



### 7 - Let's build an encrypted messaging






 
 
 









