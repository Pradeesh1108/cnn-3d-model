import streamlit as st
from model.cnn_model import build_model
from model.utils import train_model, predict
from data.load_data import load_data
from visualization.cnn_3d_plot import plot_3d_activations
from visualization.threejs_component import render_threejs

st.set_page_config(layout="wide")
st.title("🧠 CNN Visualizer with 3D Output")

uploaded = st.file_uploader("Upload your image (28x28 PNG)", type=['png'])
run_training = st.button("Train & Visualize CNN")

if run_training:
    st.subheader("Loading and Preprocessing Dataset...")
    x_train, x_test, y_train, y_test = load_data()

    st.subheader("Building and Training CNN Model...")
    model, activations = train_model(build_model(), x_train, y_train)

    st.subheader("Predicting and Visualizing in 3D")
    pred, probas = predict(model, x_test[0])
    st.write(f"✅ Predicted: **{pred}**")

    st.plotly_chart(plot_3d_activations(activations), use_container_width=True)
    render_threejs(probas)