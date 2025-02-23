import argparse
import cv2
import numpy as np
from segment_anything import sam_model_registry, SamPredictor

def main():
    parser = argparse.ArgumentParser(description="SAM interactive segmentation")
    parser.add_argument("image", help="Path to input image")
    parser.add_argument("bbox", nargs=4, type=int, help="Bounding box coordinates: x0 y0 x1 y1")
    args = parser.parse_args()
    bbox = np.array(args.bbox).reshape(1, 4)
    sam_checkpoint = "sam_vit_h_4b8939.pth" #https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
    model_type = "vit_h"
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    predictor = SamPredictor(sam)
    image = cv2.imread(args.image)
    if image is None:
        print(f"Could not load image {args.image}")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    predictor.set_image(image)
    masks, scores, logits = predictor.predict(
        point_coords=None,
        point_labels=None,
        box=bbox,
        multimask_output=False,)
    mask = masks[0].astype(np.uint8) * 255
    output_mask_path = "segmentation_mask.png"
    cv2.imwrite(output_mask_path, mask)
    print(f"Segmentation mask saved as {output_mask_path}")

if __name__ == "__main__":
    main()

