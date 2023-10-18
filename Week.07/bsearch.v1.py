# Originally From:  https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

badlist = [17, 13, 19, 8, 2, 1, 0, 32, 42,]
print(binarySearch(badlist, 3))
print(binarySearch(badlist, 13))
print(binarySearch(badlist, 19))

testlist = sorted(badlist)
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print(binarySearch(testlist, 19))

# http://pythontutor.com/visualize.html#code=%23%20From%20runestone.academy%0Adef%20binarySearch%28alist,%20item%29%3A%0A%20%20%20%20first%20%3D%200%0A%20%20%20%20last%20%3D%20len%28alist%29-1%0A%20%20%20%20found%20%3D%20False%0A%0A%20%20%20%20while%20first%3C%3Dlast%20and%20not%20found%3A%0A%20%20%20%20%20%20%20%20midpoint%20%3D%20%28first%20%2B%20last%29//2%0A%20%20%20%20%20%20%20%20if%20alist%5Bmidpoint%5D%20%3D%3D%20item%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20found%20%3D%20True%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20item%20%3C%20alist%5Bmidpoint%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last%20%3D%20midpoint-1%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%20midpoint%2B1%0A%20%20%20%20return%20found%0A%0Abadlist%20%3D%20%5B17,%2013,%2019,%208,%202,%201,%200,%2032,%2042,%5D%0Aprint%28binarySearch%28badlist,%203%29%29%0Aprint%28binarySearch%28badlist,%2013%29%29%0Aprint%28binarySearch%28badlist,%2019%29%29%0A%0Atestlist%20%3D%20sorted%28badlist%29%0Aprint%28binarySearch%28testlist,%203%29%29%0Aprint%28binarySearch%28testlist,%2013%29%29%0Aprint%28binarySearch%28testlist,%2019%29%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
