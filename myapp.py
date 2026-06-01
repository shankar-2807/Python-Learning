from flask import Flask,render_template


app = Flask(__name__)

@app.route("/hello")
def demo():
    return"Welcome to Flask Framework."

@app.route("/showHtml")
def showHtml():
    return render_template("demo.html")


if __name__ == "__main__":
    app.run(debug=True)   #it will start the flask framework
    # we are in development phase , so please allow my dynamic changes.

