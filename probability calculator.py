def main():
    turns = 30
    amount = [0] * (turns * 12)
    amount = first_12(amount)
    for i in range(13,len(amount)):
        a = amount[i-2]
        b = 2 * amount[i-3]
        c = 3 * amount[i-4]
        d = 4 * amount[i-5]
        e = 5 * amount[i-6]
        f = 6 * amount[i-7]
        g = 5 * amount[i-8]
        h = 4 * amount[i-9]
        j = 3 * amount[i-10]
        k = 2 * amount[i-11]
        l = amount[i-12]
        amount[i] = a + b + c + d + e + f + g + h + j + k + l
    
    total = sum(amount)
    total_of_each_space = [0] * 40
    for i in range(len(amount)):
        total_of_each_space[i % 40] += amount[i]
    
    average_of_each_space = [0] * 40
    amount_to_space = dict()
    for i in range(len(total_of_each_space)):
        average_of_each_space[i] = total_of_each_space[i] / total
        amount_to_space[average_of_each_space[i]] = i
    
    average_of_each_space.sort(reverse=True)
    print('The most common spaces from most likely to least likely are')
    for val in average_of_each_space:
        percentage = val * 100
        print(f'Space: {amount_to_space[val]}\tPercentage: {percentage} %')
        
def first_12(lst: list) -> list:
    lst[2] = 1
    lst[3] = 2
    lst[4] = 4
    lst[5] = 8
    lst[6] = 16
    lst[7] = 32
    lst[8] = 62
    lst[9] = 124
    lst[10] = 246
    lst[11] = 488
    lst[12] = 968
    return lst

if __name__ == '__main__':
    main()