# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
#import text
cipher = open('ciphertext.txt').read()

def is_letter(c):
    valid={'A': 'H','B': 'Z','C': 'Y','D': 'W','E': 'O','F': 'R','G': 'J','H': 'D','I': 'P','J': 'T','K': 'I','L': 'G','M': 'L','N': 'C','O': 'E','P': 'X','Q': 'K','R': 'U','S': 'N','T': 'F','U': 'A','V': 'M','W': 'B','X': 'Q','Y': 'V','Z': 'S'}
    if c in valid:
        return True
    else:
        return False

def create_key(s):
    count={}
    order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    # ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}','(',')','*','^','&',' ',]
    # for i in ignore:
        # s=s.replace(i,'') #can use isalpha instead

    #count the letters
    for letter in s:
        # can add this instead of the s.replace
        if is_letter(letter):
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
    count={key: value for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    # print(count)
    for index, key in enumerate(count):
        if index>= len(order):
            continue
        count[key]=order[index]
    return count

def decode(s, key):
    r = ""
    for c in s:
        if c not in key:
            r+=str(c)
        else:
            r += str(key[c])

    return r

key= create_key(cipher)
print(key)
print(decode(cipher, key))