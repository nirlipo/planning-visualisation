///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: The file has fucntionality to set each animation object graphic properties 
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * Reviewers: Sharukh, Gang and May
 * Review date: 10/09/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */


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
        public string label;
        public bool showLabel;
        public Color color;
        public bool showName;
        public float minX;
        public float maxX;
        public float minY;
        public float maxY;
        public float rotate;
        public int depth;
        public int transferType;
		// checking if the given VisualSpriteObject is same as this class
        public bool ContentsEqual(VisualSpriteObject vso)
        {
            return              name == vso.name 
                              && prefabImage == vso.prefabImage
                              && Mathf.Approximately(minX, vso.minX) && Mathf.Approximately(maxX, vso.maxX)
                              && Mathf.Approximately(minY, vso.minY) && Mathf.Approximately(maxY, vso.maxY)
                              && color == vso.color
                              && depth == vso.depth
                              && label == vso.label                                                         
                              ;
        }
    }
}
