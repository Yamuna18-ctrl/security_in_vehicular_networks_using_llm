from flask import Flask, jsonify, render_template
from backend.data_streamer import get_live_vehicle_batch

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/live-data")
def live_data():
    try:
        return jsonify(get_live_vehicle_batch())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
