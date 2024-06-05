import cv2
import numpy as np
import time

net = cv2.dnn.readNet("model.prototxt","model.onnx")
classes = []
with open("dataset.names","r") as f :
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
cv2.setNumThreads(0)
# Loading camera
cap = cv2.VideoCapture('')

font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0
while cap.isOpened():
    _, frame = cap.read()
    frame_id += 1

    height, width, channels = frame.shape
    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids[]
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)