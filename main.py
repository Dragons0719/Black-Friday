# This is my first Flask webpage
# Made by Elijah Rotenberger
# 10/26/2022

from flask import Flask, redirect, url_for, render_template, request, flash




app = Flask(__name__, template_folder='template_folder')

@app.route('/')
def land():
    return render_template('landing-page.htm')

@app.route('/mt-shirt')
def mshirt():
    return render_template('t-shirts.html')

@app.route('/msweatshirt')
def msweat():
    return render_template('sweatshirts.html')

@app.route('/mpants')
def mpant():
    return render_template('pants.html')

@app.route('/wt-shirt')
def wshirt():
    return render_template('wt-shirts.html')

@app.route('/wsweatshirt')
def wsweat():
    return render_template('wsweatshirt.html')

@app.route('/wpants')
def wpant():
    return render_template('wpants.html')

@app.route('/computer')
def comp():
    return render_template('computer.html')

@app.route('/phone')
def pho():
    return render_template('phones.html')

@app.route('/accs')
def acs():
    return render_template('accs.html')

@app.route('/kap')
def kitap():
    return render_template('kitchen.html')

@app.route('/bap')
def beap():
    return render_template('bedroom.html')

@app.route('/lrap')
def lr():
    return render_template('livingroom.html')

@app.route('/cc')
def cha():
    return render_template('charge.html')

@app.route('/dec')
def deco():
    return render_template('decoration.html')

@app.route('/hobby')
def hobb():
    return render_template('hobby.html')

@app.route('/wit')
def whisth():
    return render_template('wit.html')

@app.route('/wdid')
def whdoido():
    return render_template('wdid.html')

@app.route('/EG')
def ElGa():
    return render_template('EG.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
