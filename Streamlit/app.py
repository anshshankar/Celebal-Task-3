import subprocess
import sys
import os
import distutils.core
subprocess.run(["git", "clone", "https://github.com/facebookresearch/detectron2"])
dist = distutils.core.run_setup("./detectron2/setup.py")
subprocess.run(["python", "-m", "pip", "install"] + dist.install_requires)
sys.path.insert(0, os.path.abspath('./detectron2'))
import cv2
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor
import streamlit as st
import numpy as np
from detectron2.config import get_cfg
import base64

# Load the saved configuration
cfg = get_cfg()
cfg.SOLVER.OPTIMIZER = "ADAM"
cfg.merge_from_file("/content/drive/MyDrive/Dataset/config.yaml")

# Set the path to the saved model weights
cfg.MODEL.WEIGHTS = "/content/drive/MyDrive/Dataset/model_final.pth"
predictor = DefaultPredictor(cfg)


def process_image(file):
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    outputs = predictor(image)

    # Visualize the predictions
    v = Visualizer(image[:, :, ::-1],
                   metadata=MetadataCatalog.get("coco_dataset"),
                   scale=0.7)
    annotated_image = v.draw_instance_predictions(outputs["instances"].to("cpu")).get_image()

    return annotated_image

def main():
    st.title("Object Detection App ")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        annotated_image = process_image(uploaded_file)

        # Display the annotated image
        st.image(annotated_image, use_column_width=True, channels="BGR")
        
if __name__ == "__main__":
    main()

