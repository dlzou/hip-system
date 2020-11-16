# hip-system

Hot Interior Protection System, a project for Hack Month 2020

## Detection

Given our time constraint and limited expertise, we decide to "borrow" the [YOLOv5](https://github.com/ultralytics/yolov5) model to do the heavy-lifting of our camera detection functionality. However, we customized several parts to better align with the HIP System. 

### Retraining

The pretrained model parameters included with YOLOv5 can identify up to 80 classes of objects within any image, but the HIP System only needs to detect the "person" class. Therefore, we decided to retrain the YOLOv5 model on a filtered set of data.

Our starting point was YOLOv5s (small) for better inference performance on smaller devices. After adjusting a few hyperparameters and writing a script filter the COCO dataset for only "person" class labels, we retrained the model on the filtered dataset onboard a student-maintained GPU cluster at UC Berkeley. After about 40 epochs, the validation accuracy increased from 0.66 to about 0.73. 

### Signal Buffer

As object detection is running, a signal must be sent to hardware controllers whenever a "person" object is registered. However, we found the naive approach of calling a function within the detect loop to be inadequate for noisy data. Things would quickly get annoying for parents...

We created a simple transmitter structure that is intended to be called on each frame, during which will update its internal buffer with the last n outputs. If the proportion of hits to the buffer size is greater than an arbitrary threshold, a signal is emitted, and the buffer is flushed. The transmitter makes the HIP System more resilient against occasional misclassifications.

### Sample Output

`detect.py` supports both live feed and images. The following are the bounding box outputs on two sample stock images, for demonstration purposes only; a physical prototype would be using a live feed.

![baby1.jpg](/detection/inference/output/baby1.jpg)

![baby2.jpg](/detection/inference/output/baby2.jpg)

This second example shows that the detection can handle more than one object. This robustness is thanks to the design of the YOLO algorithm. 
