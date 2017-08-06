[topopt]:http://www.topopt.dtu.dk
[simp]: http://www.topopt.dtu.dk/files/matlab.pdf
[topy]:https://github.com/williamhunter/topy
[top4040]:https://storage.googleapis.com/top4040/TOP4040.zip

![](./src/top_dataset_pics.png)
# TOP: Topology Optimization Process

[**Download (3.08 Gb)**][top4040]

The dataset of topology optimization process. It contains the precise solutions of 10,000 randomly stated problems. Each object is a tensor of shape `(100, 40, 40)`: 100 iterations, `40×40` grid. 

## How it is generated
We used [ToPy][topy] for the generation of the current dataset. It is based on [SIMP][simp] approach. 

The constraints and loads for each of the problem are chosen in the following way:

- The number of nodes with fixed ***x*** and ***y*** translations and the number of loads are sampled from the Poisson distribution:

```
Nx ∼ P(λ=2)
Ny ∼ P(λ=1)
NL ∼ P(λ=1)
```

- The nodes for each of the above described constraints are sampled from the distribution defined on the grid. The probability to choose the boundary node is 100 times higher than that for inner node.
<img src="./src/probs.png" width=30%>

- The load values are chosen as **-1**
- The volume fraction is sampled from the normal distribution `N(μ=0.5,σ=0.1)`

You can generate your own dataset just by using scripts from `code/` folder. `sampler.py` defines all the required distributions, and `generate_data.py` is just a convenient wrapper for ***ToPy***. Install [ToPy][ToPy] and run:

```
python code/generate_data.py --dir DIR_TO_SAVE --num NUMBER_OF_SAMPLES
```

## How to use
Each tensor is stored in compressed format `.npz`. It could be extracted easily with ***numpy***:

```python
import numpy as np

data = np.load(PATH_TO_FILE)['arr_0']
```

We recommend to use horizontal and vertical flips as well as `90°` rotation to augment the initial dataset. These operations allow one to get the dataset of 80,000 objects.

## What TopOpt is
If you want to learn more about topology optimization you can visit the [website][topopt] of TopOpt Research Group from DTU. 
