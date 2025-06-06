# Sprint_6
# Проект тестов для "Яндекс Самокат"

Этот проект содержит автоматизированные тесты для веб-сайта [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/), онлайн-сервиса для аренды самокатов.

Тесты написаны с использованием Python, Selenium и pytest. Они покрывают различные сценарии работы с сайтом.

## Описание тестов
Тесты охватывают следующие сценарии:

1. **Вопросы о важном:**
- Проверка всех полей в разделе FAQ на активацию ответов по нажатию на вопрос; 
- Проверка на соответствие вопросов и ответов.
   
2. **Заказ самоката:**
- Проверка перехода на страницу с заказом для двух кнопок «Заказать»;
- Проверка успешного заказа самоката (с двумя наборами данных);
- Проверка перехода на главную страницу по клику на «Самоката» (после заказа);
- Проверка перехода на главную страницу по клику на «Яндекс» (после заказа).

## Требования
Для запуска тестов необходимо установить:
- Python 3.7 и выше
- Selenium
- pytest
- WebDriver для браузера

## Структура проекта
```
project/
├── tests/                  # Тесты
├── pages/                  # PageObject-классы
├── helpers/                # Вспомогательные функции и данные
├── conftest.py             # Pytest фикстуры
├── requirements.txt        # Зависимости
├── allure_results/         # Raw-результаты (в .gitignore)
├── allure_report/          # Сгенерированный HTML-отчёт (временно добавлен)
└── README.md               # Документация проекта
```

## Установка

1. Клонирование репозитория:

```bash
git clone git@github.com:L1ghTyyyy/Sprint_6.git
```

2. Установка зависимостей:

```bash
pip install -r requirements.txt
```

3. Запуск теста:

```bash
pytest
```

4. Генерация отчета о тестировании:

```bash
allure generate allure_results --clean -o allure_report
```

5. Просмотр отчета:

```bash
 allure open allure_report
```
