#calculates the entropy of a given set
import numpy as np

def get_entropy(df):
    """ Calculates the entropy of the df """

    labels, counts = np.unique(df[:,-1], return_counts = True) # array of labels (true-false, red-blue-green...) and array of number of occurance
    probability = counts / float(df.shape[0])
    entropy = -np.sum( probability * np.log2(probability))
    return entropy


def get_info_gain(df, partial_df_list):
    """ Calculates the information gain by splitting the dataframe into partial dataframes (partial_df_list)"""

    sum_entropy_times_prop = 0
    for par_df in partial_df_list:
        # the proportion of the number of elements of each partial dataframe
        # to the number of elements in the origing df times the entropy of each subset
        sum_entropy_times_prop += (par_df.shape[0]/df.shape[0]) * get_entropy(par_df)
    return get_entropy(df) - sum_entropy_times_prop



def split_positions(df,column):
    """ Calculates the positions where the df must be splited up"""

    unique, frequency = np.unique(df[:,column], return_counts = True) #returns unique values and their frequency
    split_positions = np.array([frequency[0]]) # array with only the first frequency
    for x in range(frequency.shape[0] - 2): # add frequency to current position to get split position
        new = split_positions[x] + frequency[ x+1 ]
        split_positions = np.append(split_positions, new)
    return split_positions



def split_up(df,col):
    """ Splits the dataframe into partial dataframes an saves them in a list"""
    df = df[df[:,col].argsort()] # sorts array by values in a particular column(col)
    return np.split(df, split_positions(df,col)) # split df at certain positions



def find_best_split(df, max_branching):
    """ Find the best column to split the df by their values in this column.

    If there is no good split whith an information gain
    the function returns the gain 0 and no best_column
    """
    best_gain = 0 # worst possible gain is 0
    best_column = None

    # Loop over all feature-columns minus the label column to find the best possible info_gain
    for column in range(df.shape[1] - 1):
        partial_df_list = split_up(df, column) # splits df in partial_df values of given column
        # calculate information gain of this split by this feature by evaluating the entropy of every resulting array
        gain = get_info_gain(df, partial_df_list)

        # overwrite old gain and best feature to split if the gain is higher and the df is split up in less than "max_branching" peaces
        if (gain > best_gain) and (len(partial_df_list) <= max_branching) :
            best_gain, best_column = gain, column

    return best_gain, best_column
