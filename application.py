from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__, template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/tictactoe', methods=['GET', 'POST'])
def first_name():
    yourname = request.form['yourname']
    game = request.form['game']
    if game == 'tictactoe':
    	return render_template('tictactoe.html', name = yourname)
    else:
    	return render_template('minesweeper.html', name = yourname)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run()
