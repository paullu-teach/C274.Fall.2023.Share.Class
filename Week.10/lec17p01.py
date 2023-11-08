# Copyright 2023 Paul Lu

import matplotlib.pyplot as xyplt

class XYSingle:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
        return

    def x(self,data=None):
        if data is None:
            return self.__x
        else:
            self.__x = data
        return

    def y(self,data=None):
        if data is None:
            return self.__y
        else:
            self.__y = data
        return

    def __str__(self):
        s = "XYSingle" + str(self.x()) + " " + str(self.y())
        return s

    def __repr__(self):
        s = "Id<"+ str(id(self)) + ">" + str(self.x()) + " " + str(self.y())
        return s


class XYData:
    def __init__(self,name=""):
        self.__array = []
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

    def dump(self):
        # print(self.__array)
        print("x","y",self.name())
        for i in self.__array:
            print(i.x(), i.y())
        return

    def x(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        if len(data) == 0:              # Getter
            l = []
            for i in self.__array:
                l.append(i.x())
            return(l)
        elif type(data) is list:        # Setter
            y = self.y()
            l = []
            for i in range(len(data)):
                if len(y) <= i:
                    oldY = 0
                else:
                    oldY = y[i]
                xy = XYSingle(data[i],oldY)
                l.append(xy)
            self.__array = l.copy()
            return(len(data))

        assert False, "Should not be here: x"
        return None

    def y(self,data=[]):
        # HINT: Borrow idea from Lecture 14 worksheet, polymorphism
        if len(data) == 0:
            l = []
            for i in self.__array:
                l.append(i.y())
            return(l)
        elif type(data) is list:
            x = self.x()
            l = []
            for i in range(len(data)):
                if len(x) <= i:
                    oldX = 0
                else:
                    oldX = x[i]
                xy = XYSingle(oldX,data[i])
                l.append(xy)
            self.__array = l.copy()
            return(len(data))
        assert False, "Should not be here: x"
        return None


    def plotpng(self):
        xyplt.figure(figsize=(8, 4))
        xyplt.scatter(self.x(), self.y(), label=self.name())
        xyplt.legend([" x "], loc="upper left")
        xyplt.savefig(self.name() + ".png")
