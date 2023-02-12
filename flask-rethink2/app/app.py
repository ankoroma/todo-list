from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = 'vrcWmmhzVtSTS7Pg0lDoeA'

import views

