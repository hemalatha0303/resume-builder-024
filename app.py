from flask import Flask, redirect, render_template, request

app = Flask(__name__, template_folder='templates')


# Route to serve the homepage (main.html)
@app.route('/')
def home():
    return render_template('main.html')  # This looks for main.html in templates folder


# Route to serve the signin page (signin.html)
@app.route('/signin')
def signin():
    return render_template('sign in.html')

# Route to serve the home page (home.html) after signup
@app.route('/home')
def user_home():
    return render_template('home.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        terms = request.form['terms']
        
        # You can handle the form submission here, such as saving user data to a database
        
        return redirect('/home')  # Redirect to home after successful signup
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
