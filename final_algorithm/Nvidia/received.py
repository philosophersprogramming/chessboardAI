import pickle
with open('initial_array.pkl', 'rb') as initial_file:
    initial_array = pickle.load(initial_file)
for row in initial_array:
    print(row)
