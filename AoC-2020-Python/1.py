
def foo():
    file_input = open('./input_1.txt', 'r')
    input_nums = [int(x) for x in file_input.readlines()]

    len_input = len(input_nums)
    for i in range(len_input):
        num_1 = input_nums[i]
        for j in range(len_input):
            if j+1 >= len_input:
                break

            num_2 = input_nums[j+1]

            if num_1 + num_2 == 2020:
                print(f"The two numbers are {num_1} & {num_2}")
                return num_1 * num_2


def foo2():
    file_input = open('./input_1.txt', 'r')
    input_nums = [int(x) for x in file_input.readlines()]

    len_input = len(input_nums)
    for i in range(len_input):
        num_1 = input_nums[i]
        for j in range(len_input):
            if j+1 >= len_input:
                break
            num_2 = input_nums[j+1]

            for k in range(len_input):
                if k+2 >= len_input:
                    break
                num_3 = input_nums[k+2]

                if num_1 + num_2 + num_3 == 2020:
                    print(f"The three numbers are {num_1} & {num_2} & {num_3}")
                    return num_1 * num_2 * num_3

print(foo2())