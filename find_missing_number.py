

def find_missing_number(number):
    set_number = set(number)
    missing_number= []

    for i in range(1,number[-1]):
        if i not in set_number:
            missing_number.append(i)
    return missing_number

number = [1, 2, 3, 5, 6,7,8, 7, 8, 9, 10, 11, 13, 14, 20]

print(find_missing_number(number))