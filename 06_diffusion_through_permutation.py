from diffusion_ee6215282094b4ae8cd1b20697477712 import *

# Complete Inverse Shift Rows

# Run inverse mix columns on the state
inv_mix_columns(state)
# Run inverse shift rows on the state
inv_shift_rows(state)
# Convert to bytes
print(bytes([state[i][j] for i in range(4) for j in range(4)]))