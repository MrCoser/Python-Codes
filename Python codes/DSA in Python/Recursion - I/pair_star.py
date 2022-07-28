
# Online Python - IDE, Editor, Compiler, Interpreter

# Function to insert * at desired position
def pairStar(Input, Output, i = 0) :
     
    # Append current character
    Output = Output + Input[i]
 
    # If we reached last character
    if (i == len(Input) - 1) :
        print(Output)
        return;
 
    # If next character is same,
    # append '*'
    if (Input[i] == Input[i + 1]) :
        Output = Output + '*'
 
    pairStar(Input, Output, i + 1)
 
# Driver code
if __name__ == "__main__" :
 
    Input = input()
    Output = ""
    pairStar(Input, Output)