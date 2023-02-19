from azureml.core import Run
import pandas as pd

import os

# Get the experimental context
run = Run.get_context()

df = pd.read_csv('diabetes.csv')

# Log the number of rows
rowCount = (len(df))
run.log('observations', rowCount)
print('Analyzing {} rows of data'.format(rowCount))

# Log the summary statistics for numeric columns
medicalColumns = ['Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure',
       'TricepsThickness', 'SerumInsulin', 'BMI', 'Age' ]

summaryStatistics = df[medicalColumns].describe().to_dict()
for col in summaryStatistics:
    keys = list(summaryStatistics[col].keys())
    values = list(summaryStatistics[col].values())
    for idx in range(len(keys)):
        run.log_row(col, stat=keys[idx], values=values[idx])

# Log distinct pregnancy counts
pregnancies = df.Pregnancies.unique()
run.log_list('Pregnancy Categories', pregnancies)

# Count and Log Diabetic Lables
diabeticCounts = df['Diabetic'].value_counts()
print(diabeticCounts)
for k, v in diabeticCounts.items():
    run.log('Label:' + str(k), v)

# IF RUNNING THIS AS A STANDALONE IN-LINE SCRIPT, UNCOMMENT THIS TO GENERATE VISUALISATIONS

# # Plot and log the distribution of diabetic vs non-diabetic
# import matplotlib.pyplot as plt
# diabeticCounts = df['Diabetic'].value_counts()
# fig = plt.figure(figsize=(6,6))
# ax = fig.gca()    
# diabeticCounts.plot.bar(ax = ax) 
# ax.set_title('Patients with Diabetes') 
# ax.set_xlabel('Diagnosis') 
# ax.set_ylabel('Patients')
# plt.show()
# run.log_image(name='label distribution', plot=fig)

# Save a sample of the data
os.makedirs('outputs', exist_ok=True)
df.sample(100).to_csv("outputs/diabetesSample.csv", index=False, header=True)

run.complete()
