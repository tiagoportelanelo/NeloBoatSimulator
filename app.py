# importing libraries
from flask import Flask, request, Response, jsonify, render_template
import random
import json

# creating an instance of the flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# route to dget gps speed
@app.route('/api/speed/gps', methods=['GET'])
def get_gps_speed():
    '''return gps speed'''
    return json.dumps({'gps_speed': round(random.uniform(0, 6), 2)
                       })


@app.route('/api/speed/real', methods=['GET'])
def get_real_speed():
    '''return real speed'''
    return json.dumps({'real_speed': round(random.uniform(0, 6), 2)
                       })


@app.route('/api/speed/max', methods=['GET'])
def get_max_speed():
    '''return real speed'''
    return json.dumps({'max_speed': round(random.uniform(0, 6), 2)
                       })


@app.route('/api/speed/avg', methods=['GET'])
def get_avg_speed():
    '''return real speed'''
    return json.dumps({'avg_speed': round(random.uniform(0, 6), 2)
                       })


@app.route('/api/destination/distance', methods=['GET'])
def get_destination_distance():
    '''return real speed'''
    return json.dumps({'distance_destination': round(random.uniform(0, 100), 2)
                       })


@app.route('/api/destination/compass', methods=['GET'])
def get_destination_compass():
    '''return real speed'''
    return json.dumps({'compass_destination': round(random.uniform(0, 360), 2)
                       })


@app.route('/api/stroke/spm', methods=['GET'])
def get_stroke_spm():
    '''return real speed'''
    return json.dumps({'spm': round(random.randint(0, 180), 2)
                       })


@app.route('/api/stroke/distance', methods=['GET'])
def get_stroke_distance():
    '''return real speed'''
    return json.dumps({'distance_per_stroke': round(random.uniform(0, 1.5), 2)
                       })


@app.route('/api/stroke/spm/avg', methods=['GET'])
def get_stroke_spm_avg():
    '''return real speed'''
    return json.dumps({'average_spm': round(random.randint(0, 180), 2)
                       })


@app.route('/api/lap/time', methods=['GET'])
def get_lap_time():
    '''return real speed'''
    return json.dumps({'lap_time': round(random.uniform(0, 2), 2)
                       })


@app.route('/api/lap/distance', methods=['GET'])
def get_lap_distance():
    '''return real speed'''
    return json.dumps({'lap_distance': round(random.uniform(0, 100), 2)
                       })


@app.route('/api/hr/max', methods=['GET'])
def get_hr_max():
    '''return real speed'''
    return json.dumps({'hr_max': round(random.uniform(0, 5), 2)
                       })


@app.route('/api/hr', methods=['GET'])
def get_hr():
    '''return real speed'''
    return json.dumps({'hr': round(random.uniform(0, 5), 2)
                       })


@app.route('/api/hr/avg', methods=['GET'])
def get_hr_avg():
    '''return real speed'''
    return json.dumps({'hr_avg': round(random.uniform(0, 5), 2)
                       })


@app.route('/api/boat/angle', methods=['GET'])
def get_angle_surf():
    '''return real speed'''
    return json.dumps({'angle_surf': round(random.uniform(0, 45), 2)
                       })


@app.route('/api/boat/active', methods=['GET'])
def get_boat_active_time():
    '''return real speed'''
    return json.dumps({'active_time': round(random.uniform(0, 500), 2)
                       })


@app.route('/api/boat/resting', methods=['GET'])
def get_boat_resting_time():
    '''return real speed'''
    return json.dumps({'resting_time': round(random.uniform(0, 500), 2)
                       })


@app.route('/api/environment/water/temperature', methods=['GET'])
def get_water_temperature():
    '''return real speed'''
    return json.dumps({'water_temperature': round(random.uniform(-2, 20), 2)
                       })


if __name__ == "__main__":
    app.run(port=1234, debug=True)
