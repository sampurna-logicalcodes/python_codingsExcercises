# 6.list of multiples of first element with second element consecutive items
def list_of_multiples(num,length):
    return[i*num for i in range(1,length+1)]
print(list_of_multiples(5,5))
