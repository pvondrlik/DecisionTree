# DecisionTree
##### Implementation of a decision tree build with ID3-Algorithm and visualization of correctly classified data.

1. Introduction
2. Requirements
3. scope and functionalities
4. Troubleshootings
5. Authors and acknowledge
6. Sources

### 1. Introduction
In this Project I implemented an ID3 algorithm to train a decision tree.
see how accurately the resulting decision tree
labels the data correctly compared to a randomly chosen label.

My motivation was to improve my understanding of this categorization method
and to understand how to manipulate the training of a decision tree to increase the accuracy.

In this project one can train a Decision tree with data of csv files and
can see the percentage of cases in which the decision tree finds the right label

### Structure

The implementation is structured in a main document that contains the main function
and calls a function to calculate the mean and standart deviation of

### What is the ID3
The ID3 algorithm creates a Decision tree by analyzing a trainingset.
-> What is the ID3: https://en.wikipedia.org/wiki/ID3_algorithm

### Functionalities

You can test the implementation by just using the commands `python test_decicionTree.py` and see how it works by default.

##### Plot the number of correct prediction


![picture/plot.png](picture/plot.png)


#### Change values
You can change values in the test_decicionTree.py document in the main() function. Changing the first have a look at the Documentation of main.
You can also try to use your own data but (have a look at the Data requirenments in the Imput format section).


#### Change values
You can change values to manipulate how the tree is trained
- max_branching()
- max_depth()
- ratio_list ()

Or how to compare the data
- ratio_list

-> idea: possibility to compare data by different max_branching()/max_depth()

ratio_list
#### Documentation of main:
main(df, print_label=None, has_col_index=True, max_branching=5, max_depth =4 ;trials=4, ratio_list=[.1,.2,.3,.4,.5,.6,.7,.8,.9 ])

Parameters  df : 2-dimensional array
                Used to train and test the decision tree

            print_label : string
                The label for which all possible value combination should be printed in the terminal.
                Otherwise nothing is printed

            has_col_index: bool
                If False, a numerical column index is added to the data-frame (only necessary to  apply "Decision_Tree.print_tree")

            max_branching: int
                Influences the training of the decision tree.
                Limits the branching of the tree, i.e. with a factor of 5, each node can have a maximum of 5 children.

            max_depth: int
              Influences the training of the decision tree.
              Limits the depth of the tree, so after a certain depth the label is calculated
              by the remaining data without a further split.

            trials: int
                Determines from how many trained and tested trees the value/mean and the standard deviation
                per type (in this version only ratio of testing and training data-ratio) is determined.

                The default value is low to reduce the runtime during trying out new features and demonstration.

            ratio_list: list
                 Influences the training of the decision tree.
                 A list of the ratio between training- and testing set.
                 For each value the program runs some trials and calculates the mean and standard deviation





##### Print tree
An additional feature for more trasparency is the possibility to print every possible combination of values that lead to a certain label  "Decision_Tree.print_t".
This allows to understand why certain data is labeld how?

![picture/print.png](picture/print.png)



""""

###input format:

1) data-set with N-1 first data as features and the last column as Labels
2) kwargs to specify the training and evaluation properties
      -

      ##Data requirenments and Problems
      The Data for the analysis of the prediction accuracy need to be labeld,
      The label must be in the last column -> change the
      The Data have no Index for the Columns -> no Problem, "prepare_data.prepare()" takes care of this issue



### more ideas
- which patrameter should be excluded to get the best prediction?
- possibility to exclude some fetures and to compare
- compare different max_depth or max_branching
- calculate maximal accuracy

### requirenments

Before you start, you have all the packages listed in requirements.txt (e.g. with pip install -r requirements.txt).

you can run, if you are asked to *run* a command like

    $ pip install -r requirements.txt

or install them individually

it means that you should type `run this command` in the terminal and press <kbd>Enter</kbd>.

You can test the implementation by just using the commands `python test_decicionTree.py` and see how it works by deafault
or change some values in `test_decisionTree´ before runing it


###Problems with data and (not optimal) solutions
Some Problems occur when working with DecisionTrees.
I implemented solutions for those which might be suboptimal and other solutions
would increase the accuracy of the Decision tree.
However, it is not the focus of this project to find those:

- Test-datarow has value which was not part of the training datarow
->assume data would have random value of values given in the trainingset (Decision_Node._classify())

- Training data has equal distribution of data with different Labels
->choose the first one (Label_Leaf.__init__)

- Data-column has to many different values:
  if they are numerical:
  -> create scopes
   else:
  -> just do not allow a split by the values of this column
