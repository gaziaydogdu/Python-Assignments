sentence = input("enter a sentence: ")
processed = {}

for i in sentence :
    if i in processed :
        processed[i] += 1
    else :
        processed[i] = 1

print(processed)
