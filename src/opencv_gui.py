import cv2


coordinates = [{'top': (100, 100), 'bottom': (200, 200), 'id': 1},
               {'top': (300, 300), 'bottom': (400, 400), 'id': 2},
               {'top': (500, 500), 'bottom': (600, 600), 'id': 3}]


def draw_on_image(image_to_edit, top_left_corner, bottom_right_corner, person_id):
    red = person_id * 30 % 255
    green = person_id * 30 % 255
    blue = person_id * 30 % 255
    color = (red, green, blue)
    thickness = 1
    edited_image = cv2.rectangle(image_to_edit, top_left_corner, bottom_right_corner, color, thickness)

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (top_left_corner[0], top_left_corner[1] - 20)
    font_scale = 1
    edited_image = cv2.putText(edited_image, 'ID:' + str(person_id), org, font,
                               font_scale, color, thickness, cv2.LINE_AA)

    return edited_image


def create_crops(crop_coordinates, image_to_crop):
    resulting_crops = []
    for to_crop in crop_coordinates:
        top_left = to_crop['top']
        bottom_right = to_crop['bottom']
        width = bottom_right[0] - top_left[0]
        height = bottom_right[1] - top_left[1]
        resulting_crops.append(
            {
                'id': to_crop['id'],
                #numpy image slicing for cropping
                'crop': image_to_crop[bottom_right[0]:bottom_right[0] + height,
                                      top_left[0]:top_left[0] + width].copy()
            }
        )
    return resulting_crops


image = cv2.imread("F:/GIT/HKA-AutonomeSystemeLab/test.png", cv2.IMREAD_COLOR)

for entry in coordinates:
    image = draw_on_image(image, entry['top'], entry['bottom'], entry['id'])

window_name = 'Image'
cv2.imshow(window_name, image)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)

cv2.destroyAllWindows()
