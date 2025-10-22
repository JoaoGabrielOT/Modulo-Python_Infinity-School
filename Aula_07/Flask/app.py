from flask import Flask, render_template as rt, request

app = Flask(__name__)

@app.route('/')
def index():
    return rt('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form.get('nome')
    email = request.form.get('email')
    return f'Nome: {nome}, Email: {email}'


if __name__ == "__main__":
    app.run(debug=True)