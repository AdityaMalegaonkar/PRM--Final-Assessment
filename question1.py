def sorted_lst(lst , n):
    lst.sort()
    temp_lst = [0] * (n+1)
    lst_index = 0
    i = n-1
    j = 0
    while(i > n // 2 or j < n // 2):
        temp_lst[lst_index] = lst[i]
        lst_index += 1
        temp_lst[lst_index] = lst[j]
        lst_index += 1
        i -= 1
        j += 1

    for i in range(0 , n):
        lst[i] = temp_lst[i]

lst = [int(item) for item in input("Enter the items of list seperated by space : ").split()]
n = len(lst)
sorted_lst(lst , n)
for i in range(0 , n):
    print(lst[i] , end = " ")