def del_duplicate(arr) :
    for i in range(len(arr)) :
        store = arr[i]
        arr.remove(arr[i])
        arr.append(store)
    
def len_sorting(arr) :
    for i in range(len(arr)-1) :
        j = i+1
        while len(arr[j-1]) > len(arr[j]) and j > 0 :
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

def dict_sorting(arr) :
    i = 0
    j = 1
    while i < len(arr) :
        while len(arr[i]) == j :
            b = i+1
            while arr[b-1] > arr[b] and b > 0 :
                arr[b-1], arr[b] = arr[b], arr[b-1]
                b -= 1
            j += 1
'''
잘못된 알고리즘으로 time out이 나와서 다른 코드를 짤 것임
'''
input_cnt = int(input())
sorting_list = []

for i in range(input_cnt) :
    sorting_list.append(input())

del_duplicate(sorting_list)
len_sorting(sorting_list)
dict_sorting(sorting_list)

for i in range(len(sorting_list)) :
    print(sorting_list[i])