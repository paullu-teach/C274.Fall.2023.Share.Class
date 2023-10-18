class VStore:
    def __init__(self):
        self.value = []             # NOTE:  Uses a list
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
        return

    # Overrides VStore.find()
    def find(self, value):
        self.value = sorted(self.value)     # FIXME expensive

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

    vsL = VStore()
    vsB = VStoreBSearch()

    for i in range(10000000):   # 10 000 000 ==10 million
        vsL.add(i)
        vsB.add(i)

    print("\nFind 1:")
    vsL.find(1)
    vsB.find(1)

    # New code here (and elsewhere)

    return


if __name__ == "__main__":
    main()


