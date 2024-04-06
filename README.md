# MRI Scan Prediction Project

This project is designed to predict the presence of a tumor in MRI scans using machine learning models. The project consists of two main components: a Streamlit web application for real-time prediction and a Jupyter Notebook for model training and evaluation.

## Streamlit Web Application

The `main.py` file contains the code for the Streamlit web application. This application allows users to upload MRI scans and select from a variety of pre-trained machine learning models to predict tumor presence. The user interface also displays model scores and provides feedback on the prediction results.

### Dependencies

- `streamlit`
- `PIL`
- `numpy`

### Usage

To run the Streamlit web application, execute the following command in your terminal:

```bash
streamlit run main.py
```

### Jupyter Notebook for Model Training

The main.ipynb Jupyter Notebook is used for model training and evaluation. It includes the following steps:

- Data Loading and Preprocessing
- Model Training
- Model Evaluation
- Saving Trained Models

# Dependencies

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `opencv-python`

# Usage

To execute the Jupyter Notebook, open it using Jupyter Notebook or Jupyter Lab and run each cell sequentially.

# Models and Model Scores
The models directory contains pre-trained machine learning models serialized using pickle. The model_table dictionary in main.py provides scores for each model based on its performance.

# Dataset
The dataset used for training and testing the models consists of MRI scan images stored in the tumor directory. The data is split into training and testing sets for model evaluation.
