from flask import Flask, request, jsonify, render_template, url_for
from flask_bootstrap import Bootstrap
import pickle
import numpy as np

app = Flask(__name__)
Bootstrap(app)
model = pickle.load(open('./model/page_block_classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]

    height, length, blackpix, blackand, wb_trans = int_features
    area = height*length
    eccen = length/height
    p_black = blackpix/area 
    p_and = blackand/area
    mean_tr = blackpix / wb_trans

    complete_features = [ height, length, area, eccen, p_black, p_and, mean_tr, blackpix, blackand, wb_trans ]
    final_features = [np.array(complete_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    page_block_dict = {
        1: "text",
        2: "horizontal line",
        3: "picture ",
        4: "vertical line",
        5: "graphic"
        }

    return render_template('index.html', prediction_text='The type of the page block you set up is: {}'.format(page_block_dict.get(output)))

if __name__ == "__main__":
    #démarre un serveur en local qui serve ma webapp
    print(app.url_map)
    app.run(host="127.0.0.1",port=5000,debug=True)