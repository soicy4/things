import random

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "{}!()$\_#@%*"

all = a + b + c + d
length = 8
password = "".join(random.sample(all,length))
print(password)
input()
