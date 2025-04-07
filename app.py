from flask import Flask, request, jsonify, make_response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    render_template('aman.html')

@app.route('/sheet-data')
def get_sheet_data():
    try:
        google_sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSeQiSIUd9wAv87sVslP_lpRCosorGrmhKMM2KkvfQU1NR2C8hnQLpCA88Zdls-MUgRuNb3PpwAYmSl/pub?gid=0&single=true&output=csv'  # Replace with your Google Sheet URL
        response = requests.get(google_sheet_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return make_response(jsonify({'error': str(e)}), 500)


if __name__ == '__main__':
    app.run(debug=True)