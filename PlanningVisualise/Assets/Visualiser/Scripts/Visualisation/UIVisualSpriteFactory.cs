/* File name: UIVisualSpriteFactory
 * This class file is used to generate image object for animation   
 */


using System;
using UnityEngine;
using UnityEngine.UI;

namespace Visualiser
{
    public class UIVisualSpriteFactory : MonoBehaviour
    {
        // Instantiate prefabImage gameobject
        static public GameObject CreateBuiltIn(string prefabImage)
        {
            GameObject sprite;
            var spritePrefab = Resources.Load<GameObject>(prefabImage);
            sprite = Instantiate(spritePrefab);

            return sprite;
        }

        // Create Gameobect using image string for animation
        static public GameObject CreateCustom(string imageString)
        {
            GameObject sprite;
            var spritePrefab = Resources.Load<GameObject>("EmptyVisualSprite");
            sprite = Instantiate(spritePrefab);

            var imageComp = sprite.GetComponent<Image>();
            var texture = new Texture2D(1, 1);
            texture.LoadImage(Convert.FromBase64String(imageString));
            texture.Apply();
            var rectTrans = sprite.GetComponent<RectTransform>();
            var imgSprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f));
            imageComp.sprite = imgSprite;

            return sprite;
        }
    }
}
