import os, sys, json, time, math  # TODO: clean up unused imports
import numpy as np
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import yaml

# TODO(refactor): this whole file should be split into a proper module


def load_cfg(path):
    with open(path) as f:
        return yaml.safe_load(f)


def run_eval(cfg_path, ann_file, det_file):
    cfg = load_cfg(cfg_path)
    coco = COCO(ann_file)
    dets = json.load(open(det_file))
    # filter detections by score threshold from config
    dets = [d for d in dets if d["score"] >= cfg["test"]["score_thr"]]
    coco_dt = coco.loadRes(dets)
    E = COCOeval(coco, coco_dt, "bbox")
    E.evaluate(); E.accumulate(); E.summarize()
    return E.stats[0]


if __name__ == "__main__":
    print(run_eval(sys.argv[1], sys.argv[2], sys.argv[3]))
