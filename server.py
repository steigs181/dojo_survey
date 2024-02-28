from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'abc123'

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/result/submit', methods=['POST'])
def update_page():
    session['your_name'] = request.form['your_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    session['gender'] = request.form['gender']
    session['agreement_accept'] = request.form['agreement_accept']
    return redirect('/result')

@app.route('/result/return', methods=['POST'])
def go_back_home ():
    session['go_back'] = request.form['go_back']
    session.clear()
    return redirect('/')

@app.route('/result')
def result_page():
    return render_template('result.html', your_name = session['your_name'],
dojo_location = session['dojo_location'], fav_language = session['fav_language'], comment = session['comment'], gender = session['gender'],
agreement_accept = session['agreement_accept'])



if __name__ == '__main__':
    app.run(debug=True)