


def is_palindrome(s):

    orginal_string = s

    reverse_string = reverse(s)

    if orginal_string == reverse_string:
        return True
    else:
        return False


def reverse(data):

    # string into a list of character
    data = list(data)
    start_index = 0
    end_index = len(data)-1

    while start_index < end_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index -1


    return '' .join(data)


if __name__ == '__main__':
    n = input("enter any text:")
    print(is_palindrome(n))