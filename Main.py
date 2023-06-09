from Game import *
from Tile import *
from TaijiAI import *

def parseMove(move):
    moveList = move.split()
    moveDict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9}
    try:
        moveList[0] = int(moveList[0]) - 1
        moveList[1] = moveDict[moveList[1].upper()] - 1
        moveList[2] = int(moveList[2])
    except:
        print("Invalid input, please try again")
    return moveList

def updateCurrentNode(node, tile):
    for child in node.children:
        if child.tile == tile:
            return child
    return node.addSpecificChild(tile)

if __name__ == "__main__":
    print("Rows are labeled A-I while columns are labeled 1-9")
    print("Position of tile is the coordinate of the white side of the tile")
    print("Tile orientation :")
    print("white--black : 0")
    print("white")
    print("  |          : 1")
    print("black")
    print("black--white : 2")
    print("black")
    print("  |          : 3")
    print("white")
    playerToStart = input("Enter 1 to start first or 2 for the computer to start first: ")

    game = Game()
    notGameEnded = True
    game.setPlayer(int(playerToStart))

    print(game)

    rootNode = Node(game)
    currentNode = rootNode

    while (notGameEnded):
        if game.getPlayer() == 1:
            print("Player to move:")
            
            move = input("Enter row column orientation (e.g 5 A 0): ")
            moveParsed = parseMove(move)
            tile = Tile(moveParsed[0], moveParsed[1], moveParsed[2])
            game.update(tile.getRepresentation())
            print(game)
            currentNode = updateCurrentNode(currentNode, tile)
            notGameEnded = not game.isTerminal()
            
            # possibleMoves = enumeratePossibleMoves(game, currentNode.tile)
            # moveIndex = pickRandomMove(possibleMoves)
            # tile = possibleMoves[moveIndex]
            # game.update(tile.getRepresentation())
            # print(game)
            # currentNode = updateCurrentNode(currentNode, tile)
            # notGameEnded = not game.isTerminal()
            
        elif game.getPlayer() == 2:
            print("Computer to move:")
            newTile = MCTS(currentNode)
            game.update(newTile.getRepresentation())
            print(game)
            currentNode = updateCurrentNode(currentNode, newTile)
            notGameEnded = not game.isTerminal()

    print("Game Ended")
    p1_scoreList = game.generateScoreList(1)
    print(f"p1_scoreList: {p1_scoreList}")
    p2_scoreList = game.generateScoreList(2)
    print(f"p2_scoreList: {p2_scoreList}")
    finalScores = game.calculateScore(p1_scoreList, p2_scoreList)
    winner = game.evaluateWinner(finalScores)
    if winner == 0:
        print("Draw")
    elif winner == 1:
        print("You win")
    else:
        print("You lose")