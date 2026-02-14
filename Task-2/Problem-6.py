import string
import random

choices = string.ascii_letters + string.digits

password = ""

for _ in range(8):
    password += random.choice(choices)

print(password)

