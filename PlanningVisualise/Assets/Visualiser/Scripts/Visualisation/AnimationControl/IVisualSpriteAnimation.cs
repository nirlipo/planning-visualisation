using System;
using UnityEngine;

namespace VisualSpriteAnimation
{
    public interface IVisualSpriteAnimation
    {
        void Animate(GameObject gameObject, float speed);
    }
}
