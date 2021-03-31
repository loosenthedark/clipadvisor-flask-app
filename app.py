import os
from flask import Flask
if os.path.exists('env.py'):
    import env


app = Flask(__name__)


@app.route('/')
def hello():
    return "Version 2.0!"


ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP'), port=5000)
