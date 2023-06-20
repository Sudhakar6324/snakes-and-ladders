import random
sal=[]
c=30
for i in range(6):
    a=[]
    if(i%2==0):
        c-=4
        t=True
    else:
        c-=6
        t=False
    for j in range(5):
        a.append(c)
        if(t):
            c+=1
        else:
            c-=1
    sal.append(a)
def display(sal):
    for i in range(len(sal)):
        for j in range(len(sal[0])):
            if(i>=len(sal)-2):
                print(sal[i][j],end="  ")
            else:
                print(sal[i][j],end=" ")
        print()
def score_cal(player,score,player_pos,other_pos,sal):
    dice=[1,2,3,4,5,6]
    sl={3:2,5:8,11:26,20:29,1:4,19:7,21:9,27:1}
    top_shows=random.choice(dice)
    print("the dice shows",top_shows)
    if(top_shows+score>30):
        return score,player_pos
    if(other_pos[0]==player_pos[0] and player_pos[1]==other_pos[1]):
        if(player=="c"):
            sal[player_pos[0]][player_pos[1]]="s"
        else:
            sal[player_pos[0]][player_pos[1]]="c"
    else:
        sal[player_pos[0]][player_pos[1]]=score
    if(top_shows+score>30):
        return score,player_pos
    if(top_shows+score in sl):
        score=sl[top_shows+score]
    else:
        score+=top_shows
    find=False
    for i in range(len(sal)):
        for j in range(len(sal[0])):
            if(sal[i][j]==score):
                sal[i][j]=player
                find=True
                player_pos=[i,j]
                break

    if(find==False):
        player_pos=other_pos
        sal[other_pos[0]][other_pos[1]]+=player
    if(top_shows==6):
        return score_cal(player,score,player_pos,other_pos,sal)
    return score,player_pos
player1="s"
player2="c"
player1_score=1
player2_score=1
player1_pos=[5,4]
player2_pos=[5,4]
while(1):
    n=int(input("enter any intger it is your chance"))
    player1_score,player1_pos=score_cal(player1,player1_score,player1_pos,player2_pos,sal)
    display(sal)
    if(player1_score==30):
        print("sudhakar wins")
        break
    player2_score,player2_pos=score_cal(player2,player2_score,player2_pos,player1_pos,sal)
    display(sal)
    if(player2_score==30):
        print("computer wins")
        break





