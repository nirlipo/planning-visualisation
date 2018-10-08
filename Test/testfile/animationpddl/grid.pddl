(define (animation grid)

; Defines the Animation profile for Grid
; See AP Guide.md for information on the language.
; Available at https://bitbucket.org/planning-researchers/classical-domains/src/208a850d2ff2a27068329ad578ad99af9ec7e5c5/classical/?at=master
; 08/10/2018
; Written for Project Planning Visualisation
; By Yi Ding

; Specifies that two objects are connected
; We just draw a line between them
   (:predicate conn
               :parameters (?x ?y)
               :effect(
               (action (function draw_line (objects ?x ?y)))
               )
  )

; Specifies that a key has a certain shape
; We just set the key name to the name of a prefabImage
  (:predicate key-shape
               :parameters (?k ?s)
               :effect(
               (equal (?k prefabImage) (?s prefabImage))
               )
  )
 
 ; Specifies that a lock has a certain shape
 ; Again we just set the lock name to the name of a prefabImage
  (:predicate lock-shape
               :parameters (?x ?s)
               :effect(
               (equal (?x prefabImage) (?s prefabImage))
               )
  )
 
 ; Specifies that an object is at another object
 ; Used for placing objects at nodes
 ; We use teh distribute function to achieve this
  (:predicate at
               :parameters (?r ?x)
               :effect(
               (assign (?r x y) (function distribute_within_objects_vertical (objects ?r ?x)(settings (spacebtw 20))))
               )
  )

; Specifies that the robot is at a position
; We place the robot's x and y coordinates at this point
  (:predicate at-robot
               :parameters (?x)
               :custom robot
               :effect(
               (equal (robot x) (add (?x x) 20))
               (equal (robot y) (add (?x y) 20))
               )
  )

; Specifies that an object is a place (node)
; Here we just distribute the objects in a grid formation on screen
; This distribute function automatically aligns objects on-screen based on any
; numbers detected in the objects' name. Hence we require that nodes are named according
; to the convention node0-0, node2-1, etc, or similar.
  (:predicate place
               :parameters (?p)
               :effect(
               (assign (?p x y) (function distribute_grid_around_point (objects ?p)))
               )
  )

; Specifies that a lock is locked. We just change its colour to pink
  (:predicate locked
               :parameters (?x)
               :effect(
               (equal (?x color) #FAA2B5)
               )
  )

; Specifies that an object is being held by the key. We just place it near the robot
  (:predicate holding
               :parameters (?k)
               :custom robot
               :effect(
               (equal (?k x) (add (robot x) 10))
               (equal (?k y) (add (robot y) 5))
               )
  )

; Specifies that a lock is open (unlocked)
; We just make it green
  (:predicate open
               :parameters (?x)
               :effect(
               (equal (?x color) #b0c664)
               )
  )

; Custom object representing the robot
; Moves around according to at-robot predicate
  (:visual robot
            :type custom
            :objects robot
            :properties(
              (prefabImage img-robot)
              (showName FALSE)
              (x Null)
              (y Null)
              (color WHITE)
              (width 40)
              (height 40)
              (depth 2)
            )
  )

; Predefined circle object (node)
  (:visual circle
            :type predefine
            :objects circle
            :properties(
              (prefabImage img-circle)
              (showName FALSE)
            )
  )

; Predefined square object (node)
  (:visual square
            :type predefine
            :objects square
            :properties(
              (prefabImage img-square)
              (showName FALSE)
          )
  )

; Predefined triangle object (node)
  (:visual triangle
            :type predefine
            :objects triangle
            :properties(
              (prefabImage img-triangle)
              (showName FALSE)
          )
  )

; Predefined diamond object (node)
  (:visual diamond
            :type predefine
            :objects diamond
            :properties(
              (prefabImage img-diamond)
              (showName FALSE)
          )
  )

; Predefined key object
; By default is a circle, but this can be modified by key-shape predicate
  (:visual key
            :type predefine
            :objects (key0 key1 key2 key3 key4 key5 key6 key7 key8 key9 key10 key11)
            :properties(
              (prefabImage img-circle)
              (showName FALSE)
              (x Null)
              (y Null)
              (color #14A5DB)
              (width 20)
              (height 20)
              (depth 3)
          )
  )

; Default node type. Circle shape by default.
  (:visual node
            :type default
            :properties(
              (prefabImage img-circle)
              (showName FALSE)
              (x Null)
              (y Null)
              (color GREEN)
              (width 80)
              (height 80)
              (depth 1)
          )
  )
 (:image (img-circle iVBORw0KGgoAAAANSUhEUgAAApIAAAKSCAQAAADLgfPtAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF7WlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDAgNzkuMTYwNDUxLCAyMDE3LzA1LzA2LTAxOjA4OjIxICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMTgtMDgtMTJUMTI6MTU6NTkrMTA6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDE4LTA4LTE1VDIwOjM2OjE5KzEwOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDE4LTA4LTE1VDIwOjM2OjE5KzEwOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMSIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9IkRvdCBHYWluIDIwJSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoyZjBiZjY2NS1lNjljLTQx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)
          (img-diamond iVBORw0KGgoAAAANSUhEUgAAAXEAAAFxCAIAAAAK5Q/zAAABN2lDQ1BBZG9iZSBSR0IgKDE5OTgpAAAokZWPv0rDUBSHvxtFxaFWCOLgcCdRUGzVwYxJW4ogWKtDkq1JQ5ViEm6uf/oQjm4dXNx9AidHwUHxCXwDxamDQ4QMBYvf9J3fORzOAaNi152GUYbzWKt205Gu58vZF2aYAoBOmKV2q3UAECdxxBjf7wiA10277jTG+38yH6ZKAyNguxtlIYgK0L/SqQYxBMygn2oQD4CpTto1EE9AqZf7G1AKcv8ASsr1fBBfgNlzPR+MOcAMcl8BTB1da4Bakg7UWe9Uy6plWdLuJkEkjweZjs4zuR+HiUoT1dFRF8jvA2AxH2w3HblWtay99X/+PRHX82Vun0cIQCw9F1lBeKEuf1UYO5PrYsdwGQ7vYXpUZLs3cLcBC7dFtlqF8hY8Dn8AwMZP/fNTP8gAAAAJcEhZcwAACxMAAAsTAQCanBgAAAXxaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0MCA3OS4xNjA0NTEsIDIwMTcvMDUvMDYtMDE6MDg6MjEgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAxOC0wOC0xMlQxMjoxOTo1MSsxMDowMCIgeG1wOk1vZGlmeURhdGU9IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiBwaG90b3Nob3A6SUNDUHJvZmlsZT0iQWRvYmUgUkdCICgxOTk4KSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo5MGRmODdjNy1lN2YxLTQ5NmMtYjE1Yy1kYjIzNDAxNDQxZWMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6ZmJlOWI4NTQtNDJlYy00ODE3LTgxNWQtMzY0YjAxMTRiODQ3IiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6ZmJlOWI4NTQtNDJlYy00ODE3LTgxNWQtMzY0YjAxMTRiODQ3Ij4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpmYmU5Yjg1NC00MmVjLTQ4MTctODE1ZC0zNjRiMDExNGI4NDciIHN0RXZ0OndoZW49IjIwMTgtMDgtMTJUMTI6MTk6NTErMTA6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo5MGRmODdjNy1lN2YxLTQ5NmMtYjE1Yy1kYjIzNDAxNDQxZWMiIHN0RXZ0OndoZW49IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4gPC94bXBNTTpIaXN0b3J5PiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ppcsu5QAAASfSURBVHic7dTBCQAgEMAwdf+dzyUKgiQT9NU9Mwsgcl4HAF/xFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoXWSoBd9t2wfhAAAAAElFTkSuQmCC)
          (img-triangle iVBORw0KGgoAAAANSUhEUgAAAf4AAAG4CAYAAACkboVUAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF8mlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDAgNzkuMTYwNDUxLCAyMDE3LzA1LzA2LTAxOjA4OjIxICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMTgtMDgtMTJUMTI6MTk6MTIrMTA6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDE4LTA4LTE2VDE1OjI0OjMyKzEwOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDE4LTA4LTE2VDE1OjI0OjMyKzEwOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmM1MTgxYmVjLTcwNjAtNDgyYS1hM2ZiLTk4MjRlZjQyMjRmZSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDowOTNiNjUzOC1hNjYwLTRmMWEtOTBmMC02ODczMzU3OGIwMTkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDowOTNiNjUzOC1hNjYwLTRmMWEtOTBmMC02ODczMzU3OGIwMTkiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjA5M2I2NTM4LWE2NjAtNGYxYS05MGYwLTY4NzMzNTc4YjAxOSIgc3RFdnQ6d2hlbj0iMjAxOC0wOC0xMlQxMjoxOToxMisxMDowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKE1hY2ludG9zaCkiLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmM1MTgxYmVjLTcwNjAtNDgyYS1hM2ZiLTk4MjRlZjQyMjRmZSIgc3RFdnQ6d2hlbj0iMjAxOC0wOC0xNlQxNToyNDozMisxMDowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKE1hY2ludG9zaCkiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+ZY6wvAAADQ1JREFUeJzt2FdiG1cMQFEm+9+z8+G4SKLIKa+gnLMBy+QMLsB/fvz48QBaefbS/7P8rwC2+Hf3HwCE4AKAJoQfehF4aE74oY930bcUQAPCDwCNCD/0cPSad/VDccIP9Z2NufhDYcIPAI0IP9R29Xp39UNRwg8AjQg/1HX3anf1Q0HCDzWNirb4QzHCDwCNCD/UM/pKd/VDIcIPAI0IP9Qy6zp39UMRwg91zI6z+EMBwg8AjQg/1LDqGnf1Q3LCDwCNCD/kt/oKd/VDYsIPuYkwcIrwA1dYOCAp4Ye8dsd3978PXCD8ANCI8ENOUa7tKH8HcJDwQz5iC1wm/MBdFhFIRPghl6iRjfp3AZ8IPwA0IvyQR/SrOvrfBzyEH7IQVWAI4QdGsqBAcMIP8YkpMIzwA6NZVCAw4YfYskY0698N5Qk/ADQi/BBX9qs5+98PJQk/xCSawBTCD8xkgYFghB/iqRbLav8fSE34AaAR4YdYql7HVf9fkI7wQxziCEwn/MAqFhsIQPghBlEElhB+YCULDmwm/LBftxh2+/9CKMIPe4kgsJTwAztYeGAT4Yd9xA9YTviBXSw+sIHwwx6iB2wh/MBOFiBYTPhhPbH7yOcBCwk/rCVywFbCD0RgIYJFhB/WETdgO+EHorAYwQLCD2uI2jE+J5hM+GE+MQPCEH4gGosSTCT8MJeIAaEIPxCRhQkmEX6YR7yAcIQf5hD9+3yGMIHwA5GJPwwm/DCeWAFhCT8QnUUKBhJ+GEukgNCEH8jAQgWDCD+MI05z+XxhAOGHMUQJSEH4gUwsWHCT8MN9YgSkIfxANhYtuEH44R4RAlIRfrhO9Pfx2cNFwg9kJf5wgfDDNaIDpCT8QGYWMDhJ+OE8sQHSEn4gO4sYnCD8cI7IAKkJPxwn+nH5buAg4QeqEH84QPjhGFEBShB+oBILGrwh/PCemABlCD9QjUUNXhB+eE1EcvK9wTeEH74nHkA5wg9UZXGDJ4QfnhMNoCThByqzwMEnwg9fiQVQlvAD1Vnk4C/CDx+JRE2+V/if8MMf4gCUJ/xAFxY7eAg//CIKQAvCD3RiwaM94QcxABoRfroT/X5857Qm/EBH4k9bwk9nhj/QjvADXVn8aEn46crQB1oSfqAzCyDtCD8dGfZAW8JPN6LPZ54JWhF+APGnEeGnE8MdaE/4AX6yGNKC8NOFoQ7wEH56EH2O8qxQnvADfCT+lCb8VGeIA/xF+AG+sjBSlvBTmeEN8InwAzxncaQk4acqQxvgCeGnItFnFM8S5Qg/wGviTynCTzWGNMALwg/wnoWSMoSfSgxngDeEnypEn9k8Y5Qg/ADQiPBTgUuMVTxrpCf8AOeIP6kJP9kZwgAnCD/AeRZO0hJ+MjN8AU4SfrISfXbzDJKS8ANAI8JPRi4tovAsko7wA9wj/qQi/GRjyALcIPxkIvpE5dkkDeEHgEaEnyxcVETnGSUF4QcYR/wJT/jJwDAFGET4AcayqBKa8BOdIQowkPATmeiTlWeXsIQfABoRfqJyMZGdZ5iQhB9gHvEnHOEnIsMSYBLhB5jLIksowk80hiTARMJPJKJPVZ5twhB+AGhE+InCRUR1nnFCEH6AdcSf7YSfCAxDgEWEn91En24882wl/ADQiPCzk8uHrjz7bCP8AHuIP1sIP7sYegAbCD/APhZglhN+djDsADYRflYTffjIO8FSwg8AjQg/K7ls4DnvBssIP0AM4s8Sws8qhhpAAMIPEIcFmemEnxUMM4AghJ/ZRB/O8c4wlfADQCPCz0wuF7jGu8M0wg8Qk/gzhfAzi6EFEJDwA8RlgWY44WcGwwogKOFnNNGHsbxTDCX8ANCI8DOSywTm8G4xjPAD5CD+DCH8jGIoASQg/Iwg+rCGd43bhB8AGhF+7nKBwFreOW4RfoB8xJ/LhJ87DB+AZIQfICeLN5cIP1cZOgAJCT9XiD7E4F3kNOEHgEaEn7NcGBCLd5JThB8gP/HnMOHnDMMFIDnhB6jBYs4hws9RhgpAAcLPEaIPOXhXeUv4AaAR4ecdFwTk4p3lJeEHqEf8+Zbw84rhAVCM8PMd0YfcvMM8JfwA0Ijw84xLAWrwLvOF8ANAI8LPZy4EqMU7zQfCD1Cf+POb8PM3wwGgOOHnF9GH2rzjPB4P4QeAVoSfx8MlAF141xF+AOhE+HEBQC/e+eaEH6Af8W9M+Hvz8gM0I/x9iT70ZgY0JfwA0Ijw92TTBx4Ps6Al4QfoTfybEf5+vOQAjQk/AA6CRoS/Fy83QHPC34foA6+YEU0IPwC/iH8Dwt+DlxmAx+Mh/B2IPnCGmVGc8ANAI8Jfm80duMLsKEz4AXhG/IsS/rq8tAB8Ifw1iT4wgllSkPADQCPCX48NHRjJTClG+AGgEeGvxWYOzGC2FCL8ABwh/kUIfx1eSgDeEv4aRB9YwawpQPgBoBHhz88GDqxk5iQn/ACcJf6JCX9uXj4AThH+vEQf2MkMSkr4AaAR4c/Jpg1EYBYlJPwA0Ijw52PDBiIxk5IRfgDuEv9EhD8XLxcAtwh/HqIPRGZGJSH8ANCI8OdgkwYyMKsSEH4ARhL/4IQ/Pi8RAMMIf2yiD2RkdgUm/ADQiPDHZWMGMjPDghJ+AGhE+GOyKQMVmGUBCT8AM4l/MMIfj5cEgGmEPxbRByoy2wIRfgBoRPjjsBEDlZlxQQg/AKuIfwDCH4OXAYAlhH8/0Qc6MfM2E34AaET497L5Ah2ZfRsJPwA0Ivz72HiBzszATYQfgF3EfwPh38PDDsAWwr+e6AP8YSYuJvwA0Ijwr2WzBfjKbFxI+AGgEeFfx0YL8D0zchHhByAK8V9A+NfwMAMQgvDPJ/oAx5mZkwk/ADQi/HPZXAHOMzsnEn4AaET457GxAlxnhk4i/ABEJf4TCP8cHlYAQhL+8UQfYBwzdTDhB4BGhH8smynAeGbrQMIPAI0I/zg2UoB5zNhBhH8MDyTAfGbtAMIPAI0I/302UIB1zNybhB8AGhH+e2yeAOuZvTcIPwAZif9Fwn+dhw6AdIT/GtEH2M8svkD4AaAR4T/PhgkQh5l8kvADQCPCf47NEiAes/kE4QegAvE/SPiP81ABkJ7wHyP6APGZ1QcIPwA0Ivzv2SAB8jCz3xB+AGhE+F+zOQLkY3a/IPwAVCT+3xD+73loAChH+J8TfYD8zPInhB8AGhH+r2yIAHWY6Z8IPwA0Ivwf2QwB6jHb/yL8f3gwAOoy4/8n/ADQiPD/ZBMEqM+sfwg/ALQi/DZAgE7az3zhB4BGuoe//eYH0FDr2d85/K2/eIDm2jagc/gBoJ2u4W+76QHwW8sWdA0/ALTUMfwtNzwAnmrXhI7hB4C/tYp/t/C3+nIB4LNO4Rd9AL7TphGdwg8A7XUJf5tNDoDLWrSiS/gBgEeP8LfY4AAYonwzOoQfAM4oHf/q4S/95QHAWZXDL/oAXFW2IZXDDwB8UjX8ZTc1AJYp2ZKq4QcAnqgY/pIbGgBblGtKtfCX+4IA2K5UW6qFHwB4oVL4S21kAIRSpjGVwg8AvFEl/GU2MQDCKtGaKuEHAA6oEP4SGxgAKaRvTvbwp/8CAEgndXuyhx8AOCFz+FNvXACklrZBmcMPAJyUNfxpNy0AykjZoqzhBwAuyBj+lBsWACWla1K28Kf7gAEoL1WbsoUfALghU/hTbVQAtJKmUZnCDwDclCX8aTYpANpK0aos4QeADMLHP0P4w3+IAJBF9PCLPgDZhG5X9PADAANFDn/ojQkAXgjbsMjhBwAGixr+sJsSABwUsmVRww8AFYSLf8Twh/uQAKCKaOEXfQCqCdW2aOEHACaKFP5QGxEADBSmcZHCDwBMFiX8YTYhAJgkROsihD/EBwEAC2xvXoTwAwCL7A7/9s0HABbb2r7d4QcAFtoZftc+AF1ta6CLHwAa2RV+1z4A3W1p4Y7wiz4A/LS8iX7qB4BGVofftQ8AHy1to4sfABpZGX7XPgA8t6yRLn4AaGRV+F37APDaklauCL/oA8Ax05vpp34AaGR2+F37AHDO1Ha6+AGgkZnhd+0DwDXTGuriB4BGZoXftQ8A90xp6Yzwiz4AjDG8qX7qB4BGRofftQ8AYw1tq4sfABoZGX7XPgDMMayxLn4AaGRU+F37ADDXkNaOCL/oA8Aat5vrp34AaORu+F37ALDWrfa6+AGgkTvhd+0DwB6XG+ziB4BGrobftQ8Ae11q8ZXwiz4AxHC6yX7qB4BGzobftQ8AsZxqs4sfABo5E37XPgDEdLjRLn4AaORo+F37ABDboVYfCb/oA0AOb5vtp34AaORd+F37AJDLy3a7+AGgkVfhd+0DQE7fNtzFDwCNfBd+1z4A5Pa05S5+AGjkWfhd+wBQw5emu/gBoLYP8f8cftc+ABT2d/hFHwBq+t14P/UDQCPCDwA9/Hg8/oTfz/wA0ICLHwAa+ffh2geALn64+AGgEeEHgEb+A3NT/oPjb2UtAAAAAElFTkSuQmCC)
          (img-square iVBORw0KGgoAAAANSUhEUgAAAXEAAAFxCAIAAAAK5Q/zAAABN2lDQ1BBZG9iZSBSR0IgKDE5OTgpAAAokZWPv0rDUBSHvxtFxaFWCOLgcCdRUGzVwYxJW4ogWKtDkq1JQ5ViEm6uf/oQjm4dXNx9AidHwUHxCXwDxamDQ4QMBYvf9J3fORzOAaNi152GUYbzWKt205Gu58vZF2aYAoBOmKV2q3UAECdxxBjf7wiA10277jTG+38yH6ZKAyNguxtlIYgK0L/SqQYxBMygn2oQD4CpTto1EE9AqZf7G1AKcv8ASsr1fBBfgNlzPR+MOcAMcl8BTB1da4Bakg7UWe9Uy6plWdLuJkEkjweZjs4zuR+HiUoT1dFRF8jvA2AxH2w3HblWtay99X/+PRHX82Vun0cIQCw9F1lBeKEuf1UYO5PrYsdwGQ7vYXpUZLs3cLcBC7dFtlqF8hY8Dn8AwMZP/fNTP8gAAAAJcEhZcwAACxMAAAsTAQCanBgAAAXxaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/PiA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0MCA3OS4xNjA0NTEsIDIwMTcvMDUvMDYtMDE6MDg6MjEgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAxOC0wOC0xMlQxMjoxOTo1MSsxMDowMCIgeG1wOk1vZGlmeURhdGU9IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiBwaG90b3Nob3A6SUNDUHJvZmlsZT0iQWRvYmUgUkdCICgxOTk4KSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo5MGRmODdjNy1lN2YxLTQ5NmMtYjE1Yy1kYjIzNDAxNDQxZWMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6ZmJlOWI4NTQtNDJlYy00ODE3LTgxNWQtMzY0YjAxMTRiODQ3IiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6ZmJlOWI4NTQtNDJlYy00ODE3LTgxNWQtMzY0YjAxMTRiODQ3Ij4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpmYmU5Yjg1NC00MmVjLTQ4MTctODE1ZC0zNjRiMDExNGI4NDciIHN0RXZ0OndoZW49IjIwMTgtMDgtMTJUMTI6MTk6NTErMTA6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo5MGRmODdjNy1lN2YxLTQ5NmMtYjE1Yy1kYjIzNDAxNDQxZWMiIHN0RXZ0OndoZW49IjIwMTgtMDgtMTVUMjA6MzY6NDgrMTA6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChNYWNpbnRvc2gpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4gPC94bXBNTTpIaXN0b3J5PiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ppcsu5QAAASfSURBVHic7dTBCQAgEMAwdf+dzyUKgiQT9NU9Mwsgcl4HAF/xFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoeQpQ8hSg5ClAyVOAkqcAJU8BSp4ClDwFKHkKUPIUoOQpQMlTgJKnACVPAUqeApQ8BSh5ClDyFKDkKUDJU4CSpwAlTwFKngKUPAUoXWSoBd9t2wfhAAAAAElFTkSuQmCC)
          (img-robot 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)
          (line  iVBORw0KGgoAAAANSUhEUgAAA84AAAAFCAIAAAAbsCLlAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGwGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDAgNzkuMTYwNDUxLCAyMDE3LzA1LzA2LTAxOjA4OjIxICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpBQTA1RUE1QjMzMjA2ODExODIyQUM4NjE0MERCRDI1NiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFNUU1MTE2OEZBQTExMUUzODBFQ0E4Mjg2RkNEODNGOSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2MGJhZmVjNy1iMDY3LTRlYWMtYTdhYS0yOWQyNGFkYmEyZTYiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMTgtMDgtMTJUMTI6MjA6MzMrMTA6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDE4LTA4LTE1VDIwOjM2OjQyKzEwOjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDE4LTA4LTE1VDIwOjM2OjQyKzEwOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RkI3RjExNzQwNzIwNjgxMTgzRDE5QTYzMUY5NDkyQUEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QUEwNUVBNUIzMzIwNjgxMTgyMkFDODYxNDBEQkQyNTYiLz4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6YjhhMTA1MjQtNGViMS00NGEwLWI4ZDgtNGQwNWY2Y2U2NjdhIiBzdEV2dDp3aGVuPSIyMDE4LTA4LTEyVDEyOjIxOjU0KzEwOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NjBiYWZlYzctYjA2Ny00ZWFjLWE3YWEtMjlkMjRhZGJhMmU2IiBzdEV2dDp3aGVuPSIyMDE4LTA4LTE1VDIwOjM2OjQyKzEwOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5XefbLAAAAOElEQVRoge3WwQ0AIBDDMGD/ncsSVCche4I8s5MsAADgtTMdAAAAf7LaAABQYbUBAKDCagMAQMUF9FADB/07X9MAAAAASUVORK5CYII=)
 )
)