import chess
import chess.engine
import urllib.parse

# Check if input is a valid SAN move
def is_valid_san(board, raw_move):
    try:
        board.parse_san(raw_move)
        return True
    except ValueError:
        return False

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("bin/stockfish")
engine.configure({"Skill Level": 1})
count = 1
error = False

while not board.is_game_over():
    if board.turn == chess.WHITE:
        raw_move = input(str(count) + " ")
        valid_move = is_valid_san(board, raw_move)
        if error:
            for _ in range(4):
                print("\033[F\033[K", end="")
            print(str(count) + " " + raw_move)
            error = False
        if not valid_move:
            print("Sorry, but '" + raw_move + "' is not a valid move")
            print("See board: https://lichess.org/analysis/" + urllib.parse.quote(board.fen()))
            error = True
        else:
            board.push_san(raw_move)
    else:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        print(str(count) +  "...", board.san(result.move))
        board.push(result.move)
        count += 1

engine.quit()
