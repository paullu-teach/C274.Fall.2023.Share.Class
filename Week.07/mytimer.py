import time
import random

class TimeObj():
    def __init__(self, msg=""):
        self._msg = msg
        self._start = time.perf_counter()
        self.tick()
        self.tock()

    def tick(self,print_clock=False):
        self._tick_save = time.perf_counter()

    def tock(self,print_clock=False):
        self._tock_save = time.perf_counter()
        if(print_clock):
            print(self._msg,self.__str__())

    def __str__(self):
        assert(self._tock_save > self._tick_save), "Non-monotonic"
        t = self._tock_save - self._tick_save
        assert(float(t)>0.0), "Non-monotonic 2"
        s = ("%f" % (t)) + "s"
        return(s)


# Not the cleverest way to do this
def rand_list_ints(l,num):
    for i in range(num):
        l.append(random.randint(0,10000000))


def test_main():
    a = TimeObj("All:")

    b = TimeObj("Create:")
    my_list = []
    rand_list_ints(my_list,1000000)
    b.tock(True)

    c = TimeObj("Sort:")
    c.tick()
    my_list.sort()
    c.tock()

    print("Sorting:",c)

    a.tock(True)

if __name__ == "__main__":
    test_main()
