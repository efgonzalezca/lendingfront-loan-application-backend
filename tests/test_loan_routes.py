import pytest
from flaskr import create_app

test_route = '/api/loan/evaluate'

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_valid_loan_request_approved(client):
    payload = {
        'tax_id': '12345890',
        'name': 'Test Company',
        'amount': 40000
    }
    res = client.post(test_route, json=payload)
    assert res.status_code == 200
    data = res.get_json()
    assert data["decision"] == "Approved"

def test_valid_loan_request_undecided(client):
    payload = {
        'tax_id': '12345890',
        'name': 'Test Company',
        'amount': 50000
    }
    res = client.post(test_route, json=payload)
    assert res.status_code == 200
    data = res.get_json()
    assert data["decision"] == "Undecided"

def test_valid_loan_request_declined(client):
    payload = {
        'tax_id': '12345890',
        'name': 'Test Company',
        'amount': 60000
    }
    res = client.post(test_route, json=payload)
    assert res.status_code == 200
    data = res.get_json()
    assert data["decision"] == "Declined"

def test_negative_amount(client):
    payload = {
        "taxId": "123456",
        "name": "Empresa Y",
        "amount": -100
    }
    res = client.post(test_route, json=payload)
    assert res.status_code == 400
    assert "amount" in res.get_json()["errors"]