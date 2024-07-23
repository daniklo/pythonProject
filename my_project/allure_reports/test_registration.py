import allure
#test_registration.py
@allure.suite("Registration Suite")
def test_valid_registration():
    assert 1 == 1

@allure.suite("Registration Suite")
def test_invalid_registration():
    assert 1 == 0

