import streamlit as st
from clientside.client import post_request_and_prepare_prediction


SCHEMA = [
    'Alcohol', 'Malic', 'Ash',
    'Alcalinity', 'Magnesium', 'Phenols', 'Flavanoids',
    'Nonflavanoids', 'Proanthocyanins', 'Color', 'Hue', 'Dilution',
    'Proline'
]

API_URL = "http://127.0.0.1:5000/predict/"


def split_data(input_data: str) -> list:
    _data = input_data.strip()
    _data = _data.split(",")
    _data = [float(item) for item in _data]
    return _data


def input_valid(input_data: list) -> bool:
    if len(input_data) != 14:
        return False
    return True


inputs = st.text_area('Wine Data', "")

if len(inputs) > 0:
    data = split_data(inputs)
    if input_valid(data):
        request_data = dict(zip(SCHEMA, data))
        result = post_request_and_prepare_prediction(url=API_URL, payload=request_data)
        st.json({"class": result})
