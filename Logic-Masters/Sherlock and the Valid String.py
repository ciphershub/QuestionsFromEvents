def isValid(s):
    # Write your code here
    from collections import Counter
    counter = sorted(list(Counter(s).items()), key=lambda x: x[1], reverse=True)
    pat = counter[0][1]
    b = all(v == pat for _, v in counter)
    b1 = all(v == pat - 1 for _, v in counter[1:])
    b2 = all(v == pat for _, v in counter[:-1]) and counter[-1][1] == 1
    return ('NO', 'YES')[b or b1 or b2]