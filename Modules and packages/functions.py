def chkEven(num):
    if(num % 2 == 0):
        return True
    else:
        return False
    

def chkPos(num):
    if(num > 0):
        return True
    else:
        return False
    

if(__name__ == '__main__'):
    print('testing.......')
    print(chkeven(10))

    print(__name__)  

    # if you run same file - __main__
                    
    # if you run different file - file_name
