# 🔐 Cryptography Systems Implementation

This repository contains educational implementations of three classical public-key cryptosystems:

- ✅ Rabin Cryptosystem  
- ✅ Knapsack Cryptosystem  
- ✅ Diffie-Hellman Key Exchange  

Implemented using **Python** for backend logic and **HTML/CSS/JavaScript** for frontend, with no web frameworks.

---

## 📌 Cryptosystems Overview

### 🔹 Rabin Cryptosystem

**Key Generation:**

- Choose two large prime numbers `p` and `q` such that:  
  - `p ≡ 3 mod 4`  
  - `q ≡ 3 mod 4`
- Compute the public key:  
  - `n = p × q`

**Encryption:**  
- Pad the message, then compute:  
  - `c = m² mod n`

**Decryption:**  
- Use `p` and `q` to compute four square roots of `c mod n` using the Chinese Remainder Theorem.  
- Select the correct root based on the original padding.

---

### 🔹 Knapsack Cryptosystem

**Key Generation:**

- Start with a **super-increasing sequence**, e.g., `[1, 3, 7, 15, 31]`
- Choose:
  - Modulus `m` such that `m > sum(private_key)`
  - Multiplier `n` such that `gcd(n, m) = 1`
- Public key is computed as:  
  - `public_key[i] = (private_key[i] × n) mod m`

**Encryption:**

- Convert message to binary.
- Compute ciphertext as:  
  - `c = Σ (bit[i] × public_key[i])`

**Decryption:**

1. Compute modular inverse: `n⁻¹ mod m`
2. Calculate: `x = (ciphertext × n⁻¹) mod m`
3. Solve the subset-sum problem using the private key to retrieve the binary message.

---

### 🔹 Diffie-Hellman Key Exchange

**Public Parameters:**

- Prime number `P`
- Primitive root `g` of `P`

**Private Keys:**

- Alice chooses secret `a`
- Bob chooses secret `b`

**Public Key Computation:**

- Alice: `A = gᵃ mod P`
- Bob: `B = gᵇ mod P`

**Shared Secret Key:**

- Alice computes: `k = Bᵃ mod P`
- Bob computes: `k = Aᵇ mod P`
- Result:  
  - `k = gᵃᵇ mod P = gᵇᵃ mod P`

---

## 🛡️ Attacks on Cryptosystems

### 🔸 Trivial Division (Rabin Cryptosystem)

The **Trivial Division** factorization algorithm attempts to factor a composite number by dividing it successively by integers starting from `2`.

In the context of Rabin Cryptosystem:

- If an attacker can factor the public key `n = p × q`, they can retrieve the private keys `p` and `q`.
- Once `p` and `q` are known, any encrypted message `c = m² mod n` can be decrypted.

**Mitigation:**  
Use sufficiently large primes to make factorization computationally infeasible.

---

### 🔸 Small Subgroup Attack (Diffie-Hellman)

This attack occurs when the public base `g` lies in a **small subgroup** of the group modulo `P`.

- An attacker exploits the limited number of possible shared keys due to the small order of `g`.
- This can allow brute-forcing the shared secret.

**Preventive Measures:**

- Ensure that `P − 1` has a large prime factor.
- Choose `g` such that it generates a large-order subgroup of `Zₚ*`.

---

### 🔸 Man-in-the-Middle Attack (Diffie-Hellman)

A third-party attacker (e.g., Oscar) can intercept and manipulate the key exchange.

#### Attack Process:

1. Alice sends `A = gᵃ mod P` to Bob — Oscar intercepts it.
2. Oscar generates:
   - Private keys: `o₁`, `o₂`
   - Public keys: `w₁ = gᵒ¹ mod P`, `w₂ = gᵒ² mod P`
3. Oscar sends `w₁` to Bob, pretending to be Alice.
4. Bob replies with `B = gᵇ mod P` — Oscar intercepts it.
5. Oscar sends `w₂` to Alice, pretending to be Bob.
6. Now:
   - Alice computes: `k₁ = w₂ᵃ mod P`, Oscar computes: `k₂ = Aᵒ² mod P`
   - Bob computes: `k₄ = w₁ᵇ mod P`, Oscar computes: `k₃ = Bᵒ¹ mod P`

Oscar now knows both shared keys and can:

- Decrypt messages from Alice.
- Re-encrypt them using Bob’s key.
- Fully impersonate both sides without detection.

**Mitigation:**

- Use digital signatures or authenticated key exchange protocols to verify identities.

---

## 🚀 How to Use

### Requirements

- Python 3.x
- Any modern browser (for frontend demo)

### Run Python Scripts

```bash
python3 rabin.py
python3 knapsack.py
python3 diffie_hellman.py
