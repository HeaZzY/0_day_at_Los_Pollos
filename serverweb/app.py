from flask import Flask, render_template, request, redirect, url_for, session, flash
import subprocess
from database import *
from utils import *

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if create_user(username, password):
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists.', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username, password)
        if user:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        coins = get_coins(username)
        print(coins)
        return render_template('profile.html', username=username, coins=coins)
    return redirect(url_for('login'))

@app.route('/get_free_wings')
def get_free_wings():
    if 'username' in session:
        username = session['username']
        if not alreadyvouched(username):
            voucher_code = generate_voucher_code()
            create_voucher(username, voucher_code, 5)
            return redirect(url_for('use_voucher',voucher_code=voucher_code))
        return redirect(url_for('profile'))
    return redirect(url_for('login'))

@app.route('/use_voucher')
def use_voucher():
    if 'username' in session:
        username = session['username']
        voucher_code = request.args.get('voucher_code')
        print(voucher_code)
        if used_voucher(username, voucher_code):
            flash('Voucher used successfully!', 'success')
        else:
            flash('Invalid or already used voucher.', 'danger')
        return redirect(url_for('profile'))
    return redirect(url_for('login'))

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        if 'username' in session:
            username = session['username']
            coins = get_coins(username)
            if coins >= 10:
                delete_coins(username, 10)
                plat = request.form.get('plat')  # Récupère la valeur de 'plat' du formulaire POST
                print(plat)
                # Utilisation de Markup pour rendre la valeur de plat sûre (échappement automatique)
                result = subprocess.Popen(plat, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                message = f"succes to buy :{result.stdout.read().decode('latin-1')}{result.stderr.read().decode('latin-1')}"
                coins = get_coins(username)  # Mettre à jour les coins après déduction
                return render_template('shop.html', username=username, coins=coins, message=message)
            else:
                return render_template('shop.html', username=username, coins=coins, message="Désolé, vous n'avez pas assez de points")
        return redirect(url_for('login'))
    else:
        if 'username' in session:
            username = session['username']
            coins = get_coins(username)
            return render_template('shop.html', username=username, coins=coins)
        return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)