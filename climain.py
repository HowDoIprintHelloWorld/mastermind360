from backend.game import *
from backend.tools import *
from sys import exit

def simulate():
    r = [2, 2]
    id = genId("board")
    test = Board(False, 5, 7, id)
    playerId = genId()
    test.addPlayer(playerId)
    # print(f"Game made! {id}/{playerId}")
    return test, f"{id}/{playerId}", playerId
    


def siminput(test, id):    
    r = [2, 2]
    while r[0] != 0:
        inpt = input(">> ")
        if inpt in ["exit", "quit"]: exit(0)
        r = test.makeGuess(id, inpt.split())
        print(*r[1])



if __name__ == "__main__":
  board, ids, playerid = simulate()
  siminput(board, playerid)