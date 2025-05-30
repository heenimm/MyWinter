# MyWinter

# 🎣 Игра: «Фишинг. Охота на доверчивых!»

Интерактивная викторина с графическим интерфейсом, целью которой является повышение осведомлённости о фишинговых атаках и безопасном поведении в сети.

---

### Установить зависимости:

```bash
pip install customtkinter CTkMessagebox
```

---

### Запуск игры:
------------------------------------------------

```bash
python main.py
```

---

## ////////////////////////////////////////////////////////////////////////////

## ВАЖНО: При первом запуске создаётся база данных `ques.db`, содержащая вопросы викторины. Вы можете отредактировать или добавить новые вопросы вручную через SQLite.////////////////////////////////////////////////////////////////////////////

---

## 📋 Пример вопросов:

1. Вам отправили письмо:  
   _«Дорогой покупатель, вы стали обладателем подарочного купона на сумму 5000₽.  
   Для получения купона перейдите по адресу - http://drive.com/d/54673dggsdhj6573...»_

   Ваши действия?

   ```
   А. Перейду на сайт — в адресе нет ничего подозрительного  
   Б. Нет, безличное обращение вызывает сомнение  
   В. Нет, отсутствует безопасное соединение HTTPS
   ```

   ✅ Правильный ответ: **В**

---




### Интерфейс:

```
Приветствуем тебя в игре "Фишинг. Охота на доверчивых!"
Как тебя зовут?
>> Иван
Привет, Иван

"И так, первый вопрос:
Вам отправили письмо: ... "
```

Каждое неверное действие приводит к потере очков/завершению игры, правильные ответы — к продолжению.

---

## 📂 Структура проекта

```
phishing-quiz/
├── main.py               # Основная игра (customtkinter)
├── ques.db               # SQLite база с вопросами
└── README.md             # Документация
```

---

## 🧑‍💻 Возможности:

- Простой интерфейс для обучения пользователей
- Визуальные окна обратной связи
- Автоматическое переключение между вопросами
- Консольная версия для терминалов

---


