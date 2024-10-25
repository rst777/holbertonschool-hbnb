#!/user/bin/python3

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.email == "john.doe@example.com"
    print("Test réussi pour la création d'utilisateur !")

test_user_creation()

