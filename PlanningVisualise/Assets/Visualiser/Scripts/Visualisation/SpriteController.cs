
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: This file is used to control behaviour of sprite objects of unity application
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * Reviewers: Sharukh, Gang and May
 * Review date: 10/09/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */


using System;
using UnityEngine;
using UnityEngine.UI;

namespace Visualiser
{
    /*
     * The controller of a visual sprite
     * It controls how to render a specific visible object on the screen
     */
    public class SpriteController : MonoBehaviour
    {

        VisualSpriteObject visualSprite; // The game object this script binding to
        Animator animator; // An animator use to control animations
        bool willDestory; // Indicates whether the object should be destroyed
        public event EventHandler OnDestory; // Trigged when the object is going to be destroyed

        bool isMoving = false;  // Indicates whether the object is moving
        RectTransform rectTran; // A reference to the RectTransform component of the object
        Vector2 minOffset;  // Offsets of minX and minY
        Vector2 maxOffset;  // Offsets of maxX and maxX
        int frameCount = 0; // Indicates the progess of animation
        double framepersecond = 60;
        GameObject speedbar;
        double framspeed = 1;
        // Unity built-in method, fired when the script is initialised
        void Awake()
        {
            animator = gameObject.GetComponent<Animator>();

        }

        // Binds this script to a visual sprite object
        public void BindVisualSpriteObject(VisualSpriteObject visualSpriteObject)
        {
            visualSprite = visualSpriteObject;
        }

        // Exams whether the binding object has changed
        public bool IsVisualSpriteObjectChanged(VisualSpriteObject vso)
        {
            return !visualSprite.ContentsEqual(vso);
        }

        // Starts rendering, this method is called by the VisualiserController
        public void Init()
        {
            speedbar = GameObject.Find("Slider");
            // Sets up size, position and rotation
            UpdateRect();
            // Sets sprite name
            gameObject.name = visualSprite.name;
            // Renders name text on the sprite
            if (visualSprite.showName)
            {
                var emptyUIObject = Resources.Load<GameObject>("EmptyUIObject");
                var spriteName = Instantiate(emptyUIObject);
                var label = spriteName.AddComponent<Text>();
                label.font = Resources.Load<Font>("Arial");
                label.color = Color.black;
                label.text = visualSprite.name;
                label.alignment = TextAnchor.MiddleCenter;
                label.resizeTextForBestFit = true;
                var nameRectTransform = spriteName.GetComponent<RectTransform>();
                nameRectTransform.anchorMin = new Vector2(0, 0);
                nameRectTransform.anchorMax = new Vector2(1, 1);
                nameRectTransform.offsetMin = new Vector2(0, 0);
                nameRectTransform.offsetMax = new Vector2(0, 0);
                spriteName.transform.SetParent(gameObject.transform, false);

            }
            // Sets sprite colour
            var image = gameObject.GetComponent<Image>();
            image.color = visualSprite.color;
            // Sets default opacity of sprite
            var canvasGroup = gameObject.GetComponent<CanvasGroup>();
            canvasGroup.alpha = 0;
        }

        // Updates the size, position and rotation of the sprite
        void UpdateRect()
        {
            var newAnchorMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var newAnchorMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            var rectTransform = gameObject.GetComponent<RectTransform>();
            rectTransform.anchorMin = newAnchorMin;
            rectTransform.anchorMax = newAnchorMax;
            rectTransform.offsetMin = new Vector2(0, 0);
            rectTransform.offsetMax = new Vector2(0, 0);
            //set depth
            transform.SetSiblingIndex(visualSprite.depth);
            //set rotate
            rectTransform.rotation = Quaternion.Euler(0, 0, visualSprite.rotate);
        }

        // Unity built-in method, it is fired when the script starts running
        void Start()
        {
            var canvas = GetComponent<Canvas>();
            canvas.overrideSorting = true;
        }

        // Unity built-in method, it is fired in every frame
        void Update()
        {
            // Updates animation
            if (isMoving)
            {
                float speed = speedbar.GetComponent<Slider>().value;
                int rev_speed_per_sec = (int)(60 / speed);
                var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
                var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
                rectTran.anchorMin = Vector2.MoveTowards(rectTran.anchorMin, vecMin, speed * Time.deltaTime);// - minOffset * 1/rev_speed_per_sec;
                rectTran.anchorMax = Vector2.MoveTowards(rectTran.anchorMax, vecMax, speed * Time.deltaTime);//rectTran.anchorMax - maxOffset * 1/rev_speed_per_sec;
                if (rectTran.anchorMin.Equals(vecMin) && rectTran.anchorMax.Equals(vecMax))//++frameCount % rev_speed_per_sec == 0)
                {
                    isMoving = false;
                    // Updates color
                    var imgComp = gameObject.GetComponent<Image>();
                    imgComp.color = visualSprite.color;
                }
            }
        }
        public bool moving()
        {
            return isMoving;
        }
        // Calculates the transition offets and starts the animation
        public void MoveToNewPosition()
        {
            isMoving = true;

            rectTran = gameObject.GetComponent<RectTransform>();
            var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            minOffset = rectTran.anchorMin - vecMin;
            maxOffset = rectTran.anchorMax - vecMax;
        }

        #region Fade in/out animation methods
        public void FadeOutForUpdate()
        {
            animator.SetTrigger("Hide");
        }
        // play the animation of fade out and detroy the sprite object next
        public void FadeOutForDestory()
        {
            animator.SetTrigger("Destory");
            willDestory = true;
        }
        // play the animation of fade in and show the sprite object
        public void FadeInForUpdate()
        {
            animator.SetTrigger("Show");
        }
        // Reset the animator "Show" trigger to default
        public void OnFadeInFinished()
        {
            animator.ResetTrigger("Show");
        }
        // Reset the animator "Hide" triggerto default and detroy the sprite object if it is set to destroy
        public void OnFadeOutFinished()
        {
            animator.ResetTrigger("Hide");
            UpdateRect();
            if (willDestory)
            {
                OnDestory?.Invoke(this, null);
            }
            else
            {
                animator.SetTrigger("Show");
            }
        }
        #endregion

    }
}
