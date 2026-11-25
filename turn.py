import main as m
def play_turn(your_hand, box, table, indexes):
    
    if indexes==["d"]:
            return None
    else:
        #   return indexes
        # a=m.read_player_move(indexes)
        m.play_set(your_hand, table, indexes,box)
        