## Quick Links
- [HuggingFace Space](https://huggingface.co/spaces/Asser-IO/digit-classifier)
- [Presentation Slides](https://www.canva.com/design/DAGvV3wce6Q/lKE85t2fpSIc153Ky4FxXA/edit?utm_content=DAGvV3wce6Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## About the project 
- This project uses a neural network model (mlp) to recognize handwritten digits using the MNIST dataset and gradio interface.

- It includes data preprocessing, model training, and targeted data augmentation to improve performance on frequently misclassified digits.

- The final model delivers high accuracy and is optimized for real-world digit recognition, with an interactive Gradio app providing a user-friendly interface.

 ## Built With
- Python 3.13  
- Pandas  
- NumPy  
- tensorflow
- Gradio

## Prerequisites 
Ensure you have:

- python 3.13 

## Installation
### Installation
1. Clone the repo:
   ```sh
   git clone https://github.com/Asir-IO/digit-classification.git
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   venv\\Scripts\\activate  # Windows
   pip install -r requirements.txt
   ```
3. Launch the Gradio app:
   ```sh
   py app.py
   ```

   ## Roadmap
- [x] Data preprocessing
- [x] Data augmentation for training
- [x] Trained an MLP model on the MNIST dataset using TensorFlow/Keras.
- [x] Gradio app construction
- [x] Basic error handling
- [x] Deployment on Hugging face
- [ ] Improve the UI layout
- [ ] Train with More Complex Digits
- [ ] Multi-digit Input
      
