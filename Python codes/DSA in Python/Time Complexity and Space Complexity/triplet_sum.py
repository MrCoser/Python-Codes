
# Online Python - IDE, Editor, Compiler, Interpreter

from sys import stdin

def tripletSum(arr, n, num) :
	#Your code goes here
    
    arr.sort()
    numTriplets = 0
    
    for i in range(n):
        pairSumFor = num - arr[i] 
        numPairs = pairSum(arr, (i+1), (n-1), pairSumFor)
        
        numTriplets += numPairs
        
    return numTriplets

def pairSum(arr, start, end, num):
    
    numPair = 0
        
    while(start < end):
        if(arr[start] + arr[end] < num):
            start += 1
            
        elif(arr[start] + arr[end] > num):
            end -= 1
                
        else:
            elementAtStart = arr[start]
            elementAtEnd = arr[end]

            if elementAtStart == elementAtEnd :
                totalElementsFromStartToEnd = (end - start) + 1
                numPair += (totalElementsFromStartToEnd * (totalElementsFromStartToEnd - 1) // 2)

                return numPair

            tempStartIndex = start + 1
            tempEndIndex = end - 1

            while (tempStartIndex <= tempEndIndex) and (arr[tempStartIndex] == elementAtStart) :
                tempStartIndex += 1

            while (tempEndIndex >= tempStartIndex) and (arr[tempEndIndex] == elementAtEnd) :
                tempEndIndex -= 1

            totalElementsFromStart = (tempStartIndex - start)
            totalElementsFromEnd = (end - tempEndIndex)

            numPair += (totalElementsFromStart * totalElementsFromEnd)

            start = tempStartIndex
            end = tempEndIndex
    
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
    print(tripletSum(arr, n, num))

    t -= 1