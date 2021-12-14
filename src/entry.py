# import getTensors

import database

# import Person
# import PxFeatureVector
# import feature_extractor_interface_example
from feature_extractor_interface_example import example


class entry:

    # tensors = getTensors.getTensors()
    # db = database.database(-1, -1)  # Gute Werte???
    # print("Test")

    # alltensors = tensors.getTensors()
    # db.update_tensorList(alltensors)
    feature_example = example()
    feature_example.extractor_example()
