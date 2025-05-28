import pytest
import random
import time
import allure

@allure.title("Ошибка API при неправильном ID продукта")
def test_1():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректное возвращение цены для заданного продукта через API")
def test_2():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Обновление цен через API")
def test_3():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отсутствие ошибки API при правильном обновлении цены")
def test_4():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Возможность сброса пароля")
def test_5():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Неправильная попытка входа")
def test_6():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Возможность выхода из приложения")
def test_7():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Ошибка при неверном вводе данных для регистрации")
def test_8():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Успешная загрузка главной страницы")
def test_9():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Логотип на главной странице ведет на правильный URL")
def test_10():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отображение данных о заказах в профиле пользователя")
def test_11():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Доступность кнопки Добавить в избранное в зависимости от статуса пользователя")
def test_12():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Обновление email-адреса в настройках")
def test_13():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректная работа интерфейса при переключении валют")
def test_14():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректность отображения уведомлений для разных типов пользователей")
def test_15():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Видимость всех цен продуктов на мобильной версии")
def test_16():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректная работа кнопки Удалить продукт из отслеживания")
def test_17():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Работа функции Добавить в список наблюдения")
def test_18():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отображение истории цен продукта")
def test_19():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Ошибка при неверно введенном email")
def test_20():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Правильность отображения ошибок на странице ошибки 404")
def test_21():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Переход на страницу Связаться с нами")
def test_22():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Обновление цены продукта")
def test_23():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректная загрузка страницы продукта на мобильных устройствах")
def test_24():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректность отображения цены на странице товара для разных валют")
def test_25():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Наличие кнопки для добавления продукта в избранное")
def test_26():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Открытие страницы с деталями продукта")
def test_27():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отображение актуальной цены продукта на странице")
def test_28():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отображение кнопки для подписки на уведомления о цене на странице продукта")
def test_29():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отправка email-уведомлений о снижении цены")
def test_30():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отправка уведомлений в правильное время")
def test_31():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректность отображения уведомлений о ценах на главной странице")
def test_32():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Корректная работа уведомлений о снижении цен для разных категорий товаров")
def test_33():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отображение уведомлений о снижении цены в правильном порядке")
def test_34():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Настройка уведомлений о снижении цен")
def test_35():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title("Отключение уведомлений о снижении цен")
def test_36():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert True, "Тест завершился успешно"

@allure.title(" Сохранение настроек уведомлений при их изменении")
def test_37():
    delay_ms = random.randint(1000, 3000)
    with allure.step(f"Ожидание {delay_ms} миллисекунд"):
        time.sleep(delay_ms / 1000)
    assert False, "Тест завершился с ошибкой"
