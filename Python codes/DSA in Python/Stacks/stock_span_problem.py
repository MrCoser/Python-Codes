
# Online Python - IDE, Editor, Compiler, Interpreter

def calculateSpan(price, S): 
      
    n = len(price)  
    st = []  # empty stack declared 
    st.append(0) 
    S[0] = 1
    for i in range(1, n): 
        while(len(st) > 0 and price[st[-1]] < price[i]): #here i done changes
            st.pop()
            
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])  
        st.append(i) 
        
        
        
        
def printArray(arr, n): 
    for i in range(0, n): 
        print (arr[i], end =" ") 

        


# main
m=int(input())  
price =[int(price) for price in input().split()]
S = [0 for i in range(len(price)+1)] 
  
calculateSpan(price, S) 
printArray(S, len(price))