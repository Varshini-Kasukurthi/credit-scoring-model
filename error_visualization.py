import numpy
import matplotlib.pyplot as plot

import itertools 

def error_visualize(error_matrix, classes, normalize=False, title='Error matrix', cmap=plot.cm.Blues):
    ####
    # This function prints and plots the confusion matrix.
    # Normalization can be applied by setting `normalize=True`.
    #####
    if normalize:
        error_matrix = error_matrix.astype('float') / error_matrix.sum(axis=1)[:, numpy.newaxis]
        print("Normalized Error matrix")
    else:
        print('Error matrix, without normalization')

    print(error_matrix)

    plot.imshow(error_matrix, interpolation='nearest', cmap=cmap)
    plot.title(title)
    plot.colorbar()
    tick_marks = numpy.arange(len(classes))
    plot.xticks(tick_marks, classes, rotation=45)
    plot.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = error_matrix.max() / 2.
    for i, j in itertools.product(range(error_matrix.shape[0]), range(error_matrix.shape[1])):
        plot.text(j, i, format(error_matrix[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if error_matrix[i, j] > thresh else "black")

    plot.tight_layout()
    plot.ylabel('The True label')
    plot.xlabel('The Predicted label')







