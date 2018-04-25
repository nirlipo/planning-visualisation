using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class VisualiserController : MonoBehaviour
{
    ScenesCoordinator coordinator = ScenesCoordinator.Coordinator;

    VisualSolutionObject visualSolution;

    public GameObject AniFrameOne;
    public GameObject AniFrameTwo;

    GameObject presentingAniPanel;

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

    private void SwitchPresentingAniFrame()
    {
        //var previousFrame = presentingAniPanel;
        //previousFrame.SetActive(false);
        //previousFrame.transform.DetachChildren();

        //presentingAniPanel = presentingAniPanel == AniFrameOne ? AniFrameTwo : AniFrameOne;
        //presentingAniPanel.SetActive(true);
        var animator1 = AniFrameOne.GetComponent<Animator>();
        var animator2 = AniFrameTwo.GetComponent<Animator>();
        if (presentingAniPanel == AniFrameOne)
        {
            animator1.SetTrigger(Animator.StringToHash("ToAniFrameTwo"));
            animator2.SetTrigger(Animator.StringToHash("ToAniFrameTwo"));
            presentingAniPanel = AniFrameTwo;
        }else
        {
            animator1.SetTrigger(Animator.StringToHash("ToAniFrameOne"));
            animator2.SetTrigger(Animator.StringToHash("ToAniFrameOne"));
            presentingAniPanel = AniFrameOne;
        }
    }

    private void TryRenderFrame(VisualStageObject visualStage)
    {
        if (visualStage != null)
        {
            SwitchPresentingAniFrame();
            RenderFrame(visualStage);
        }
    }

    private void RenderFrame(VisualStageObject visualStage)
    {
        foreach (var visualSprite in visualStage.visualSprites)
        {
            var spritePerfab = Resources.Load<GameObject>(visualSprite.prefab);
            var sprite = Instantiate(spritePerfab);
            var rectTransform = sprite.GetComponent<RectTransform>();
            rectTransform.anchorMin = new Vector2(visualSprite.minX, visualSprite.minY);
            rectTransform.anchorMax = new Vector2(visualSprite.maxX, visualSprite.maxY);
            rectTransform.offsetMin = new Vector2(0, 0);
            rectTransform.offsetMax = new Vector2(0, 0);
            sprite.transform.SetParent(presentingAniPanel.transform, false);

            var emptyUIObject = Resources.Load<GameObject>("EmptyUIObject");
            var spriteName = Instantiate(emptyUIObject);
            var label = spriteName.AddComponent<Text>();
            label.font = Resources.Load<Font>("Arial");
            label.color = Color.black;
            label.text = visualSprite.name;
            label.alignment = TextAnchor.MiddleCenter;
            label.resizeTextForBestFit = true;
            var nameRectTransform = spriteName.GetComponent<RectTransform>();
            nameRectTransform.anchorMin = new Vector2(0, 0);
            nameRectTransform.anchorMax = new Vector2(1, 1);
            nameRectTransform.offsetMin = new Vector2(0, 0);
            nameRectTransform.offsetMax = new Vector2(0, 0);
            spriteName.transform.SetParent(sprite.transform, false);
        }
    }
}
