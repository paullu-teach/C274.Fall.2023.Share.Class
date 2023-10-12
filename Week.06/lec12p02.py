class Cat(Dog):
    def __init__(self, age=0, colour="brown", size="medium"):
        self.age = age
        self.colour = colour
        self.size = size

    def __str__(self):
        s = "I am a " + self.colour + " cat, of age "
        s += str(self.age) +  ", of size " + self.size
        return(s)

    def __repr__(self):
        s = "Id<"+ str(id(self)) + "> " + self.colour + " cat"
        return(s)

    def meow(self, speed="loudly"):
        print("I am meowing", speed, "said the", self.colour, "cat!")
