# abtest-mlops

# SmartAd_abtest

**Table of content**

- [Overview](##abstract)
- [Requirements](#setup)
- [Install](#install)
- [Features](#features)
  - [Data](#data.csv)
- [Notebooks](#notebooks)
  - [Classic A/B hypothesis testing](notebooks/ClassicABTest.ipynb)
  - [Sequential A/B hypothesis testing](notebooks/Sequential.ipynb)
- [Scripts](#scripts)
  - [Utility helper functions](scripts/helper.py)
  - [Plotting graph](scripts/plots.py)

## Overview

SmartAd is an advertiser agency. It designs intuitive touch-enabled advertising. It provides brands with an automated advertising experience via machine learning and creative excellence. SmartAd has implemented a new advertising campaign and collected BIO brand impact optimizer data from 3-10 July 2020 to determine the impact of the creative Ad they design.

The objective is to design a reliable hypothesis testing algorithm for the BIO service and to determine whether a recent advertising campaign resulted in a significant lift in brand awareness.

This repo demonstrate how to apply classic A/B testing and Sequential A/B testing in order to determina if a recent campaign resulted in a significant lift in brand awareness

## Requirements

Python 3.5 and above, Pip and MYSQL

## Install

```
git clone https://github.com/daniEL2371/smartAd_abtest.git
cd smartAd_abtest
pip install -r requirements.txt
```

## Features

### Data

The data collected was collected from a BIO questioner. There is a data.csv file in the Data Folder

## Notebooks

### Classic A/B hypothesis testing

- Classic A/B hypothesis testing is implemented inside notebooks/ClassicABTest.ipynb

### Sequential A/B hypothesis testing

- Sequential A/B hypothesis testing is implemented inside notebooks/Sequential.ipynb

## Scripts

- Utility helper functions is implemented in helper.py module
- Plotting graphs like scatter plot, histogram, distribution graph, heat map, bar plot, and count plot is is implemented in scripts/plots.py module
