import main as m
import turn as t
computer_tiles=[]
your_hand=[]
table=[]
def play_game():
    box=m.create_pool()
    
    m.distribution_players(box,computer_tiles,your_hand)
    print(len(your_hand))
    while True:
        indexes=(input("Enter indexes of the tiles you want to insert.").lower().split())
        # move=m.read_player_move(indexes)
        t.play_turn(your_hand, table, table, indexes)
        print(table)

       

       
        
        m.printi(your_hand)
        print(len(your_hand))






if __name__ == "__main__":
    play_game()