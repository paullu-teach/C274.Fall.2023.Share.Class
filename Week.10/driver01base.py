from lec17base import *

# Only text output
def main():
    # s = XYData("Output/driver01")
    s = XYData("driver01")
    print(s)
    s.x([1,2,3,4])
    s.y([2,4,6,8])
    print(s.x())
    print(s.y())
    s.swapxy()
    print(s.x())
    print(s.y())

if __name__ == "__main__":
    main()
