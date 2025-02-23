Install dependencies with `pip install -r requirements.txt`.
Download the model from `https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth` and place it in the same folder as the script.
Open your image and find the coordinates for the object you want to select.
Run the script with `python sam.py input.jpg x0 y0 x1 y1`, replacing `input.jpg` with your image file and entering the bounding box coordinates as four integers: `x0` and `y0` for the top-left corner, `x1` and `y1` for the bottom-right corner.
These define the rectangular area in which the model will select an object.
The script saves `segmentation_mask.png` in the same folder.

To use your black-and-white segmentation mask as a layer mask in GIMP, follow these steps:
1. **Open the Segmentation Mask Image**  
   - Open the black-and-white segmentation mask (`File > Open as Layers`) so it appears as a separate layer above your original image.
2. **Copy the Mask Image**  
   - Select the segmentation mask layer in the **Layers** panel.
   - Press **Ctrl + A** to select all.
   - Press **Ctrl + C** to copy it.
3. **Add a Layer Mask to the Original Image**  
   - Click on your original image’s layer in the **Layers** panel.
   - Right-click it and choose **Add Layer Mask**.
   - In the dialog, select **White (full opacity)** and click **Add**.
4. **Paste the Segmentation Mask into the Layer Mask**  
   - Click on the layer mask (the white box next to your original image).
   - Press **Ctrl + V** to paste the segmentation mask into it.
   - In the **Layers** panel, click the **Anchor Layer** button or press **Ctrl + H** to apply the mask.
5. **Finalize the Mask**  
   - If the mask appears inverted (wrong areas are transparent), right-click the layer mask and choose **Invert Mask**.
This will make the white areas visible and black areas transparent, allowing you to use the segmentation mask to isolate objects in GIMP.
