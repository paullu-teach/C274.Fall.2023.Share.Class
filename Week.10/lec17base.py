# Copyright 2023 Paul Lu

import matplotlib.pyplot as xyplt

class XYData:
    def __init__(self,name=""):
        self.__x = []
        self.__y = []
        self.__name = name
        return

    def __str__(self):
        s = "XYData: " + self.name()
        return s

    def __repr__(self):
        s = "Id<"+ str(id(self)) + "> " + self.name()
        return s

    def name(self):
        return(self.__name)

    def swapxy(self):
        # x = self.__x
        # y = self.__y
        x = self.x()
        y = self.y()
        self.x(y)
        self.y(x)
        return

    def x(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        if len(data) == 0:
            return(self.__x)
        elif type(data) is list:
            self.__x = data.copy()
            assert self.__x is not data, "Not copied"
            return(len(data))

        assert False, "Should not be here: x"
        return None

    def y(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        if len(data) == 0:
            return(self.__y)
        elif type(data) is list:
            self.__y = data.copy()
            assert self.__y is not data, "Not copied"
            return(len(data))

        assert False, "Should not be here: y"
        return None

    def plotpng(self):
        xyplt.figure(figsize=(8, 4))
        xyplt.scatter(self.x(), self.y(), label=self.name())
        xyplt.legend([" x "], loc="upper left")
        xyplt.savefig(self.name() + ".png")
