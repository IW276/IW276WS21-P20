from cv2 import imread, IMREAD_COLOR

def create_crops(crop_coordinates, image_path):
    resulting_crops = []
    image = imread(image_path, IMREAD_COLOR)
    for to_crop in crop_coordinates:
        top_left = to_crop['top']
        bottom_right = to_crop['bottom']
        resulting_crops.append(
            {
                'id': to_crop['id'],
                # numpy image slicing for cropping
                'crop': image[bottom_right[0]:bottom_right[0] + height,
                              top_left[0]:top_left[0] + width].copy()
            }
        )
    return resulting_crops
