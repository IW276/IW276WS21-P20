import torch

# from torch.functional import Tensor
from torchreid.utils import FeatureExtractor
import pathlib

# print("Features coming now:")
# print(features.shape)  # output (5, 512)
# print(str(features))
# testFile = open("F:\\n\\testfile.txt", "w")


class feature_extractor_interface:

    extractor = 0
    # image_list = 0
    # features = 0
    # srcfiles = 0

    def __init__(self, extractor_model, path_to_model, device_to_use):
        # model_file = pathlib.Path(path_to_model)
        # if not model_file.is_file():
        #     test_path = pathlib.Path(__file__).parent.resolve()
        #     path_to_model = (
        #         str(test_path).replace("\\", "\\\\")
        #         + "\\\\osnet_ain_x0_25_imagenet.pyth"
        #     )
        #     extractor_model = "osnet_x0_25"

        try:
            print(device_to_use)
            self.extractor = FeatureExtractor(
                model_name=extractor_model,  # extractor_model,
                model_path=path_to_model,  # path_to_model,
                device=device_to_use,
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

    def extract_images(self, list_of_images):

        if not isinstance(list_of_images, list):
            return "The given object is not a list!"

        features = self.extractor(list_of_images)
        return features

    # def extract_image(self, image):

    #     list_of_images = []
    #     list_of_images.append(image)
    #     features = self.extractor(list_of_images)
    #     return features
