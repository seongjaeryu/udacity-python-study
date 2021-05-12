# Title: Use a Pre-trained Image Classifier to Identify Dog Breeds
# Author: Jennifer S.
# Source: Udacity, 'AI Programming with Python' Nanodegree Program

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# classify_images.py
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
        #  Runs classifier function to classify the images classifier function 
        # inputs: path + filename  and  model, returns model_label 
        # as classifier label
        model_label = classifier(images_dir + key, model).lower().strip()
        results_dic[key].append(model_label)
        # Processes the results so they can be compared with pet image labels
        # set labels to lowercase (lower) and stripping off whitespace(strip)        
        # defines truth as pet image label 
        truth = results_dic[key][0]
        # If the pet image label is found within the classifier label list of terms 
        # as an exact match to on of the terms in the list - then they are added to 
        # results_dic as an exact match(1) using extend list function
        if truth in model_label:
            results_dic[key].extend([1])
        # if not found then added to results dictionary as NOT a match(0) using
        # the extend function 
        else:
            results_dic[key].extend([0])