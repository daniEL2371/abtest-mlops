# abtest-mlops

**Table of content**

- [Overview](##abstract)
- [Requirements](#setup)
- [Install](#install)
- [Hyperparameter Tuning]()
- [Model Tracking]()

- [Features](#features)
  - [Data](#data.csv)
- [Notebooks](#notebooks)

  - [Classic A/B hypothesis testing](notebooks/ClassicABTest.ipynb)
  - [Sequential A/B hypothesis testing](notebooks/Sequential.ipynb)
  - [Machine Learning Approach A/B testing](notebooks/ML_AbTest.ipynb)

- [Models](#Models)
- [Scripts](#scripts)
  - [Utility helper functions](scripts/helper.py)
  - [Logger](scripts/app_logger.py)
  - [Plotting graph](scripts/plots.py)
  - [Decision Tree Model](scripts/decisionTreesModel.py)
  - [Logistic Regression Model](scripts/logesticRegressionModel.py)
  - [Gradient Boosting Model](scripts/xGBClassifierModel.py)
  - [Decision Tree Model hyperparameter tuning](scripts/dt_tune_train.py)
  - [Logistic Regression Model hyperparameter tuning](scripts/logesticRegressionModel.py)
  - [Gradient Boosting Model hyperparameter tuning](scripts/xbg_tune_train.py)

## Overview

SmartAd is an advertiser agency. It designs intuitive touch-enabled advertising. It provides brands with an automated advertising experience via machine learning and creative excellence. SmartAd has implemented a new advertising campaign and collected BIO brand impact optimizer data from 3-10 July 2020 to determine the impact of the creative Ad they design.

The objective is to design a reliable hypothesis testing algorithm for the BIO service and to determine whether a recent advertising campaign resulted in a significant lift in brand awareness.

This repo demonstrate how to apply classic A/B testing, Sequential A/B testing and Machine learning Approach to A/B testing in order to determine if a recent campaign resulted in a significant lift in brand awareness

## Requirements

Python 3.5 and above, Pip and MYSQL

## Install

```
git clone https://github.com/daniEL2371/abtest-mlops
cd abtest-mlops
pip install -r requirements.txt
```

## Hyperparameter tuning

```
cd scripts
python dt_tune_train.py
python lr_tune_train.py
python xgb_tune_train.py
```

## Model tracking

```
cd notebooks
mlflow ui
```

## Features

### Data

- The data collected was collected from a BIO questioner, which asks users if they are aware of the brand called lux
- there are four versions of data. data versioning is implmented using dvc.

## Notebooks

### Classic A/B hypothesis testing

- Classic A/B hypothesis testing is implemented inside notebooks/ClassicABTest.ipynb

### Sequential A/B hypothesis testing

- Sequential A/B hypothesis testing is implemented inside notebooks/Sequential.ipynb

### ML AB Testing

- A machine learning approach to implement A/B testing by calculating feature importance of variables is implemented inside notbooks/ML_AbTest.ipynb
- The notebook demonstrates how to use Logistic Regression, Decision Tree and Gradient Boosting Models to calculate feature importance.
- we used two kinds of data versions for training our models. One version contains a column called platform_os and the othe data version contains a column called browser. this is donr in order to determine the effects of each column on the models.
- Then the resulting 6 models are stored in the folder called models.
- The note books also imports hyperparameter tuning scripts from the scripts folder.

## Models

All models that are trained are saved inside models folder

## Scripts

- Utility helper functions is implemented in helper.py module
- Logger class for the project is implemented in app_logger.py module
- Plotting graphs like scatter plot, histogram, distribution graph, heat map, bar plot, and count plot is is implemented in scripts/plots.py module
- A custome DecisionTree Model that extends sklearn's DecisionTree Model for A/B testing is implemeted in decisionTreesModel.py module
- A custome LogisticRegression that extends sklearn's LogisticRegression Model for A/B testing is implemeted inside logesticRegressionModel.py
- A custome xGBClassifierModel that extends sklearn's GradientBoostingClassifier Model for A/B testing is implemeted inside xGBClassifierModel.py
- xgb_tune_train.py, lr_tune_train.py and dt_tune_train.py are a hyper parameter tuning modules for xGBClassifier Model, logisticRegression Model and DecisionTree Model respectively
