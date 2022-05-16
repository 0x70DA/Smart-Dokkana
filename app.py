from flask import Flask, request, render_template, redirect, session
from flask_session import Session

app = Flask(__name__)

# Configure session.
app.config['SESSION_PERMENENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Temp dictionary to hold usernames and passwords. To be replaced with a SQL database.
USERS = {'Mahmoud Hussein': 'admin1234', 'Test': 'Test'}


@app.route('/')
def index():
    '''Define the default route.'''
    # If no user is logged in, redirect to login page.
    if not session.get('username'):
        return redirect('/login')

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Define the login route.'''
    username = request.form.get('username')
    password = request.form.get('password')
    if request.method == 'POST':
        # User submitted a form.
        # If user is in database, log them in.
        for user in USERS:
            if username == user and password == USERS[user]:
                # Add user to session and redirect to homepage.
                session['username'] = username
                return redirect('/')

        # User is not registered.
        return render_template('login.html', msg='fail')

    # GET request.
    if not session.get('username'):  # If user is not logged in.
        return render_template('login.html')
    else:
        # User already logged in.
        return redirect('/')


@app.route('/logout')
def logout():
    '''Define logout route.'''
    # Remove user from session.
    session['username'] = None
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
