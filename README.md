# AliExpress AI Telegram Bot (CSV/RSS)

Бот автоматически публикует лучшие товары с AliExpress в Telegram-канал или чат, используя CSV или RSS фиды.  
Не нужен API и документы о компании.

## Установка

1. Создайте Telegram-бота через @BotFather
2. Создайте CSV файл с товарами (пример уже есть: products.csv)
3. Создайте GitHub репозиторий и загрузите файлы

## Секреты GitHub

Добавьте Secrets:

- BOT_TOKEN — токен Telegram-бота
- CHANNEL_ID — ID канала или чата (например @mychannel)

## Запуск

GitHub Actions можно настроить для автозапуска каждые 6 часов (пример workflow есть).
