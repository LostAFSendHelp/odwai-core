######## Image Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Editor: Nguyen Chuong
# Date: 1/10/19
# Description: 
# This is the object detector of the ODWai system

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

## but I changed it to make it more understandable to me.

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import mss
import pytesseract as pt

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = '../inference_graph'
IMAGE_NAME = 'test1.jpg'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'../training','labelmap.pbtxt')

# Path to image
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

# Number of classes the object detector can identify
NUM_CLASSES = 6

# Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

class Detect_img():

    def __init__(self):
        self.objects = {
            "tb": [],
            "btn": []
        }

        self.root = {"x": 0, "y": 0}

    def __check_overlap(self, info):
        boxes = self.objects["tb"] + self.objects["btn"]
        overlapped = False
        
        for box in boxes:
            if (info["x"] > box["xmin"] and info["x"] < box["xmax"]
            and info["y"] > box["ymin"] and info["y"] < box["ymax"]):
                overlapped = True
                break
        
        return overlapped

    def capture_n_detect( self, top, left, width, height, skip_check ):
        os.system('cls')
        
        # reset object collection
        self.objects = {
            "tb": [],
            "btn": []
        }

        self.root["x"] = left
        self.root["y"] = top


        # Load the Tensorflow model into memory.
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            sess = tf.Session(graph=detection_graph)

        # Define input and output tensors (i.e. data) for the object detection classifier

        # Input tensor is the image
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        # Output tensors are the detection boxes, scores, and classes
        # Each box represents a part of the image where a particular object was detected
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

        # Each score represents level of confidence for each of the objects.
        # The score is shown on the result image, together with the class label.
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

        # Number of objects detected
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        # Load image using OpenCV and
        # expand image dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value

        sct = mss.mss()
        scrn = {"top": top, "left": left, "width": width, "height": height}

        frame = cv2.cvtColor(np.array(sct.grab(scrn)), cv2.COLOR_BGRA2BGR)
        frame_expanded = np.expand_dims(frame, axis=0)

        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: frame_expanded})

        # Draw the results of the detection (aka 'visulaize the results')

        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=8,
            min_score_thresh=0.80)

        for idx, box in enumerate(boxes[0]):
            ymin = box[0] * height
            xmin = box[1] * width
            ymax = box[2] * height
            xmax = box[3] * width

            mystr = ""

            if scores[0][idx] >= .50:
                class_name = category_index[classes[0][idx]]['name']
                
                if scores[0][idx] < .80:              
                    mystr = "{} - unknown - bias: {}({})"
                else:
                    mystr = "{} - {}({})"
                    
                    if class_name in ("tb", "btn"):
                        print(class_name)
                        
                        # corner coordinates and sizes of textboxes/buttons on the screen
                        local_top = int(top + ymin)
                        local_left = int(left + xmin)
                        local_height = int(ymax - ymin)
                        local_width = int(xmax - xmin)

                        # grab screen within textboxes/buttons
                        local_scrn = {"top": local_top, "left": local_left, "width": local_width, "height": local_height}
                        local_frame = np.array(sct.grab(local_scrn), dtype=np.uint8)
                        local_frame = np.flip(local_frame[:, :, :3], 2)
                        
                        # identify texts and append to output
                        inner_text = pt.image_to_string(local_frame)
                        mystr += inner_text

                        # center coordinates for simulation
                        center_x = int(left + (xmin + xmax)/2)
                        center_y = int(top + (ymin + ymax)/2)
                        info = { 
                            "x": center_x, 
                            "y": center_y,
                            "xmin": local_left,
                            "ymin": local_top,
                            "xmax": int(xmax + left),
                            "ymax": int(ymax + top),
                            "text": inner_text.lower(),
                        }

                        if (self.__check_overlap(info) == False):
                            self.objects[class_name].append(info)

                percent = round(scores[0][idx] * 100, 2)
                print(mystr.format(box, class_name, percent));

        if not skip_check:
        # All the results have been drawn on image. Now display the image.
            cv2.imshow('Object detector', frame)

            # Press any key to close the image
            cv2.waitKey(0)

            # Clean up
            cv2.destroyAllWindows()








    def capture_n_detect_realtime( self, top, left, width, height ):
        self.root["x"] = left
        self.root["y"] = top

        # # Name of the directory containing the object detection module we're using
        # MODEL_NAME = '../inference_graph'
        # IMAGE_NAME = 'test1.jpg'

        # # Grab path to current working directory
        # CWD_PATH = os.getcwd()

        # # Path to frozen detection graph .pb file, which contains the model that is used
        # # for object detection.
        # PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

        # # Path to label map file
        # PATH_TO_LABELS = os.path.join(CWD_PATH,'../training','labelmap.pbtxt')

        # # Path to image
        # PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

        # # Number of classes the object detector can identify
        # NUM_CLASSES = 6

        # # Load the label map.
        # # Label maps map indices to category names, so that when our convolution
        # # network predicts `5`, we know that this corresponds to `king`.
        # # Here we use internal utility functions, but anything that returns a
        # # dictionary mapping integers to appropriate string labels would be fine
        # label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        # categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        # category_index = label_map_util.create_category_index(categories)

        # Load the Tensorflow model into memory.
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            sess = tf.Session(graph=detection_graph)

        # Define input and output tensors (i.e. data) for the object detection classifier

        # Input tensor is the image
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        # Output tensors are the detection boxes, scores, and classes
        # Each box represents a part of the image where a particular object was detected
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

        # Each score represents level of confidence for each of the objects.
        # The score is shown on the result image, together with the class label.
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

        # Number of objects detected
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        # Load image using OpenCV and
        # expand image dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value

        sct = mss.mss()
        scrn = {"top": top, "left": left, "width": width, "height": height}

        while True:
            os.system('cls')

            # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
            # i.e. a single-column array, where each item in the column has the pixel RGB value
            frame = cv2.cvtColor(np.array(sct.grab(scrn)), cv2.COLOR_BGRA2BGR)
            frame_expanded = np.expand_dims(frame, axis=0)

            # Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})

            # Draw the results of the detection (aka 'visulaize the results')
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.80)

            for idx, box in enumerate(boxes[0]):
                box[0] *= height
                box[1] *= width
                box[2] *= height
                box[3] *= width

            mystr = ""

            if scores[0][idx] >= .50:
                if scores[0][idx] < .80:
                    mystr = "{} - unknown - bias: {}({})"
                else:
                    mystr = "{} - {}({})"
                
                percent = round(scores[0][idx] * 100, 2)
                print(mystr.format(box, category_index[classes[0][idx]]['name'], percent));

            # All the results have been drawn on the frame, so it's time to display it.
            cv2.imshow('Object detector', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) == ord('q'):
                break

        # Clean up
        cv2.destroyAllWindows()
