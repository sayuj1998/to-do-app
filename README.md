# **Todo App**
This is a simple todo application built with Flask.

## **Features**
* Add, edit, delete, and toggle completion status of todos.
* Search functionality to filter todos based on their descriptions.
* Database powered by SQLAlchemy for storage.
* Frontend tested with Selenium to ensure UI functionality.
* Backend tested with Pytest to ensure backend functionality.

## **Prerequisites with docker (Recommended)**
1) Install docker: Docker is a platform to build, run, and share applications with containers. You can download and install Docker Desktop from the official Docker website: [Docker Desktop](https://www.docker.com/products/docker-desktop)
3) Open a terminal (CMD prompt, Bash, Shell etc.)
4) Build the Docker image, run the following command:
```
docker build -t todoapp .
```
4) Execute the follow command to run the Docker container:
```
docker run -p 5000:5000 todoapp
```
5) You're all set! Follow the provided instructions to run the todo app with Docker. Don't forget to add, edit, delete, search, and toggle completion status of your todos. Enjoy! 

## **Prerequisites without docker**
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
* 'test_todo_app.py': Backend and API tests using Pytest.
* 'index.html': HTML templates for the frontend.
* 'style.css': CSS styling for the frontend.
