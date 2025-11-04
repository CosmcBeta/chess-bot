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
