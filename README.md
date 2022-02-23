# Taylor series

Calculates value of taylor series for 
specified function (
![\sqrt{1-2x+4x^2}](https://latex.codecogs.com/svg.latex?\sqrt{1-2x+4x^2})
) in provided point

Project contains three modules:
 - main.py
 - visualizer.py
 - taylor.py
 
### main.py

Using main.py it prints useful information
about taylor series for provided function,
including values for given argument for 
1, 5, 10, 25 and 50 additions and also
values for numbers of additions where 
difference less than 10<sup>-1</sup>, 
10<sup>-3</sup> and 10<sup>-6</sup>

```shell
Usage: $ python main.py argument
```

Where argument is the point to display
info about

```shell
$ python main.py 0.51
Num|         Taylor         |         Actual         |          Diff          
------------------------------------------------------------------------------
  1|      0.8660254037844386|      1.0101485039339513|     0.14412310014951268
  2|      1.0221409165733135|      1.0101485039339513|    0.011992412639362238
  4|       1.010606275423177|      1.0101485039339513|   0.0004577714892257667
  5|      1.0100347015591318|      1.0101485039339513|  0.00011380237481950495
  9|      1.0101477589126155|      1.0101485039339513|   7.450213357351743e-07
 10|      1.0101487313587578|      1.0101485039339513|  2.2742480654258657e-07
 25|      1.0101485039339388|      1.0101485039339513|  1.2434497875801753e-14
 50|      1.0101485039339515|      1.0101485039339513|   2.220446049250313e-16
```

Data about 1, 5, 10, 25 and 50 additions
displayed and also data about 2, 4 and 9
where difference less than 10<sup>-1</sup>,
10<sup>-3</sup> and 10<sup>-6</sup>

### taylor.py

Calculates the value of taylor 
series with _num_ additions at
_argument_

``` shell
Usage: $ python taylor.py <argument> <num>
```

Prints the information about the value 
of taylor series, actual value and the 
difference between that two

``` shell
$ python taylor.py 0.45 100
Num|         Taylor         |         Actual         |          Diff          
100|      0.9539392014169454|      0.9539392014169457|   2.220446049250313e-16
```

### visualizer.py

Visualizes the approximation of taylor
series using manim community engine, so
it is required to 
[install](https://docs.manim.community/en/stable/installation.html) 
it locally before using it.
```shell
Usage: $ python visualizer.py [-q quality] [-f format] num
```
Where:
 - quality is one of the next:
   - h (1080p60, default)
   - m (720p30)
   - l (480p15)
 - format is one of the next:
   - gif
   - mp4
   - mov
   - webm
 - num is number of additions to compute

As a result you will receive a path to
a folder where file with an animation saved

```shell
python visualizer.py -qh -f gif 50
```
![visualizer example](visualization.gif)

In animation with orange color displayed 
a given function, with yellow next
addition and with blue the overall 
taylor series function
