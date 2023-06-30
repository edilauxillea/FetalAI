# FetalAI: USING ML TO PREDICT AND MONITOR FETAL HEALTH 

This project focuses on developing a fetal health monitoring system using machine learning algorithms. The system aims to analyze decelerations and other relevant parameters to assess the health condition of the fetus. This README file provides an overview of the project and instructions on how to use and contribute to it.

# Table of Contents
- [Introduction](https://github.com/edilauxillea/FetalAI/blob/main/README.md#introduction)
- [Features](https://github.com/edilauxillea/FetalAI/blob/main/README.md#features)
- [Installation](https://github.com/edilauxillea/FetalAI/blob/main/README.md#installation)
- [Usage](https://github.com/edilauxillea/FetalAI/blob/main/README.md#usage)
- [Contributing](https://github.com/edilauxillea/FetalAI/blob/main/README.md#contributing)

# Introduction
Fetal health monitoring is a critical aspect of prenatal care. Through the analysis of relevant parameters, such as maternal age, blood pressure, heart rate, and uterine contractions, healthcare professionals can evaluate the well-being of the fetus and identify potential complications. This project focuses on developing a fetal health monitoring system using machine learning algorithms. The system aims to analyze a dataset, consisting of various parameters related to fetal health and maternal well-being. By leveraging machine learning algorithms, the system can assess the health condition of the fetus based on these input parameters.

The main goal of this project is to develop a reliable and efficient system that can classify fetal health conditions based on the input data from the Kaggle dataset. By training and evaluating machine learning models on this dataset, the system can make predictions about the fetal health status, providing valuable insights to healthcare providers. This project utilizes machine learning algorithms to automate the analysis process and provide accurate predictions regarding the fetal health status.


# Features
The fetal health monitoring system offers the following features:

- Data Preprocessing: The system includes data preprocessing modules to handle data cleaning, feature selection, and normalization tasks. It utilizes Ridge regression as a feature selection technique to identify the most relevant features for the classification task. Additionally, the system applies Min-Max scaling to normalize the input data, ensuring that all features are on a similar scale and preventing any particular feature from dominating the model training process.

- Exploratory Data Analysis (EDA): Before training the machine learning models, the system provides exploratory data analysis capabilities. EDA helps understand the dataset's characteristics, identify patterns, outliers, and relationships between variables. It includes visualizations, statistical summaries, and data profiling to gain insights into the data and guide the subsequent preprocessing and modeling steps.

- Oversampling with SMOTE: To address class imbalance in the dataset, the system incorporates Synthetic Minority Over-sampling Technique (SMOTE). SMOTE generates synthetic samples for the minority class, thereby balancing the dataset and improving the performance of the classification models.

- Machine Learning Algorithms: The system supports various machine learning algorithms, including Random Forest. Random Forest is employed for the classification task as it excels in handling complex relationships between features and provides robust predictions. The system trains Random Forest models on the preprocessed and balanced data to classify fetal health conditions effectively.

- Model Evaluation: The system includes evaluation modules to assess the performance of the trained models. Evaluation metrics such as accuracy, precision, recall, F1 score and confusion matrix are calculated to measure the model's effectiveness in predicting fetal health conditions.

- Graphical User Interface (GUI): A user-friendly GUI is provided to interact with the system. The GUI allows users to load data, select and train machine learning models, and visualize the results of predictions and model performance.

By incorporating Min-Max scaling for data normalization, conducting Exploratory Data Analysis, employing oversampling techniques such as SMOTE, and utilizing Random Forest for classification, the fetal health monitoring system achieves accurate predictions and improves the overall performance of the classification models.

# Installation
To install and set up the fetal health monitoring system, follow these steps:

1. Clone the repository:
```
git clone https://github.com/edilauxillea/FetalAI.git
```

2. Navigate to the project directory:
```
cd fetalai
```
3. Set up a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```

#Usage
To use the fetal health monitoring system, follow these steps:

1. Ensure that you have activated the virtual environment (if created) and are in the project directory.
2. Run the GUI application:
```
python gui.py
```
3. The GUI window will appear, providing options to load data, select and train machine learning models, and evaluate their performance.
4. Follow the instructions provided in the GUI to load your dataset, preprocess the data, select a machine learning algorithm, train the model, and evaluate its performance.
5. Explore the visualization features of the GUI to analyze the results of predictions and model performance.
6. Customize and extend the system according to your specific requirements by modifying the existing codebase.

# Contribution
Contributions to the fetal health monitoring system are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your modifications and enhancements to the codebase.
4. Ensure that the project's tests and linting checks pass successfully.
5. Submit a pull request, providing a detailed description of your changes and their purpose.










