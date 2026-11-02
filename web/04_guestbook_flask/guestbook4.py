import sqlite3
import flask


app = flask.Flask(__name__)
DB_NAME = 'guestbook.db'


def init_db():
    with open('schema.sql', encoding='utf-8') as schema_file:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(schema_file.read())
            print('База инициализирована')


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        name = flask.request.form.get('name')
        message = flask.request.form.get('message')

        if name.strip() != '' and message.strip() != '':
            with sqlite3.connect(DB_NAME) as conn:
                conn.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))

        return flask.redirect(flask.url_for('index'))

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, message, datetime(created_at, 'localtime') FROM messages ORDER BY id DESC")
        posts = cursor.fetchall()

    return flask.render_template('index.html', posts=posts)


init_db()
app.run(debug=True, port=8000)
