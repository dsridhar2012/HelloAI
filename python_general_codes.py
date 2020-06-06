def swap_case(s):
    for i in range(0, len(s)-1):
        if(s[i].isupper()== True):
           a.append(s[i].lower())
        else:
           a.append(s[i].upper())
    return a


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)