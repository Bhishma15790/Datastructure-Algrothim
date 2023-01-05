#it is for the reverse given array or lists

def reverse(number):
    start_index = 0
    end_index = len(number)-1

    while start_index < end_index:
        number[start_index], number[end_index] = number[end_index], number[start_index]
        start_index = start_index + 1
        end_index = end_index -1

if __name__  ==  '__main__':
    n = [2,4,5,6,7]
    reverse(n)
    print(n)

