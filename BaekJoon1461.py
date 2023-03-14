def pos_neg_cnt(arr) :
    arr_result = [0, 0]
    for i in range(len(arr)) :
        if arr[i] < 0 :
            arr_result[0] += 1
        else :
            arr_result[1] += 1
    return arr_result

num_and_bring = list(map(int, input().split(' ', 2)))

position_of_book = list(map(int, input().split(' ', num_and_bring[0])))
position_of_book.sort()

cnt_neg = pos_neg_cnt(position_of_book)[0]
cnt_pos = pos_neg_cnt(position_of_book)[1]

if cnt_neg % num_and_bring[1] != 0 :
    