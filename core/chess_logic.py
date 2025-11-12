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

    print(board.outcome())
    engine.quit()


class ChessLogic:
    def __init__(self) -> None:
        self.engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(
            "stockfish"
        )
        self.board: chess.Board = chess.Board()

    def __del__(self) -> None:
        self.engine.close()

    def get_winner(self) -> str:
        outcome = self.board.outcome()
        if outcome is None:
            return "Game not over yet"

        if outcome.winner == chess.WHITE:
            return "White wins"
        elif outcome.winner == chess.BLACK:
            return "Black wins"
        else:
            return "Draw"

    # # Returns the board (useful for getting game result and such)
    # def get_board(self):
    #     pass

    # Input user move
    # going to be a string like a1b2 moving the piece from a1 to b2
    # returns false is error, otherwise returns true
    def user_move(self, move: str) -> bool:
        try:
            m = chess.Move.from_uci(move)
            if m in self.board.legal_moves:
                self.board.push(m)
                return True
            else:
                return False
        except chess.InvalidMoveError:
            return False

    # Get move from computer
    # returns a string move like above: a1b2
    def get_move(self) -> str:
        return ""
