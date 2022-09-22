from flask import Flask, render_template
import pandas as pd
from utils import recommender


app = Flask(__name__)

df = pd.read_csv('C:/Users/Hanog/OneDrive/Masaustu/goplayrec/cleaned.csv')
@app.route('/')
def home():
    N = 9
    random6 = df.sample(N)
    random6 = [dict(random6.iloc[i]) for i in range(N)]

    return render_template('index.html', apps=random6)


@app.route('/output/<app>')
def output(app):
    result = dict(df[df['App']==app].squeeze())
    recommended_app= recommender(df, result['Genres'])
    return render_template('output.html', result=result, recommended_app=recommended_app)



if __name__ == "__main__":
    app.run(debug=True)