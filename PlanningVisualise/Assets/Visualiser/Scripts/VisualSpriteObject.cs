using UnityEngine;
using System.Collections;
using System;

[Serializable]
public class VisualSpriteObject
{
    public string name;
    public string prefab;
    public float minX;
    public float maxX;
    public float minY;
    public float maxY;
    public Color color;

    public bool ContentsEqual(VisualSpriteObject vso)
    {
        return name == vso.name && prefab == vso.prefab
                          && Mathf.Approximately(minX, vso.minX) && Mathf.Approximately(maxX, vso.maxX)
                          && Mathf.Approximately(minY, vso.minY) && Mathf.Approximately(maxY, vso.maxY);
    }
}
