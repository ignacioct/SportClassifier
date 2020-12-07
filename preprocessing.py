import pandas as pd
import numpy as np
import cv2


def preprocessing():
    """
    Given the data csv and the directory with the different instances,
    returns the numpy arrays of training, validation and test in the given fashion:
    labels (dictionary), X_train, X_s, Y_train, Y_s, X_test, X_val, Y_test, Y_val
    """

    # Labels dictionary
    labels = {
        0: 'badminton',
        1: 'baseball',
        2: 'basketball',
        3: 'boxing',
        4: 'chess',
        5: 'cricket',
        6: 'fencing',
        7: 'football',
        8: 'formula1',
        9: 'gymnastics',
        10: 'hockey',
        11: 'ice_hockey',
        12: 'kabaddi',
        13: 'motogp',
        14: 'shooting',
        15: 'swimming',
        16: 'table_tennis',
        17: 'tennis',
        18: 'volleyball',
        19: 'weight_lifting',
        20: 'wrestling',
        21: 'wwe'
    }

    #Data paths
    DATA_DIR = 'input/data/'
    DATA_CSV = 'input/data.csv' 

    #Reading csv
    df = pd.read_csv(DATA_CSV)
    print(df.head(5), "\n")
    print("Shape: \t", df.shape)
    print("Number of different classes: ", len(df['target'].unique()))

    # #Classes distribution
    # ax = sns.countplot(
    #     df['target']
    # )
    # ax.set_xticklabels(labels.values(), rotation=90)
    # ax.plot()

    # IMAGES PREPROCESSING
    train_imgs = df['image_path'].tolist()
    train_labels = df['target'].tolist()

    def read_and_process_image(list_of_images, list_of_labels, numclasses=22):
        """
        X = array of images
        Y = array of labels
        """

        X = []
        Y = []

        # X filling
        for image in list_of_images:
            X.append(cv2.resize( cv2.imread(image, cv2.IMREAD_COLOR), (64,64), interpolation=cv2.INTER_CUBIC ))


        # Y filling
        for label in list_of_labels:

            # each row will have a list of length=22 with 1 or 0 in each position depending on label value
            temp_labels = []
            for i in range(22):

                if label == i:
                    temp_labels.append(1)

                else:
                    temp_labels.append(0)
            
            Y.append(temp_labels)

        return X, Y

    X, Y = read_and_process_image(train_imgs, train_labels)

    X = np.array(X)
    Y = np.array(Y)

    print()
    print( 'Shape of image is: {}'.format(X.shape) )
    print( 'Shape of labels is: {}'.format(Y.shape) )




    # dividing data in sets

    from sklearn.model_selection import train_test_split
    X_train, X_s, Y_train, Y_s = train_test_split( X, Y, test_size=0.3, random_state=11)
    X_test, X_val, Y_test, Y_val = train_test_split( X_s, Y_s, test_size=0.5, random_state=11)

    print()
    print('Shape of train set: {}'.format(X_train.shape))
    print('Shape of test set: {}'.format(X_test.shape))
    print('Shape of validation set: {}'.format(X_val.shape))
    print('Shape of train labels set: {}'.format(Y_train.shape))
    print('Shape of test labels set: {}'.format(Y_test.shape))
    print('Shape of validation labels set: {}'.format(Y_val.shape))

    return labels, X_train, X_s, Y_train, Y_s, X_test, X_val, Y_test, Y_val
