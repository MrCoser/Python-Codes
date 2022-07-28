
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def pairSum(arr, n, num) :
    arr.sort()

    i = 0
    j = (n - 1)

    numPair = 0

    while i < j :

        if arr[i] + arr[j] < num :
            i += 1

        elif arr[i] + arr[j] > num :
            j -= 1

        else :

            elementAtStart = arr[i]
            elementAtEnd = arr[j]

            if elementAtStart == elementAtEnd :
                totalElementsFromStartToEnd = (j-i) + 1
                numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)

                return numPair

            tempStartIndex = i + 1
            tempEndIndex = j - 1

            while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart) :
                tempStartIndex += 1

            while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd) :
                tempEndIndex -= 1

            totalElementsFromStart = (tempStartIndex - i)
            totalElementsFromEnd = (j - tempEndIndex)

            numPair += (totalElementsFromStart * totalElementsFromEnd)

            i = tempStartIndex
            j = tempEndIndex


    return numPair


#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1