from flask import Flask

## WSGI Application

app = Flask(__name__)

@app.route('/')
def welcome():

    '''
    hello first function in flask 
    '''
    return "hello there! General Kenobi! HI there"


@app.route('/members')
def members():
    return "wlecome my investors! yoo!!"


if __name__=='__main__':
    app.run(debug=True)