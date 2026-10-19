from flask import Flask
app = Flask(__name__)
@app.route("/")
def hom():
    return "Welcome the"
if __name__ == '__main__':
    app.run(debug=True)