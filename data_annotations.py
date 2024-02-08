def decode(message_file):
    """
    accepts text (.txt) file and returns deciphered code
    """

    file = open(message_file, 'r')
    lines = file.readlines()

    # Extract and fill 2D list with [number, alphabet_letters] found in txt file
    num_nonnum_list = []
    for line in lines:
        only_numbers = [i for i in line.split() if i.isdigit()]
        only_non_number = [j for j in line.split() if j.isalpha()]
        num_nonnum_list.append([''.join(str(x) for x in only_numbers), ''.join(str(x) for x in only_non_number)])

    # Sort 2D list
    num_nonnum_list = sorted(num_nonnum_list, key=lambda x: int(x[0]))
    # print(num_nonnum_list)

    # extract right-most digit position in pyramid 
    count = 0
    latest_num = 0
    end_of_pyramid_nums = []

    while latest_num < int(num_nonnum_list[-1][0]):
        count += 1
        latest_num += count
        end_of_pyramid_nums.append(latest_num)
    print(end_of_pyramid_nums)

    # decipher the code
    code = ""
    for x in end_of_pyramid_nums:
        code += str(num_nonnum_list[x-1][1]) + " "

    return code

decoded_string = decode("coding_qual_input.txt")
print(decoded_string) # down dont nine lot work silver east duck done tone bit stop sun deal huge moment poem hold make like possible clock of bought