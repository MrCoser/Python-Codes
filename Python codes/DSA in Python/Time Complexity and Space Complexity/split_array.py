
# Online Python - IDE, Editor, Compiler, Interpreter

# Given an integer array A of size N, check if the input array
# can be splitted in two parts such that -
# - Sum of both parts is equal
# - All elements in the input, which are divisible by 5 should be in same group.
# - All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
# - Elements which are neither divisible by 5 nor by 3, can be put in any group.

def help(arr, n, start, lsum, rsum):
 
    #Base case for our recursive call
    if (start == n):
        return lsum == rsum
 
    # If divisible by 5 then add
    # to the left sum
    if (arr[start] % 5 == 0):
        lsum += arr[start]
 
    # If divisible by 3 but not by 5
    # then add to the right sum
    elif (arr[start] % 3 == 0):
        rsum += arr[start]
 
    # Else it can be added to any of
    # the sub-arrays
    else:
 
        return (help(arr, n, start + 1,
                lsum + arr[start], rsum) or
                help(arr, n, start + 1,
                lsum, rsum + arr[start]));
 
    # For cases when element is multiple of 3 or 5.
    return help(arr, n, start + 1, lsum, rsum)

def split(arr, n):
    return help(arr, n, 0, 0, 0)
    
    
n = int(input())
arr = [int(ele) for ele in input().split()]
ans = split(arr, n)
if ans is True:
    print('true')
else:
    print('false')