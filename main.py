from flask import Flask
app = Flask("__main__")

@app.route("/")
def home():
    print("App is running")
    return "<h1> App is running </h1>"


if __name__ == "__main__":
    app.run(debug=True)