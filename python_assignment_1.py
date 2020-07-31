def first():
    print('FIRST')
    for i in range(2,1200,7):
        if(i%5!=0):
            print(i+2000,end=',')
    
def second():
    print(end='\n')
    print('SECOND')
    first_name=str(input('enter your first name'))
    second_name=str(input('enter your second name'))
    print(first_name[::-1]+' '+second_name[::-1])
    

def third():
    print('THIRD')
    d=12
    print((4*3.14*pow(d/2,3))/3)

first()
second()
third()    

    

      


