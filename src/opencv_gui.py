import time

import cv2
import ImgIngest
import cropper
import feature_extractor_interface
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

        if not identified_images_path_param:
            cv2.namedWindow(self.window_name)
            cv2.createTrackbar("close", self.window_name, 0, 1, f)

        extractor = feature_extractor_interface.feature_extractor_interface(
            "osnet_x0_25", "F:/n/osnet_x0_25_imagenet.pth", "cuda"
        )
        db = database.database(-1, -1)

        while self.running:
            image_info = ingestion.get_frame_info()

            # creating crops
            crops_image = cropper.create_crops(image_info["img"], image_info["data"])

            # TODO deliver crops_image to feature extractor
            feature_tensor = extractor.extract_images(crops_image)
            db.update_list()
            all_ids = db.update_tensorList(feature_tensor)

            # draw BBs and IDs
            self.update_image(image_info["img"], image_info["data"], all_ids)

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

            if image_info["current_frame"] % 10 == 0:
                end_time = time.time()
                print(
                    "fps ="
                    + str(10 / (end_time - start_time))
                )
                start_time = end_time

            if image_info["frame_count_total"] <= image_info["current_frame"]:
                cv2.destroyAllWindows()
                return

    def update_image(self, image_path, coords, ids):
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        placeholder_id = 1
        i = 0
        for row in coords.itertuples():
            placeholder_id = placeholder_id + 1
            self.image = draw_on_image(
                self.image, row[3], row[4], row[5], row[6], ids[i]
                )
            i += 1
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
    #image_dir = "./../datasets/MOT20-01/img1"
    # image_dir = "F:/AS_Labor/AS_Labor/IW276WS21-P20/datasets/MOT20-01/img1"
    #detection_file = "./../datasets/MOT20-01/det/det.txt"
    # detection_file = "F:\AS_Labor\AS_Labor\IW276WS21-P20/datasets/MOT20-01/det/det.txt"
    gui = OpencvGUI()
    gui.run(image_dir, detection_file, identified_images_path)
