# not-really-math

## Overview
Category: algo  
Points: ???  
Author: AC  

## Challenge
> Have a warmup algo challenge.  
`nc not-really-math.hsc.tf 1337`

[not-really-math.pdf](./not-really-math.pdf)

## Approach
I have no clue why [`script.py`](./script.py) breaks (well I mean it's got something to do with how the input is being parsed but not sure what specifically is failing) and maybe I'll fix that after this CTF.

### Code
The `not_math` function in [`script.py`](./script.py) takes a string then splits it by "m". These are all the components it neesd to multiply. It loops through each component of that string when split by "m" then either converts it to an integer or splits by "a" and adds them all up.

### Solve
If the script worked then it would have been fine to just run the script :(. Since the script doesn't work I set two instances of the shell running, one of them was to interact with the connection `nc not-really-math.hsc.tf 1337` and the other was to run the `not_math` function.

### Flag
`flag{yknow_wh4t_3ls3_is_n0t_real1y_math?_c00l_m4th_games.com}`