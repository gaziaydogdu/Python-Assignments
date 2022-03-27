def missing_char(word, n):
    str1 = word[:n]
    str2 = word[n+1:]
    result = str1 + str2
    return result

missing_char("gazi",1)
