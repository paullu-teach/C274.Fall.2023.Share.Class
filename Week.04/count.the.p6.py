import sys

InputFilename = "file.input.txt"


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        print("File Not Found")
        return(sys.stdin)
    except OSError:
        print("OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            line = f.readline()
            print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


theCount = 0
allWords = 0
nonTarget = []
cFlag = True
inFile = open_file()        # New
while cFlag:
    line, cFlag = safe_input(inFile)
    if not cFlag:
        break
    for w in line.split():
        allWords = allWords + 1
        if w in ['the', 'The']:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
print("All words:%3s. Target words:%3s" % (allWords, theCount))
print("Non-Target words: ", nonTarget)
