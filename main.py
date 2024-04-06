import streamlit as st
from PIL import Image
import pickle
import numpy as np

model_table = {
    "Model": ['Decision Tree Classifier' , 'Gradient Boost Classifier' , 'KNeighbors Regressor' , 'KNeighbors Classifier' , 'Linear Discriminate Analysis(LDA)' , 'Logistic Regression', 'Linear Regression' , 'Lasso' , 'MLP Classifier' , 'Ridge', 'Random Forest Classifier' , 'SVC ' , 'XGB Classifier'],
    "Scores (R^2)": [95.705, 97.750, 92.433, 76.294, 86.503, 93.865, 73.442, 00.045, 95.501, 73.228, 97.137, 32.924, 97.546]
 }

def load_model(model_name):
    with open(model_name, 'rb') as file:
        model = pickle.load(file)
    return model


def predict(model, img):
    pil_image = Image.open(img)
    pil_image = pil_image.convert("L")
    pil_image = pil_image.resize((200, 200))
    image = np.array(pil_image)
    image1 = image.reshape(1, -1) / 255
    p = model.predict(image1)
    return p

def main():
    st.title('MRI Scan Prediction')

    st.subheader('Model Scores')
    st.table(model_table)

    model_name = st.selectbox('Select Model', [ 'Decision Tree Classifier' , 'Gradient Boost Classifier' , 'KNeighbors Regressor' , 'KNeighbors Classifier' , 'Linear Discriminate Analysis(LDA)' , 'Logistic Regression', 'Linear Regression' , 'Lasso' , 'MLP Classifier' , 'Ridge', 'Random Forest Classifier' , 'SVC ' , 'XGB Classifier'])
    
    model = None

    if model_name == 'Decision Tree Classifier':
            model = load_model('models/dtc.pkl')
    elif model_name == 'Gradient Boost Classifier':
            model = load_model('models/gbc.pkl')
    elif model_name == 'KNeighbors Regressor':
            model = load_model('models/knr.pkl')
    elif model_name == 'KNeighbors Classifier':
            model = load_model('models/knc.pkl')
    elif model_name == 'Linear Discriminate Analysis(LDA)':
            model = load_model('models/lda.pkl')
    elif model_name == 'Logistic Regression':
            model = load_model('models/lgr.pkl')
    elif model_name == 'Linear Regression':
            model = load_model('models/lr.pkl')
    elif model_name == 'Lasso':
            model = load_model('models/lso.pkl')
    elif model_name == 'MLP Classifier':
            model = load_model('models/mlpc.pkl')
    elif model_name == 'Ridge':
            model = load_model('models/rdg.pkl')
    elif model_name == 'Random Forest Classifier':
            model = load_model('models/rfc.pkl')
    elif model_name == 'SVC':
            model = load_model('models/svc.pkl')
    elif model_name == 'XGB Classifier':
            model = load_model('models/xgb.pkl')


    uploaded_file = st.file_uploader("Upload MRI scan", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded MRI scan', use_column_width=True)

        if st.button('Predict'):
            if model is not None:
                prediction = predict(model, uploaded_file)
                prediction_percent = prediction[0] * 100
                if prediction_percent < 60:
                    st.success(f'No Tumor Dectected. Prediction Percentage: {prediction_percent:.3f}%')
                else:
                    st.error(f'Tumor Detected. Prediction prediction: {prediction_percent:.3f}%')

if __name__ == '__main__':
    main()