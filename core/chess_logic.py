import chess
import chess.engine


# Has Stockfish play a game against itself, 100 milliseconds per move
def Stockfish():
    engine = chess.engine.SimpleEngine.popen_uci("stockfish")

    board = chess.Board()
    while not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=0.1))
        print(result.move)
        board.push(result.move)

    print(board.result)
    engine.quit()

class ChessLogic:
    def __init__(self) -> None:
        self.engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci("stockfish")
        self.board: chess.Board = chess.Board()

    # Returns the board (useful for getting game result and such)
    def get_board(self):
        pass

    # Input user move
    def user_move(self, move):
        pass

    # Get move from computer
    def get_move(self):
        pass
