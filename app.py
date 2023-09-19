from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Titanic Predict")

if __name__ == '__main__':
    app.run(debug=True, port=3300)
