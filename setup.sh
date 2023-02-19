#! /usr/bin/sh
# This script creates a resource group, an Azure Machine Learning workspace, and a compute instance.
# The script is intended to be run from the Azure Cloud Shell.

# Create workspace
echo "Creating a Azure Resource Group:"
az group create --name "andreiroibu-azureml" --location "southuk"

echo "Creating an Azure Machine Learning workspace:"
az ml workspace create --name "andreiroibu-mlworkspace" -g "andreiroibu-azureml"

# Create compute instance
guid=$(cat /proc/sys/kernel/random/uuid)
suffix=${guid//[-]/}
suffix=${suffix:0:18}
ComputeName='andreiroibu-compute'

echo "Creating a compute instance with name: " $ComputeName
az ml compute create --name ${ComputeName} --size STANDARD_DS11_V2 --type ComputeInstance -w andreiroibu-mlworkspace -g andreiroibu-azureml
