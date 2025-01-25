from flask import Flask, request, jsonify
import json
import traceback

app = Flask(__name__)

# Load JSON data from file
try:
    with open('q-vercel-python.json','r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading JSON: {e}")

#@app.route('/get_marks', methods=['GET'])
@app.route('/app', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "Name parameter is missing"}), 400

    results = ""
    for name in names:
        result = next((item for item in data if item['name'] == name), None)
        if result:
            #results.append(result['marks'])
            results += str(result['marks']) + " "
    
    
    if results:
        results = results.strip()
        return jsonify({"marks": results}), 200
    else:
        return jsonify({"error": "Names not found"}), 404

if __name__ == '__main__':
    app.run()
