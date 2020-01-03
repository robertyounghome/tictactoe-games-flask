from flask import Flask
from flask import render_template, request, redirect, jsonify
from tictactoe import TicTacToe
from minesweeper import Minesweeper

app = Flask(__name__, template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['debug'] = True
tictactoe = TicTacToe()
minesweeper = Minesweeper()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/pick_game', methods=['GET', 'POST'])
def pick_game():
    yourname = request.form['yourname']
    game = request.form['game']
    if game == 'minesweeper':
        minesweeper.setName(yourname)
        minesweeper.reset()
        return render_template('minesweeper.html', name = yourname, board_size = minesweeper.board_size, board = minesweeper.board)
    else:
        tictactoe.setName(yourname)
        tictactoe.reset()
        return render_template('tictactoe.html', name = yourname)

@app.route('/move', methods=['GET', 'POST'])
def move():
    caller = request.form.get('caller')
    h = tictactoe.player_move(int(caller[-2]), int(caller[-1]))
    h['caller'] = caller
    return jsonify(h)

@app.route('/mine_move', methods=['GET', 'POST'])
def mine_move():
    caller = request.form.get('caller')
    h = minesweeper.player_move(int(caller[caller.index('-')+1:caller.rindex('-')]), int(caller[caller.rindex('-')+1:]))
    # cannot jsonify with a tuple key, change to string i + "-" + j
    w = {}
    for k in h['updates'].keys():
        value = h['updates'][k]
        [i,j] = k
        w[str(i)+'-'+str(j)] = value
    h['updates'] = w
    h['caller'] = caller
    return jsonify(h)

@app.route('/computer_move', methods=['GET', 'POST'])
def computer_move():
    h = tictactoe.computer_move()
    return jsonify(h)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    tictactoe.reset()
    return jsonify({})

@app.route('/mine_reset', methods=['GET', 'POST'])
def mine_reset():
    minesweeper.reset()
    return jsonify({'board_size': minesweeper.board_size})

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for -- minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run()
