import os
from flask import Flask

# we put here the module name and because we have one module we write __name__ which is the default module
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5001")),
        debug=True
    )
