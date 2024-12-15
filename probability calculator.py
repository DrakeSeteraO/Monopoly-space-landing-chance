def create_list(turns: int) -> list:
    lst = [[0 for i in range(turns)] for j in range(turns * 12)]
    for i in range(7):
        lst[i][0] = i
    for i in range(7):
        lst[i+6][0] = 6 - i
    return lst


def calculate_amount(lst: list, turns: int) -> list:
    for i in range(turns * 12):
        for j in range(turns - 1):
            total = 0
            if lst[i][j + 1] == 0:
                for k in range(1, 12):
                    l = i - k - 1
                    if 0 <= l:
                        if k < 6:
                            total += lst[l][j] * k
                        else:
                            total += lst[l][j] * (12 - k)
                lst[i][j + 1] = total
    return lst


def calculate_totals(lst: list):
    sums = [0] * 40
    for i in range(len(lst)):
       sums[i % 40] += sum(lst[i]) 
    return sums, sum(sums)


def create_dictionary(sums):
    out = dict()
    for i in range(len(sums)):
        out[sums[i]] = i
    return out

def main():
    turns = int(input('How many turns would you like to calculate for? '))
    amount = create_list(turns)
    amount = calculate_amount(amount, turns)
    sums, total = calculate_totals(amount)
    amount_to_space = create_dictionary(sums)
    sums.sort(reverse=True)
    print(f'\nAfter calculating all the possibilities for {turns} turns\nThe results are:\n\t\tTotal: {total:>108,}')
    for s in sums:
        print(f'Space: {amount_to_space[s]}\tpossibilities: {s:>100,}')
            
    

if __name__ == '__main__':
    main()