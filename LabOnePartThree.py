#shift even and odd
def shift_text(even_shift, odd_shift):
    message_two = input('enter message')
    print("original message: " + message_two )  
    
    
    for i in range(len(message_two)):
        if (i%2)==0:
            res = ''.join(chr((ord(char) - 97 - even_shift) % 26 + 97 )for char in message_two)
        else: 
            res = ''.join(chr((ord(char) - 97 - odd_shift) % 26 + 97 ) for char in message_two)
    return res     

even_shift = 5
odd_shift = 2
print("string after shift:" + shift_text(even_shift, odd_shift))

