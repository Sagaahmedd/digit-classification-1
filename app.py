from tensorflow import keras
from PIL import Image
import numpy as np
import gradio as gr
import warnings
warnings.filterwarnings('ignore')

model = keras.models.load_model("model.keras")

def predict(sketchpad_input):
    if isinstance(sketchpad_input,dict):
        img=sketchpad_input["composite"]
    else:
        img=sketchpad_input

    if isinstance(img,np.ndarray):
        img=Image.fromarray(img)

    img=img.convert("L")
    img=img.resize((28,28))

    img_array=np.array(img)
    img_array=img_array / 255.0
    img_array=img_array.reshape(1,784)
    img_array = 1.0 - img_array

    probabilities = model.predict(img_array)[0]
    output = ""
    for i, p in enumerate(probabilities):
        output += f"{i}: {p*100:.2f}% \n"
    output += f"\nIt is (most likely): {np.argmax(probabilities)}"
    return output

ui=gr.Interface(fn=predict,inputs=gr.Sketchpad(),outputs="text")

ui.launch()


