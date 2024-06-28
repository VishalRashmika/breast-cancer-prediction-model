from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    print("1")
    print(request.form['t_mean_radius'])
    mean_radius = float(request.form['t_mean_radius'])
    mean_texture = float(request.form['t_mean_texture'])
    mean_perimeter = float(request.form['t_mean_perimeter'])
    mean_area = float(request.form['t_mean_area'])
    mean_smoothness = float(request.form['t_mean_smoothness'])

    print("QWE")
    print(util.get_estimated_price(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness))
    print("AWDA")
    response = jsonify({
        'estimated_price': util.get_estimated_price(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()