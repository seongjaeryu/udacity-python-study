# Title: Use a Pre-trained Image Classifier to Identify Dog Breeds
# Author: Jennifer S.
# Source: Udacity, 'AI Programming with Python' Nanodegree Program

# Imports python modules
from os import listdir

# get_pet_labels.py
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    filename_list = listdir(image_dir)
    for filename in filename_list:
        if filename[0] != '.':
            pet_label = ''
            for _str in filename.lower().split('_'): # str list
                if _str.isalpha():
                    pet_label += _str + ' '
            pet_label = pet_label.strip()
            if pet_label not in results_dic:
                results_dic[filename] = [pet_label]
            #     print(results_dic[filename])
            # else:
            #     print("\n'{}' pet label is already in list!".format(pet_label))
            #     print("'existing filename: '{}'".format(results_dic[pet_label]))
            #     print("'tried filename(not added): '{}'".format(filename))
    return results_dic