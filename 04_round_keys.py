from add_round_key_b67b9a529ae739156107a74b14adde98 import *

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    return [[sss^kkk for sss, kkk in zip(ss, kk)] for ss, kk in zip(s, k)]

print(add_round_key(state, round_key))
matrix = add_round_key(state, round_key)
print(bytes([element for row in matrix for element in row]))