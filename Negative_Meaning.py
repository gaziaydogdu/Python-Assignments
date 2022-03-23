def not_string(x):
    if "not" in x.split():
        return x
    elif not "not" in x.split():
        return ("not "+x)

print(not_string("sugar"))
