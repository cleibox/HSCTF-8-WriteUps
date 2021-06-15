# Problem Name

## Overview
Category: misc  
Points: ???  
Author: wooshi  

## Challenge
> There are at least two types of randomizers in Java, one that is purely random and one that is seeded (that is pseudorandom). Please fix this code to output the correct flag (note the flag format, and a sample has been provided).

[SeededRandomizer.java](./SeededRandomizer.java)

## Approach
After reading the code, I realized the only part of the code that needs to be changed is inside the main. The display() method is there to connect the characters into the flag. The sample() method shows you the gist of how to set up a random seed. 

Also in the sample() method, I noticed this line of code:
```java
int n = rand.nextInt(128) + b[i];
```
rand.nextInt(128) outputs a number between 0-128 and it's set as 128 because that's the maximum ASCII number. 
That line is the way it is because the line right after converts the integer n into a character (which will become part of the flag later). 

So all I need to do is copy that format in the main. 
```java
Random rand = new Random(1); // I set the seed as 1 as the placeholder
int n = (int)(rand.nextInt(128)) + c[i];
```

Well now all I have to do is find the seed. Thankfully, the author is feeling very generous and told us the range of the seed is between 0 and 1000 exclusive.

Unfortunately, my coding knowledge is (severly) lacking and so I decided to take upon the act of brute forcing (hey it works).

I set up a while loop that runs through the possible seed values which is between 0 to 1000 exclusive. In addition, I set up some if statements to only print out flags with characters containing '{' and/or '}' which allows me to see all possible flags (come on ... I'm not looking at 999 "flags").

This is my main. I did not touch the other two methods.
```java
public static void main(String[] args) {
    // sample();
    // Instantiate another seeded randomizer below (seed is integer between 0 and 1000, exclusive):
    char[] flag = new char[33]; // array of characters
    // array of integers
    int[] c = {13, 35, 15, -18, 88, 68, -72, -51, 73, -10, 63, 
            1, 35, -47, 6, -18, 10, 20, -31, 100, -48, 33, -12, 
            13, -24, 11, 20, -16, -10, -76, -63, -18, 118};
    
    int j = 1;
    boolean bracketPresent1 = false;
    boolean bracketPresent2 = false;
    while (j < 1000){
        System.out.println("j is " + j);
        Random rand = new Random(j);
        
        for (int i = 0; i < flag.length; i++) {
            int n = (int)(rand.nextInt(128)) + c[i];
            flag[i] = (char)n;
            
            if (flag[i] == '{'){
                bracketPresent1 = true;
            }
            if (flag[i] == '}'){
                bracketPresent2 = true;
            }
        }
        if (bracketPresent1 == true && bracketPresent2 == true){
            display(flag);
            bracketPresent1 = false;
            bracketPresent2 = false;
        }
        j++;
    }
}
```

Now all you need to do is scroll through the outputs and look for one that actually looks like a flag. The winner seed is 863.

### Flag
`flag{s33d3d_r4nd0m1z3rs_4r3_c00l}`