using UnityEngine;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;
using System.Linq;

namespace Visualiser
{
    public class VisualiserController : MonoBehaviour
    {
        ScenesCoordinator coordinator = ScenesCoordinator.Coordinator;

        VisualSolutionObject visualSolution;

        public GameObject AniFrameOne;
        public GameObject AniFrameTwo;

        GameObject presentingAniPanel;

        Dictionary<string, GameObject> spritePool = new Dictionary<string, GameObject>();

        // Use this for initialization
        void Start()
        {
            var parameters = coordinator.FetchParameters("Visualisation") as string;
            visualSolution = JsonUtility.FromJson<VisualSolutionObject>(parameters);
            Debug.Log(parameters);

            presentingAniPanel = AniFrameOne;
            var visualStage = visualSolution.NextStage();
            RenderFrame(visualStage);
        }

        public void PresentNextStage()
        {
            var visualStage = visualSolution.NextStage();
            TryRenderFrame(visualStage);
        }

        public void PresentPreviousStage()
        {
            var visualStage = visualSolution.PreviousStage();
            TryRenderFrame(visualStage);
        }
        public void PresentCurrent(int i)
        {
            var stages = visualSolution.visualStages;
            TryRenderFrame(stages[i]);
        }

        public void ResetStage()
        {
            var visualStage = visualSolution.ResetStage();
            TryRenderFrame(visualStage);
        }

        public void Play()
        {
            playing = true;
        }

        public void Pasue()
        {
            playing = false;
            frameCount = 0;
        }

        public void btnHelp()
        {

            Application.OpenURL("https://www.youtube.com/watch?v=8oVxPHSoRKA&t=3m22s");
        }

        private void Update()
        {
            if (playing && (frameCount++ % 60 == 0))
            {
                PresentNextStage();

            }
        }

        int frameCount = 0;
        bool playing;

        private void TryRenderFrame(VisualStageObject visualStage)
        {
            if (visualStage != null)
            {
                RenderFrame(visualStage);
            }
        }


        private void RenderFrame(VisualStageObject visualStage)
        {
            //Render all visual sprite objects of current visual stage
            foreach (var visualSprite in visualStage.visualSprites)
            {
                //Check existing sprites
                if (spritePool.ContainsKey(visualSprite.name))
                {
                    var sprite = spritePool[visualSprite.name];
                    var controller = sprite.GetComponent<SpriteController>();
                    //Do nothing if the sprite has not changed
                    if (!controller.IsVisualSpriteObjectChanged(visualSprite))
                    {
                        continue;
                    }
                    //Hide the changed sprite for updating
                    controller.BindVisualSpriteObject(visualSprite);
                    controller.FadeOutForUpdate();
                    continue;
                }
                else
                {
                    //Create a new sprite if it does not exist
                    GameObject sprite;
                    var imageKey = visualSprite.prefabImage;
                    var imageString = visualSolution.FetchImageString(imageKey);
                    // Render custom prefab image
                    if (imageString != null)
                    {
                        var spritePrefab = Resources.Load<GameObject>("EmptyVisualSprite");
                        sprite = Instantiate(spritePrefab);
                        var imageComp = sprite.GetComponent<Image>();

                        var texture = new Texture2D(1, 1);
                        texture.LoadImage(Convert.FromBase64String(imageString));
                        texture.Apply();
                        var rectTrans = sprite.GetComponent<RectTransform>();
                        var imgSprite = Sprite.Create(texture,
                                                      new Rect(new Vector2(0, 0), rectTrans.sizeDelta),
                                                      rectTrans.pivot);
                        imageComp.sprite = imgSprite;
                    }
                    // Search for built-in prefab image
                    else
                    {
                        var spritePrefab = Resources.Load<GameObject>(visualSprite.prefabImage);
                        sprite = Instantiate(spritePrefab);
                    }

                    var controller = sprite.GetComponent<SpriteController>();
                    controller.BindVisualSpriteObject(visualSprite);
                    controller.Init();
                    sprite.transform.SetParent(presentingAniPanel.transform, false);
                    spritePool.Add(sprite.name, sprite);
                    controller.FadeInForUpdate();
                }
            }
            //Remove stored sprites if they are not longer existing
            if (spritePool.Count > visualStage.visualSprites.Length)
            {
                var existingSpriteKeys = from i in visualStage.visualSprites
                                         select i.name;
                var temps = new List<string>();
                foreach (var spriteKey in spritePool.Keys)
                {
                    if (!existingSpriteKeys.Contains(spriteKey))
                    {
                        temps.Add(spriteKey);
                    }
                }
                foreach (var temp in temps)
                {
                    var sprite = spritePool[temp];
                    var controller = sprite.GetComponent<SpriteController>();
                    controller.OnDestory += (sender, e) =>
                    {
                        foreach (Transform child in sprite.transform)
                        {
                            Destroy(child.gameObject);
                        }
                        Destroy(sprite);
                        spritePool.Remove(temp);
                    };
                    controller.FadeOutForDestory();
                }
            }

        }
    }
}