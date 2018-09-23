
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
using VisualSpriteAnimation;

namespace Visualiser
{
    /*
     * The controller of a visual sprite
     * It controls how to render a specific visible object on the screen
     */
    public class SpriteController : MonoBehaviour
    {

        VisualSpriteObject visualSprite; // The game object this script binding to
        VisualSpriteAnimator animator; // An animator use to control animations

        public event EventHandler OnDestory;

        // Unity built-in method, fired when the script is initialised
        void Awake()
        {
            switch (visualSprite.transferType)
            {
                default:
                    animator = gameObject.AddComponent<LinearAnimtor>();
                    break;
            }
        }

        public void UpdateState(VisualSpriteObject vso)
        {
            if (!visualSprite.ContentsEqual(vso))
            {
                visualSprite = vso;
                // Updates color
                var imgComp = gameObject.GetComponent<Image>();
                imgComp.color = visualSprite.color;
                // Transit to new state
                animator.UpdateVisualSprite(vso);
                animator.Animating = true;
            }
        }

        public VisualSpriteObject GetVisualSprite()
        {
            return visualSprite;
        }

        // Starts rendering, this method is called by the VisualiserController
        public void Init(VisualSpriteObject vso)
        {
            // Binds visual sprite
            visualSprite = vso;
            // Sets game object name
            gameObject.name = visualSprite.name;
			Debug.Log(visualSprite.showLabel);
            // Sets up size, position and rotation
            UpdateRect();
            // Renders name text on the sprite
			if (visualSprite.showName || visualSprite.showLabel )
            {
                var emptyUIObject = Resources.Load<GameObject>("EmptyUIObject");
                var spriteName = Instantiate(emptyUIObject);
                var label = spriteName.AddComponent<Text>();
                label.font = Resources.Load<Font>("Arial");
                label.color = Color.black;
				if (visualSprite.showName)
                	label.text = visualSprite.name;
				else
					label.text = visualSprite.label;
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
            var canvas = gameObject.GetComponent<Canvas>();
            canvas.sortingOrder = visualSprite.depth + 1;
            canvas.overrideSorting = true;
            //set rotate
            rectTransform.rotation = Quaternion.Euler(0, 0, visualSprite.rotate);
        }

        // Unity built-in method, it is fired when the script starts running
        void Start()
        {
            var canvas = gameObject.GetComponent<Canvas>();
            canvas.sortingOrder = visualSprite.depth + 1;
            canvas.overrideSorting = true;
        }

        // Unity built-in method, it is fired in every frame
        void Update()
        {
        }

        public void SetSubgoal(bool flag)
        {
            animator.Highlighting = flag;
        }

        public bool IsAnimating()
        {
            return animator.Animating;
        }

        #region Fade in/out animation methods
        public void Present()
        {
            animator.Forming = true;
        }

        public void DisapperAndDestory()
        {
            animator.Dying = true;
            animator.OnDied += (object sender, EventArgs e) =>
            {
                OnDestory?.Invoke(this, null);
            };
        }
        #endregion

    }
}
