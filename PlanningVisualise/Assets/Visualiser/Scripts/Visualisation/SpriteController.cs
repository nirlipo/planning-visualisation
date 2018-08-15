using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace Visualiser
{
    public class SpriteController : MonoBehaviour
    {

        VisualSpriteObject visualSprite;

        Animator ani;

        bool willDestory;

        public event EventHandler OnDestory;

        void Awake()
        {
            ani = gameObject.GetComponent<Animator>();
        }

        public void BindVisualSpriteObject(VisualSpriteObject visualSpriteObject)
        {
            visualSprite = visualSpriteObject;
        }

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

        void UpdateRect()
        {
            var newAnchorMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var newAnchorMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            var rectTransform = gameObject.GetComponent<RectTransform>();
            rectTransform.anchorMin = newAnchorMin;
            rectTransform.anchorMax = newAnchorMax;
            rectTransform.offsetMin = new Vector2(0, 0);
            rectTransform.offsetMax = new Vector2(0, 0);
            rectTransform.SetSiblingIndex(visualSprite.depth + rectTransform.GetSiblingIndex());
            rectTransform.rotation = Quaternion.Euler(0, 0, visualSprite.rotate);
        }

        public void FadeOutForUpdate()
        {
            ani.SetTrigger("Hide");
        }

        public void FadeOutForDestory()
        {
            ani.SetTrigger("Destory");
            willDestory = true;
        }

        public void FadeInForUpdate()
        {
            ani.SetTrigger("Show");
        }

        public void OnFadeInFinished()
        {
            ani.ResetTrigger("Show");
        }

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

    }
}
