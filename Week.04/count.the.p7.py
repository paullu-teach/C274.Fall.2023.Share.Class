import sys

Debug = True   # Sometimes, print for debugging
InputFilename = "file.input.txt"
OutputFilename = "file.output.txt"


def open_file(filename=InputFilename):
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


def open_output(filename=OutputFilename):
    try:
        f = open(filename, "w")
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


def safe_input(f=None, out=None, prompt=""):
    if out is None:
        out = sys.stdout
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            line = f.readline()
            if Debug:
                print("readline: ", line, file=out, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF", file=out)
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


theCount = 0
allWords = 0
nonTarget = []
cFlag = True
inFile = open_file()
outFile = open_output()
while cFlag:
    line, cFlag = safe_input(inFile, outFile)
    if not cFlag:
        break
    for w in line.split():
        allWords = allWords + 1
        if w in ['the', 'The']:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
print("All words:%3s. Target words:%3s" % (allWords, theCount), file=outFile)
print("Non-Target words: ", nonTarget, file=outFile)
