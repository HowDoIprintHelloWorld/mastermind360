from game import Board, genId

"""
Steps:
    -> Game must function
    -> Detect which board in game from tok
    -> Detect board from ID
"""




def simulate():
    r = [2, 2]
    id = genId()
    test = Board(False, 4, 6, id)
    test.addPlayer(id)
    while r[0] != 0:
        r = test.makeGuess(id, input(">> ").split())
        print(*r)
        


if __name__ == "__main__":
    simulate()
