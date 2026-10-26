import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/estimate', methods=['POST'])
def calculate_estimate():
    data = request.json
    service_type = data.get("service", "General Repair")
    square_footage = float(data.get("sqft", 100))
    
    rates = {
        "Kitchen Remodel": 75.0,
        "Bathroom Reno": 60.0,
        "Drywall & Painting": 15.0,
        "Flooring Installation": 12.0
    }
    
    rate = rates.get(service_type, 20.0)
    estimated_cost = square_footage * rate
    
    return jsonify({
        "service": service_type,
        "sqft": square_footage,
        "estimated_cost": round(estimated_cost, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
