from flask import Flask

app = Flask(__name__)

from controllers import object_controllers

if __name__ == "__main__":
    app.run(debug=True)