from flask import Flask
import onnxruntime as ort

app = Flask(__name__)
sess = ort.InferenceSession("models/model.onnx")

@app.route('/')
def predict():
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)