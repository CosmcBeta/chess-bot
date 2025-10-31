import chess
import chess.engine

# Has Stockfish play a game against itself, 100 milliseconds per move
def Stockfish():
    engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish.exe")

    board = chess.Board()
    while not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=0.1))
        board.push(result.move)

    engine.quit()
