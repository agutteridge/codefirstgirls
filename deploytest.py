from flask import Flask, render_template

app = Flask('test-heroku-app')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/films/<number>')
def films(number):
    all_films = {
    	'1': 'The Phantom Menace',
    	'2': 'The Empire Strikes Back',
    	'3': 'Revenge of the Sith',
    	'4': 'A New Hope',
    	'5': 'The Empire Strikes Back',
    	'6': 'Return of the Jedi',
        '7': 'The Force Awakens',
        '8': 'The Last Jedi'
    }

    if number in all_films:
    	return render_template('starwars.html', title=all_films[number])
    else:
    	return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)