from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, template_folder="templates")

todos = [{"task": "Sample Todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add() -> 'redirect':
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index: int) -> 'redirect | str':
    todo = todos[index]
    if request.method == "POST":
        todo['task'] =  request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>", methods=["POST"])
def check(index: int) -> 'redirect':
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index: int):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)