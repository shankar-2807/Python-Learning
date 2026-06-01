from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/hello")
def demoHtml():
    return render_template("hello.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/verify")
def verify():
    uname = request.args.get("uname")
    pwd = request.args.get("pwd")
    if uname == "Firstbit" and pwd == "admin@123":
        return "Login Successfully"
    else:
        return "Login Failed"
    
@app.route("/getsum")
def getSum():
    return render_template("sum_of_numbers.html")

@app.route("/ShowSum")
def ShowSum():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    s = num1+num2
    return "Sum = "+ str(s)

if __name__ == "__main__":
    app.run(debug=True)


