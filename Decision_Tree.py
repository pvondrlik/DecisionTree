import numpy as np
import split_data as splt
import random

from Decision_Node import Decision_Node
from Label_Leaf import Label_Leaf

class Decision_Tree:
    """ Class definition for a DecisionTree with Nodes and Leafs. """

    def __init__(self, max_depth = 32, max_branching=4 ): # why these default values?
        self.depth = max_depth
        self.max_branching = max_branching


    def train(self, df):
        """ Build the decision tree by calling the recursive _build.tree function.

        The root saves the first Decision_Node and can be used by other functions of the class.
        """
        self.root = self._build_tree(df, self.depth)


    def _build_tree(self, df, depth, answer_value = None):
        """ Recursively build tree based on the training data and the best current split option.
        """

        # if max_depth is reached or if there are too few datarows to split the data -> add a Label_Leaf
        if (depth <= 0 or df.shape[0] < 2):
            return Label_Leaf(df, answer_value)

        # calculate the best possible split of the dataframe and the corresponding information gain
        gain, question_col = splt.find_best_split(df, self.max_branching)

        # if there is no information gain or the remaining datarows have already the same label -> add a Label_Leaf
        if (gain == 0 or np.unique(df[:,-1]).shape[0] <= 1):
            return Label_Leaf(df, answer_value)
        else:
            # partition in more dataframes, dependent on the value in the question column
            partial_df_list = splt.split_up(df, question_col)
            # recursively build tree for every partial_df/branch
            children_list = []
            for partial_df in partial_df_list:
                children_list.append(self._build_tree(partial_df, depth-1, partial_df[0, question_col]))
            return Decision_Node(answer_value, question_col, children_list)


    def predict(self, row):
        """ Returns prediction for a datarow by calling '_classify' """
        return self._classify(row, self.root)


    def _classify(self, row, node):
        """ Recursively goes down a tree branch dependent on datarow-values,
        until it reaches a Label_Leaf to label the data """

        # base case: next Node is Leaf
        if isinstance(node, Label_Leaf):
            return node.get_label()

        # recursive case: search branch corresponding to value
        for child in node.get_children():
            # search trough children and compare the answer value to the given question
            if child.get_answer() == row[node.get_question()]:
                return self._classify(row, child)
            # if value is not in test data -> choose random tree
            else:
                return self._classify(row, random.choice(node.get_children()))


    def test_prediction(self, test_df):
        """ Tests how good the prediction is by predicting
        all rows of the test-data and comparing the prediction with the correct label"""

        correct_pred = 0

        for row in range(test_df.shape[0]):
            if self.predict(test_df[row,:]) == test_df[row,-1]: # predicted label == correct label
                correct_pred +=1
        return correct_pred, test_df.shape[0] # test_df.shape[0] = totsl prediczions


    def _print_tree(self, node, indx, search_label, questions, answers):
        """ Print which properties lead to wich label by iterating through all possible branches"""

        if isinstance(node, Label_Leaf):
            if node.get_label() == search_label:
                for question, answer in zip(questions, answers):
                     print("If:", indx[question], "is:" ,answer)
                print("then ",indx[-1],"is", node.get_label(), "\n\n")
            pass

        else:
            questions.append(node.get_question())

            for child in node.get_children():
                answers.append(child.get_answer())
                self._print_tree(child, indx, search_label, questions, answers)
                answers.pop() #
            questions.pop()
            pass


    def print(self, indx, search_label):
        print("\n\n\n","Datarows with the following values are labeld as: ", search_label, "\n")
        questions = []
        answers = []
        return self._print_tree(self.root, indx, search_label, questions, answers)
