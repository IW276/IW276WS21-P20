from scipy.spatial import distance


class PxFeatureVector:
    # id = -1  # add ID to the vector itself?
    attributes = {"0": 0}  # TODO Must be implemented!!

    def __init__(self, newTensor):
        # print(str(self.attributes))
        # print(newTensor)
        # for testi in newTensor:
        #    tester = testi.item()
        #    print(str(tester))
        self.attributes = newTensor
        # print(str(self.attributes))
        pass

    # def get_attribute(self, num):
    #     return -1

    # def get_attributes(self):
    #     return -1

    # def compare_px_vectors(self, compare_with):
    #     euclid = distance.euclidean
    #     my_vector = self.attributes.values()
    #     list = []
    #     add = list.add
    #     for vector in compare_with:
    #         dist2 = euclid(my_vector, vector.attributes.values())
    #         add(dist2, vector)
    #     return list

    def compare_px_vector(self, compare_with):

        # print(str(compare_with))
        # print(str(self.attributes))
        euclid = distance.euclidean
        my_vector = self.attributes
        # print(my_vector)
        # other_vector = compare_with.attributes
        dist2 = euclid(self.attributes.cpu(), compare_with.cpu())

        return dist2
