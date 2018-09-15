using UnityEngine;
using System.Collections;

namespace VisualSpriteAnimation
{

    public class LinearAnimtor : VisualSpriteAnimator
    {
        RectTransform rectTransform;

        protected override void Setup()
        {
            rectTransform = GetComponent<RectTransform>();
        }

        protected override void Animate()
        {
            float speed = aniSpeedSlider.value;
            int rev_speed_per_sec = (int)(60 / speed);
            var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            rectTransform.anchorMin = Vector2.MoveTowards(rectTransform.anchorMin, vecMin, speed * Time.deltaTime);// - minOffset * 1/rev_speed_per_sec;
            rectTransform.anchorMax = Vector2.MoveTowards(rectTransform.anchorMax, vecMax, speed * Time.deltaTime);//rectTransform.anchorMax - maxOffset * 1/rev_speed_per_sec;
            if (rectTransform.anchorMin.Equals(vecMin) && rectTransform.anchorMax.Equals(vecMax))//++frameCount % rev_speed_per_sec == 0)
            {
                Animating = false;
            }
        }
    }
}
