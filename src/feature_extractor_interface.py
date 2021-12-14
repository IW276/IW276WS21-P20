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
    image_list = 0
    features = 0
    srcfiles = 0

    def __init__(self, extractor_model, path_to_model, device_to_use):
        # model_file = pathlib.Path(path_to_model)
        # if not model_file.is_file():
        #     test_path = pathlib.Path(__file__).parent.resolve()
        #     path_to_model = (
        #         str(test_path).replace("\\", "\\\\")
        #         + "\\\\osnet_ain_x0_25_imagenet.pyth"
        #     )
        #     extractor_model = "osnet_x0_25"

        if not "cpu" in device_to_use:
            if not torch.cuda.is_available:
                device_to_use = "cpu"
            if not "gpu" in device_to_use:
                device_to_use = "gpu"

        try:
            test = self.extractor = FeatureExtractor(
                model_name=extractor_model,  # extractor_model,
                model_path=path_to_model,  # path_to_model,
                # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
                # model_path="F:\\n\\mlfn-9cb5a267.pth.tar",
                # model_path="F:\\n\\osnet_ibn_x1_0_imagenet.pth",
                # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
                device=device_to_use,
            )
        except:
            default_model = "osnet_x0_25"

            base_path = pathlib.Path(".")  # pathlib.Path(__file__).parent.resolve()
            for default_path in base_path.iterdir():
                print(str(default_path))
                if default_path.is_file() & ("osnet_ain_x0_25" in str(default_path)):
                    print(str(default_path))

                    test = self.extractor = FeatureExtractor(
                        default_model, default_path, device="cpu"
                    )
                    # default_path = (
                    #    str(base_path).replace("\\", "\\\\")
                    #    + "\\\\osnet_ain_x0_25_imagenet.pyth"
                    # )

        print(str(test))

    def extract_images(self, list_of_images):

        if not isinstance(list_of_images, list):
            return "The given object is not a list!"

        features = self.extractor(list_of_images)
        return features

    def extract_image(self, image):

        list_of_images = []
        list_of_images.append(image)
        features = self.extractor(list_of_images)
        return features
