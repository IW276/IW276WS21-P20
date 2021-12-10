import time

import cv2
import ImgIngest


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


class OpencvGUI:
    coordinates = [{'top': (100, 100), 'bottom': (200, 200), 'id': 1},
                   {'top': (300, 300), 'bottom': (400, 400), 'id': 2},
                   {'top': (500, 500), 'bottom': (600, 600), 'id': 3}]
    image = None
    window_name = 'Personenidentifikation mit rapid Re-Identification'

    def run(self, image_dir_param, detection_file_param):
        ingestion = ImgIngest.ImgIngest()
        ingestion.set_path_img_folder(image_dir_param)
        ingestion.set_path_detection_file(detection_file_param)
        ingestion.read_detection_file()
        start_time = time.time()
        while True:
            image_info = ingestion.get_frame_info()
            self.update_image(image_info['img'], self.coordinates)
            cv2.imshow(self.window_name, self.image)
            cv2.waitKey(1)

            if image_info['frame_count_total'] <= image_info['current_frame']:
                end_time = time.time()
                print('fps =' + str(image_info['frame_count_total']/(end_time - start_time)))
                cv2.destroyAllWindows()
                return

    def update_image(self, image_path, coordinates):
        self.image = cv2.imread(image_path.__str__(), cv2.IMREAD_COLOR)

        for entry in self.coordinates:
            self.image = draw_on_image(self.image, entry['top'], entry['bottom'], entry['id'])
        return


if __name__ == '__main__':
    image_dir = './../datasets/MOT20-01/img1'
    detection_file = './../datasets/MOT20-01/det/det.txt'
    gui = OpencvGUI()
    gui.run(image_dir, detection_file)
