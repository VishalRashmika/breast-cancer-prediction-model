import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness):
    # try:
    #     loc_index = __data_columns.index(location.lower())
    # except:
    #     loc_index = -1

    # x = np.zeros(4)
    # x[0] = mean_radius
    # x[1] = mean_texture
    # x[2] = mean_perimeter
    # x[3] = mean_area
    # x[4] = mean_smoothness
    # if loc_index>=0:
    #     x[loc_index] = 1
    input1 = [mean_radius]
    input1 = [mean_texture]
    input1 = [mean_perimeter]
    input1 = [mean_area]
    input1 = [mean_smoothness]

    data = {
        "x" : input
    }
    data_set = pd.DataFrame(data)


    return (__model.predict(data_set))


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/breast_cancer_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()

    # print(get_location_names())
    print(get_estimated_price(20.29,14.34,135.1,1297.0,0.1003))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location