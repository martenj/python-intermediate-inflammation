"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views
import json


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    
 #   data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
 #   if len(data_file_paths) == 0:
 #       raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
 #   data = map(models.load_csv, data_file_paths)
    
    data = data_source.load_inflammation_data()

    #means_by_day = map(models.daily_mean, data)
    #means_by_day_matrix = np.stack(list(means_by_day))

#    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    daily_standard_deviation = compute_standard_deviation_by_day(data)
    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    #views.visualize(graph_data)
    #print(graph_data)
    return compute_standard_deviation_by_day(data)
    #return daily_standard_deviation

def compute_standard_deviation_by_day(data):
    #if not data:
    #    raise ValueError("No data provided for standard deviation calculation.")
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation

class CSVDataSource:
    """Class to handle loading CSV data from a specified directory."""

    def __init__(self, data_path='data'):
        self.data_path = data_path

    def load_inflammation_data(self):
        """Load inflammation data from CSV files in the 'data' directory."""
        
        if not os.path.exists(self.data_path):
            raise ValueError(f"Data directory {self.data_path} does not exist.")
        
        data_file_paths = glob.glob(os.path.join(self.data_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_path}")
        
        #return [models.load_csv(file_path) for file_path in data_file_paths]
        return list(map(models.load_csv, data_file_paths))


class JSONDataSource:
    """Class to handle loading JSON data from a specified directory."""
    
    def __init__(self, data_path='data'):
        self.data_path = data_path

    def load_inflammation_data(self):

        if not os.path.exists(self.data_path):
            raise ValueError(f"Data directory {self.data_path} does not exist.")

        data_file_paths = glob.glob(os.path.join(self.data_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_path}")
        
        #return [models.load_csv(file_path) for file_path in data_file_paths]
        return list(map(models.load_json, data_file_paths))
     