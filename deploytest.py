from flask import Flask

app = Flask('test-heroku-app')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/films/<number>')
def films(number):
    all_films = {
        "7": "The Force Awakens"
    }

    return all_films[number]

if __name__ == '__main__':
    app.run(debug=True)