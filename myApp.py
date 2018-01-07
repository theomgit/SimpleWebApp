from flask import Flask
import sqlite3

app = Flask(__name__) # __main__


@app.route('/')
def hello_world():
    return "Hello, Flask"


@app.route('/hello')
def hello2():
    return "A simple hello"


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=4995)


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES (145123212, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


# create_table()
# data_entry()




