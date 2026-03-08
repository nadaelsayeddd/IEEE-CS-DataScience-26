# poisson distribution -- x = 5

import math

mean = 2.5
value = 5

probability = (math.exp(-mean) * (mean ** value)) / math.factorial(value)

print(round(probability, 3))