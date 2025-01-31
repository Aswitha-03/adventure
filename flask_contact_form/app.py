from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create or connect to SQLite database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            email TEXT,
                            message TEXT)''')
        conn.commit()

# Route to display the contact form
@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert data into SQLite database
        with sqlite3.connect('database.db') as conn:
            conn.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
                         (name, email, message))
            conn.commit()

        return redirect(url_for('thank_you'))

    return render_template('index.html')

# Route to thank the user after submission
@app.route('/thank_you')
def thank_you():
    return "Thank you for contacting us!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
