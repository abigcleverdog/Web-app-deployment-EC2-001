from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("main.html")
##    return "Hi there. I am still alive"
if __name__ == "__main__":
    app.run()
