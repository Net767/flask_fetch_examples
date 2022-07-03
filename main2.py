from flask import (
    Flask, jsonify, render_template, request
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index2.html")

    val = request.json.get("c_check")
    print(val)
    return jsonify({"data": {"val": val}})
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)