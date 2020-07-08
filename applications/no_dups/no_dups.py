def no_dups(s):
    #alternatively we could use a set here instead of a dict, but were practicing the latter
    unique_words={}
    result=''
    s = s.split()
    for word in s:
        if word not in unique_words:
            unique_words[word]=True
    for k,v in unique_words.items():
        result+=' ' + k
    if result == '':
        return ''
    else:
        return result[1:]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))