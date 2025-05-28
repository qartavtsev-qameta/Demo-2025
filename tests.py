import allure
import pytest
import random
import time
import allure

@allure.title("Успешный тест с ожиданием")
def test_success_with_random_delay():
    delay = random.randint(1, 30)
    with allure.step(f"Ожидание {delay} секунд"):
        time.sleep(delay)
    assert True, "Тест завершился успешно"

@allure.title("Неуспешный тест с ожиданием")
def test_failure_with_random_delay():
    delay = random.randint(1, 30)
    with allure.step(f"Ожидание {delay} секунд"):
        time.sleep(delay)
    assert False, "Тест завершился с ошибкой"
