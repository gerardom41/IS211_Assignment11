from flask import Flask, render_template, request, redirect, url_for
import re
app = Flask(__name__)
to_do_test = []

@app.route("/")
def home():
    return render_template("index.html", to_do_test=to_do_test)

@app.route("/submit", methods=["POST"])
def submit():
    task = request.form.get("task")
    email = request.form.get("email")
    priority = request.form.get("priority")
    if not re.match(r".+@.+\.(com|net|org|co|io)$", email):
        return redirect(url_for("home"))
    if priority not in ["Low", "Medium", "High"]:
        return redirect(url_for("home"))

    to_do_test.append([task, email, priority])
    return redirect(url_for('home'))

@app.route("/clear", methods=["POST"])
def clear():
    del to_do_test[:]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
