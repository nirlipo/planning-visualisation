using UnityEngine;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;
using System.Linq;

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

    private void Update()
    {
        if (playing && (frameCount++ % 30 == 0))
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
            if (spritePool.ContainsKey(visualSprite.name))
            {
                var sprite = spritePool[visualSprite.name];
                var controller = sprite.GetComponent<SpriteController>();
                if (controller.IsVisualSpriteObjectChanged(visualSprite))
                {
                    continue;
                }
                controller.BindVisualSpriteObject(visualSprite);
                controller.FadeOutForUpdate();
                continue;
            }
            else
            {
                var spritePerfab = Resources.Load<GameObject>(visualSprite.prefab);
                var sprite = Instantiate(spritePerfab);
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
