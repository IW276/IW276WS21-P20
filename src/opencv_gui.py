import time

import cv2
from torchreid.utils import FeatureExtractor
from cv2 import IMREAD_COLOR
import ImgIngest
import database
import argparse


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

    def run(self, image_dir_param, detection_file_param, identified_images_path_param):
        # init ingest
        ingestion = ImgIngest.ImgIngest()
        ingestion.set_path_img_folder(image_dir_param)
        ingestion.set_path_detection_file(detection_file_param)
        ingestion.read_detection_file()

        start_time = time.time()
        scale_percent_1 = 80

        current_frame = 0
        total_amount_frames = ingestion.total_number_of_frames

        if not identified_images_path_param:
            cv2.namedWindow(self.window_name)
            cv2.createTrackbar("close", self.window_name, 0, 1, f)

        try:
            self.extractor = FeatureExtractor(
                model_name="osnet_x0_25",  # extractor_model,
                model_path="./../osnet_ain_x0_25_imagenet.pyth",  # path_to_model,
                device="cuda",
            )
        except Exception as e:
            print(e)
            self.extractor = FeatureExtractor(
                "osnet_x0_25", "./../osnet_ain_x0_25_imagenet.pyth", device="cpu"
            )

        db = database.database(-1, -1)

        while self.running:
            image_info = ingestion.get_frame_info()
            start = time.time()

            resulting_crops = []
            image = cv2.imread(image_info["img"], IMREAD_COLOR)
            for row in image_info["data"].itertuples():
                top = row[3]
                left = row[4]
                height = row[5]
                width = row[6]
                resulting_crops.append(
                    image[left : left + width, top : top + height].copy()
                )

            time_images = time.time()
            crops_image = resulting_crops

            feature_tensor = self.extractor(crops_image)
            time_features = time.time()

            db.update_list()
            all_ids = db.update_tensorList(feature_tensor)
            time_db = time.time()

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

            if not identified_images_path_param:
                cv2.imshow(self.window_name, rescaled_image)
                cv2.waitKey(1)

                if cv2.getTrackbarPos("close", self.window_name) == 1:
                    cv2.destroyAllWindows()
                    return
            else:
                cv2.imwrite(identified_images_path_param + str(image_info["current_frame"]) + ".jpg", rescaled_image)

            time_draw = time.time()

            with open("fpscheckerfile.txt", "a") as the_file:

                time_draw -= time_db
                time_db -= time_features
                time_features -= time_images
                time_images -= start
                time_all = time_draw + time_db + time_images + time_features

                the_file.write(
                    "Read Image: "
                    + str(time_images)
                    + " Extract features: "
                    + str(time_features)
                    + " update db: "
                    + str(time_db)
                    + " draw image: "
                    + str(time_draw)
                    + " all: "
                    + str(time_all)
                    + "\n"
                )

            if image_info["current_frame"] % 10 == 0:
                end_time = time.time()
                print("Frame: " + str(image_info["current_frame"]) + " fps =" + str(10 / (end_time - start_time)))
                start_time = end_time

            if image_info["frame_count_total"] <= image_info["current_frame"]:
                cv2.destroyAllWindows()
                return

if __name__ == "__main__":
    # get command line arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--image_path", type=str)
    argument_parser.add_argument("--detection_path", type=str)
    argument_parser.add_argument("--identified_images", type=str)
    arguments = argument_parser.parse_args()
    image_dir = arguments.image_path
    detection_file = arguments.detection_path
    identified_images_path = arguments.identified_images
    if not image_dir:
        image_dir = "./../datasets/MOT20-01/img1"
    if not detection_file:
        detection_file = "./../datasets/MOT20-01/det/det.txt"
    if not identified_images_path:
        identified_images_path = None
    gui = OpencvGUI()
    gui.run(image_dir, detection_file, identified_images_path)
