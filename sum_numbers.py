def my_sum(*sayilar):
    total = 0
    
    for i in sayilar :
        total += i
    return total

my_sum(1, 3, 5, 7, 8)
