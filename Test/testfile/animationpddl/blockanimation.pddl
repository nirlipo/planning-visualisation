(define (animation blocksworld)
 
  (:predicate on
                 :parameters (?x ?y)
                 :effect(
                 (equal (?x x) (?y x))
                 (equal (?x y) (add (?y y) (?y height)))
                 )
  )
 

  (:predicate on-table
                 :parameters (?x)
                 :effect(
                 (assign (?x x) (function distributex (objects ?x) (settings (spacebtwn 40))))
                 (equal (?x y) 0)
                 )
   )
 
  (:predicate holding
 
                 :parameters (?x)
                 :custom claw
                 :effect (
                 (equal (?x x) (claw x))
                 (equal (?x y) (claw y))
                 )
 
  )
  (:visual block
              :type default
              :properties(
                (prefabimage img-block)
                (showname TRUE)
                (x Null)
                (y Null)
                (color RANDOMCOLOR)
                (width 80)
                (height 80)
              )
  )
 
  (:visual claw
              :type custom
              :objects claw
              :properties(
                (prefabimage img-claw)
                (showname FALSE)
                (x 230)
                (y 500)
                (color BLACK)
                (width 80)
                (height 40)
               )
  )
  (:visual board
              :type custom
              :objects board
              :properties(
                (prefabimage img-board)
                (showname FALSE)
                (x 0)
                (y 0)
                (color BLACK)
                (width PANEL_SIZE)
                (height 5)
            
              )
  )

  (:image (img-claw iVBORw0KGg...oAA)
          (img-square iVBORw0KGg...oAA)
          (img-board iVBORw0KGg...oAA)
  )
)