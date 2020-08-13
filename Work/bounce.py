# bounce.py
#
# Exercise 1.5

height = 100
factor = float(3/5)

for i in range(1, 11):
    height = height*factor
    print(i, height.__round__(4))
