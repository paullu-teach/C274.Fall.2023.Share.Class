from dog import *

a = Dog()
print(a)
a.wag_tail()

b = Dog(age=2, colour="black", size="Great Dane big")
print(b)

a.bark()
b.bark()
a.bark("even more loudly")
b.bark("loud plus infinity")
