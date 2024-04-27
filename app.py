from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home() -> str:
    if request.method == "POST":
        if "todo_name" in request.form:
            todo_name = request.form["todo_name"].strip()
            if todo_name:
                cur_id = random.randint(1, 1000)
                todos.append({
                    'id': cur_id,
                    'name': todo_name,
                    'checked': False
                })
                return redirect(url_for("home"))  # Redirect after form submission
            else:
                return render_template("index.html", items=todos, error="Todo name cannot be blank.")
    return render_template("index.html", items=todos)

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id: int) -> str:
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked']
            break
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id:int) -> str:
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for("home"))

@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id) -> str:
    new_name = request.form.get("new_name")
    for todo in todos:
        if todo['id'] == todo_id:
            todo['name'] = new_name
            break
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
