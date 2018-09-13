# 1 Introduction


## 1.1 Purpose


An Animation Profile (AP) is a user-written PDDL file which tells the Visualiser how a Domain is to be visualised. Each Animation Profile corresponds to one Domain. 


Essentially, the AP provides a set of visual objects ("shapes") within the domain, along with a set of mappings from Predicates to animation behaviours.


## 1.2 Scope


The AP Language is designed to be flexible enough to allow for the animation of many simple PDDL domains, such as those found at https://bitbucket.org/planning-researchers/classical-domains/src/208a850d2ff2a27068329ad578ad99af9ec7e5c5/classical/?at=master. 


Currently, APs have been written for four domains from this repository: Blocks, Towers of Hanoi, Logistics, and Grid.


Other simple domains can be visualised in the language. For more complicated domains, additional functions or object properties may be added (See section 4).


# 2 Using the Language



This section contains complete documentation for the syntax and semantics of the AP language. For a quick starting point to writing your own AP, see section 3.


## 2.1 Key Components


### 2.1.1 Predicates


The first content of the AP should be the Predicate blocks. Here is an example of a Predicate block.
```
(:predicate holding
 
                 :parameters (?x claw)
                 :effect (
                 (equal (?x x y) (claw x y))
                 )
 
  )
```
There should be one or zero Predicate blocks for each Predicate in the Domain. If there is no Predicate block for a Predicate in the domain, the Predicate is ignored by the solver.


Predicate Blocks contain:
* The name of the Predicate, for example ```holding```.
* The parameters of the Predicate. Parameters are objects to which the Predicate applies. For example, ```holding(?x)``` means that the predicate on-table is true for the object ?x.
* The effect of the Predicate. This is a logical statement concerning object properties which holds true when the predicate holds true. For example, ```(equal (?x x y) (claw x y))``` means that the object ```?x``` is at the object ```claw```.


### 2.1.2 Shapes

Shapes are visual objects represented on the screen.


An example of a Shape block is:


```
(:shape block
              :type default
              :properties(
                (showname false)
                (x NULL)
                (y NULL)
                (color (function randomcolor)) 
                (width 80)
                (height 80)
                (base64image iVBORw0KGg...oAA)
              )
  )
```


Shape blocks contain:
* The name of the shape, for example ```block```
* The type of the object. Types can either be ```default``` or ```custom```. ```default``` objects apply to any objects mentioned in the problem file. A 'block' in the problem file is an example of a default object. ```custom``` objects are additional to the problem file, and are created by the user for visual effect. The 'claw' is an example of a custom object - it mainly serves a visual purpose and is not specified in the problem or domain file.
* Object properties. These properties govern the position and appearance of the object. See section 2.4 for a detailed list of object properties.

## 2.2 Syntax


### 2.2.1 Description


The syntax of the language is based on PDDL syntax, which is itself based on Lisp. See Section 2.2.2 for detailed resources on these languages.






### 2.2.2 Resources


* PDDL information: https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language
* PDDL examples, solver: http://planning.domains/
* Lisp information: https://en.wikipedia.org/wiki/Lisp_(programming_language)
* Lisp Tutorial: https://www.tutorialspoint.com/lisp/


## 2.3 Types


A type is a class of variable to which a property can be assigned. The use of the word 'type' is therefore fairly loose.


AP supports a number of 'types':
* Integer
* Boolean - ```true``` or ```false```
* Function - Allocates a property based on some function, for example, ```distribute_horizontal```
* Colour - either a colour constant (see below), the random_colour function (see section 2.5), or an rgb value specified, for example, by (rgb 232 232 323)
* Constant - A number of pre-defined constants exist. These should by convention be written in CAPITALS.
	* Colours: BLACK, RED, BLUE, GREEN, YELLOW
	* Integer Constants: PANEL_SIZE
	* ```NULL``` - A ```NULL``` value means the user is not specifying the property. ```NULL``` properties are typically be set by Predicate rules.



A list of the types to which each property can be assigned is in section 2.4.







## 2.4 Object Properties


A number of Object Properties can be assigned for each Shape.
* showname (Boolean): whether to display the shape's name on screen
* x (Integer): x position of the shape on screen
* y (Integer): y position of the shape on screen
* colour (Colour): Colour of the shape
* width (Integer): Width of the object on screen
* height: Height of the object on screen
* base64image: A Base64 string representing the shape's image. Base64 images can be generated at https://www.base64decode.org/



## 2.5 Functions

Functions have two uses:
* In Predicate blocks: here they are 'declarative' in nature and when specified, are true for their parameters
* In object properties: Here they return a value (eg random_colour).


List of functions:


Distribution:
Distribution functions 'distribute' objects in a certain manner. They are used to lay objects out on the screen. All objects for which the same parameters of 'distribute' are called will be included in the distribution. Distribution works such that objects will be placed in a certain area without overlapping. Between animation frames, objects will not move (unless their positions are reset).

* distribute_horizontal
	* This function distributes objects along a horizontal plane. 
* distribute_vertical
	* This function distributes objects along a vertical plane. 
* distribute_grid
	* This function distributes objects within a grid-like structure 
* distribute_within_object
	* This function distributes objects within the bounds of another object. For example, cars can be distributed within a city.


Other:
* draw_line
	* Draws a line between two objects
* check_smaller
	* Specifies that one object is smaller than another. Useful in domains such as the Towers of Hanoi
* random_colour
	* Specifies that an object has a random colour.


# 3 Worked Example

The following example is for the Blocks domain.
To see the final result for this AP, see the link in section 1.2 for the associated domain and problem files. These can be visualised with this animation profile.

The following is an example problem visualised with this animation profile:

![Blocks example](https://bitbucket.cis.unimelb.edu.au:8445/projects/SWEN90013/repos/swen90013-2018-pl/raw/Docs/images/ap/blocks_example.png?at=refs%2Fheads%2Ffeature-userdocs).


The animation profile is as follows (comments  added with a # symbol):


```
(define (animation blocksworld)

	# the 'on' predicate takes two parameters (objects) ?x and ?y
  (:predicate on
                 :parameters (?x ?y)
                 :effect( 


				# the effect of the `on` predicate is that ?x's x value is equal to ?y's x value, and that ?x's y value is equal to ?y's ?y value plus its height.
				# that is, object ?x is on top of object ?y
                 (equal (?x x y) (?y x (sum y height)) 
                 )
  )

  (:predicate on-table

                 :parameters (?x)
                 :effect(


				# the predicate on-table specifies that the object should be distributed horizontally, with a y value of 0
				# and a margin of 5
                 (equal (?x x y) (function distribute_horizontal (margin 5)(y 0))
                 )

  (:predicate holding

                 :parameters (?x claw)
                 :effect ( 
                 (equal (?x x y) (claw x y))
                 )

  )



	# Below are the list of shapes


  (:shape block
				#block shape is the default shape type. All domain objects have this type by default
			  :type default


				# all 'shape' objects have the following properties
              :properties(
                (showname false)
                (x false)
                (y false)


				# randomcolor assigns a random color to the object
                (color (function randomcolor))
                (width 80)
                (height 80)


				# this is a base64 string representing the image of the object
                (base64image iVBORw0KGg...oAA)
              )
  )

  (:shape claw
				#custom object types do not appear in the domain
				#they are mainly cosmetic. This object represents the claw (the claw does not move)
              :type custom
              :properties(
                (showname false)
                (x 230)
                (y 500)
                (color black)
                (width 80)
                (height 40)
                (base64image iVBORw0KGg...oAA)
               )
  )
  (:shape board
              :type custom
              :properties(
                (showname false)
                (x 0)
                (y 0)
                (color black)
                (width panel_size)
                (height 5)
                (base64image iVBORw0KGg...oAA)
              )
  )

)
```

# 4 Extending the Language


## 4.1 Extension Areas

There are two primary methods of extending the AP language:	
1. Object properties (section 2.4)
	* This is for simple ways of extending the appearance of objects, eg adding rotation or the font of 'showname'
2. Adding functions (section 2.5)
	* This is for more complex ways of describing object behaviours and interactions, eg adding new object layout options


## 4.2 Extension Steps


1. Modify the extensions.py file in the directory to add any functions or properties. See the document 'VFG Documentation.md' for more information.
2. In limited advanced cases, exta functions may need to be written for Visualiser (Unity)
3. Add the necessary documentation in this .md file.
