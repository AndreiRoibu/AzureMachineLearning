# AzureMachineLearning
Repository containing code of a Microsoft Azure machine learning project I completed to reinforce my learning.

## Installation
To install the above code, one needs to follow these steps to create an Azure workspace and compute instance.

1. Open an [Azure portal](https://portal.azure.com/?azure-portal=true) and sign in.
2. Open the Cloud Shell
3. Select *Bash* 
4. If prompted, *Create Storage*
5. In the terminal, run in sequence the following codes:

```bash
rm -r AzureMachineLearning -f
git clone https://github.com/AndreiRoibu/AzureMachineLearning.git
cd AzureMachineLearning
./setup.sh
```

## Code Initialisation
To interact with the code and reproduce the work presented above, clone this repo by following these steps:

1. Open [Azure ML Studio](https://ml.azure.com/)
2. Enter your workspace, in this case: *Workspaces > andreiroibu-mlworkspace*
3. Start the *Compute Instance* if not already running by going to *Compute > Compute Instance*
4. Open *Applications*
5. Then, open *Terminal*
6. Enter the following code

```bash
git clone https://github.com/AndreiRoibu/AzureMachineLearning.git
```

7. Then, all codes should be available under *Notebooks*. You might need to refresh view!