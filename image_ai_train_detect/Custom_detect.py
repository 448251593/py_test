from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
#detector.setModelPath("hololens-ex-60--loss-2.76.h5") # download via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/hololens-ex-60--loss-2.76.h5
#detector.setJsonPath("detection_config.json") # download via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/detection_config.json

detector.setModelPath("./custom_detect_train_data/models/detection_model-ex-017--loss-0015.946.h5") 
detector.setJsonPath("./custom_detect_train_data/json/detection_config.json") 

detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="./custom_detect_train_data/otherdata/100.jpg", output_image_path="./custom_detect_train_data/otherdata/100_detect.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])