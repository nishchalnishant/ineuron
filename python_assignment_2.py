def first():
    for i in range(1,6):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(4,0,-1):
        for j in range(i):
            print('*',end='')
        print()
            
    
def second():
    first_name=str(input('enter your word'))
    print(first_name[::-1])
    

first()
second()
