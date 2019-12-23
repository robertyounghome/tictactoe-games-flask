from flask import Flask
from flask import render_template, request, redirect, jsonify
from tictactoe import TicTacToe

app = Flask(__name__, template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
tictactoe = TicTacToe()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/pick_game', methods=['GET', 'POST'])
def pick_game():
    yourname = request.form['yourname']
    game = request.form['game']
    if game == 'tictactoe':
        tictactoe.setName(yourname)
        tictactoe.reset()
        return render_template('tictactoe.html', name = yourname)
    else:
    	return render_template('minesweeper.html', name = yourname)

@app.route('/move', methods=['GET', 'POST'])
def move():
    caller = request.form.get('caller')
    h = tictactoe.player_move(int(caller[-2]), int(caller[-1]))
    h['caller'] = caller
    return jsonify(h)

@app.route('/computer_move', methods=['GET', 'POST'])
def computer_move():
    print('inside computer move')
    # caller = request.form.get('caller')
    h = tictactoe.computer_move()
    print(h)
    return jsonify(h)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    tictactoe.reset()
    return jsonify({})

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
