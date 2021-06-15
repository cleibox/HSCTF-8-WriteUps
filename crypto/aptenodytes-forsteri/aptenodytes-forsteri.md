# aptenodytes-forsteri

## Overview
Category: crypto  
Points: ???  
Author: AC  

## Challenge
> Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.

[output.txt](./output.txt) [aptenodytes-forsteri.py](./aptenodytes-forsteri.py)

## Approach
if we take a look at line 6 of [`aptenodytes-forsteri.py`](./aptenodytes-forsteri.py) we'll see how each character is encoded.
```python
encoded+=letters[(letters.index(character)+18)%26] #encode each character
```
It's simply just a [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) with a shift of 18. If we change `+18` to `-18` and run it on `output.txt` we can reverse it to get the flag:
```python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = open('output.txt','r').read()
decoded = ""
for character in encoded:
    decoded+=letters[(letters.index(character)-18)%26] #decode each character
print("flag{" + decoded + "}") # sad no f strings :(

```
The code is basically the same lol.

### Flag
`flag{QWERTYUIOP}`