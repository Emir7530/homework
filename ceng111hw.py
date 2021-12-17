import random
#CENG113_HW3_GroupID.py
#Bora Ersoy 280201024
#Emir Kaldirimci 280201036


def is_frame(a):



def is_spare(a,b):
def is_open(a,b):
def main():
    list=['A','B']
    first_player=random.choice(list)
    newlist=list.remove(first_player)
    second_player=newlist[0]
    first=[]
    second=[]
    a=int(input('Pins:'))
    count=0
    if a!=10:
        b=int(input('Pins:'))
    

    
        while a >10 or a<0:
            
            a=int(input('An invalid input. Pins:'))
        while b>10 or b<0:
            
            b=int(input('An invalid input. Pins:'))
        
        if a+b==10:
            count+=1
            is_spare(a,b)
        elif a+b<10:
            count+=1
            is_open(a,b)
    elif a==10:
        count+=1
        is_frame(a)
    sum=0
    sum2=0
    for i in first:
        sum+=i
    for b in second:
        sum2+=b
    if sum>sum2:
        print('winner is',first_player)
    else:
        print('winner is',second_player)




main()

            
