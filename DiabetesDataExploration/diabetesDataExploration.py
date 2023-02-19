from azure.core import Run
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the experimental context
run = Run.get_context()

df = pd.read_csv('datasets/diabetes.csv')

# Log the number of rows
rowCount = len(df)
run.log('no_observations', rowCount)

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
labels = df['Diabetic'].value_counts()
for key, value in labels:
    run.log('Label:' + str(key), value)

# Plot and log the distribution of diabetic vs non-diabetic
diabeticCounts = df['Diabetic'].value_counts()
fig = plt.figure(figsize=(6,6))
ax = fig.gca()    
diabeticCounts.plot.bar(ax = ax) 
ax.set_title('Patients with Diabetes') 
ax.set_xlabel('Diagnosis') 
ax.set_ylabel('Patients')
plt.show()
run.log_image(name='label distribution', plot=fig)

# Save a sample of the data
df.sample(100).to_csv('diabetesSample.csv', index=False, header=True)
run.upload_file(name='outputs/diabetesSample.csv', path_or_stream='./diabetesSample.csv')

run.complete()
