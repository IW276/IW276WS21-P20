from scipy.spatial import distance


class PxFeatureVector:
    id = -1  # add ID to the vector itself?
    attributes = {  # TODO Must be implemented!!
        "0": 0
    }

    def __init__(self):
        pass

    def get_attribute(self, num):
        return -1

    def get_attributes(self):
        return -1

    def compare_pxvectors(self, compare_with):
        euclid = distance.euclidean
        my_vector = self.attributes.values()
        list = []
        add = list.add
        for vector in compare_with:
            dist2 = euclid(my_vector, vector.attributes.values())
            add(dist2, vector)
        return list
