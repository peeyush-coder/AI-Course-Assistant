import sqlite3

DATABASE="database/chatbot.db"


def connect():

    return sqlite3.connect(DATABASE)


def create_database():

    conn=connect()

    cur=conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS chat_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    cur.execute("""

    CREATE TABLE IF NOT EXISTS uploaded_documents(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()

def save_chat(question, answer):

    conn = connect()

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO chat_history(

    question,

    answer

    )

    VALUES(?,?)

    """,

    (question, answer)

    )

    conn.commit()

    conn.close()