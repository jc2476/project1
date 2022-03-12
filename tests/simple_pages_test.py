"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/">Home</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/pf">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/resources">Resources</a>' in response.data
    assert b'<a class="nav-link" href="/calculator">Calculator</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"IS601 Project 1" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"docker" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/pf")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/calculator")
    assert response.status_code == 200
    assert b"Calculator" in response.data

def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/resources")
    assert response.status_code == 200
    assert b"Resources" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
