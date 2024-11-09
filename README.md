# Практикум - 1 лабораторная (e2e тесты) 

## Автотестирование сайта с использованием Pytest и Playwright

Этот репозиторий содержит программу для автотестирования веб-сайта, написанную на Python с использованием фреймворков Pytest и Playwright. Проект предназначен для проверки функциональности веб-приложений и автоматизации тестирования.

Для тестирования были взяты тест кейсы:

1 Вход с некорректными данными

2 Вход с пустыми полями

4 добавление одного товара в корзину.

В папках tests и pages содержаться пустые файлы init.py 
т.к. без них не виделись файлы.

## Содержание

- [Описание](#описание)
- [Установка](#установка)
- [Запуск тестов](#запуск-тестов)

## Описание

Проект включает в себя набор тестов, которые проверяют различные аспекты работы веб-сайта. Тесты написаны с использованием Pytest и Playwright, что позволяет легко управлять тестами и запускать их в различных средах.
сайт: https://www.saucedemo.com/

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Dmitry505/workshop_5_semester.git
   cd workshop_5_semester/lab_1
   
2. Установите зависимости:

    ```bash
    python -m pip install --upgrade pip
    pip install pytest playwright pytest-html

3. Установите браузеры Playwright:

    ```bash
   python -m playwright install

## Запуск тестов

```bash
pytest

    