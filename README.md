# Diabetes Prediction

## Project Description

This project aims to develop a prediction model for the likelihood of a patient having diabetes or not in Pima Indians living in the Phoenix area of Arizona, United States. In analyzing this dataset, the main goal is to study the relationship between certain risk factors and a person's likelihood of developing diabetes, as well as to develop a prediction model that can help identify patients who are at high risk of developing diabetes.

## Background of the Problem

Diabetes is one of the chronic diseases experienced by many people. Early detection of diabetes is very important to prevent more serious complications and improve the quality of life of patients. However, early detection is often difficult because the symptoms of diabetes are not always visible in the early stages. Therefore, the development of a diabetes prediction model can be an effective solution to assist doctors in conducting early detection.

## Project Output

The output of this project is the Random Forest Classifier model after hyperparameter tuning, the model produces higher accuracy values compared to other models. However, the model has difficulty in predicting class 1 (diabetic patients), with a high number of false negatives (13). This could indicate a data imbalance problem in the test data. Therefore, hospitals need to perform external validation on data that has not been seen before and update the model regularly to ensure its performance remains optimal.

## Brief Description of Data Used

The data used in this project is [Pima Indians Diabetes Database dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database). This dataset contains information about Pima Indians patients that includes attributes such as age, blood glucose level, blood pressure, skin thickness, insulin, body mass index, family history of diabetes, and diabetes test results.

## Methods Used

This project used a machine learning approach to develop a diabetes prediction model. The methods used include:

1. Data pre-processing: Cleaning the data from null values, performing feature scaling, and dividing the data into training set and test set.
2. Model building: Using machine learning algorithms such as Logistic Regression, SVM, Decision Tree Classifier, Random Forest Classifier, KNN Classifier to train the model with the training data.
3. Model evaluation: Using evaluation metrics such as accuracy, precision, recall, and F1-score to measure model performance.

## Stack Used

In this project, we used several technologies and tools as follows:
- Programming Language: Python
- Libraries and Frameworks: scikit-learn, pandas, numpy, matplotlib, seaborn, feature_engine
- Development Environment: Jupyter Notebook or Visual Studio Code

## Project Pros and Cons

The advantages of this project are:

- Helps in early detection of diabetes and provides appropriate medical action.
- Using publicly available datasets to develop prediction models.
- Using common machine learning methods that are proven to be effective in diabetes prediction.

Disadvantages of this project are:

- The accuracy of the model may be affected by the quality and amount of data available.

### [Deployment](https://huggingface.co/spaces/dayuima01/Milestone2)