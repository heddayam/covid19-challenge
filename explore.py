import numpy as np
import json
import os

file_path_base = '/home/tm/Documents/heddayam/covid19/CORD-19-research-challenge/'
file_path_1 = file_path_base + 'biorxiv_medrxiv/biorxiv_medrxiv/'
file_path_2 = file_path_base + 'comm_use_subset/comm_use_subset/'
file_path_3 = file_path_base + 'noncomm_use_subset/noncomm_use_subset/'
file_path_4 = file_path_base + 'custom_license/custom_license/'

data_directories = [file_path_1, file_path_2, file_path_3, file_path_4]

for k, d in enumerate(data_directories):
    if k == 0:
        for i, filename in enumerate(os.listdir(d)):
            if i == 0:
                with open(d + filename, 'rb') as data_file:
                    json_data = json.load(data_file)
                    #print(json_data['body_text'][0].keys())
                    print(json_data.keys())
        #for p in data_file:

