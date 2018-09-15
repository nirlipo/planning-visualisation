using UnityEngine;
using System.Collections;
using Visualiser;
using System;

namespace VisualSpriteAnimation
{

    public class LinearTransitionAni : VisualSpriteAnimator
    {
        RectTransform rectTran;

        protected override void Setup()
        {
            rectTran = GetComponent<RectTransform>();
        }

        protected override void Animate()
        {
            float speed = aniSpeedSlider.value;
            int rev_speed_per_sec = (int)(60 / speed);
            var vecMin = new Vector2(visualSprite.minX, visualSprite.minY);
            var vecMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            rectTran.anchorMin = Vector2.MoveTowards(rectTran.anchorMin, vecMin, speed * Time.deltaTime);// - minOffset * 1/rev_speed_per_sec;
            rectTran.anchorMax = Vector2.MoveTowards(rectTran.anchorMax, vecMax, speed * Time.deltaTime);//rectTran.anchorMax - maxOffset * 1/rev_speed_per_sec;
            if (rectTran.anchorMin.Equals(vecMin) && rectTran.anchorMax.Equals(vecMax))//++frameCount % rev_speed_per_sec == 0)
            {
                Animating = false;
            }
        }
    }
}
