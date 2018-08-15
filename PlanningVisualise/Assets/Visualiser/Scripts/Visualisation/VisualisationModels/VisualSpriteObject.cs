using UnityEngine;
using System.Collections;
using System;

namespace Visualiser
{
    [Serializable]
    public class VisualSpriteObject
    {
        public string name;
        public string prefabImage;
        public Color color;
        public bool showName;
        public float minX;
        public float maxX;
        public float minY;
        public float maxY;
        public float rotate;
        public int depth;

        public bool ContentsEqual(VisualSpriteObject vso)
        {
            return name == vso.name && prefabImage == vso.prefabImage
                              && Mathf.Approximately(minX, vso.minX) && Mathf.Approximately(maxX, vso.maxX)
                              && Mathf.Approximately(minY, vso.minY) && Mathf.Approximately(maxY, vso.maxY)
                              && color == vso.color
                              && depth == vso.depth;
        }
    }
}
