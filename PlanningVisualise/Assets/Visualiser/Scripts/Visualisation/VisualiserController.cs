
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: The controller of the entire visualisation [********Important file**********]
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * Reviewers: Sharukh, Gang and May
 * Review date: 10/09/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */



using UnityEngine;
using System.Collections.Generic;
using UnityEngine.UI;
using System;
using System.Linq;
namespace Visualiser
{
    /*
     * The controller of the entire visualisation
     * It manages the solution file and all visual objects in every stage
     */
    public class VisualiserController : MonoBehaviour
    {
        // Editor interface
        public GameObject AniFrame;
        public GameObject InforScreen;
        public GameObject Speedbar;

        // Private fields
        ScenesCoordinator coordinator = ScenesCoordinator.Coordinator; // Manages scenes
        VisualSolutionObject visualSolution; // Contains all the information of a solution
        Dictionary<string, GameObject> spritePool = new Dictionary<string, GameObject>(); // Visible objects pool

        int frameCount = 0; // Indicates the progress of an animation
        bool playing;   // Indicates if palying animation

        // dynamic interface

        public GameObject buttonPrefab;
        public GameObject stepPanel;

        // Use this for initialization

        void Start()
        {
            // Reads visualisation file data
            var parameters = coordinator.FetchParameters("Visualisation") as string;

            // Creates a visual solution
            visualSolution = JsonUtility.FromJson<VisualSolutionObject>(parameters);
            Debug.Log(parameters);
            Debug.Log("transferType" + visualSolution.transferType);
            // Renders the first frame of the visualisation
            var visualStage = visualSolution.NextStage();
            RenderFrame(visualStage);
            RenderSteps(visualSolution);
            RenderInformationFrame(visualStage);
        }

        private void RenderSteps(VisualSolutionObject visualSolution)
        {
            int numberOfSteps = visualSolution.getTotalStages();
            Debug.Log(numberOfSteps);
            for (int i = 0; i < numberOfSteps; i++)
            {

                string stepName = visualSolution.visualStages[i].getStageName();
                // Create Step button
                GameObject button = (GameObject)Instantiate(buttonPrefab);
                // Attach button to Step panel
                button.transform.SetParent(stepPanel.transform);
                // Add Stage name as child component of button
                button.GetComponentInChildren<Text>().text = i + "." + stepName;
                button.GetComponent<Button>().onClick.AddListener(

                            () => { PresentSelectedStage(tokenizerToGetIndex(button.GetComponentInChildren<Text>().text)); }

                    );

            }
        }

        private int tokenizerToGetIndex(string indexedStepName)
        {
            int index = 0;


            string[] tokens = indexedStepName.Split('.');
            return Int32.TryParse(tokens[0], out index);
        }

        //      #region UI event handlers

        // UI event handler: Presents the contents of selected stage

        public void PresentSelectedStage(int stage)
        {
            var visualStage = visualSolution.visualStages[stage];
            TryRenderFrame(visualStage);
            TryRenderInformationFrame(visualStage);
        }

        // UI event handler: Presents the contents of next stage
        public void PresentNextStage()
        {
            var visualStage = visualSolution.NextStage();
            TryRenderFrame(visualStage);
            TryRenderInformationFrame(visualStage);


        }

        // UI event handler: Presents the contents of previous stage
        public void PresentPreviousStage()
        {
            var visualStage = visualSolution.PreviousStage();
            TryRenderFrame(visualStage);
            TryRenderInformationFrame(visualStage);
        }

        // UI event handler: Presents the contents of current stage
        public void PresentCurrent(int i)
        {
            var stages = visualSolution.visualStages;
            TryRenderFrame(stages[i]);
            TryRenderInformationFrame(stages[i]);

        }

        // UI event handler: Cleans up visualisation states and goes back to the first stage
        public void ResetStage()
        {
            var visualStage = visualSolution.ResetStage();
            TryRenderFrame(visualStage);
        }

        // UI event handler: Plays visualisation (animation)
        public void Play()
        {
            playing = true;
        }

        // UI event handler: Pasues visualisation (animation), but all states are remained
        public void Pasue()
        {
            playing = false;
            frameCount = 0;
        }

        // UI event handler: Jumps to user manual page 
        public void btnHelp()
        {

            Application.OpenURL("https://www.youtube.com/watch?v=8oVxPHSoRKA&t=3m22s");
        }
        //  #endregion
        bool Allstop()
        {
            foreach (GameObject spriteobject in spritePool.Values)
            {
                if (spriteobject.GetComponent<SpriteController>().moving())
                {
                    return false;
                }
            }
            return true;
        }
        // Unity built-in method, it will be fired in every frame
        void Update()
        {
            // Plays animation
            if (playing && Allstop())
            {
                PresentNextStage();
            }
        }

        // Renders a frame if it is not null
        void TryRenderFrame(VisualStageObject visualStage)
        {
            if (visualStage != null)
            {
                RenderFrame(visualStage);
            }
        }

        void TryRenderInformationFrame(VisualStageObject visualStage)
        {
            if (visualStage != null)
            {
                RenderInformationFrame(visualStage);
            }
        }
        //Render a frame (stage), stage information of given stage is rendered
        void RenderInformationFrame(VisualStageObject visualStage)
        {
            string emptyString = "";
            String stepInformation = visualStage.getStageInfo();
            if (stepInformation == null || stepInformation.Equals(emptyString))
            {
                InforScreen.GetComponentInChildren<Text>().text = "No Step Informattion available";
            }

            else
            {
                InforScreen.GetComponentInChildren<Text>().text = stepInformation;
            }

        }

        // Renders a frame (stage), all visible objects will be drawn on the screen in this process
        void RenderFrame(VisualStageObject visualStage)
        {
            //Render all visual sprite objects of current visual stage
            foreach (var visualSprite in visualStage.visualSprites)
            {
                //Check existin
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
                    //controller.FadeOutForUpdate();
                    controller.MoveToNewPosition();

                }
                /*
                 * This part should be refactored in order to achieve better OO design
                 * Some code placed here are for temporary experiments
                 */
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
                        var imgSprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), new Vector2(0.5f, 0.5f));
                        imageComp.sprite = imgSprite;

                        //add canvas
                        var canvas = sprite.GetComponent<Canvas>();
                        canvas.sortingOrder = visualSprite.depth + 1;
                        canvas.overrideSorting = true;
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
                    sprite.transform.SetParent(AniFrame.transform, false);
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