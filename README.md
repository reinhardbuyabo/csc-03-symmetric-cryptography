# SYMMETRIC ENCRYPTION

## 1. Keyed Permutations

## 2. Resisting Bruteforce
- Biclique Attack

## 3. Structure of AES
### Phases of AES
1. Key Expansion || Key Schedule

2. Initial key addition
- AddRoundKey - the bytes of the first round key are XOR'd with the bytes of the state.

- Write a matrix2bytes function **to turn that matrix back into bytes**, and submit the resulting plaintext as the flag
- Converting plain text into a state matrix.
- Matrix to bytes
```python

```
- Output:
```bash
b'c\x00\x00\x00r\x00\x00\x00y\x00\x00\x00p\x00\x00\x00t\x00\x00\x00o\x00\x00\x00{\x00\x00\x00i\x00\x00\x00n\x00\x00\x00m\x00\x00\x00a\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00x\x00\x00\x00}\x00\x00\x00'
b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00'
```
- Flattening a Matrix: `print([element for row in matrix for element in row])`

## 4. Round Keys
- 16 byte key to produce 11 4*4 matrices called Round Keys derived from the initial key.
- Round Keys -> Extra Mileage.
- AddRoundKey XORs the current state with the current round key.
- 

# 5. Confusion through Substitution
-  the relationship between the ciphertext and the key should be as complex as possible.
- `print(chr(sbox[i][j]), end="")`

# 6. Diffusion Through Permutation
- This relates to how every part of a cipher's input should spread to every part of the output.
- After implementing `inv_shift_rows`, take the state, run `inv_mix_columns` on it, then `inv_shift_rows`, convert to bytes and you will have your flag.

