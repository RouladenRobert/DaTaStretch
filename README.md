# DaTaStretch
This project introduces a new framework for pipeline-operations.
It provides an easy way to create arbitrary pipelines and is capable to run them in parallel.
Tasks executed by the pipeline are fully specified by the developer, furthermore the dependencies among the tasks
must be specified. DaTaStretch then finds the best way to parallelize the execution of those tasks with respect to the
defined dependencies. Therefore it builds a _task graph_ and an _execution graph_ which represent the order of 
task-executions. Both graphs can be plotted by DaTaStretch for debugging-purposes.

## How to setup
The setup can be done as follows:
1. Execute 'pip install datastretch'
2. Import 'datastretch'
3. Define your tasks by creating classes inheriting from the Task-class
4. Define dependencies between your tasks.
5. Create a Pipeline-object
6. Create the needed stages and add your tasks there
7. Add the stages to the pipeline and run it!

# Libraries used
- [networkx](https://networkx.github.io/documentation/stable/index.html)
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [matplotlib](https://matplotlib.org/)

