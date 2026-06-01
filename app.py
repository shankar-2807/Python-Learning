from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form.get("uname")
        pwd = request.form.get("pwd1")
        if uname == "Shankar" and pwd == "admin@123":
            return "Login Successful"
        else:
            return "Login Failed"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

