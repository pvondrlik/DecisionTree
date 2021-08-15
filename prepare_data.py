"helper fuctions to prepare the data"
import numpy as np


def digits_to_scope(arr, number_of_scopes):
    """
    Convert numerical data to data scopes, to make it easier to build a tree from it.

    To calculate the scopes we calculate the min/ max
    and divide the range by the number of scopes we want to assign to our data.

    The scope is represented in the new array only by the left bounderie.

    We replace the value by the left bounderie of the scope (min + x*scope)
    if the value is greater than the left bounderie (min + x*scope) and smaler than the right (min + (x+1) *scope)
    """
    try: # true if the column can be coverted into integer array
        arr = arr.astype(np.uint8)# evtl float

        min = np.min(arr)
        max = np.max(arr)
        scope = (max - min)/ (number_of_scopes)

        for x in range(number_of_scopes - 1):
            arr[((arr > (min + x*scope)) & (arr < (min + (x+1)*scope)))] = min + x*scope # replace the values if they are in the scope
        arr[arr > (min + (number_of_scopes-1)*scope)] = min + (number_of_scopes-1)*scope # replace all higher values by the highest scope
        return arr #return modified array
    except:
        return arr


def reduce_amount_of_values(df, max_branching):
    """calls digits_to_scope() for each column where the amount of unique values
     is higher than the prefered amount of children(max_branching) per Node

    """
    for col in range(df.shape[1]): # for each column
        labels = np.unique(df[:, col])

        if (labels.shape[0] > max_branching):
            df[:,col] = digits_to_scope(df[:, col], max_branching)
    return df

def seperate_indexrow(df):
    index, df = df[0, :], df[1:, :]
    return index, df

def split_test_training_set(df,ratio_training_test = 0.75):# split data into test and traing set with optional value
    x = int(df.shape[0]*ratio_training_test) # calculates where to split the data
    np.random.shuffle(df) # shuffle data
    training, test = df[:x,:], df[x:,:]# split data
    return training, test

#executes the above
def prepare(df, ratio_training_test = 0.75, max_branching = 20, has_col_index = True):
    #seperate indexrow if data has index row or create index
    if has_col_index:
        indx, df = seperate_indexrow(df)
    else:
        indx = np.array(range(df.shape[0])) # for i in range(0,5)
    reduce_amount_of_values(df, max_branching) #
    training_df, test_df = split_test_training_set(df, ratio_training_test)
    return indx, training_df, test_df
