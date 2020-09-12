from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ''' result = request.args.get('Name') '''
        user = request.form['Name']
        resp = make_response()
        resp.set_cookie('userID', user)
        return resp

@app.route('/getCookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)
