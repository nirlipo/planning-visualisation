using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Animations;

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

        bool isMoving = false;
        RectTransform rectTran;
        Vector2 minOffset;
        Vector2 maxOffset;
        int frameCount = 0;
        private void Update()
        {
            if (isMoving)
            {
                rectTran.anchorMin = rectTran.anchorMin - minOffset * Time.deltaTime;
                rectTran.anchorMax = rectTran.anchorMax - maxOffset * Time.deltaTime;
                if (++frameCount % 60 == 0)
                {
                    isMoving = false;
                }
            }
        }

        public void MoveToNewPosition()
        {
            isMoving = true;

            rectTran = gameObject.GetComponent<RectTransform>();
            var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            minOffset = rectTran.anchorMin - vecMin;
            maxOffset = rectTran.anchorMax - vecMax;

            //var rectTran = gameObject.GetComponent<RectTransform>();
            //var moveAni = gameObject.GetComponent<Animation>();
            //if (moveAni == null)
            //{
            //    moveAni = gameObject.AddComponent<Animation>();
            //}
            //var minX = rectTran.anchorMin.x;
            //var minY = rectTran.anchorMin.y;
            //var maxX = rectTran.anchorMax.x;
            //var maxY = rectTran.anchorMax.y;

            //var curveMinX = AnimationCurve.Linear(0f, minX, 1f, visualSprite.minX);
            //var curveMinY = AnimationCurve.Linear(0f, minY, 1f, visualSprite.minY);
            //var curveMaxX = AnimationCurve.Linear(0f, maxX, 1f, visualSprite.maxX);
            //var curveMaxY = AnimationCurve.Linear(0f, maxY, 1f, visualSprite.maxY);

            //var clipMinX = new AnimationClip();
            //clipMinX.legacy = true;
            //clipMinX.SetCurve("", typeof(RectTransform), "anchorMin.x", curveMinX);

            //var clipMinY = new AnimationClip();
            //clipMinY.legacy = true;
            //clipMinY.SetCurve("", typeof(RectTransform), "anchorMin.y", curveMinY);

            //var clipMaxX = new AnimationClip();
            //clipMaxX.legacy = true;
            //clipMaxX.SetCurve("", typeof(RectTransform), "anchorMax.x", curveMaxX);

            //var clipMaxY = new AnimationClip();
            //clipMaxY.legacy = true;
            //clipMaxY.SetCurve("", typeof(RectTransform), "anchorMax.y", curveMaxY);

            //moveAni.AddClip(clipMinX, "MoveMinX");
            //moveAni.AddClip(clipMinX, "MoveMinY");
            //moveAni.AddClip(clipMinX, "MoveMaxX");
            //moveAni.AddClip(clipMinX, "MoveMaxY");
            //moveAni.playAutomatically = false;

            //moveAni.Play("MoveMinX");
            //moveAni.Play("MoveMinY");
            //moveAni.Play("MoveMaxX");
            //moveAni.Play("MoveMaxY");
        }

    }
}
