# Flask ONNX Inference

This is a simple flask app that loads a model from an ONNX file and makes predictions.

## Prerequisites

Docker installed on your system

## Setup

```bash
git clone https://github.com/metehankutlu/flask-onnx-inference.git

docker compose up -d
```

## Making Predictions

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"Material_A_Charged_Amount": 2.0, "Material_B_Charged_Amount": 3.0, "Reactor_Volume": 4.0, "Material_A_Final_Concentration_Previous_Batch": 5.0}' \
  http://localhost:8000/predict/
```

## Project Structure

```code
flask-onnx-inference/
│
├── app/
│   ├── models/
│   │   └── model.onnx
│   ├── src/
│   │   ├── app.py
│   │   └── model.py
│   ├── tests/
│   │   └── test_app.py
│   ├── Dockerfile
│   ├── pytest.ini
│   └── requirements.txt
├── .gitignore
├── docker-compose.yml
└── README.md
```
