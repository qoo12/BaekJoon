input_cnt = int(input())
sorting_dict = {}

for i in range(input_cnt) :
    input_words = input()
    sorting_dict[input_words] = len(input_words)

sorted_dict = sorted(sorting_dict.items(), key = lambda item : (item[1], item[0]))

len_cnt = sorted_dict[-1][1]

for i in range(len(sorted_dict)) :
    print(sorted_dict[i][0])