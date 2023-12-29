# Drug Name Detection using Detectron2

## Project Information

- Project Name: Drug Name Detection using Detectron2
- Group ID: 3
- Domain: Data Science
- Code by Ansh Shankar, Preet Jain

## Detectron2 Model Details

- Model Used: "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
- Average Precision at 50% (ap50): 98.209%

## Screenshots

Below are screenshots of the Flask API, Flask UI, and Streamlit UI.

[Flask API Screenshot](Flask/API.jpg)
[Flask UI Screenshot](Flask/UI.png)
[Streamlit UI Screenshot](Streamlit/UI.jpg)

## Basic Overview

### Training Detectron2 Model

1. Mount Google Drive.
2. Clone the Detectron2 repository.
3. Install required dependencies.
4. Load necessary libraries and print versions.
5. Define file paths for images and labels.
6. Define a function to convert COCO-style dataset annotations to Detectron2 format.
7. Register the dataset and visualize a few samples.
8. Configure and train a Detectron2 model.
9. Evaluate the model on the validation set.
10. Save the trained model and configuration.

### Flask App with ngrok

1. Mount Google Drive.
2. Install Flask, Flask-ngrok, pyngrok, and Streamlit.
3. Load Detectron2 libraries and set authentication token for ngrok.
4. Load the saved configuration and model weights.
5. Create a Flask app and set up ngrok.
6. Define a route for handling image uploads, making predictions, and rendering results.
7. Start the Flask app.

### Streamlit App

1. Import necessary libraries.
2. Connect to ngrok and print the public URL.
3. Run the Streamlit app (`app.py`).

## Project Structure

- `/data`: Contains dataset and annotations.
- `/models`: Stores trained model and configuration files.
- `/screenshots`: Screenshots of the Flask API, Flask UI, and Streamlit UI.
- `train.py`: Script for training Detectron2 model.
- `app.py`: Flask application script.
- `streamlit_app.py`: Streamlit application script.

## How to Run

1. Set up the environment by following the installation steps in the respective scripts (`train.py`, `app.py`, `streamlit_app.py`).
2. Train the Detectron2 model using `train.py`.
3. Run the Flask app using `app.py`.
4. Run the Streamlit app using `streamlit_app.py`.

Feel free to explore the code and customize it according to your needs!

For any issues or questions, please create an issue on the GitHub repository.
