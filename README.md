# DSLR

## Description
A linear classification model: the logistic regression.

Developed as an academic project at 42 Lyon.

## Installation
To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
Here are some usage examples:

```bash
python3 describe.py dataset.csv
python3 histogram.py  # Histogram
python3 scatter_plot.py  # Scatter plot
python3 pair_plot.py  # Pair plot (Histograms on the diagonal)

python3 logreg_train.py dataset_train.csv  # Train
# Saves the weights (weights.csv)

python3 logreg_predict.py dataset_test.csv weights.csv  # Prediction
# Generates a prediction CSV (houses.csv)

python3 evaluate.py  # Requested accuracy of 98%
```

## Features

```bash
python3 separate_train_dataset dataset_train.csv
# Generates 2 datasets (80/20)
```

## Contact
tdutel@student.42lyon.fr

qpupier@student.42lyon.fr
