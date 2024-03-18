import os, time
import numpy as np
import pandas as pd
import tensorflow.keras as keras
from .utils.utils import save_test_duration

cur_directory = os.path.dirname(os.path.realpath(__file__))

def inference(x_test):
    start_time = time.time()

    model = keras.models.load_model(f'{cur_directory}/best_model.hdf5')
    
    y_pred = model.predict(x_test)
    y_pred_numbered = np.argmax(y_pred, axis=1)

    test_duration = time.time() - start_time
    save_test_duration(f'{cur_directory}/test_duration.csv', test_duration)
    return y_pred_numbered


def run_inference():
    start = time.time()
    
    possible_categories = ['Beauty', 'Education', 'Entertainment ', 'Knowledge', 'Music', 'News', 'Sports', 'Technology', 'Food', 'Game', 'Movie']
    
    data_path=f'{cur_directory}/data_csv'
    x_test = pd.read_csv(os.path.join(data_path,'test_shortlist.csv'))
    print(x_test.shape)
    x_test = x_test.iloc[:10, :3000]
    
    y_pred_numbered = inference(x_test)
    print(y_pred_numbered)

    results = list(map(lambda x: possible_categories[x], y_pred_numbered))

    end = time.time()
    print('Running time: %s Seconds' % (end - start))

    return results


if __name__ == "__main__":
    run_inference()
