#!/bin/bash

# Define the required Python packages and their versions
packages=("matplotlib==3.6.0" "pandas==1.5.2" "plotly==5.15.0" "scikit-learn==1.2.2" "seaborn==0.13.1" "numpy==1.23.3")

# Install the packages using pip
pip install "${packages[@]}"
