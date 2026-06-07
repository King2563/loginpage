from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email == "admin@gmail.com" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Email or Password"

if __name__ == '__main__':
    app.run(debug=True)