import feature_extractor_interface
import database
import pathlib


class example:
    def extractor_example(self):

        test_path = pathlib.Path(__file__).parent.resolve()
        default_path = (
            str(test_path).replace("\\", "\\\\") + "\\\\osnet_ain_x0_25_imagenet.pyth"
        )
        print(str(test_path))

        # print(defaultPath)

        # extractor = FeatureExtractor(
        model_name = "osnet_x0_25"
        # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
        # model_path="F:\\n\\mlfn-9cb5a267.pth.tar",
        # model_path = "F:\\n\\osnet_ain_x0_25_imagenet.pyth"
        # model_path = defaultPath
        # model_path="F:\\n\\osnet_ibn_x1_0_imagenet.pth",
        # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
        device = "cpu"
        # )
        model_name = "xxxx"
        default_path = "xxxx"
        extractor_interface = feature_extractor_interface.feature_extractor_interface(
            model_name, default_path, device
        )

        db = database.database(-1, -1)

        image_list = [
            "F:\\n\\image001.jpg",
            "F:\\n\\image002.jpg",
            "F:\\n\\image003.jpg",
            "F:\\n\\image004.jpg",
            "F:\\n\\image005.jpg",
        ]

        feature_list = extractor_interface.extract_images(image_list)
        db.update_tensorList(feature_list)
        db.update_list()

        # features = extractor(image_list)
        # testFile = open("F:\\n\\testfile.txt", "w")
        # for objec in features:
        # print(str(objec))
        # testFile.write(str(objec) + "\n")
        # print(str(objec))
        # testFile.write(str(objec) + "\n")
        # return features
