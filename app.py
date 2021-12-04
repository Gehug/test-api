from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


input_val = []

@app.route("/", methods=["GET", "POST"])
def root():
    app_json = []

    if request.method == "POST":
        input_val.append(json.dumps(request.json))

    return render_template("base.html", input_val=input_val)
@app.route("/reset", methods=["GET"])
def reset():
    input_val.clear() 
    print("ba")
    return redirect("/")
    


if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")

