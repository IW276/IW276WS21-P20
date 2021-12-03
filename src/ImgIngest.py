#ImgIngest.py
import os
import pandas
import pathlib


class ImgIngest(object):

    # define class
    def __init__ (self):
        self.data_frame = None
        self.path_img_folder = ""
    #    self.path_img = ""
        self.path_detection_file = ""
        self.frame_counter = 1
        self.images = None
    #    self.path = ""

    # getter and setter for fields
    def set_path_img_folder(self, path):
        self.path_img_folder = path
        self.images = pathlib.listdir(self.path_img_folder)

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
        frame_lines = self.data_frame.query(column_names[0] + ' = ' + self.frame_counter)
        return frame_lines

    # return the important stuff
    def get_frame_info(self):
        frame_info = {
            "img": pathlib(self.path_img_folder).join(self.images[self.frame_counter-1]),
            "data": self.get_frame_lines(),
            "frame_counter": self.frame_counter,
            "frame_count": self.images.count()
        }
        self.frame_counter += 1
        return frame_info
