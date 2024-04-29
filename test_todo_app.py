import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    """Making test client for app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_home(client):
    """Test if home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_add_todo(client):
    """Test adding a new todo"""
    response = client.post("/home", data={"todo_name": "Test Todo"})
    assert response.status_code == 302

def test_checked_todo(client):
    """Test toggling the checked box of the todo"""
    todo = Todo(description="Test Todo")
    db.session.add(todo)
    db.session.commit()

    assert todo.checked == False
    response = client.post(f"/checked/{todo.id}")
    assert response.status_code == 302
    assert todo.checked == True

def test_delete_todo(client):
    """Test deleting a todo"""
    todo = Todo(description="Test Todo")
    db.session.add(todo)
    db.session.commit()

    response = client.post(f"/delete/{todo.id}")

    assert response.status_code == 302
    assert Todo.query.get(todo.id) is None

def test_edit_delete_todos(client):
    """Test adding, editing, checking and deleting multiple todos"""
    todos = []
    for i in range(10):
        todo = Todo(description=f"Test Todo {i + 1}")
        db.session.add(todo)
        todos.append(todo)
    db.session.commit()

    for todo in todos:
        new_name = f"Edited {todo.description}"
        response = client.post(f"/edit/{todo.id}", data={"new_name": new_name})
        assert response.status_code == 302

        updated_todo = Todo.query.get(todo.id)
        assert updated_todo.description == new_name

        assert todo.checked == False
        response = client.post(f"/checked/{todo.id}")
        assert response.status_code == 302
        assert todo.checked == True

    for todo in todos:
        response = client.post(f"/delete/{todo.id}")
        assert response.status_code == 302
        assert Todo.query.get(todo.id) is None

if __name__ == "__main__":
    pytest.main()


