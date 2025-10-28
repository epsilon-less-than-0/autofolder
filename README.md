# autofolder
This is a SageMath package for generating the folding automaton of a given stratum of pseudo-Anosov homeomorphisms on the disk with n marked points, through elementary folding operations on trian tracks.


## Overview

This package provides tools for working with train tracks on the disk with n marked points. The main functionality allows users to:

- Construct and encode train tracks from user-specified geometric data
- Perform elementary folding operations at a cust (left-over-right or right-over-left)
- Build the associated folding automata, including standardizing braids, by systematically folding all cusps
- Analyze the resulting automaton structure


## Features

- **Train Track Construction**: Create a train track object by inputing number of marked points, unmarked points, singularity types, infinitesimal polygons, and graph structure. This can be done directly or by calling the train track constructor function.
- **Automated Elementary Folding**: Fold a train track at a cusp in either directions
- **Automaton Generation**: Build the automaton as a directed graph, with edges decorated by standardizing braids
- **Isomorphism Detection**: Identify when two train tracks are ambient isotopic
- **Transition Matrices**: Track how edges transform under folding operations
- **Standardization**: Maintain canonical forms using braid operations

## Installation


### If you just want to generate the folding automaton
1. Clone or download this repository
2. While in the directory, run the following:
   
```python
sage automaton.sage
```
The script will promt you to enter in data for your train track.

### If you want to use this as a SageMath package to use all features (In Development!)
1. Clone or download this repository
2. Open Sage in terminal
3. Execute the following:
4. 
```python
sage:  
```
## Example Input Session
### If you just want to generate the folding automaton
#### Input Requirements

The program will prompt you for the following information:

1. **Marked Points**: Number and singularity types of marked points
2. **Marked Polygons**: Vertices enclosing each marked point (counterclockwise)
3. **Side-Swapping Edges**: Edges that swap sides for each marked polygon
4. **Unmarked Singularities**: Number and types of interior singularities
5. **Unmarked Polygons**: Vertices for each unmarked singularity
6. **Boundary Information**: Singularity type of the boundary
7. **Graph Structure**: Underlying graph with vertex connections
8. **Cusp Information**: Cusps between real edges only

Suppose we would like to input the following train track on the disk with 4 marked points:
<img width="312" height="272" alt="image" src="https://github.com/user-attachments/assets/39bf43bf-430d-4ddd-9277-0b3e5a2b80c9" />


This is a train track with four one-pronged singularities at the five marked points, represented by the four monogons surrounding the marked points; and one four-pronged unmarked singularity, represented by the four-gon. There is one cusp marked c on the diagram.

We imagine the underlying graph of this train track to look like this:
<img width="500" height="397" alt="image" src="https://github.com/user-attachments/assets/0680a095-ad3e-4a9c-bd13-a41846e2db48" />



We would enter the following responses to the prompts of the script:
Enter the number of marked points: 5
List the singularity types of the marked points as a list, from left to right: [1,1,1,1]
Starting from left to right, consider the 1th marked point, which has the singularity type 1. 
In counterclockwise order, enter the vertices that enclose this marked point as a list: [0]
Enter the side-swapping edge for this marked polygon as a tuple: (0,0)
...


