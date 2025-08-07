import gradio as gr
import numpy as np
import tensorflow as tf
from PIL import Image

model = tf.keras.models.load_model("model.keras")
with open("styling.css") as f:
    css = f.read()

def predict(sketchpad_input):
    if isinstance(sketchpad_input, dict):
        img = sketchpad_input["composite"]
    else:
        img = sketchpad_input
    if isinstance(img, np.ndarray):
        img = Image.fromarray(img)

    img = img.convert("L").resize((28, 28))

    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1, 784)
    img_array = 1.0 - img_array

    probabilities = model.predict(img_array)[0]
    probs = {str(i): float(probabilities[i]) for i in range(10)}
    return probs

def clear():
    return None, {}

with gr.Blocks(css=css) as demo:
    gr.Markdown("## What digit is it?", elem_classes=["title"])
    with gr.Row():
        with gr.Column():
            sketchpad = gr.Sketchpad()
            predict_btn = gr.Button("Predict")
            clear_btn = gr.Button("Clear")
        
        with gr.Column():
            label_output = gr.Label(num_top_classes=10, label="Prediction")
    predict_btn.click(fn=predict, inputs=sketchpad, outputs=label_output)
    clear_btn.click(fn=lambda: None, inputs=None, outputs=[sketchpad, label_output])

demo.launch()

