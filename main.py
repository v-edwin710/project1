from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# Sample JSON Data
data = {
    "status": "200",
    "data": [
        {
            "id": 264,
            "cre": "1",
            "pre": "1",
            "sgn": None,
            "dtn": "2025-02-24T10:19:26",
            "dtu": "2025-03-03T11:32:23",
            "lock": None,
            "cc": "pacs",
            "wo": "2509000002",
            "so": "SO-00001",
            "area": "UNIT 11",
            "line": "DOOSAN 3-AXIS",
            "pn": "430000-N567-R07",
            "dsc": "2",
            "dtetd": "2025-03-05T00:00:00",
            "lot": "2509000002-01",
            "type": "NEW LOT",
            "prcs": "IQC",
            "lstprc": "INVENTORY",
            "shift": None,
            "emp": None,
            "empnm": None,
            "dtin": "2025-02-24 10:19:19",
            "tmin": None,
            "qtyin": 2.0,
            "dtout": None,
            "tmout": None,
            "qtyout": None,
            "sts": "ASSIGNED",
            "rmk": "",
            "defCtr": 1,
            "asgnMac": "3AD1",
            "asgnSeq": "1",
            "plnStrt": "28-Feb-25 4:58:26 PM",
            "plnEnd": "28-Feb-25 8:58:26 PM"
        },
        {
            "id": 266,
            "cre": "1",
            "pre": "1",
            "sgn": None,
            "dtn": "2025-02-24T10:19:26",
            "dtu": "2025-03-03T11:32:23",
            "lock": None,
            "cc": "pacs",
            "wo": "2509000002",
            "so": "SO-00001",
            "area": "UNIT 1300",
            "line": "DOOSAN 5-AXIS",
            "pn": "430000-N567-R07",
            "dsc": "2",
            "dtetd": "2025-03-05T00:00:00",
            "lot": "2509000002-01",
            "type": "NEW LOT",
            "prcs": "IQC",
            "lstprc": "INVENTORY",
            "shift": None,
            "emp": None,
            "empnm": None,
            "dtin": "2025-02-24 10:19:19",
            "tmin": None,
            "qtyin": 2.0,
            "dtout": None,
            "tmout": None,
            "qtyout": None,
            "sts": "ASSIGNED",
            "rmk": "",
            "defCtr": 1,
            "asgnMac": "3AD1",
            "asgnSeq": "1",
            "plnStrt": "28-Feb-25 4:58:26 PM",
            "plnEnd": "28-Feb-25 8:58:26 PM"
        }
    ]
}

# Home Route (Fixes 404 Error)
@app.route('/')
def home():
    return "Welcome to the API! Use /api/data to fetch data."

# API Route to Fetch Data
@app.route('/api/data', methods=['POST', 'GET'])
def get_data():
    return jsonify(data)

# Health Check Route
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API is running"}), 200

# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)