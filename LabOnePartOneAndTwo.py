#reverse word 
message = input("enter message")
reverse = " "
i = len(message) -1 
while i >= 0:
    reverse = reverse + message[i]
    i = i-1
#shift 
def encrypt_text(reverse, s):
    ans = " "
    
    for i in range(len(reverse)):
        t = reverse[i]
        
        if t== " ":
            ans +=" "   
        else: ans += chr((ord(t) + s-97) %26 + 97)
    return ans
s = 1
print("revese word: " + reverse)
print("with shift: " + encrypt_text(reverse,s ) )   

