# NRC

## Overview
Category: web  
Points: ????  
Author: goose  

## Challenge
> Find the flag :)  
[http://no-right-click.hsc.tf/](http://no-right-click.hsc.tf/)

## Approach
*Visit the website*.  
Click ctrl + shift + I and realize there's a suspicious `useless-file.css` linked to it:
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="useless-file.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&amp;display=swap" rel="stylesheet">

</head>
```
Visit [http://no-right-click.hsc.tf/useless-file.css](http://no-right-click.hsc.tf/useless-file.css) and the flag is at the bottom:
```css
body {
    text-align: center;
    font-size: 5rem;
    font-family: 'Abril Fatface', cursive;
}

.small {
    margin-top: 50vh;
    font-size: 0.5rem;
}

/* cause i disabled it in index.js */
/* no right click = n.r.c. */
/* flag{keyboard_shortcuts_or_taskbar} */
```

### Flag
`flag{keyboard_shortcuts_or_taskbar}`