import glob
import pandas as pd
list_csv = glob.glob('*.csv')
list_csv:['source1.csv','source2.csv','source3.csv']
list_json = glob.glob('*.json')
list_json:['source1.json','source2.json','source3.json']

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines = True)
    return dataframe
