from tinyrouter import Route
from flask import Flask

app = Flask(__name__)

def user_index():
    ...

routes = [
    Route('user.index', '/user', user_index)
]

print(Route('user.index', '/user', user_index))