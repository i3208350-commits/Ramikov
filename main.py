import random
import turn as t
computer_tiles=[]
your_hand=[]
table=[]
def create_pool():
     box=[]
     color=["R","B","O","K"]
     for i in range(2):
          for g in color:
               for k in range(1,14):
                    box.append([k,g])
     random.shuffle(box)


     return(box)


     print(len(box))

def distribution_players(box,computer_tiles,your_hand):
    for i in range(len(box)):
        if i % 2 ==0:
            
            computer_tiles.append(box.pop(i))
            
            if len(computer_tiles)==10:
                break
        if i % 2 ==1:
            your_hand.append(box.pop(i))
            
            if len(your_hand)==10:
                break
    print(sorted(your_hand),len(box))       
    return computer_tiles,your_hand

def is_valid_set(tiles):
    a=list(sorted(tiles,key=lambda n: int(n[0])))
    print(a)
    is_sequence=True
    is_group=True
    conter=0
    conter_s=0
    for i in range(len(a)-1):
        print(a[i][0])
        if a[i][0] +1 ==a[i+1][0] and a[i][1] == a[i+1][1] :
            conter+=1
            
        else:
            is_group=False
        if a[i][0]==a[i+1][0] and a[i][1] != a[i+1][1]:
            conter_s+=1
        else:
                is_sequence=False
        if is_group==True and conter>2 or is_sequence==True and conter_s>2:
            return True
# def read_player_move(indexes):
    
#         indexes_y=[]
#         for i in indexes:
             
#              indexes_y.append(int(i))
#         return indexes_y
             

def play_set(your_hand, table, indexes,box):
    hand=[]
    print(indexes)
    if indexes[0] == "d":
            print("ooooo")
            your_hand.append(box[0])
            print("draw")
            print(len(your_hand))
    else:
        indexes_y=[]
        for i in indexes:
                     
            indexes_y.append(int(i))
        
        for i in (indexes_y):        
                print(your_hand[i-1])
                hand.append(your_hand.pop(i-1))    
        if is_valid_set(hand)==True:
            table.append(hand)
            
            return
        else:
            for i in hand:
                  your_hand.append(i)
                  
            return
                  

def printi(your_hand):
    print(f"""Computer tiles:{len(your_hand)}ppppp,
{your_hand}:
""")
