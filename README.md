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

### Option 1: Local Installation (Recommended)

1. Clone or download this repository
2. Place the package directory in your working directory or add it to your Python path
3. In SageMath, import the module:

```python
# If in the same directory
import sys
sys.path.append('.')
from automaton import *

# Or if installed as a package
from train_track_autofolder.automaton import *
```

### Option 2: Direct Import

Place all `.py` files in your SageMath working directory and import:

```python
load('automaton.py')
```

## Usage

### Basic Usage

The main entry point is the `automaton.py` script. When run, it will interactively prompt you to construct a train track:

```python
sage: exec(open('automaton.py').read())
```

### Input Requirements

The program will prompt you for the following information:

1. **Marked Points**: Number and singularity types of marked points
2. **Marked Polygons**: Vertices enclosing each marked point (counterclockwise)
3. **Side-Swapping Edges**: Edges that swap sides for each marked polygon
4. **Unmarked Singularities**: Number and types of interior singularities
5. **Unmarked Polygons**: Vertices for each unmarked singularity
6. **Boundary Information**: Singularity type of the boundary
7. **Graph Structure**: Underlying graph with vertex connections
8. **Cusp Information**: Cusps between real edges only

### Example Input Session


Suppose we would like to input the following train track on the disk with 4 marked points:
<img width="1196" height="1000" alt="image" src="https://github.com/user-attachments/assets/05b37217-cac9-4088-a224-337effe717f3" />

This is a train track with four one-pronged singularities at the five marked points, represented by the four monogons surrounding the marked points; and one four-pronged unmarked singularity, represented by the four-gon. There is one cusp marked c on the diagram.

We imagine the underlying graph of this train track to look like this:
![image alt](https://github.com/epsilon-less-than-0/autofolder/blob/fc52264d1a33568727d1836c8a25e40196fed02c/signal-2025-10-23-110047_002.png.png)


We would enter the following responses to the prompts of the script:
Enter the number of marked points: 5
List the singularity types of the marked points as a list, from left to right: [1,1,1,1]
Starting from left to right, consider the 1th marked point, which has the singularity type 1. 
In counterclockwise order, enter the vertices that enclose this marked point as a list: [0]
Enter the side-swapping edge for this marked polygon as a tuple: (0,0)
...
```

<!-- ### Output
The program generates:
- `AutomatonDict`: Dictionary mapping indices to train track objects
...
...
## Acknowledgments
Based on train track theory and surface topology research. Thanks to contributors and the SageMath community. -->

