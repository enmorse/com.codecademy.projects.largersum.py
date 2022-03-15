# Write your function here
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for i in lst2:
        sum2 += i
    return lst1 if sum1 >= sum2 else lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))
