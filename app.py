from flask import Flask, render_template, request

app = Flask(__name__)


input_val = []

@app.route("/", methods=["GET", "POST"])
def root():

    if request.method == "POST":
        input_val.append(request.json)
        print(input_val)

    return str(input_val)


if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")

