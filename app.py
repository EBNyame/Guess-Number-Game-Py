from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production

@app.route('/', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['computer_number'] = random.randint(0, 100)
        return redirect(url_for('game'))
    return render_template('name.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'name' not in session or 'computer_number' not in session:
        return redirect(url_for('get_name'))

    message = ""
    won = False  # ✅ Define this early

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            computer_number = session['computer_number']
            name = session['name']

            if guess == computer_number:
                message = f"🎉 Congratulations {name}, you guessed correctly!"
                session.pop('computer_number')
                won = True
            elif guess < computer_number:
                message = "❌ Too low. Try a higher number!"
            else:
                message = "❌ Too high. Try a lower number!"
        except ValueError:
            message = "Please enter a valid number."

    return render_template('game.html', message=message, name=session.get('name'), won=won)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('get_name'))

if __name__ == '__main__':
    app.run(debug=True)
