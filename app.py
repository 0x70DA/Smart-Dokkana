from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from database import Database

app = Flask(__name__)

# Configure session.
app.config['SESSION_PERMENENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Temp dictionary to hold usernames and passwords. To be replaced with a SQL database.
# USERS = {'Mahmoud Hussein': 'admin1234', 'Test': 'Test'}

# Configure database.
db_file = "database.db"
db = Database(db_file)


@app.route('/')
def index():
    '''Define the default route.'''
    # If no user is logged in, redirect to login page.
    if not session.get('id'):
        return redirect('/login')

    # Get user's data.
    user_data = db.select(session.get('id'))
    
    return render_template('index.html', user_data=user_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Define the login route.'''
    if request.method == 'POST':
        # User submitted a form.
        username = request.form.get('username')
        password = request.form.get('password')

        # Get all rows from db.
        rows = db.select_all()

        # If user is in database, log them in.
        for row in rows:
            if username == row['username'] and password == row['password']:
                # Add user to session and redirect to homepage.
                session['id'] = row['id']
                return redirect('/')

        # User is not registered.
        return render_template('login.html', msg='fail')

    # GET request.
    if not session.get('id'):  # If user is not logged in.
        return render_template('login.html')
    else:
        # User already logged in.
        return redirect('/')


@app.route('/logout')
def logout():
    '''Define logout route.'''
    # Remove user from session.
    session['id'] = None
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
