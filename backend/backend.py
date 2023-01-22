from game import Board, genId
from flask import Flask, jsonify, request
from tools import gameById, playerById


"""
Steps:
    -> Game must function
    -> Detect which board in game from tok
    -> Detect board from ID
"""

app = Flask(__name__)



@app.route("/")
def main():
    return "Enter a game ID!"


@app.route("/game/<id>/<player>") #, methods=["GET", "POST"])
def game(id, player):
    game = gameById(games, id)
    board = None
    if not game:
        return jsonify({"message":"unknown game with such ID"})
    print("Player: "+player)
    board = playerById(game, player)
    if board == None:
        return jsonify({"message":"unknown player with such ID"})
        
    args = request.args
    if "action" in args.keys():
        action = args["action"]
        # if action.strip() == ""
        return action
    else:
        return jsonify({"message":"no action specified"})




def simulate():
    r = [2, 2]
    id = genId("board")
    test = Board(False, 4, 6, id)
    playerId = genId()
    test.addPlayer(playerId)
    print(f"Game made! {id}/{playerId}")
    return test
    
    
def siminput(test):    
    while r[0] != 0:
        r = test.makeGuess(id, input(">> ").split())
        print(*r)
        


if __name__ == "__main__":
    games = []
    test = simulate()
    games.append(test)
    #siminput(test)
    app.run()
