class VStore:
    def __init__(self):
        self.store = dict()
        return
    # FIXME add __str__() and __repr()__

    def add(self, value):
        # Make add() polymorphic by checking type
        # print(type(value))
        # NOTE: Python has isinstance()
        if type(value) is int:
            self.store[value] = True
        elif type(value) is list:
            for v in value:     # FIXME Probably a faster way
                self.store[v] = True
        else:
            print("add() cannot handle", type(value))
        return

    def find(self, value):
        if value in self.store:
            return True
        else:
            return False

    def delete(self, value):
        if value in self.store:
            del self.store[value]
            return True
        else:
            return False

    def print_all(self):
        print(self.store.keys())


def main():
    vs = VStore()

    vs.add(95)
    vs.add(90)
    vs.add(85)
    print(vs.find(90))
    print(vs.find(85))
    print(vs.delete(85))
    print(vs.find(85))
    print(vs.delete(70))
    vs.print_all()

    vs.add([1, 2, 3])
    vs.print_all()
    vs.add((4, 5, 6))
    return

if __name__ == "__main__":
    main()
