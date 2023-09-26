import sys

Debug = False   # Sometimes, print for debugging
InputFilename = "file.input.txt"


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if True or Debug:   # Always on
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


def main():
    # Important scope implications of using main()
    theCount = 0
    allWords = 0
    nonTarget = []
    inFile = open_file()
    assert not (inFile is None), "Assume valid file object"

    cFlag = True
    while cFlag:
        line, cFlag = safe_input(inFile)
        if not cFlag:
            break
        assert cFlag, "Assume valid input hereafter"
        for w in line.split():
            allWords = allWords + 1
            if w in ['the', 'The']:
                theCount = theCount + 1
            elif w != '':
                if w not in nonTarget:
                    nonTarget.append(w)
    print("All words:%3s. Target words:%3s" % (allWords, theCount))
    print("Non-Target words: ", nonTarget)


if __name__ == "__main__":
    main()
