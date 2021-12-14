import collections
import PxFeatureVector


class Person:
    my_px_feature_vectors = collections.deque(maxlen=5)
    id = -1
    age = 0

    def __init__(self, my_i_d):
        self.id = my_i_d

    def get_px_vector(self, num):
        return self.my_px_feature_vectors.index(num)

    def get_px_vectors(self):
        return self.my_px_feature_vectors

    def add_px_vector(self, new_tensor):
        if 0 == 0:
            pass  # _implement checkup if new_vector is a fitting vector!
        # print(str(new_tensor))
        new_vector = PxFeatureVector.PxFeatureVector(new_tensor)
        self.my_px_feature_vectors.append(new_vector)
        self.age = 0
        return 1

    def add_px_vectors(self, new_vectors):
        for new_vector in new_vectors:
            self.add_px_vector(new_vector)

    def compare_me_to_px_vector(self, px_vector):
        average_ranking = 0
        amount_of_frames = 0

        for compare_with in self.my_px_feature_vectors:
            average_ranking += compare_with.compare_px_vector(px_vector)
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

    def set_i_d(self, my_i_d):
        self.id = my_i_d
