import requests

def test_httpbin_get():
    """Test the /get endpoint of httpbin."""
    response = requests.get('http://httpbin/get')
    assert response.status_code == 200
    assert 'url' in response.json()

def test_httpbin_status_code():
    """Test the /status/:code endpoint of httpbin."""
    status_code = 200
    response = requests.get(f'http://httpbin/status/{status_code}')
    assert response.status_code == status_code
