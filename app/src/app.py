import json
from flask import Flask, request
import onnxruntime as ort
from marshmallow import ValidationError

from model import InputSchema

app = Flask(__name__)
sess = ort.InferenceSession("models/model.onnx")

@app.route('/predict/', methods=["POST"])
def predict():
    json_input = request.get_json()
    try:
        input_data = InputSchema().load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    output = sess.run(["output_label", "output_probability"], input_data)
    return {
        "label": output[0][0],
        "probability": output[1][0]
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)