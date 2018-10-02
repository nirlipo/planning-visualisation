(define (animation hanoi)
 
  (:predicate on
               :parameters (?x ?y)
               :priority 1
               :effect (
               (equal (?x x) (function align_middle (objects ?x ?y)))
               (equal (?x y) (add (?y y) 20))
  )
  )
   (:predicate smaller
               :parameters (?x ?y)
               :priority 0
               :effect(
               (equal (?x width) (function apply_smaller (objects ?x ?y) (settings (increase_width 6))))
               )
  )
 
 
  (:visual peg1
            :type predefine
            :objects (peg1)
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x 0)
              (y 0)
              (color BLACK)
              (width 10)
              (height 200)
              (depth 0)
            )
  )

   (:visual peg2
            :type predefine
            :objects (peg2)
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x 100)
              (y 0)
              (color BLACK)
              (width 10)
              (height 200)
              (depth 0)
            )
  )

   (:visual peg3
            :type predefine
            :objects (peg3)
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x 200)
              (y 0)
              (color BLACK)
              (width 10)
              (height 200)
              (depth 0)
            )
  )

  (:visual disk
            :type default
            :properties(
              (prefabimage img-square)
              (showname TRUE)
              (x Null)
              (y Null)
              (color BLUE)
              (width 20)
              (height 20)
              (depth 1)
          )
  )
 (:image (img-square VBORw0KGg...oAE)

 )
)