from flask import Flask, render_template, request

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
    return render_template("index.html", content="testing")

@app.route("/",methods=["POST"])
def parse_data():
    print("test")
    if request.method == "POST":
        data = request.form
        return render_template('index3.html', content=data)


if __name__ == "__main__":
    app.run(debug=True)
