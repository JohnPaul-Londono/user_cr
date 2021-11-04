from flask import Flask, render_template, request, redirect

from user import Users
app = Flask(__name__)


@app.route ("/")
def get_all():
    users = Users.get_all()
    # print(users)
    return render_template("index.html", users=users)


@app.route("/createuser")
def create_user():
    return render_template("create.html")


@app.route("/create", methods=["POST"])
def create():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    Users.save(data)
    return redirect("/")
            
if __name__ == "__main__":
    app.run(debug=True)