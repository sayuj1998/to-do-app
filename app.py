from flask import Flask, render_template, request, url_for, redirect
from models import db, Todo
from flask_migrate import Migrate
from flask import Response

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home() -> Response:
    """Render home page with todos and search, add new todos and reload if todo name is empty"""
    search = request.args.get("search", "").strip()
    filtered_todos = [todo for todo in todos() if search.lower() in todo.description.lower()]

    if request.method == "POST":
        if "todo_name" in request.form:
            todo_name = request.form["todo_name"].strip()
            if todo_name:
                db.session.add(Todo(description=todo_name))
                db.session.commit()
                return redirect(url_for("home"))
            else:
                return render_template("index.html", items=todos())
    return render_template("index.html", items=filtered_todos, search=search)

def todos() -> list[Todo]:
    """Retrieve all todos from the database"""
    return db.session.execute(db.select(Todo)).scalars()

@app.route("/checked/<int:todo_id>", methods=["POST"])
def checked_todo(todo_id: int) -> Response:
    """Toggle the checked status of the todo and redirect to home page"""
    todo = Todo.query.get_or_404(todo_id)
    todo.checked = not todo.checked
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id) -> Response:
    """Delete the todo from the database and redirect to home page"""
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_todo(todo_id) -> Response:
    """Edit the todo in the database and redirect to home page"""
    todo = Todo.query.get_or_404(todo_id)
    new_name = request.form.get("new_name")
    todo.description = new_name
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
