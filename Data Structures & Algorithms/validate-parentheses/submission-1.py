# create a dictionary with all the brackets, in it
#loop through the string,
#push the brackets into the stack, 
#pop them in order, if not equal to the prev, return false 
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s: 
    #if opening append immediately, if closing: mcompare with the most recent thing in the stack then pop if similar
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                  stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
    
            
        




        
    

        




       


        




