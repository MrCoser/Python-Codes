
# Online Python - IDE, Editor, Compiler, Interpreter

def maximumProfit(arr, n):
	#Implement Your Function here
    max = 0
    arr.sort()
    for i in arr:
        if max < i*n:
            max = i*n
        
        n = n - 1
    return max

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr, n)
print(ans)