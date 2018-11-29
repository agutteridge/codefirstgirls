from flask import Flask

app = Flask('my_app')

@app.route('/')
def hello():
	return 'Hello, World!'

@app.route('/films/<number>')
def films(number):
	all_films = {
		"7": "The Force Awakens"
	}

	return all_films[number]

app.run(debug=True)