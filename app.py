from flask import Flask, render_template, request
from models.Classifier import model
import pandas as pd
app = Flask(__name__)
# Routes
@app.route('/')
def home():
    return render_template('index.html', title="Titanic Predict")

#Route Form
@app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        pclass = int(request.form['class'])

   
        data={
            'age':age, 
            'sex':sex,
            'pclass':pclass
            }
        df = pd.DataFrame(data, index=[0])
        resultat = model.survie(df)
        print(age, sex, pclass)
        return render_template ('form.html',result=resultat, title="resultat")
    else:
        return render_template ('form.html', title="resultat")


if __name__ == '__main__':
    app.run(debug=True, port=3300)
