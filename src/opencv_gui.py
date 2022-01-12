import time

import cv2
import ImgIngest
import numpy

# import cropper
# import feature_extractor_interface
import database
from cv2 import imread, IMREAD_COLOR
from torchreid.utils import FeatureExtractor


def draw_on_image(image_to_edit, left, top, width, height, person_id):
    red = person_id * 30 % 255
    green = person_id * 30 % 255
    blue = person_id * 30 % 255
    color = (red, green, blue)
    thickness = 1
    top_left_corner = (left, top)
    bottom_right_corner = (left + width, top + height)
    edited_image = cv2.rectangle(
        image_to_edit, top_left_corner, bottom_right_corner, color, thickness
    )
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (top_left_corner[0], top_left_corner[1] - 20)
    font_scale = 1
    edited_image = cv2.putText(
        edited_image,
        "ID:" + str(person_id),
        org,
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA,
    )

    return edited_image


def f(*args):
    return


class OpencvGUI:
    coordinates = [
        {"top": (100, 100), "bottom": (200, 200), "id": 1},
        {"top": (300, 300), "bottom": (400, 400), "id": 2},
        {"top": (500, 500), "bottom": (600, 600), "id": 3},
    ]
    image = None
    window_name = "Personenidentifikation mit rapid Re-Identification"
    running = True
    extractor = 0  # Added as cover for inlining feature_extractor_interface

    def close(self, *args):
        self.running = False
        cv2.destroyAllWindows()

    def run(self, image_dir_param, detection_file_param):
        # init ingest
        ingestion = ImgIngest.ImgIngest()
        ingestion.set_path_img_folder(image_dir_param)
        ingestion.set_path_detection_file(detection_file_param)
        ingestion.read_detection_file()

        start_time = time.time()
        scale_percent_1 = 80

        cv2.namedWindow(self.window_name)
        cv2.createTrackbar("close", self.window_name, 0, 1, f)
        # extractor = feature_extractor_interface.feature_extractor_interface(
        #     "osnet_x0_25", "F:\\n\\osnet_x0_25_imagenet.pth", "cuda"
        # )

        try:
            self.extractor = FeatureExtractor(
                model_name="osnet_x0_25",  # extractor_model,
                model_path="F:\\n\\osnet_x0_25_imagenet.pth",  # path_to_model,
                device="cuda",
            )
        except Exception as e:
            print(e)
            self.extractor = FeatureExtractor(
                "osnet_x0_25", "./../osnet_ain_x0_25_imagenet.pyth", device="cpu"
            )
            # default_path = (
            #    str(base_path).replace("\\", "\\\\")
            #    + "\\\\osnet_ain_x0_25_imagenet.pyth"
            # )

        db = database.database(-1, -1)

        while self.running:
            image_info = ingestion.get_frame_info()

            # creating crops
            # def create_crops(image_path, crop_coordinates):

            resulting_crops = []
            image = imread(image_info["img"], IMREAD_COLOR)
            for row in image_info["data"].itertuples():
                top = row[3]
                left = row[4]
                height = row[5]
                width = row[6]
                resulting_crops.append(
                    image[left : left + width, top : top + height].copy()
                )

            crops_image = resulting_crops

            # TODO deliver crops_image to feature extractor
            feature_tensor = self.extractor(crops_image)

            # def extract_images(self, list_of_images):

            db.update_list()
            all_ids = db.update_tensorList(feature_tensor)

            # draw BBs and IDs
            # self.update_image(image_info["img"], image_info["data"], all_ids)
            # def update_image(self, image_path, coords, ids):
            self.image = cv2.imread(image_info["img"], cv2.IMREAD_COLOR)
            placeholder_id = 1
            i = 0
            for row in image_info["data"].itertuples():
                placeholder_id = placeholder_id + 1
                self.image = draw_on_image(
                    self.image, row[3], row[4], row[5], row[6], all_ids[i]
                )
                i += 1
            # return

            # image scaling
            width_1 = int(self.image.shape[1] * (scale_percent_1 / 100))
            height_1 = int(self.image.shape[0] * (scale_percent_1 / 100))
            dim_1 = (width_1, height_1)
            rescaled_image = cv2.resize(self.image, dim_1, interpolation=cv2.INTER_AREA)
            cv2.imshow(self.window_name, rescaled_image)
            cv2.waitKey(1)

            if cv2.getTrackbarPos("close", self.window_name) == 1:
                cv2.destroyAllWindows()
                return

            if image_info["frame_count_total"] <= image_info["current_frame"]:
                end_time = time.time()
                print(
                    "fps ="
                    + str(image_info["frame_count_total"] / (end_time - start_time))
                )
                cv2.destroyAllWindows()
                return

    # def update_image(self, image_path, coords, ids):
    #     self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    #     placeholder_id = 1
    #     i = 0
    #     for row in coords.itertuples():
    #         placeholder_id = placeholder_id + 1
    #         self.image = draw_on_image(
    #             self.image, row[3], row[4], row[5], row[6], ids[i]
    #         )
    #         i += 1
    #     return


if __name__ == "__main__":
    # image_dir = #"./../datasets/MOT20-01/img1"
    image_dir = "F:/AS_Labor/AS_Labor/IW276WS21-P20/datasets/MOT20-01/img1"
    # detection_file = #"./../datasets/MOT20-01/det/det.txt"
    detection_file = "F:\AS_Labor\AS_Labor\IW276WS21-P20/datasets/MOT20-01/det/det.txt"
    gui = OpencvGUI()
    gui.run(image_dir, detection_file)
