# ImgIngest.py
import os
import pandas
import pathlib


class ImgIngest:

    # define class
    def __init__(self):
        self.data_frame = None
        self.path_img_folder = ""
        #    self.path_img = ""
        self.path_detection_file = ""
        self.frame_counter = 1
        self.images = []
        self.total_number_of_frames = 0

    #    self.path = ""

    # getter and setter for fields
    def set_path_img_folder(self, path):
        self.images = []
        self.path_img_folder = path
        pathlib_path = pathlib.Path(path)
        print(str(pathlib_path.is_file()))
        for child in pathlib_path.iterdir():
            self.images.append(child.__str__())
        self.images.sort()
        self.total_number_of_frames = len(self.images)

    def get_path_img_folder(self):
        return self.path_img_folder

    # def set_path_img(self, path):
    #    self.path_img = path

    # def get_path_img(self):
    #    return self.path_img

    def set_path_detection_file(self, path):
        self.path_detection_file = path

    def get_path_detection_file(self):
        return self.path_detection_file

    def set_frame_counter(self, counter):
        self.frame_counter = counter

    def get_frame_counter(self):
        return self.frame_counter

    # def set_path(self, path):
    #    self.path = path

    # def get_path(self):
    #    return self.path

    # read detection file
    def read_detection_file(self):
        with open(self.path_detection_file) as f:
            self.data_frame = pandas.read_csv(f)

    def get_frame_lines(self):
        column_names = self.data_frame.columns
        frame_lines = self.data_frame.loc[
            self.data_frame[column_names[0]] == self.frame_counter
        ]
        # frame_lines = self.data_frame['frame == ' + str(self.frame_counter)]
        # frame_lines = self.data_frame[self.dataframe.frame == self.frame_counter]
        # frame_lines = self.data_frame.query(column_names[0] + ' = ' + str(self.frame_counter))

        return frame_lines

    # return the important stuff
    def get_frame_info(self):
        frame_info = {
            "img": self.images[self.frame_counter - 1],
            "data": self.get_frame_lines(),
            "current_frame": self.frame_counter,
            "frame_count_total": self.total_number_of_frames,
        }
        self.frame_counter += 1
        return frame_info
