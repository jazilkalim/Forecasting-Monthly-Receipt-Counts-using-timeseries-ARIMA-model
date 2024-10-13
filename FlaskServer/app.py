from flask import Flask, request, jsonify, render_template
import utils
from custom_arima import custom_ARIMA
import os
import sys

# Get the directory of the currently running script
current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# Change the current working directory to the script's directory
os.chdir(current_directory)

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('app.html')  # This will serve the HTML page located in the 'templates' folder

# Route for prediction API
@app.route('/predict_receipt_count', methods=['POST'])
def predict_receipt_count():
    year_ent = int(request.form['year'])
    month_ent = int(request.form['month'])

    response = jsonify({
        'estimated_count': utils.get_prediction(year_ent, month_ent)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Receipt Count...")
    utils.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)
