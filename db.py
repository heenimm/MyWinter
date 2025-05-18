import customtkinter
from CTkMessagebox import CTkMessagebox
import sqlite3

def db_start():
    global conn, cur
    conn = sqlite3.connect('ques.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions(
            id INTEGER PRIMARY KEY, 
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM questions")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO questions (question, answer) VALUES (?, ?)",
                    ("Какой язык программирования ты изучаешь?", "Python"))
        conn.commit()


def show_question():
    cur.execute("SELECT * FROM questions WHERE id=?", (question_number,))
    question = cur.fetchone()
    if question:
        question_label.configure(text=question[1])
    else:
        msg = CTkMessagebox(title='Викторина', message='Вопросы закончились!', option_1='Ок')
        if msg.get() == 'Ок':
            root.quit()

def next_question():
    global question_number
    question_number += 1
    show_question()

def check_answer():
    cur.execute("SELECT * FROM questions WHERE id=?", (question_number,))
    question = cur.fetchone()
    if question and answer_entry.get().strip().lower() == question[2].strip().lower():
        CTkMessagebox(title='Викторина', message='Правильный ответ!')
    else:
        CTkMessagebox(title='Викторина', message='Неправильный ответ!')
    answer_entry.delete(0, customtkinter.END)
    next_question()

root = customtkinter.CTk()
root.title('Игра на Python')
root.geometry('600x200')

question_number = 0

question_label = customtkinter.CTkLabel(
    root,
    text='',
    font=customtkinter.CTkFont(family='Arial', size=14, weight='bold'),
    wraplength=550,
    justify='left'
)
question_label.pack(pady=10)

answer_entry = customtkinter.CTkEntry(
    root,
    font=customtkinter.CTkFont(family='Arial', size=12)
)
answer_entry.pack(pady=5)

submit_button = customtkinter.CTkButton(
    root,
    text='Ответить',
    command=check_answer
)
submit_button.pack(pady=5)

db_start()
next_question()
root.mainloop()
conn.close()
