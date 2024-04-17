from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/move', methods=['GET'])
def move():
    response_data = {
        "title": "MISSION DAY",
        "subtitle": "SOL 74",
        "time": "22:19",
        "logEntry": "WATNEY #120",
        "image": "/images/KenKaneki.jpg",
        "pressure": "12.46 PSI",
        "oxygen": "20% O2",
        "temperature": "-16.0 °C",
        "roverInfo": "ROVER 2 > DASHCAM",
        "connectionInfo": "CONNECTED 08021912WE2VC-LC-100240-23-3",
        "cabPressure": "12.47 PSI",
        "mode": "PRK",
        "roverStatus": "Active"
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
