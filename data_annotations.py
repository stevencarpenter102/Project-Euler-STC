file = open('coding_qual_input.txt', 'r')
Lines = file.readlines()
 
count = 0
list_of_numbers_extracted = []
for line in Lines:
    only_numbers = [int(i) for i in line.split() if i.isdigit()]
    # only_non_number = [str(j) for j in line.split() if j.isalpha()]
    # list = [only_numbers, only_non_number]
    # list_of_numbers_extracted.append(list)
    list_of_numbers_extracted.extend(only_numbers)
    count += 1
    print("Line{}: {}".format(count, only_numbers))
    # print(list_of_numbers_extracted, '\n')

list_of_numbers_extracted.sort()

print("Largest number in list is: {}", list_of_numbers_extracted[-1])

count = 0
latest_num = 0
end_of_pyramid_nums = []

print(list_of_numbers_extracted[-1])

while latest_num < list_of_numbers_extracted[-1]:
    count += 1
    latest_num += count
    end_of_pyramid_nums.append(latest_num)

print(end_of_pyramid_nums)



    