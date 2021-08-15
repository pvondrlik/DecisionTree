import numpy as np

class Decision_Node():
    """A decision node ask the questions about the next feature.

    It holds a reference to the different child Nodes, the value wich lead to this node and the next feature to ask about
    """

    def __init__(self, answer_value, question_col, children_list):
        self.answer_value = answer_value #data - which value leads to this node
        self.question_col = question_col # data - which is the next column to look at
        self.children_list = children_list # children - which Nodes contain the answer to this question


    def get_answer(self):
        return self.answer_value


    def get_question(self):
        return self.question_col


    def get_children(self):
        return self.children_list
