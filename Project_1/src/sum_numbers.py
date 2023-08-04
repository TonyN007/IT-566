def sum_numbers():
    user_input = input('Enter a series of numbers with spaces: ')
    string_array = user_input.split()
    print(string_array)

    float_array = [0] *len(string_array)

    i = 0
    for s in string_array:
        float_array[i] = float(s)
        i += 1

    print(f'{float_array} ')
    print(f' Sum = {sum(float_array)}')


def main():
    sum_numbers()

if __name__ == '__main__':
    main()