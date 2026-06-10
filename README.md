# Stroke Prediction Project

This repository contains a stroke prediction project built with Streamlit, Python, and machine learning.

## Contents

- `stroke_app.py` - Streamlit application for predicting stroke risk.
- `pipeline.pkl` - Saved machine learning pipeline used by the app.
- `healthcare-dataset-stroke-data.csv` - Stroke dataset used for training or analysis.
- `Stroke .ipynb` - Jupyter notebook for exploration, preprocessing, or model development.
- `BMI.png`, `Glucose.png` - Supporting images likely generated during analysis.

## Description

The app allows users to input personal and health-related data including gender, age, hypertension, heart disease, marital status, work type, residence type, smoking status, BMI, and average glucose level. It converts BMI and glucose values into categorical features and predicts the probability of stroke using a trained machine learning pipeline.

## Requirements

- Python 3.8+
- `streamlit`
- `pandas`
- `joblib`

You may also need any dependencies required by the saved `pipeline.pkl` model.

## Run the App

From the project directory, run:

```bash
streamlit run stroke_app.py
```

Then open the provided local URL in your browser.

## Notes

- Ensure `pipeline.pkl` is present in the same directory as `stroke_app.py`.
- The dataset `healthcare-dataset-stroke-data.csv` can be used for additional analysis or retraining.
- If the app reports missing dependencies, install them with:

```bash
pip install streamlit pandas joblib
```
=======
# Stroke Prediction Project

This repository contains a stroke prediction project built with Streamlit, Python, and machine learning.

## Contents

- `stroke_app.py` - Streamlit application for predicting stroke risk.
- `pipeline.pkl` - Saved machine learning pipeline used by the app.
- `healthcare-dataset-stroke-data.csv` - Stroke dataset used for training or analysis.
- `Stroke .ipynb` - Jupyter notebook for exploration, preprocessing, or model development.
- `BMI.png`, `Glucose.png` - Supporting images likely generated during analysis.

## Description

The app allows users to input personal and health-related data including gender, age, hypertension, heart disease, marital status, work type, residence type, smoking status, BMI, and average glucose level. It converts BMI and glucose values into categorical features and predicts the probability of stroke using a trained machine learning pipeline.

## Requirements

- Python 3.8+
- `streamlit`
- `pandas`
- `joblib`

You may also need any dependencies required by the saved `pipeline.pkl` model.

## Run the App

From the project directory, run:

```bash
streamlit run stroke_app.py
```

Then open the provided local URL in your browser.

## Notes

- Ensure `pipeline.pkl` is present in the same directory as `stroke_app.py`.
- The dataset `healthcare-dataset-stroke-data.csv` can be used for additional analysis or retraining.
- If the app reports missing dependencies, install them with:

```bash
pip install streamlit pandas joblib
```
>>>>>>> 9ecc921ae8283bda245d97abefc7983498b55136
