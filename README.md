# ML_Implementations
This is a basic program (in progress) that will perform a user's choice among several ML algorithms, implemented mostly from scratch.  Basic diagnostics, such as accuracy, confusions matrices, and in certain circumstances, graphical results will be displayable.

## Interface
The program will initially be command line based.  Future work, once a majority of the algorithms I want to implement are up, include providing a basic GUI interface.

## Dataset Inferrence / Prep
(In progress) The program will read in data into a pandas df and then perform basic inferrence on the datatypes and or prepare them for use in the algorithms (i.e. for certain algorithms it will scale numeric variables).  It will also provide a basic text interface for making changes to the dataset prior to running algorithms.

## Naive Bayes
This is a basic NB implementation.  Currently, only implemented for categorical variables, after datatype inference (to identify numeric variables) is done, I will add a basic Gaussian model for estimating probability of numerics.

## K-Nearest Neighbors
Currently implemented for categorical variables, distance for numeric variables will use standard Euclidean distance.

## SVM
To be implemented

## Decision Tree / Forest
To be implemented

## Regression / MV Regression
To be implemented

## Neural Network
To be implemented

## K-Means Clustering
To be implemented
