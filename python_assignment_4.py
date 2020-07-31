def area(a,b,c,s):
    return ((s*(s-a)*(s-b)*(s-c))**0.5)

def first():
    a=int(input("Length of first side"))
    b=int(input("Length of second side"))
    c=int(input("Length of third side"))
    s=(a+b+c)/2
    print("Area of triangle is {}".format(area(a,b,c,s)))



def filter_long_words(words,length):
    result=[]
    for i in words:
        if (len(i)>length):
            result.append(i)
    return (result)
    
def second():
    n = int(input("Enter number of words : "))
    words=[]
    for _ in range(n):
        words.append(input("enter the word :"))
    length=int(input("Enter the threshold length "))
    print(filter_long_words(words,length))




def length(word):
    for i in range(len(word)):
        word[i]=len(word[i])
    return(word)

def third():
    n = int(input("Enter number of words : "))
    word=[]
    for _ in range(n):
        word.append(input("enter the word :"))
    print(length(word))


def check(enter):
    if (ord(enter) in [65,69,73,79,85,97,101,105,111,117]):
        return True

def fourth():
    enter=input("enter the alphabet")
    print(check(enter))
    

first()
second()
third()
fourth()                   
