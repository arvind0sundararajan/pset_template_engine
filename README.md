# Practice Problem Tracker

This project contains code to organize practice problems in any subject, from any source.

Functionality is as follows:

* User enters a command to add a new question.
* Program creates the template files necessary: .tex files for problem body and solution, and metadata file with question information. the title of these files is the question id, which is a simple counter of the ith problem added.

## Mechanics

An organizational scheme for practice problems.

* The template files
	* fill in 

* `create_problem.py`: creates source file for a problem
	*	inputs: a `problem_id` for the problem (e.g. `126_6_1` for problem 1 on HW 6 of EECS 126)
	*	outputs: 
		*	a simple `.tex` file `problem_id.tex`; holds the title (if it exists), the problem body, and the solution.

* `create_pset.py`: creates a problem set from arbitrary sources.
	*	inputs: 
		* the title of the problem set `pset_title`
		* a list of problem source file paths to include in the problem set
	*	outputs: renders `build/pset_title.tex` with each problem bound	

## Motivation

Consider a bipartite graph with the first set containing practice problems, and the second set containing relevant concepts. There is an undirected edge between a problem and a concept if that concept is relevant to the problem. This program aims to make it easy to review concepts by succinctly going over the problems which cover that concept.


Also to make it easy to make problem sets for classes.