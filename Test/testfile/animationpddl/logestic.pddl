(define (animation logistics-strips)
 
  (:predicate city
               :parameters (?city)
               :effect (
               (assign (?city y) (function distributey (objects ?city)))
                )
  )
   (:predicate in-city
               :parameters (?obj ?city)
               :effect(
               (equal (?obj y) (?city y))
               (assign (?obj x) (function distribute_within_objects_horizontal (objects ?obj ?city)))
               )
  )
   (:predicate at
               :parameters (?obj ?loc)
               :effect(
               (equal (?obj y) (?loc y))
               (assign (?obj x) (function distribute_within_objects_horizontal (objects ?obj ?loc)))
               )
  )
   (:predicate in
               :parameters (?obj1 ?obj2)
               :effect(
               (equal (?obj1 y) (?obj2 y))
               (equal (?obj1 x) (?obj2 x))
               (assign (?obj2 label) (function calculate_label (objects ?obj1 ?obj2)))
               )
  )
 
  (:visual package
            :type default
            :properties(
              (prefabimage img-diamond)
              (showname FALSE)
              (x NULL)
              (y NULL)
              (color RGBA(0.5,1,1,1))
              (width 50)
              (height 50)
              (depth 4)
            )
  )

  (:visual truck
            :type predefine
            :objects (truck1 truck2 truck3 truck4 truck5 truck6)
            :properties(
              (prefabimage img-truck)
              (showname FALSE)
              (x NULL)
              (y NULL)
              (color RGBA(1,1,1,1))
              (width 60)
              (height 100)
              (depth 3)
              (showLabel TRUE)
              (label 0)
            )
  )

  (:visual plane
            :type predefine
            :objects (plane1 plane2)
            :properties(
              (prefabimage img-plane)
              (showname FALSE)
              (x NULL)
              (y NULL)
              (color RGBA(1,1,1,1))
              (width 60)
              (height 100)
              (depth 3)
              (showLabel TRUE)
              (label 0)
            )
  )
  (:visual hub
            :type predefine
            :objects (city6-1 city5-1
            city4-1 city3-1 city2-1 city1-1 city6-2 city5-2 city4-2 city3-2 city2-2 city1-2)
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x NULL)
              (y NULL)
              (color RGBA(0.7,0.647,0.858,1))
              (width 600)
              (height 150)
              (depth 2)
            )
  )

  (:visual city
            :type predefine
            :objects (city6 city5 city4 city3 city2 city1)
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x 0)
              (y NULL)
              (color RGBA(0.08,0.647,0.858,1))
              (width PANEL_SIZE)
              (height 200)
              (depth 1)
            )
  )
 (:image (img-square VBORw0KGg...oAE)
         (img-diamond VBORw0KGg...oAE)
         (img-truck VBORw0KGg...oAE)
         (img-plane VBORw0KGg...oAE)
 )
)