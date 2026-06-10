"""Streamlit app for Stroke risk prediction.

This module provides a small Streamlit UI for collecting user inputs
and returning a probability from a pre-trained pipeline saved as
``pipeline.pkl`` in the same folder.
"""

from pathlib import Path
import logging
from typing import Any

import joblib
import pandas as pd
import streamlit as st

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="Stroke AI App", page_icon="✨")


def bmi_to_cat(value: float) -> str:
    """Convert BMI to categorical bucket.

    Buckets follow common clinical cutoffs.
    """
    if value < 18.5:
        return "UnderWeight"
    if value < 25:
        return "Normal"
    if value < 30:
        return "OverWeight"
    if value < 35:
        return "Obese"
    return "ExtremelyObese"


def glucose_to_cat(value: float) -> str:
    """Convert average glucose level to a categorical bucket."""
    if value < 60:
        return "VeryLow"
    if value < 80:
        return "Low"
    if value < 120:
        return "Normal"
    if value < 180:
        return "High"
    return "VeryHigh"


def load_pipeline(path: Path) -> Any:
    """Load a serialized sklearn pipeline from `path`.

    Returns the loaded object or None on failure.
    """
    try:
        logger.info("Loading model from %s", path)
        return joblib.load(path)
    except Exception as exc:  # pragma: no cover - surface-level app handling
        logger.exception("Failed to load pipeline: %s", exc)
        return None


def format_prob(p: float) -> str:
    return f"{p:.1%}"  # e.g. 12.3%


def main() -> None:
    """Render the Streamlit UI and perform prediction on submit."""
    st.title("Stroke Risk Predictor")

    model_path = Path(__file__).parent / "pipeline.pkl"
    pipeline = load_pipeline(model_path)
    if pipeline is None:
        st.error("Model not available. Ensure pipeline.pkl is present.")
        return

    with st.form(key="input_form"):
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            hypertension = st.selectbox("Hypertension", [0, 1])
            heart_disease = st.selectbox("Heart disease", [0, 1])
            ever_married = st.selectbox("Ever married", ["Yes", "No"])
            work_type = st.selectbox(
                "Work type",
                ["Private", "Self-employed", "Govt_job", "children", "Never_worked"],
            )

        with col2:
            residence_type = st.selectbox("Residence type", ["Urban", "Rural"])
            smoking_status = st.selectbox(
                "Smoking status", ["never smoked", "formerly smoked", "smokes"]
            )

            age = st.number_input("Age", min_value=0, max_value=120, value=40)
            avg_glucose_level = st.number_input(
                "Average glucose level", min_value=0.0, max_value=300.0, value=100.0
            )
            bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)

        submit = st.form_submit_button("Submit")

    if not submit:
        return

    user_input = pd.DataFrame(
        {
            "gender": gender,
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "ever_married": ever_married,
            "work_type": work_type,
            "Residence_type": residence_type,
            "smoking_status": smoking_status,
            "bmi_cat": bmi_to_cat(bmi),
            "glucose_cat": glucose_to_cat(avg_glucose_level),
        },
        index=[0],
    )

    try:
        proba = float(pipeline.predict_proba(user_input)[0, 1])
    except Exception as exc:  # pragma: no cover - runtime safety
        logger.exception("Prediction failed: %s", exc)
        st.error("Prediction failed. Check model and input schema.")
        return

    if proba < 0.5:
        st.success(f"Low stroke probability'You are Okay': {format_prob(proba)}")
    else:
        st.error(f"Elevated stroke probability'You should consult a doctor': {format_prob(proba)}")


if __name__ == "__main__":
    main()

