import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """WebDriver instance for Firefox"""
    options = Options()
    options.profile = os.environ.get("SELENIUM_FIREFOX_PROFILE", None)

    options.add_argument("--headless")

    driver = webdriver.Firefox(options)

    yield driver
    driver.close()

def test_add_todo(driver):
    """Test adding a new todo"""
    driver.get("http://localhost:5000")

    add_todo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "todo_name")))

    add_todo.send_keys("Test todo")

    todo_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-todo")))

    todo_button.click()

    assert "Test todo" in driver.page_source

def test_edit_todo(driver):
    """Test editing a todo"""
    driver.get("http://localhost:5000")

    edit_todo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "new_name")))

    edit_todo.send_keys("Edited test todo")

    edit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "edit-button")))

    edit_button.click()

    assert "Edited test todo" in driver.page_source

def test_toggle_checked(driver):
    """Test toggling checkbox"""
    driver.get("http://localhost:5000")

    checkbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/form[1]/input")))

    checkbox.click()

    toggled_checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[1]/input")
    assert toggled_checkbox.is_selected()

def test_search_todo(driver):
    "Adding search todo, filtering and deleting it"
    driver.get("http://localhost:5000")

    add_search_todo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "todo_name")))

    add_search_todo.send_keys("Search todo")
    add_search_todo.send_keys(Keys.ENTER)
    time.sleep(1)

    filter_search_todo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
    filter_search_todo.click()
    filter_search_todo.send_keys("Search todo")

    search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "search-button")))
    search_button.click()

    assert "Search todo" in driver.page_source
    assert "Edited test todo" not in driver.page_source

    delete_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/form[2]/button")))

    delete_button.click()

def test_delete_todo(driver):
    """Test deleting a todo"""
    driver.get("http://localhost:5000")

    delete_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/form[2]/button")))

    delete_button.click()
    assert "Edited test todo" not in driver.page_source
