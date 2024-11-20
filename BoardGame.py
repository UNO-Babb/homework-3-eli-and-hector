#Example Flask App for a hexaganal tile game
#Logic is in this python file

from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure random key

def roll_dice():
    """Simulate rolling two dice and return their values and total."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2, die1 + die2

@app.route('/')
def index():
    """Home page with game instructions and player setup."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """Initialize game with players."""
    num_players = int(request.form['num_players'])
    session['players'] = [f"Player {i + 1}" for i in range(num_players)]
    session['current_player'] = 0  # Index of the current player
    session['game_active'] = True
    return redirect(url_for('play_game'))

@app.route('/play', methods=['GET', 'POST'])
def play_game():
    """Handle the game play logic."""
    if not session.get('game_active', False):
        return redirect(url_for('index'))

    players = session['players']
    current_player_idx = session['current_player']
    current_player = players[current_player_idx]

    if request.method == 'POST':
        die1, die2, total = roll_dice()

        if total == 7 or total == 11:
            session['winner'] = current_player
            session['game_active'] = False
            return redirect(url_for('end_game'))
        elif die1 == 1 and die2 == 1:
            session['loser'] = current_player
            session['game_active'] = False
            return redirect(url_for('end_game'))
        else:
            # Move to the next player
            session['current_player'] = (current_player_idx + 1) % len(players)

        return render_template('play.html', player=current_player, die1=die1, die2=die2, total=total)

    return render_template('play.html', player=current_player)

@app.route('/end')
def end_game():
    """Display the game result."""
    winner = session.get('winner')
    loser = session.get('loser')

    if winner:
        message = f"Congratulations, {winner}! You rolled a winning total and won the game!"
    elif loser:
        message = f"Oh no, {loser}! You rolled double 1s and lost the game."
    else:
        message = "The game ended with no winner or loser."

    return render_template('end.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

