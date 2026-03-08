import math
# n = 6
# only two outcomes -- boy or girl  -- binomial distribution

# p for boy 
p = 1.09 / (1.09 + 1)
# for girl
q = 1 - p

n = 6
probability = 0
for i in range(3, 7):
    probability += math.comb(n, i) * (p ** i) * (q ** (n - i))

print(round(probability, 3))

