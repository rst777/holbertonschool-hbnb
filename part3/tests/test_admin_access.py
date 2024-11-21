def test_admin_can_create_user(client, admin_user, headers):
    response = client.post('/users', json={
        'email': 'newuser@example.com',
        'password': 'password123'
    }, headers=headers)
    assert response.status_code == 201

def test_non_admin_cannot_create_user(client, non_admin_user, headers):
    response = client.post('/users', json={
        'email': 'newuser@example.com',
        'password': 'password123'
    }, headers=headers)
    assert response.status_code == 403
