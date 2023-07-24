# Tumor Classification using Machine Learning

This project is a tumor classification application using machine learning techniques. It aims to predict whether a tumor is positive or negative based on input images.

## Overview

The application uses the following steps to perform tumor classification:

1. Data Preparation:
   - The application reads images from two directories: "tumor/training/no" and "tumor/training/yes".
   - The images are resized to a standard size of 200x200 pixels.
   - The pixel values of the images are normalized to the range [0, 1] to facilitate model training.

2. Feature Extraction:
   - The images are converted into one-dimensional arrays of pixel values.
   - The feature extraction step helps in transforming images into a format suitable for model training.

3. Model Training:
   - The application uses the support vector machine (SVM) algorithm for binary classification.
   - The SVM model is trained using the extracted features and corresponding target labels (positive or negative tumor).

4. Model Evaluation:
   - The trained SVM model is evaluated using a separate test dataset to measure its accuracy in tumor classification.

5. Visualization:
   - The application includes visualizations of misclassified tumor images to gain insights into model performance.

## How to Use

1. Clone the repository and navigate to the project directory.

2. Place the tumor images in the appropriate directories: "tumor/training/no" for negative tumor images and "tumor/training/yes" for positive tumor images.

3. Run the application using Python to perform tumor classification and visualization.

4. The application will display the total number of misclassified tumor images along with the corresponding predicted and actual tumor labels.

5. Additionally, the application will generate plots of tumor images, indicating whether the tumor is positive or negative based on the SVM model's predictions.

## Note

- The application is for educational and demonstration purposes only and may not provide accurate results in all scenarios.

- It is advisable to use a larger and more diverse dataset for more reliable tumor classification.

- If you encounter any issues or have suggestions for improvement, feel free to create an issue or submit a pull request in the GitHub repository.
