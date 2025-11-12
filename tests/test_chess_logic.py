import pytest

from core.chess_logic import ChessLogic

# class ChessLogic:
#     def __init__(self) -> None:
#         self.engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci("stockfish")
#         self.board: chess.Board = chess.Board()

#     def get_winner(self) -> str:
#         outcome = self.board.outcome()
#         if outcome is None:
#             return 'Game not over yet'

#         if (outcome.winner == chess.WHITE):
#             return 'White wins'
#         elif (outcome.winner == chess.BLACK):
#             return 'Black wins'
#         else:
#             return 'Draw'

#     # # Returns the board (useful for getting game result and such)
#     # def get_board(self):
#     #     pass

#     # Input user move
#     # going to be a string like a1b2 moving the piece from a1 to b2
#     # returns false is error, otherwise returns true
#     def user_move(self, move: str) -> bool:
#         try:
#             m = chess.Move.from_uci(move)
#             self.board.push(m)
#             return True
#         except chess.InvalidMoveError:
#             return False


@pytest.fixture
def logic():
    return ChessLogic()


@pytest.mark.parametrize(
    "invalid_move",
    [
        (""),
        ("weoijfqiuwehfqwdfadjkhvqwefgyyibegwfggrehu"),
        ("a1"),
        ("a1a9"),
        ("a1a0"),
        ("gggg"),
        ("something aint right"),
        ("ahhhhhhhhh"),
        ("j2d4"),
        ("a11p"),
    ],
)
def test_user_move_invalid(logic, invalid_move):
    assert not logic.user_move(invalid_move)


@pytest.mark.parametrize(
    "valid_move", [("a1a1"), ("a1a2"), ("a1b5"), ("a1a8"), ("a1g6"), ("g3d8")]
)
def test_user_move_valid(logic, valid_move):
    assert not logic.user_move(valid_move)


def test_get_winner_still_playing(logic):
    assert logic.get_winner() == "Game not over yet"
