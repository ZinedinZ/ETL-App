from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "python"


@app.route("/", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        form = request.files["file"]
        check_file(form)
        return render_template("home.html", file=form.filename, secure_filename=secure_filename(form.filename))
    return render_template("home.html")



def check_file(file_name):
    file_ext = os.path.splitext(file_name.filename)[1].lower()
    if file_ext == ".xlml":
        file_name.save("static/" + file_name.filename)
        print("File saved")
    else:
        flash("wrong file type")
    print(file_ext)

if __name__ == "__main__":
    app.run(debug=True)
