class VStore:
    def __init__(self):
        self.value = []
        return
    # FIXME add __str__() and __repr()__

    def add(self, value):
        self.value.append(value)
        return

    def find(self, value):
        i = 0
        while i < len(self.value):
            if self.value[i] == value:
                return True
            else:
                i += 1
        return False

    def delete(self, value):
        i = 0
        while i < len(self.value):
            if self.value[i] == value:
                del self.value[i]
                return True
            else:
                i += 1
        return False

    def print_all(self):
        print(self.value)


class VStoreBSearch(VStore):
    def __init__(self):
        # https://realpython.com/python-super/
        super().__init__()
        self.needsSorting = False
        return

    # Overrides VStore.add()
    def add(self, value):
        self.needsSorting = True
        return(super().add(value))

    # Overrides VStore.delete()
    def delete(self, value):
        self.needsSorting = True
        return(super().delete(value))

    # Still inherits VStore.print_all()

    # Overrides VStore.find()
    def find(self, value):
        if self.needsSorting:
             print("* Sort")
             self.value = sorted(self.value)     # FIXED:  FIXME expensive
             self.needsSorting = False
        
        # FIXME:  How might one avoid cloing the code below??

        # Originally From:  https://runestone.academy/runestone/
        #    books/published/pythonds/SortSearch/TheBinarySearch.html
        first = 0
        last = len(self.value)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if self.value[midpoint] == value:
                found = True
            else:
                if value < self.value[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found


def main():
    vs = VStoreBSearch()

    vs.add(95)
    vs.add(90)
    vs.add(85)
    print(vs.find(90))
    print(vs.find(85))
    print(vs.delete(85))
    print(vs.find(85))
    print(vs.delete(70))
    vs.print_all()

    vs2 = VStoreBSearch()
    vs2.add(17)
    vs2.add(13)
    vs2.add(19)
    vs2.add(8)
    vs2.add(2)
    vs2.add(1)
    vs2.add(0)
    vs2.add(32)
    vs2.add(42)
    print("->", vs2.find(3))
    print("->", vs2.find(13))
    print("->", vs2.find(19))
    vs2.print_all()
    vs.print_all()
    return


if __name__ == "__main__":
    main()
