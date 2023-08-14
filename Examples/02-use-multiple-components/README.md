#using multiple components in `INUI`



```python
from inui.elements import (
    Body,
    Head,
    Html,
    Title,
    Div,
    Meta,
    Comment,
    Strong,
    Hr,
    A
)

INUI_IS_THE_BEST = Div((
    Strong(
        (
            A('INUI', href='https://github.com/MohammadrezaAmani/INUI'), 'IS THE BEST'), style="color:red",
    ),
    Hr()
))

h = Html(data=(
    Comment("this is black door =`) "),
    Head(
        (
            Title("INUI"),
            Meta(charset="utf-8"),
            Meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0",
            ),
        )
    ),
    Body(
        (

            [INUI_IS_THE_BEST for i in range(10)]
        ),
    ),
), style="background:#000000;")

print(h)
```

### output:

```html

<html style="background:#000000;">
 <!-- >
this is black door =`) 
 -->
 <head>
  <title>
   INUI
  </title>
  <meta charset="utf-8"/>
  <meta charset="utf-8" content="width=device-width, initial-scale=1.0" name="viewport"/>
 </head>
 <body>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
 </body>
</html>

```


<html style="background:#000000;">
 <!-- >
this is black door =`) 
 -->
 <head>
  <title>
   INUI
  </title>
  <meta charset="utf-8"/>
  <meta charset="utf-8" content="width=device-width, initial-scale=1.0" name="viewport"/>
 </head>
 <body>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
  <div>
   <strong style="color:red">
    <a href="https://github.com/MohammadrezaAmani/INUI">
     INUI
    </a>
    IS THE BEST
   </strong>
   <hr/>
  </div>
 </body>
</html>
