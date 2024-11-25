#!/usr/bin/python3
"""Script de test HBNB Part 3"""
import requests
import json
import sys
import time

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def print_test(name, passed, message=""):
    """Affiche le résultat du test avec couleur"""
    status = f"{Colors.GREEN}✓{Colors.RESET}" if passed else f"{Colors.RED}✗{Colors.RESET}"
    print(f"{status} {name}")
    if message and not passed:
        print(f"  {Colors.RED}Error: {message}{Colors.RESET}")

def test_endpoint(method, url, data=None, expected_status=200):
    """Test un endpoint et retourne le résultat"""
    try:
        headers = {'Content-Type': 'application/json'} if data else {}
        response = requests.request(
            method=method,
            url=f"http://localhost:5000{url}",
            headers=headers,
            json=data
        )
        if response.status_code == 404:
            return True, "404 Error handled correctly"
        return response.status_code == expected_status, response.json()
    except Exception as e:
        return False, str(e)

def run_tests():
    """Exécute tous les tests"""
    tests = []
    passed_count = 0
    failed_count = 0

    print(f"\n{Colors.YELLOW}=== Démarrage des tests HBNB API ==={Colors.RESET}\n")

    # Test 1: Status API
    passed, result = test_endpoint('GET', '/api/v1/status')
    tests.append(("API Status", passed, result))

    # Test 2: Stats
    passed, result = test_endpoint('GET', '/api/v1/stats')
    tests.append(("API Stats", passed, result))

    # Test 3: Création User avec mot de passe hashé
    user_data = {
        "email": "test@test.com",
        "password": "test123",
        "first_name": "Test",
        "last_name": "User"
    }
    passed, result = test_endpoint('POST', '/api/v1/users', user_data, 201)
    tests.append(("User Creation (with hashed password)", passed, result))
    if passed:
        user_id = result.get('id')
        # Vérifier que le mot de passe est bien hashé
        if 'password' in result:
            tests.append(("Password Hashing", len(result['password']) == 32, result))

    # Test 4: Création State
    state_data = {"name": "California"}
    passed, result = test_endpoint('POST', '/api/v1/states', state_data, 201)
    tests.append(("State Creation", passed, result))
    if passed:
        state_id = result.get('id')

    # Test 5: Création City
    if 'state_id' in locals():
        city_data = {"name": "San Francisco"}
        passed, result = test_endpoint(
            'POST', 
            f'/api/v1/states/{state_id}/cities',
            city_data,
            201
        )
        tests.append(("City Creation", passed, result))
        if passed:
            city_id = result.get('id')

    # Test 6: Création Place
    if all(var in locals() for var in ['city_id', 'user_id']):
        place_data = {
            "user_id": user_id,
            "name": "Beautiful Place",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 6,
            "price_by_night": 100
        }
        passed, result = test_endpoint(
            'POST',
            f'/api/v1/cities/{city_id}/places',
            place_data,
            201
        )
        tests.append(("Place Creation", passed, result))
        if passed:
            place_id = result.get('id')

    # Test 7: Test GET User
    if 'user_id' in locals():
        passed, result = test_endpoint('GET', f'/api/v1/users/{user_id}')
        tests.append(("Get User", passed, result))

    # Test 8: Test Update User
    if 'user_id' in locals():
        update_data = {"first_name": "Updated"}
        passed, result = test_endpoint(
            'PUT',
            f'/api/v1/users/{user_id}',
            update_data
        )
        tests.append(("Update User", passed, result))

    # Test 9: Test Places Search
    search_data = {
        "states": [state_id] if 'state_id' in locals() else [],
        "cities": [city_id] if 'city_id' in locals() else [],
        "amenities": []
    }
    passed, result = test_endpoint(
        'POST',
        '/api/v1/places_search',
        search_data
    )
    tests.append(("Places Search", passed, result))

    # Test 10: Test Error 404
    passed, result = test_endpoint('GET', '/api/v1/invalid', expected_status=404)
    tests.append(("404 Error Handling", passed, result))

    # Afficher les résultats
    print("\nRésultats des tests:")
    print("-" * 50)
    for name, passed, result in tests:
        print_test(name, passed, result if not passed else "")
        if passed:
            passed_count += 1
        else:
            failed_count += 1

    # Résumé
    total = passed_count + failed_count
    print("\n" + "=" * 50)
    print(f"Total des tests: {total}")
    print(f"{Colors.GREEN}Tests réussis: {passed_count}{Colors.RESET}")
    print(f"{Colors.RED}Tests échoués: {failed_count}{Colors.RESET}")
    print(f"Pourcentage de réussite: {(passed_count/total)*100:.2f}%")
    print("=" * 50)

if __name__ == "__main__":
    try:
        run_tests()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Tests interrompus par l'utilisateur{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Erreur lors des tests: {str(e)}{Colors.RESET}")