# Settings reported in the paper (RetinaNet R50-FPN, 1x)
- train scale: shorter side 800, max 1333
- test scale: shorter side 800, max 1333
- batch size 16, lr 0.01, 12 epochs, steps at 8 and 11
- eval: score threshold 0.05, max 100 detections per image, NMS IoU 0.5
- result: COCO val2017 mAP 36.5
