from flask import Flask

const PORT = process.env.PORT || '8080'
app = Flask(__name__)
app.set("port", PORT)


app.config.from_object("config.DevelopmentConfig")

from app import views
