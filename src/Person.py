import collections

# import PxFeatureVector
from scipy.spatial import distance


class Person:
    my_px_feature_vectors = None
    id = -1
    age = 0
    # x_pos = -1
    # x_length = -1
    # y_pos = -1
    # y_length = -1
    attributes = {"0": 0}  # TODO Must be implemented!!

    def __init__(self, my_i_d):
        self.id = my_i_d
        self.my_px_feature_vectors = collections.deque(maxlen=5)

    # def get_px_vector(self, num):
    #     return self.my_px_feature_vectors.index(num)

    # def get_px_vectors(self):
    #     return self.my_px_feature_vectors

    def add_px_vector(self, new_tensor):
        if 0 == 0:
            pass  # _implement checkup if new_vector is a fitting vector!
        # print(str(new_tensor))
        # new_vector = PxFeatureVector.PxFeatureVector(new_tensor)
        self.my_px_feature_vectors.append(new_tensor)
        self.age = 0
        return 1

    # def add_px_vectors(self, new_vectors):
    #     for new_vector in new_vectors:
    #         self.add_px_vector(new_vector)
    #     age = 0

    def compare_me_to_px_vector(self, px_vector):
        average_ranking = 0
        amount_of_frames = 0

        for compare_with in self.my_px_feature_vectors:

            # print(str(compare_with))
            # print(str(self.attributes))
            euclid = distance.euclidean
            # my_vector = self.attributes
            # print(my_vector)
            # other_vector = compare_with.attributes
            # dist2 = euclid(self.attributes, compare_with)
            average_ranking += euclid(compare_with, px_vector)
            # average_ranking += compare_with.compare_px_vector(px_vector)

            amount_of_frames += 1
        if amount_of_frames == 0:
            return -1
        return average_ranking / amount_of_frames

    def get_age(self):
        return self.age

    def increase_age(self):
        self.age += 1

    def get_i_d(self):
        return self.id

    # def set_i_d(self, my_i_d):
    #     self.id = my_i_d
