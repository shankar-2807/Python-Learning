from flask import Flask, request, jsonify, send_from_directory
import io, os, base64, numpy as np
from PIL import Image

app = Flask(__name__, static_folder='.')

MODEL_PATH = "model.h5"

def base64_to_pil(data_url):
    header, encoded = data_url.split(",", 1)
    data = base64.b64decode(encoded)
    return Image.open(io.BytesIO(data)).convert("RGB")

# Fallback color-threshold detector (works if no ML model available)
def detect_color_square_pil(img):
    arr = np.array(img)
    # downsample for speed
    small = img.resize((128, 128))
    a = np.array(small)
    # compute mean channel intensities
    r = a[:, :, 0].mean()
    g = a[:, :, 1].mean()
    b = a[:, :, 2].mean()

    if r > g and r > b:
        color = 'red'
        mask = a[:, :, 0] > (a[:, :, 1] + a[:, :, 2]) / 2 + 40
    elif g > r and g > b:
        color = 'green'
        mask = a[:, :, 1] > (a[:, :, 0] + a[:, :, 2]) / 2 + 40
    else:
        color = 'blue'
        mask = a[:, :, 2] > (a[:, :, 0] + a[:, :, 1]) / 2 + 40

    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    x0, x1 = xs.min(), xs.max()
    y0, y1 = ys.min(), ys.max()

    # scale back to original image size
    sx = img.width / 128.0
    sy = img.height / 128.0
    bbox = [int(x0 * sx), int(y0 * sy), int((x1 - x0 + 1) * sx), int((y1 - y0 + 1) * sy)]

    return {"class": color, "bbox": bbox, "score": 0.5}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({"error": "no image"}), 400

    img = base64_to_pil(data['image'])

    # Try to load a trained Keras model (if exists)
    try:
        from tensorflow.keras.models import load_model
        model = load_model(MODEL_PATH)

        img_small = img.resize((128, 128))
        x = np.array(img_small).astype('float32') / 255.0
        x = np.expand_dims(x, 0)

        pred = model.predict(x)[0]  # [x_center, y_center, w, h, class0, class1, class2]
        bx = pred[0:4]
        classes = pred[4:]
        cls = int(np.argmax(classes))
        cls_name = ['red', 'green', 'blue'][cls]

        # convert center-based bbox to pixel coords
        x_c, y_c, bw, bh = bx
        imgw, imgh = img.width, img.height
        x = int((x_c - bw / 2) * imgw)
        y = int((y_c - bh / 2) * imgh)
        w = int(bw * imgw)
        h = int(bh * imgh)

        return jsonify({"class": cls_name, "bbox": [x, y, w, h], "score": float(np.max(classes))})

    except Exception:
        # fallback detector if model not available
        res = detect_color_square_pil(img)
        if res is None:
            return jsonify({"error": "no square detected"}), 200
        return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    