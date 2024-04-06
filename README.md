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
