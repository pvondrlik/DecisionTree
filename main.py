import numpy as np
import math
import matplotlib.pyplot as plt


from prepare_data import prepare
from Decision_Tree import Decision_Tree

"""This library offers different possibilities :
    you can:
    first you must trai jthe tree


    -> you can test with labeld data, how much data the Decision tree labels correct
    -> you can print the Decision which can lead to labels
"""
#train and test
def trial(df, ratio_training_test, max_branching, max_depth):
    #data preparation
    indx, training_df, test_df = prepare(df, ratio_training_test, max_branching)
    tree = Decision_Tree(max_depth) # create a tree
    tree.train(training_df) # train the tree with data
    correct_pred, total_pred = tree.test_prediction(test_df) # test accuracy of Decision tree

    return tree, correct_pred, total_pred

# accuracy to compare with tree
def accuracy_random_labeling(df):
    labels = np.unique(df[:,-1]) # get the number of possible labels
    return 1/labels.shape[0]


def calculate_mean_std(df, ratio_training_test, max_branching, max_depth, trials):
    #runs the ID3 algorithm various times(trials) and calculates std and mean
    correct_arr = np.array([])

     # run trials and save the number of correct predicrion in an array
    for i in range(trials):
        tree, correct_pred, total_pred = trial(df, ratio_training_test, max_branching, max_depth)
        correct_arr = np.append(correct_arr, correct_pred)

    return correct_arr.mean(), total_pred, correct_arr.std()


def compare_accuracy_bydifferent_ratio(df, max_branching, max_depth, trials, ratio_list):

    baseline = accuracy_random_labeling(df) #
    means, totals, stds = np.array([[],[],[]]) #

    for ratio_training_test in ratio_list:
        mean, total, std = calculate_mean_std(df, ratio_training_test,  max_branching, max_depth,  trials)
        means = np.append(means,mean)
        totals = np.append(totals,total)
        stds = np.append(stds,std)
    return means, totals, stds, ratio_list, baseline



def plotting(x, y1, y2,  std, baseline):
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex = True)
    fig.suptitle("Accuracy of Decision Tree")

    ax[0].set(
    	title = "Absolut ",
    	ylabel = "Prediction",
        xlim=[0, 1],
        xticks=(x)
    )
    ax[0].bar(x, y2, width = 0.05, bottom=0, align = "center", color="red", edgecolor="black",
             label = "TotalPred")
    ax[0].bar(x, y1, width = 0.05, align = "center", color="green", edgecolor="black",
             label = "CorrectPred")
    ax[0].errorbar(x, y1, std, linestyle='None', color ="black")
    ax[0].legend(loc="upper right")


    accuracy = y1/y2  # realativ accuracy: correct prediction / total predictions
    relative_std = std/y2

    ax[1].set(
    	title = "Relative ",
    	ylabel = "CorrectPred/TotalPred",
    	xlabel = "ratio of training data",
        xlim=[0, 1],
        ylim=[0, 1],
        xticks=(x)

    )
    ax[1].plot(x, accuracy, color="green", label = "CorrectPred/totalPred")
    ax[1].errorbar(x, accuracy, relative_std, linestyle='None', color ="black")
    ax[1].axhline(y=baseline, color="blue", linewidth=2, label = "RandomPred" )
    ax[1].legend(loc="upper right")
    plt.show()


def main(df, print_label=None, has_col_index=True, max_branching=5, max_depth = 4, trials=4, ratio_list=[.1,.2,.3,.4,.5,.6,.7,.8,.9 ]):

    # print every possible combination of values that lead to a certain label = print_tree)
    if print_label != None:
        indx, training_df, test_df = prepare(df, max_branching, 0.80, has_col_index)
        tree = Decision_Tree(max_depth)
        tree.train(training_df)
        tree.print(indx, print_label)

    # train decision trees with data and plot how often the tree finds the right label
    correct, total, stds, ratio_list, baseline = compare_accuracy_bydifferent_ratio(df, max_branching, max_depth,trials, ratio_list)
    plotting(ratio_list, correct, total, stds, baseline)



""""
In this part you can change values. For more information have a look into the README.

#examples:
data = "Data/drug200.csv" source: https://www.kaggle.com/ibrahimbahbah/drug200
data = "Data/student-mat.csv"  source: https://www.kaggle.com/uciml/student-alcohol-consumption

#main(df, "drugC")
#main(df, max_branching=2, max_depth = 10, trials=4, ratio_list=[.8])

"""


if __name__ == "__main__":
    data = "Data/drug200.csv"
    df = np.loadtxt(data, dtype=str, delimiter=',')
    main(df, "drugC")
    pass
