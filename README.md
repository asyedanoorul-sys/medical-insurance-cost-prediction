# Medical Insurance Cost Prediction

## Project Overview

This project predicts medical insurance charges using Machine Learning.

The project uses Multiple Linear Regression to estimate insurance costs based on customer information such as age, BMI, gender, smoking status, number of children, and region.

## Problem Statement

Medical insurance costs can vary depending on several personal and demographic factors.

The objective of this project is to build a machine learning model that predicts estimated medical insurance charges based on these factors.

## Machine Learning Type

Regression

## Dataset

The project uses the Medical Cost Personal Dataset.

The dataset contains information about:

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region
- Medical insurance charges

### Target Variable

`charges`

### Input Features

- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Google Colab
- GitHub

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked for missing values.
3. Checked for duplicate records.
4. Removed duplicate records where applicable.
5. Converted categorical variables into numerical variables using one-hot encoding.
6. Prepared the dataset for machine learning.

## Exploratory Data Analysis

The following relationships were explored:

- Age vs Insurance Charges
- BMI vs Insurance Charges
- Smoking Status vs Insurance Charges
- Number of Children vs Insurance Charges
- Correlation between features and insurance charges

## Machine Learning Model

Multiple Linear Regression was selected because the target variable, `charges`, is a continuous numerical value.

The dataset was divided into:

- 80% training data
- 20% testing data

The model was trained using the training dataset.

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

Replace the values below with your actual Phase 6 results:

| Metric | Result |
|---|---:|
| MAE | YOUR_VALUE |
| MSE | YOUR_VALUE |
| RMSE | YOUR_VALUE |
| R² Score | YOUR_VALUE |

## Prediction Application

A Streamlit application was created where users can enter:

- Age
- BMI
- Gender
- Smoking status
- Number of children
- Region

The application then predicts the estimated medical insurance cost.

## Example Prediction

The application was tested using different input combinations to verify that it produces prediction results.

## Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Prediction
   ↓
Streamlit Application
   ↓
Deployment
