file = open('coding_qual_input.txt', 'r')
Lines = file.readlines()

# FIND NUMBERS in TXT FILE
count = 0
list_of_numbers_extracted = []
num_nonnum_list = []
for line in Lines:
    only_numbers = [int(i) for i in line.split() if i.isdigit()]
    only_non_number = [str(j) for j in line.split() if j.isalpha()]
    list = [''.join(str(x) for x in only_numbers), ''.join(str(x) for x in only_non_number)]
    num_nonnum_list.append(list)
    list_of_numbers_extracted.extend(only_numbers)
    count += 1

# SORT 2D LIST with each list in form: [number, word]
num_nonnum_list = sorted(num_nonnum_list, key=lambda x: int(x[0]))
# print(num_nonnum_list)

list_of_numbers_extracted.sort()
# print("Largest number in list is: {}", list_of_numbers_extracted[-1])

# EXTRACT RIGHT-MOST PYRAMID NUMBERS
count = 0
latest_num = 0
end_of_pyramid_nums = []

# print(list_of_numbers_extracted[-1])

while latest_num < list_of_numbers_extracted[-1]:
    count += 1
    latest_num += count
    end_of_pyramid_nums.append(latest_num)

# print(end_of_pyramid_nums)
next_string = ""
for num in end_of_pyramid_nums:
    next_string += str(num_nonnum_list[num-1][1]) + " "

print(next_string)
