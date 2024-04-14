from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/display_page', methods=['POST','GET'])
def print_input():
    name = request.form['name']
    return render_template('print_input.html', name = name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)