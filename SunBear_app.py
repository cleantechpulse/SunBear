from flask import Flask, render_template, redirect, request, jsonify
import model
import API
import os

app = Flask(__name__)
app.secret_key = os.environ["flask_app_key"]


@app.route("/")
def index():
    pass



def main():
    pass



if __name__ == "__main__":
    main()
    # app.run(host="0.0.0.0", debug=False)
    app.run(debug=True)

