import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("bin/stockfish")
count = 1

while not board.is_game_over():
    if board.turn == chess.WHITE:
        move = input(str(count) + " ")
        board.push_san(move)
    else:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        print(str(count) +  "...", board.san(result.move))
        board.push(result.move)
        count += 1

engine.quit()
