from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/play")
def Op():
    print("Blueboxes")
    print("*"*25)
    return render_template("index.html")


@app.route("/play/<int:numBoxes>")
def NumBoxes(numBoxes):
    print(numBoxes, "Boxes")
    print("*"*25)
    return render_template("play(x).html", boxNum=numBoxes)


@app.route("/play/<int:numBoxes>/<color>")
def colorBoxes(numBoxes, color):
    print(numBoxes, color, "Boxes")
    print("*"*25)
    return render_template("pickAColor.html", boxNum=numBoxes, pickOne=color)


@app.route("/")
def Admin():
    print("*"*25)
    return redirect(url_for("Op"))


if __name__ == "__main__":
    app.run(debug=True)
