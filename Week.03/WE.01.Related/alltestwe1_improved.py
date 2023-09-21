# Copyright 2023 Paul Lu
# Python Intro Labs covers import
from passwordvalidate import *

# If your solutions passes the tests with either this version,
#   or the version given to your originally, then you will get full marks.
#   These next 2 lines of code are relevant if the input files are missing,
#   which will not be the case when we test.
import sys
Debug = True

def open_file(filename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)

if __name__ == "__main__":
    #
    # Use tests from input file
    #
    f = open_file("./input.txt")
    in_passwords = f.readlines()
    f.close()

    f = open_file("./output.txt")
    out_answer = f.readlines()
    f.close()

    all_tests = zip(in_passwords,out_answer)
    for p, a in all_tests:
        p = p.strip()
        a = a.strip()
        r = validate(p)
        if r == a:
            print("  Passed:  %s | %s == %s" % (p,r,a))
        else:
            print("* Failed:  %s | %s != %s" % (p,r,a))
