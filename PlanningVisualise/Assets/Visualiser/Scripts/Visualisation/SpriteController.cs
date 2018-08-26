using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Animations;

namespace Visualiser
{
	/* The SpriteController is associated with each single VisualSpriteObject in the current problem,
	 * it controls the sprite's animation and updating its information at each visualstage.*/
    public class SpriteController : MonoBehaviour
    {

        VisualSpriteObject visualSprite;

        Animator ani;

        bool willDestory;

        public event EventHandler OnDestory;
		// link to the given animator
        void Awake()
        {
            ani = gameObject.GetComponent<Animator>();
        }
		// Associate this controller with the given VisualSpriteObject
        public void BindVisualSpriteObject(VisualSpriteObject visualSpriteObject)
        {
            visualSprite = visualSpriteObject;
        }
		// Checking if the VisualSpriteObject changed from its previous stored information
        public bool IsVisualSpriteObjectChanged(VisualSpriteObject vso)
        {
            return !visualSprite.ContentsEqual(vso);
        }

        public void Init()
        {
            UpdateRect();
            //set sprite name
            gameObject.name = visualSprite.name;
            //render name text on sprite
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
            //set sprite colour
            var image = gameObject.GetComponent<Image>();
            image.color = visualSprite.color;
            //set default opacity of sprite
            var canvasGroup = gameObject.GetComponent<CanvasGroup>();
            canvasGroup.alpha = 0;

        }
		// updating the sprite objects information
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
            //update color
            var imgComp = gameObject.GetComponent<Image>();
            imgComp.color = visualSprite.color;



        }

        private void Start()
        {
            var canvas = GetComponent<Canvas>();
            canvas.overrideSorting = true;
        }
		// play the animation of fade out and hide the sprite object
        public void FadeOutForUpdate()
        {
            ani.SetTrigger("Hide");
        }
		// play the animation of fade out and detroy the sprite object next
        public void FadeOutForDestory()
        {
            ani.SetTrigger("Destory");
            willDestory = true;
        }
		// play the animation of fade in and show the sprite object
        public void FadeInForUpdate()
        {
            ani.SetTrigger("Show");
        }
		// Reset the animator "Show" trigger to default
        public void OnFadeInFinished()
        {
            ani.ResetTrigger("Show");
        }
		// Reset the animator "Hide" triggerto default and detroy the sprite object if it is set to destroy
        public void OnFadeOutFinished()
        {
            ani.ResetTrigger("Hide");
            UpdateRect();
            if (willDestory)
            {
                OnDestory?.Invoke(this, null);
            }
            else
            {
                ani.SetTrigger("Show");
            }
        }

        bool isMoving = false;
        RectTransform rectTran;
        Vector2 minOffset;
        Vector2 maxOffset;
        int frameCount = 0;
        private void Update()
        {
            if (isMoving)
            {
                rectTran.anchorMin = rectTran.anchorMin - minOffset * 1/60;
                rectTran.anchorMax = rectTran.anchorMax - maxOffset * 1/60;
                if (++frameCount % 60 == 0)
                {
                    isMoving = false;
                    //UpdateRect();
                    //update color
                    var imgComp = gameObject.GetComponent<Image>();
                    imgComp.color = visualSprite.color;
                }
            }
        }
		// set the next timestep position of the sprite object
        public void MoveToNewPosition()
        {
            isMoving = true;

            rectTran = gameObject.GetComponent<RectTransform>();
            var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            minOffset = rectTran.anchorMin - vecMin;
            maxOffset = rectTran.anchorMax - vecMax;
        }

    }
}
