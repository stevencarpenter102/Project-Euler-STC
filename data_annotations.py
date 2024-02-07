file = open('coding_qual_input.txt', 'r')
Lines = file.readlines()

# FIND NUMBERS in TXT FILE
count = 0
list_of_numbers_extracted = []
num_nonnum_list = []
for line in Lines:
    only_numbers = [int(i) for i in line.split() if i.isdigit()]
    only_non_number = [str(j) for j in line.split() if j.isalpha()]
    # print(type(only_numbers))
    list = [''.join(str(x) for x in only_numbers), ''.join(str(x) for x in only_non_number)]
    num_nonnum_list.append(list)
    # list_of_numbers_extracted.append(list)
    list_of_numbers_extracted.extend(only_numbers)
    count += 1
    # print("Line{}: {}".format(count, only_numbers))
print(num_nonnum_list, '\n')

# list_of_numbers_extracted.sort()

# print("Largest number in list is: {}", list_of_numbers_extracted[-1])

# EXTRACT RIGHT-MOST PYRAMID NUMBERS
# count = 0
# latest_num = 0
# end_of_pyramid_nums = []

# print(list_of_numbers_extracted[-1])

# while latest_num < list_of_numbers_extracted[-1]:
#     count += 1
#     latest_num += count
#     end_of_pyramid_nums.append(latest_num)

# print(end_of_pyramid_nums)





# list1 = [0,1]
# list2 = [2,3]
# list3 = [list1]
# list3.extend([list2])

# print(list3)