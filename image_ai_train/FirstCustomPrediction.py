
from imageai.Prediction.Custom import CustomImagePrediction
from imageai.Detection import ObjectDetection
import os
#os.environ["CUDA_VISIBLE_DEVICES"]="-1" 
execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "model_ex-100_acc-0.550000.h5"))
prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
prediction.loadModel(num_objects=2)


predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "guazi.jpg"), result_count=2)


for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(str(eachPrediction) + " : " + str(eachProbability))






#pic_name="guazi"
#detector = ObjectDetection()
#detector.setModelTypeAsRetinaNet()
#
## detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.h5"))
#detector.setModelPath( os.path.join(execution_path , "model_ex-100_acc-0.550000.h5"))
#detector.loadModel()
## detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , pic_name+".jpg"), output_image_path=os.path.join(execution_path , pic_name+"new.jpg"))
#detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , pic_name+".jpg"), output_image_path=os.path.join(execution_path , pic_name+"new.jpg"))
#for eachObject in detections:
#    print(eachObject["name"] + " : " + str(eachObject["percentage_probability"]))
#    print("x1 = " + str(eachObject["box_points"][0]))
#    print("y1 = " + str(eachObject["box_points"][1]))
#    print("x2 = " + str(eachObject["box_points"][2]))
#    print("y2 = " + str(eachObject["box_points"][3]))
#    print("--------------------------------")