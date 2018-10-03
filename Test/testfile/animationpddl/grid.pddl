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
               :parameters (?r ?x)
               :effect(
               (equal (?r x y) (function distribute_within_objects_vertical (objects ?r ?x)(settings (spacebtw 20))))
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
               :parameters (?p)
               :effect(
               (equal (?p x y) (function distribute_grid_around_point (objects ?p)))
               (equal (?p depth) 10)
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
               :parameters (?k)
               :custom robot
               :effect(
               (equal (?k x) (add (robot x) 10))
               (equal (?k y) (add (robot y) 5))
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
              (color pink)
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