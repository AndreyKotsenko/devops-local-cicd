from flask import Flask, jsonify

app = Flask(__name__)

#Glory to Ukraine! Start CI-CD...
@app.route("/")
def home():
    return jsonify({"message": "Hello, DevOps World!"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
