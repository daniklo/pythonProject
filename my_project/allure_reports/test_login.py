import allure
#test_login.py
@allure.suite("login Suite")
def test_valid_login():
    assert 1 == 1

@allure.suite("login Suite")
def test_invalid_login():
    assert 1 == 0

