

# In the api, you are usually given an id
# find the game with the matching id
def gameById(games, id):
    for game in games:
            if str(game.id) == str(id):
                return game
    return None


def playerById(game, id):
    for rid, board in game.boards.items():
        print(rid)
        print("id="+id)
        if str(id).strip() == str(rid).strip():
            print("is same")
            return board
    return None
