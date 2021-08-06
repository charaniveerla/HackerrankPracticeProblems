"""
TCS DIGITAL 2022 ADV. CODING SAMPLE QUESTION 

https://www.youtube.com/watch?v=9hy0aTlXsJw

Goto the above Link for Detailed Question, Constarints and Input cases!
"""
n=int(input())
match=[]
size=(n*(n-1))//2
scores=[0]*256
for i in range(0,size):
    match=list(map(str,input().split()))
    home=match[0]
    away=match[1]
    goals=list(match[-1].split('-'))
    goalsOfHome=int(goals[0])
    goalsOfAway=int(goals[-1])
    if(goalsOfHome>goalsOfAway):#home team wins
        scores[ord(home)]+=3
    elif(goalsOfHome==goalsOfAway):#both draw
        scores[ord(home)]+=1
        scores[ord(away)]+=1
    else:#away team wins
        scores[ord(away)]+=3
for i in range(len(scores)):
    if(max(scores)==scores[i]):
        print(chr(i))
        print(max(scores))
        break
