(define (problem blocksworld-12-0)
(:domain blocksworld)
(:objects i d b e k g a f c j l h )
(:init (clear h) (clear l) (clear j) (on-table c) (on-table f) (on-table j)
 (on h a) (on a g) (on g k) (on k e) (on e b) (on b d) (on d i) (on i c)
 (on l f) (arm-free))
(:goal (and (on i c) (on c b) (on b l) (on l d) (on d j) (on j e) (on e k) (on k f) (on f a) (on a h) (on h g))))