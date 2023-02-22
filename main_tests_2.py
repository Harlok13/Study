import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp_connection():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as connect:
        yield connect

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    # поднимем исключение, чтобы посмотреть 
    # что происходит в выводе `pytest`
    assert 0  

def test_noop(smtp_connection):
    response, _ = smtp_connection.noop()
    assert response == 250
    assert 0
