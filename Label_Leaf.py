""" Class definition for a Leafs . """
import numpy as np

class Label_Leaf():
    """The Label_Leaf classifies data.

    It holds a reference to the value wich lead to this node and label wich ist most frequent in the remaining dataset.
    """

    def __init__(self, df, answer_value):
        self.answer_value = answer_value #data - which value leads to this node
        unique, frequency = np.unique(df[:,-1], return_counts = True)
        self.label = unique[np.argmax(frequency)] # returns most frequent label - in case of multiple maxima the first is returned.


    def get_answer(self):
        return self.answer_value



    def get_label(self):
        return self.label
