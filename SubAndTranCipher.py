import math
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "qwertyuiopmnbvcxzghfjdklsa"
keyword = "keyword"
text = "Fiction is fun"
trans_key = 8
matrix = []
result = ""
#substitution 
for i in text:
    if i.lower() in alphabet:
        result += key[alphabet.find(i.lower())]
    else:
        result += i
print(result)       

#transposition
def encryptMessage(result):
    cipher = " "
    key_index = 0
    res_len = float(len(result))
    res_lst = list(result)
    keyword_lst = sorted(list(keyword))
    
    col = len(keyword)
    row = int(math.ceil(res_len / col))
    
    empty_space = int((row * col) - res_len)
    res_lst.extend('-' * empty_space)
    
    matrix = [res_lst[i: i + col]
              for i in range(0, len(res_lst), col)]
    
    for i in range(col):
        indx = keyword.index(keyword_lst[key_index])
        cipher += ''.join([row[indx]
                       for row in matrix])
        key_index += 1
    return cipher 

print(encryptMessage(result))    
        
        
