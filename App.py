from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])

        add = a + b
        sub = a - b
        mul = a * b

        if b != 0:
            div = a / b
        else:
            div = "0 ga bo‘lib bo‘lmaydi"

        return render_template(
            "result30.html",
            add=add,
            sub=sub,
            mul=mul,
            div=div
        )

    return render_template("index30.html")

if __name__ == "__main__":
    app.run(debug=True)
