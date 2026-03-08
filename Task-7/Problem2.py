# 12% pistons rejected --p
# batch of 10 pistons -- n
# p <= 2 , p => 2

import math

p = 0.12
q = 1 - p
n = 10

probability = 0
for i in range(0, 3):
    probability += math.comb(n, i) * (p ** i) * (q ** (n - i))

print(round(probability, 3))

probability = 1 - (math.comb(n, 0) * (p ** 0) * (q ** (n - 0)) + math.comb(n, 1) * (p ** 1) * (q ** (n - 1)))

print(round(probability, 3))