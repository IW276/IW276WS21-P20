from torchreid.utils import FeatureExtractor

extractor = FeatureExtractor(
    model_name="osnet_x1_0",
    # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
    # model_path="F:\\n\\mlfn-9cb5a267.pth.tar",
    model_path="F:\\n\\osnet_ain_x1_0_imagenet.pth",
    # model_path="F:\\n\\osnet_ibn_x1_0_imagenet.pth",
    # model_path="F:\\n\\shufflenet-bee1b265.pth.tar",
    device="cpu",
)

image_list = [
    "F:\\n\\image001.jpg",
    "F:\\n\\image002.jpg",
    "F:\\n\\image003.jpg",
    "F:\\n\\image004.jpg",
    "F:\\n\\image005.jpg",
]

features = extractor(image_list)
print("Features coming now:")
print(features.shape)  # output (5, 512)
print(str(features))

testFile = open("F:\\n\\testfile.txt", "w")

for objec in features:
    print(str(objec))
    testFile.write(str(objec) + "\n")
