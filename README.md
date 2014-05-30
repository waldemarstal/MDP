# MDP

## Getting Started

### Install On your local PC

#### Download Sources

use git

```bash
git clone git@github.com:waldest/MDP.git
```

Or download from [Here](https://github.com/waldest/MDP/zipball/master)

#### Install

If you are in directory with setup.py, use command:

```bash
python setup.py install
```


Now you can run my script using command:
```bash
mdp file_name
```

#### Structure of sample file:

    N M D A B G GB
    *  *  *  G 
    *  F  *  GB
    *  *  *  *

Where:
    N - size x
    M - size y
    D - value of discouting
    A - value of probability misses
    B - value of probability hits
    G - value of terminal state
    GB - value of bonus
    NS - value of normal state