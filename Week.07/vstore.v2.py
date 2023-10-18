class VStore:
    def __init__(self):
        self.value = []         # NOTE:  Uses list
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
    return

if __name__ == "__main__":
    main()
