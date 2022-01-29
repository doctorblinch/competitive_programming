def countAndSay(n: int) -> str:
    if n == 1:
        return '1'

    s = countAndSay(n-1)
    cur_number = s[0]
    counter = 1
    res = ''

    for i in s[1:]:
        if i == cur_number:
            counter += 1
            continue

        res += f'{counter}{cur_number}'  # faster due to string immutability and memory allocation??
                                         # res = f'{res}{counter}{cur_number}'
        cur_number = i
        counter = 1

    res += f'{counter}{cur_number}'
    return res


if __name__ == '__main__':
    true_answers = [j.strip() for i in """
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221 
    6.     312211
    7.     13112221
    8.     1113213211
    9.     31131211131221
    10.     13211311123113112211
    """.split('\n') if i for j in i.split('     ') if '.' not in j]

    for i in range(1, 11):
        cs = countAndSay(i)
        if cs != true_answers[i-1]:
            print(f'{i}. is not correct!\nTrue output "{true_answers[i-1]}", got "{cs}"')
        else:
            print(f'{i}. {cs}')
