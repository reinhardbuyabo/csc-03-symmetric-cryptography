from sbox_8fc04ffb95faf5a5e6959195d5e2d94e import *

result = sub_bytes(state, sbox=inv_s_box)
print(bytes([element for row in result for element in row]))