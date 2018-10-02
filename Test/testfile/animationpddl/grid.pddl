(define (animation grid)

 
  (:predicate key-shape
               :parameters (?k ?s)
               :effect(
               (equal (?k prefabImage) (?s prefabImage))
               )
  )
 
  (:predicate lock-shape
               :parameters (?x ?s)
               :effect(
               (equal (?x prefabImage) (?s prefabImage))
               )
  )
 
  (:predicate at
               :parameters (?x ?y)
               :effect(
               (equal (?x x y) (function distribute_within_objects_vertical (objects ?x ?y)(settings (spacebtw 20))))
               )
  )
 
  (:predicate at-robot
               :parameters (?x)
               :custom robot
               :effect(
               (equal (robot x) (add (?x x) 20))
               (equal (robot y) (add (?x y) 20))
               )
  )
 
  (:predicate place
               :parameters (?x)
               :effect(
               (equal (?x x y) (function distribute_grid_around_point (objects ?x)))
               (equal (?x depth) 10)
               )
  )
 
  (:predicate key
               :parameters (?x)
               :effect(
               (equal (?x depth) 10)
               )
  )
 
  (:predicate locked
               :parameters (?x)
               :effect(
               (equal (?x color) RED)
               )
  )
 
  (:predicate holding
               :parameters (?x)
               :custom robot
               :effect(
               (equal (?x x) (add (robot x) 10))
               (equal (?x y) (add (robot y) 5))
               )
  )
 
  (:predicate open
               :parameters (?x)
               :effect(
               (equal (?x color) GREEN)
               )
  )
 
  (:visual robot
            :type custom
            :objects robot
            :properties(
              (prefabimage img-robot)
              (showname FALSE)
              (x Null)
              (y Null)
              (color RGBA(255,255,255,1))
              (width 40)
              (height 40)
              (depth 2)
            )
  )
 
  (:visual circle
            :type predefine
            :objects circle
            :properties(
              (prefabimage img-circle)
            )
  )
 
  (:visual square
            :type predefine
            :objects square
            :properties(
              (prefabimage img-square)
          )
  )
 
  (:visual triangle
            :type predefine
            :objects triangle
            :properties(
              (prefabimage img-triangle)
          )
  )
 
  (:visual diamond
            :type predefine
            :objects diamond
            :properties(
              (prefabimage img-diamond)
          )
  )
 
  (:visual key
            :type predefine
            :objects (key0 key1 key2 key3 key4 key5 key6 key7 key8 key9 key10 key11)
            :properties(
              (predabImage img-circle)
              (showname FALSE)
              (x Null)
              (y Null)
              (color BLUE)
              (width 20)
              (height 20)
              (depth 3)
          )
  )
  (:visual node
            :type default
            :properties(
              (predabImage img-circle)
              (showname FALSE)
              (x Null)
              (y Null)
              (color BLUE)
              (width 20)
              (height 20)
              (depth 1)
          )
  )
 (:image (img-circle iVBORw0KGgoAAAANSUhEUg)
          (img-diamond iVBORw0KGgoAAAANSUhEUg)
          (img-triangle iVBORw0KGgoAAAANSUhEUg)
          (img-square iVBORw0KGgoAAAANSUhEUg)
          (img-robot iVBORw0KGgoAAAANSUhEUg)
          (img-line iVBORw0KGgoAAAANSUhEUg)
 )
)