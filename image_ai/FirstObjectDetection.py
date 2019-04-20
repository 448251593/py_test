#qq:448251593,业余python,c ucos Linux 物联网
#需要安装pip3 install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

from imageai.Detection import ObjectDetection
import os

pic_name="b1"

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , pic_name+".jpg"), output_image_path=os.path.join(execution_path , pic_name+"new.jpg"))

for eachObject in detections:
    print(eachObject["name"] + " : " + str(eachObject["percentage_probability"]))
    print("x1 = " + str(eachObject["box_points"][0]))
    print("y1 = " + str(eachObject["box_points"][1]))
    print("x2 = " + str(eachObject["box_points"][2]))
    print("y2 = " + str(eachObject["box_points"][3]))
    print("--------------------------------")