from flask import Flask, render_template, request
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)
model = keras.models.load_model('fetal_anomaly_detection.h5')

@app.route('/')
def index():
    return render_template("index.html", name="Tariq")

@app.route('/prediction', methods=["POST"])
def prediction():
    patient_name = request.form['patient_name']
    week_of_fetal = request.form['week_of_fetal']
    img = request.files['img']
    img.save('img.jpg')

    img = image.load_img("img.jpg", target_size=(224, 224))
    x = image.img_to_array(img) / 255
    resized_img_np = np.expand_dims(x, axis=0)
    prediction = model.predict(resized_img_np)
    
    if prediction[0][0] > 0.5:
        pred = "Status of Sonography Report: Normal"
    else:
        pred = "Status of Sonography Report: Abnormal"

    return render_template("prediction.html", data=pred, patient_name=patient_name, week_of_fetal=week_of_fetal)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
