using UnityEngine;
using System.Collections;
using System;

namespace Visualiser
{
	/* This class contains information of an individual object at a stage in the Visualisation file,
	 * this including its name, image, and location*/
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
		// checking if the given VisualSpriteObject is same as this class
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
