def find_dublicate(arry):
    for item in arry:
        if arry[abs(item)] >= 0:
            arry[abs(item)] = -arry[abs(item)]
        else:
            print('repetation found: %s' % str(abs(item)))



if __name__ == '__main__':
    num = [1, 2, 3, 2]
    find_dublicate(num)