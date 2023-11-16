from flask import Flask,jsonify,request,render_template,redirect, url_for

app = Flask(__name__)

@app.route('/') # HOme API
def my_fun():
    print("Hello Flask")
    return render_template('login.html')

@app.route('/result/int : <name>')
def result(name):
    return f'Hello {name} You are in result API'

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        print("In Login API")
        print("NAme:",name)
        return redirect(url_for('result',name = name))
    

    if request.method == 'GET':
        name = request.args.get("name")
        print("NAme:",name)
        return redirect(url_for('result',name = name))

app.run(debug = True)