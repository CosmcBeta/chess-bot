import pytest

from core.chess_logic import ChessLogic


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


def test_empty_fen_string(logic):
    assert not logic.set_board_from_fen("")


def test_valid_starting_position_fen(logic):
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    assert logic.set_board_from_fen(fen)


@pytest.mark.parametrize(
    "fen",
    [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR",
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R",
        "8/8/8/8/8/8/8/8",
    ],
)
def test_multiple_valid_fens(logic, fen):
    assert logic.set_board_from_fen(fen)


@pytest.mark.parametrize(
    "fen", ["8/8/8/8/8/8/8/K7", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"]
)
def test_boundary_valid_fens(logic, fen):
    assert logic.set_board_from_fen(fen)


@pytest.mark.parametrize(
    "invalid_fen",
    [
        "invalid",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR/8",
        "rnbqkbnr/ppppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNX",
        "ahuyhyhhhhh",
    ],
)
def test_invalid_fen_strings(logic, invalid_fen):
    assert not logic.set_board_from_fen(invalid_fen)


def test_value_error_returns_false(logic):
    assert not logic.set_board_from_fen("totally_invalid_fen")


def test_consecutive_valid_fen_calls(logic):
    fen1 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    fen2 = "8/8/8/8/8/8/8/8"

    assert logic.set_board_from_fen(fen1)
    assert logic.set_board_from_fen(fen2)


def test_valid_then_invalid_fen(logic):
    valid_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    invalid_fen = "invalid"

    assert logic.set_board_from_fen(valid_fen)
    assert not logic.set_board_from_fen(invalid_fen)
