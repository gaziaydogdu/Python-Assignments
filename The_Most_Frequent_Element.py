def most_freq(*x) :

    if list(x[0]).count(max(list(x[0]), key=list(x[0]).count)) > 1:
        return max(list(x[0]), key=list(x[0]).count)
    else :
        return 0
