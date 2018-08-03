# Planning Visualisation - Visualsition File Generator

This python program takes the domain PDDL, problem PDDL and the animation profile to generate the Visualisation file for the Visualisor program.

## How to run the program
In the terminal, with python3 installed, run the following command and it will generate a file called visualisation.json in the root folder

```
python main.py [dommainfile] [problemfile] [animationprofile]

eg. python main.py domain_blocks.pddl problems/bw01.pdd animation_profile.json
```

## Versioning

1.0

## Limitations

### Planning domain API
The planning domain API could only solve the block problems that the total number of block is below 25, otherwise the API has high chance return timeout error

### Parser:
Current parser we wrote is not general, it works well with the domain file and problem file we provided which use the following predicates:
* (on ?x ?y)
* (on-table ?x)
* (clear ?x)
* (arm-free)
* (holding ?x)

And also all the text must be lowercases. We have provided an converter for the block problem PDDL.
```
line=re.sub(r"\bontable\b","on-table",line)
```

The code above will replace the text "ontable" to "on-table" .
You can add more lines like this to convert your predicates to the predicates we accept.

We will update and make our parse more genearl in the future sprint。

### Animation Profile
In this sprint the Animation Profile is create by ourself, it is written in Json, and the structure can not be changed.
In the next sprint we will create an UI for user to define the animation profile.

### Visualisation File Generator
The visualisation file generator is only work for the block domain at the moment. And it accept three kinds of objects:
* Block
* Claw
* Board

#### Block
The distributex function is used to given the x postion of the block(for predicate on-table),and currently it didn't remove
the block from space if a block is removed from table. 
For example: Given space of 4 slots => [a,b,c,4], if b is removed and e is distribute on the table, e will get the slot 4, 
because our algorithm didn't take b away. And it may cause the screen unnecessary wide.

This is not a bug, but a design decision. We will try to improve this algorithum in the next sprint.

#### Claw
The position of Claw is fixed which is defined in the animation profile, the postion of claw may looks weird for some problem PDDL.

We will try to implement an middle of screen funtion, to make claw always in the middle of the screen, Or we can make the Claw move around.



## Authors
* **Team Planning Visualisation** - *Initial work* -


## Acknowledgments

* Planning domain API (http://solver.planning.domains/)
