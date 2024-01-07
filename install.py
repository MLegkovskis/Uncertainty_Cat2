import zipfile
import os
import sys
import subprocess

# Function to extract the zip file containing the packages
def extract_zip_file(zip_path, extract_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

# Function to install a package using pip with --no-index flag
def install_package(package_path, package_folder):
    subprocess.check_call([sys.executable, "-m", "pip", "install", 
                           "--no-index", "--find-links=" + package_folder, package_path])

# Define the paths
zip_path = '/mnt/data/python_packages.zip'
extract_folder = '/mnt/data/python_packages'

# Extract the zip file
extract_zip_file(zip_path, extract_folder)

# List the extracted files and sort them in the installation order
extracted_files = os.listdir(extract_folder)
extracted_files.sort()

# Install each package in the specified order
for package in extracted_files:
    package_path = os.path.join(extract_folder, package)
    install_package(package_path, extract_folder)

print("Installation of Python packages completed.")
