# this is the solution for the reverse the integer not array


def reverse_integer(num):
    reverse = 0



    while (num > 0):
        remainder = num % 10
        

        reverse = reverse*10 + remainder
        num = num // 10
    

    return reverse

if __name__ == '__main__':
    num = int(input("enter any intege: "))
    
    print(reverse_integer(num))