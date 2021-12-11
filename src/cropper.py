from cv2 import imread, IMREAD_COLOR


def create_crops(image_path, crop_coordinates):
    resulting_crops = []
    image = imread(image_path, IMREAD_COLOR)
    for row in crop_coordinates.itertuples():
        top = row[3]
        left = row[4]
        height = row[5]
        width = row[6]
        resulting_crops.append(
            image[left:left + width,
                  top:top + height].copy()
        )
    return resulting_crops
