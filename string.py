# Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.
def comparision(a,b):
    if a.upper() == b.upper():
        print('True')
    elif (a.find(b) != -1):
        print('True')
    else:
        print('False')

def main():
    a = input('Enter first string : ')
    b = input('Enter second string : ')
    comparision(a,b)

if __name__ == '__main__':
    main()