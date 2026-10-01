def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Chetanay" in response.data
    assert b"Portfolio" in response.data

def test_404_error(client):
    """Test that a non-existent page returns a 404 error."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
    assert b"Page Not Found" in response.data
