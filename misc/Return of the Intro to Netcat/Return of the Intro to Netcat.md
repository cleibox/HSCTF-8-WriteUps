# Return of the Intro to Netcat

## Overview
Category: misc  
Points: ???  
Author: meow  

## Challenge
> hey, netcat seems fun! (with a twist)  
`nc return-of-the-intro-to-netcat.hsc.tf 1337`

## Approach
With any Linux system, connect to the shell:  
```shell
$ nc return-of-the-intro-to-netcat.hsc.tf 1337
== proof-of-work: enabled ==
please solve a pow first
You can run the solver with:
    python3 <(curl -sSL https://goo.gle/kctf-pow) solve s.AACF.AAC+aBANGchm8+XtkEe9ZuqN
===================

Solution?
```
Open a new shell:
```shell
$ python3 <(curl -sSL https://goo.gle/kctf-pow) solve s.AACF.AAC+aBANGchm8+XtkEe9ZuqN
Solution:
s.AAA0FzSBNS7swaTbp9LBj2bYUFINTHZSDYomrOCzKrpV6lkcheQ3dEbNJi12E3hVEbm9zvLy+Lig+G2hav09LdLPtfqN49pumlT9N/u8doAWy3zY2PZa1QX+GKx9gjy6tEyScsPuCu9MWJ+1qWy1rqzhmKVCP789kNx3RwzXd7+1E0WPlzCfp7Dxk5C+jw5lnipSNFoV8cnENWbPh9zD7PSP
```
Now we go back to the first shell instance and paste that in.
```shell
Solution? s.AAA0FzSBNS7swaTbp9LBj2bYUFINTHZSDYomrOCzKrpV6lkcheQ3dEbNJi12E3hVEbm9zvLy+Lig+G2hav09LdLPtfqN49pumlT9N/u8doAWy3zY2PZa1QX+GKx9gjy6tEyScsPuCu9MWJ+1qWy1rqzhmKVCP789kNx3RwzXd7+1E0WPlzCfp7Dxk5C+jw5lnipSNFoV8cnENWbPh9zD7PSP
Correct
You got it! Here's what you're looking for: flag{the_cat_says_meow}
```

### Flag
`flag{the_cat_says_meow}`