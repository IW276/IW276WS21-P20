from torchreid.utils import FeatureExtractor

extractor = FeatureExtractor(
    model_name="osnet_x1_0",
    model_path="F:\\AS_Labor\\IW276WS21-P20\\person_reid\\deep-person-reid\\torchreid\\models\\densenet.py",
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
print(features.shape)  # output (5, 512)

