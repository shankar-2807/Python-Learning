from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import os
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load pretrained model
model = MobileNetV2(weights="imagenet")

# Map many ImageNet labels to simpler animal categories
animal_mapping = {
    # Horses
    "sorrel": "Horse", "Appaloosa": "Horse", "Arabian_horse": "Horse", "Palomino": "Horse",
    # Dogs (group all dog breeds)
    "German_shepherd": "Dog", "Labrador_retriever": "Dog", "golden_retriever": "Dog",
    "beagle": "Dog", "pug": "Dog", "dalmatian": "Dog",
    # Cats (group cat breeds)
    "Siamese_cat": "Cat", "Persian_cat": "Cat", "Egyptian_cat": "Cat", "tabby": "Cat",
    # Lions
    "lion": "Lion",
    # Buffalos / ox family
    "ox": "Buffalo", "bison": "Buffalo", "water_buffalo": "Buffalo",
    # Elephants
    "Indian_elephant": "Elephant", "African_elephant": "Elephant"
}

users = {}

@app.route('/')
def index():
    return render_template('signup_login.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return "User already exists"
    users[username] = password
    return redirect(url_for('login_page'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('main_page'))
    return "Invalid credentials"

@app.route('/login_page')
def login_page():
    return render_template('signup_login.html')

@app.route('/main')
def main_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded = decode_predictions(predictions, top=1)[0][0]

    label = decoded[1]
    confidence = round(float(decoded[2]) * 100, 2)

    if label in animal_mapping:
        predicted_class = animal_mapping[label]
    else:
        predicted_class = "Unknown"

    return render_template("index.html", prediction=f"{predicted_class} ({confidence}%)", image_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)




