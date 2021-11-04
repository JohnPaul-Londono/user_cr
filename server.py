from flask import Flask, render_template, request, redirect

from user import Users
app = Flask(__name__)


@app.route ("/users")
def get_all():
    users = Users.get_all()
    # print(users)
    return render_template("index.html", users=users)


@app.route("/createuser")
def create_user():
    return render_template("create.html")

@app.route("/homepage")
def go_back_home():
    return redirect("/users")

@app.route("/show/<int:id>")
def show_new_user(id):
    data ={
        "id":id
    }
    user = Users.show_user(data)
    print(user)
    return render_template("newinfo.html", u=user)

@app.route("/edit/<int:id>")
def edit_user(id):
    data ={
        "id":id
    }
    user = Users.show_user(data)
    return render_template ("edituser.html",u=user)

@app.route("/update/<int:id>", methods=["POST"])
def edit_user_db(id):
    data ={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "id":id
    }
    Users.edit_user(data)
    return redirect (f"/show/{id}")


@app.route("/delete/<int:id>")
def delete_user(id):
    data ={
        "id":id
    }
    Users.delete_user(data)
    return redirect ("/users")



@app.route("/create", methods=["POST"])
def create():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    new_id = Users.save(data)
    return redirect(f"/show/{new_id}")



if __name__ == "__main__":
    app.run(debug=True)