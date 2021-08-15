# DecisionTree
##### Implementation of a decision tree build with ID3-Algorithm and visualization of correctly classified data.

1. Introduction
2. Requirements
3. scope and functionalities
4. Troubleshootings
5. Authors and acknowledge
6. Sources

### 1. Introduction
In this Project I implemented an ID3 algorithm to see how accurately the resulting decision tree
labels the data correctly compared to a randomly chosen label.
My motivation was to improve my understanding of this categorization method.

In this project one can train a Decision tree with data of csv files and
can see the percentage of cases in which the decision tree finds the right label

### What is the ID3
The ID3 algorithm creates a Decision tree by analyzing a trainingset.
-> What is the ID3: https://en.wikipedia.org/wiki/ID3_algorithm

###functionalities
an additional feature for more trasparency is the possibilityto print every possible combination of values that lead to a certain label  "Decision_Tree.print_t". 

![picture/plot.png](picture/plot.png)

![picture/print.png](picture/print.png)

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



###Problems with data and (not optimal) solutions
Some Problems occur when working with DecisionTrees.
I implemented solutions for those which might be suboptimal and other solutions
would increase the accuracy of the Deccision tree.
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
