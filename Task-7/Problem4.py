# normal distribution 
# mean = 20 hours , std = 2 hours
# p(x<19.5) , p(20<x<22)


import math
mean = 20
std = 2
def normal_cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

probability = normal_cdf(19.5)
print(round(probability, 3))

probability = normal_cdf(22) - normal_cdf(20)
print(round(probability, 3))