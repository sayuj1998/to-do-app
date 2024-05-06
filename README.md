![screenshot](Todo App.png)

# **Todo App**
This is a simple todo application built with Flask.

## **Features**
* Add, edit, delete, and toggle completion status of todos.
* Search functionality to filter todos based on their descriptions.
* Database powered by SQLAlchemy for storage.
* Frontend tested with Selenium to ensure UI functionality.
* Backend tested with Pytest to ensure backend functionality.

## **Prerequisites**
* Python 3.x
* Flask
* Flask-migrate
* SQLAlchemy
* Selenium
* Firefox browser (for testing)

## **Installation**
1) Clone the repository:
```
git clone https://github.com/sayuj1998/to-do-app
cd flask-todo-app
```
2) Install dependencies:
```
pip install -r requirements.txt
```
## **Usage**
1) Run the Flask application:
```
python app.py
```
2) Open your web browser and go to http://localhost:5000
3) Use the interface to add, edit, delete, and toggle completion status of todos.

## **Testing**
### **Frontend Testing**
Frontend tests are located in the frontend_test.py file. These tests use Selenium to simulate user interactions with the frontend interface.

To run frontend tests:
```
pytest frontend_tests.py
```
### **Backend Testing**
Backend tests are located in the backend_test.py file. These tests also use Selenium to test the backend functionality.

To run backend tests:
```
pytest test_todo_app.py
```
## **Structure**
* 'app.py': Main Flask application file.
* 'models.py': Defines the database models using SQLAlchemy.
* 'frontend_tests.py': Frontend tests using Selenium.
* 'test_todo_app.py': Backend tests using Pytests.
* 'index.html': HTML templates for the frontend.
* 'style.css': CSS styling for the frontend.