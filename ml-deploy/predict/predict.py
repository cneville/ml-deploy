import pickle

filename = 'kmeans_model.pkl'
file_path = r'../models/{}'.format(filename)
km_loaded_pickle = pickle.load(open(file_path, 'rb'))
result = km_loaded_pickle.labels_
print(result)
