import pickle
import sys
import pandas as pd

with open('Gradient_Boost.pkl','rb') as file:
    loaded_model=pickle.load(file)

with open("Label_Encoder.pkl",'rb') as file:
    loaded_lbl = pickle.load(file)


#Load Test Data
test_df = pd.read_csv(sys.argv[1])

#Preprocessing
test_data = test_df.copy()
test_data = test_data.drop(columns = ['uuid','datasetId'])
test_data['condition'] =loaded_lbl.transform(test_data['condition'])

#predictions
predictions = loaded_model.predict(test_data)

#Display final result
final_ans = pd.DataFrame(dict({'uuid':test_df['uuid'].values, 'HR':predictions}))

final_ans.to_csv('results.csv',index=False)
