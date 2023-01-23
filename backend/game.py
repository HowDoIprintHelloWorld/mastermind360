from random import randint, sample


# Note: playercount will be limited to 2
class Board():
    def __init__(self, multiplayer, nrBalls, nrColors, id):
        self.multiplayer = multiplayer
        self.nrBalls = nrBalls
        self.colors = self.genColors(nrColors)
        self.ids = []
        self.boardId = genId("board")
        self.boards = {} # id:board
        self.correct = self.genCorrect()
        self.id = id
        print(self.correct)

        self.addPlayer(id)


    
    def genColors(self, nrColors):
        colors = ["red", "blue", "black", "white", "gray", "purple", "yellow", "orange"]
        if nrColors >= len(colors) or nrColors <= 1:
            nrColors = 5
        return colors[:nrColors]


    def addPlayer(self, id):
        if id not in self.ids:
            self.ids.append(id)
            self.boards[id] = []

    
    def genCorrect(self):
        return sample(self.colors, self.nrBalls)

    
    # returns code, colorseq
    # ids: 0=correct, 1=part wrong, 2=wrong guess count, 3=unknown id, 4 = unknown color
    def makeGuess(self, id, guessSeq):
        toRet = []
        print(f"{len(guessSeq)=}, {self.nrBalls=}")
        if len(guessSeq) != self.nrBalls:
            return 2, []
        elif id not in self.ids:
            return 3, []
        
        for indx, guess in enumerate(guessSeq):
            guess = guess.strip().lower()
            if guess not in self.colors:
                return 4, []
            if self.correct[indx] == guess:
                toRet.append("black")
            elif guess in self.correct:
                toRet.append("white")

        if not any([c for c in toRet if c != "black"]) and len(toRet) == self.nrBalls:
            return 0, toRet

        return 1, toRet

            


def genId(mode=None):
        id = ""
        l = 4 if mode == "board" else 15
        id = "".join([str(randint(0, 9)) for i in range(l)])
        return id



    
