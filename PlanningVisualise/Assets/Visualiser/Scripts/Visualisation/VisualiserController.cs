
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
using System.Collections;
using System.Diagnostics;
using Debug = UnityEngine.Debug;
using UnityEngine.EventSystems;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Visualiser
{
    /*
     * The controller of the entire visualisation
     * It manages the solution file and all visual objects in every stage
     */
    public class VisualiserController : MonoBehaviour
    {
        // Editor interface
        public Transform SubgoalPanel;
        public GameObject AniFrame;
        public GameObject InforScreen;
        public GameObject Speedbar;
        public GameObject stepButtonPrefab;
        public GameObject[] StepsButtons;


        // Private fields
        ScenesCoordinator coordinator = ScenesCoordinator.Coordinator; // Manages scenes
        VisualSolutionObject visualSolution; // Contains all the information of a solution
        Dictionary<string, GameObject> spritePool = new Dictionary<string, GameObject>(); // Visible objects pool

        int frameCount = 0; // Indicates the progress of an animation
        bool playing;   // Indicates if palying animation

        // dynamic interface


        public SimpleObjectPool buttonObjectPool;
        public Transform stepPanel;


        // Use this for initialization
        void Start()
        {
            // Reads visualisation file data
            var parameters = coordinator.FetchParameters("Visualisation") as string;

            // Creates a visual solution
            visualSolution = JsonUtility.FromJson<VisualSolutionObject>(parameters);

            // ------- json parsing work around
            var jo = JsonConvert.DeserializeObject<Dictionary<string, object>>(parameters);
            var smjo = JObject.FromObject(jo["subgoalMap"]);
            var spjo = JObject.FromObject(jo["subgoalPool"]);
            var smjs = smjo.ToString(Formatting.None);
            var spjs = spjo.ToString(Formatting.None);
            var sm = JsonConvert.DeserializeObject<SubgoalMapDictionary>(smjs);
            var sp = JsonConvert.DeserializeObject<SubgoalPoolDictionary>(spjs);
            for (var i = 0; i < sm.m_keys.Length; ++i)
            {
                visualSolution.subgoalMap.Add(sm.m_keys[i], sm.m_values[i]);
            }
            for (var i = 0; i < sp.m_keys.Length; ++i)
            {
                visualSolution.subgoalPool.Add(sp.m_keys[i], sp.m_values[i]);
            }
            // -------- 


            UnityEngine.Debug.Log(parameters);
            Debug.Log("transferType" + visualSolution.transferType);
            // Renders the first frame of the visualisation
            var visualStage = visualSolution.NextStage();
            RenderSubgoals();
            RenderSteps(visualSolution);
            RenderFrame(visualStage);
            RenderInformationFrame(visualStage);
            stepButtonPrefab.GetComponent<Button>().interactable = false; ;


        }

        public SimpleObjectPool subgoalPool = new SimpleObjectPool();
        public void RenderSubgoals()
        {
            foreach (var subgoal in visualSolution.subgoalMap)
            {
                var stageIndex = subgoal.Key;
                var subgoalName = subgoal.Value;
                GameObject subgoalBtn = subgoalPool.GetObject();
                subgoalBtn.transform.SetParent(SubgoalPanel, false);

                var btnText = stageIndex + ". ";
                foreach (var sn in subgoalName)
                {
                    btnText += sn + " | ";
                }
                var textCompt = subgoalBtn.GetComponentInChildren<Text>();
                textCompt.text = btnText;
                textCompt.alignment = TextAnchor.MiddleLeft;
                Button btnComp = subgoalBtn.GetComponent<Button>();
                btnComp.onClick.AddListener(() =>
                {
                    PresentStageByIndex(stageIndex);
                });

                subgoalBtn.SetActive(true);
            }
        }


        public void PresentStageByIndex(int index)
        {
            var stage = visualSolution.GetStageByIndex(index);
            visualSolution.setCurrentStage(index);
            TryRenderFrame(stage);
            TryRenderInformationFrame(stage);
        }

        public void RenderSteps(VisualSolutionObject visualSolution)
        {
            int numberOfSteps = visualSolution.getTotalStages();
            StepsButtons = new GameObject[numberOfSteps];
            Debug.Log(numberOfSteps);
            for (int i = 0; i < numberOfSteps; i++)
            {
                int tempInt = i;

                // Create Step button
                GameObject goButton = buttonObjectPool.GetObject();
                goButton.transform.SetParent(stepPanel, false);
                // Add Stage name as child component of button
                goButton.SetActive(true);

                var stage = visualSolution.visualStages[i].stageName;
                goButton.GetComponentInChildren<Text>().text = i + ". " + stage;
                StepsButtons[i] = goButton;
                Button tempButton = goButton.GetComponent<Button>();

                tempButton.onClick.AddListener(() => ButtonClicked(tempInt));


            }
        }


        public void highlightButton(int index)
        {

            EventSystem.current.GetComponent<EventSystem>().SetSelectedGameObject(null);
            StepsButtons[index].GetComponent<Button>().Select();


        }

        void ButtonClicked(int buttonNo)
        {
            Debug.Log("Button clicked = " + buttonNo);
            PresentCurrent(buttonNo);
        }

        void setCurrentStageIndex(int i)
        {
            visualSolution.setCurrentStage(i);
        }
        int getCurrentStageIndex()
        {
            return visualSolution.getCurrentStage();
        }


        //      #region UI event handlers


        // UI event handler: Presents the contents of next stage
        public void PresentLastStage()
        {
            int lastStageNumber = visualSolution.getTotalStages() - 1;
            var stages = visualSolution.visualStages;

            TryRenderFrame(stages[lastStageNumber]);
            TryRenderInformationFrame(stages[lastStageNumber]);
            highlightButton(lastStageNumber);





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
            setCurrentStageIndex(i);
            Pasue();
            var stages = visualSolution.visualStages;
            //highlightButton(i);
            TryRenderFrame(stages[i]);
            TryRenderInformationFrame(stages[i]);


        }

        // UI event handler: Presents the contents of current stage
        public void PresentCurrentSavedState()
        {
            PresentCurrent(getCurrentStageIndex());
        }


        // UI event handler: Cleans up visualisation states and goes back to the first stage
        public void ResetStage()
        {
            Pasue();
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
                if (spriteobject.GetComponent<SpriteController>().IsAnimating())
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
            //get subgoals
            var stageIndex = visualSolution.GetCurrentStageIndex();
            var subgoalNames = visualSolution.GetSubgoalNames(stageIndex);
            var subgoalObjectNames = visualSolution.GetSubgoalObjectNames(stageIndex);
            //highlight stage object for rendering
            highlightButton(getCurrentStageIndex());
            //Render all visual sprite objects of current visual stage
            foreach (var visualSprite in visualStage.visualSprites)
            {
                //Check existin
                if (spritePool.ContainsKey(visualSprite.name))
                {
                    var sprite = spritePool[visualSprite.name];
                    var controller = sprite.GetComponent<SpriteController>();
                    controller.UpdateState(visualSprite);
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
                    sprite = imageString != null
                        // Render custom prefab image
                        ? UIVisualSpriteFactory.CreateCustom(imageString)
                        // Render built-in prefab
                        : UIVisualSpriteFactory.CreateBuiltIn(visualSprite.prefabImage);
                    // Set parent relationship
                    sprite.transform.SetParent(AniFrame.transform, false);
                    // Store in sprite pool
                    spritePool.Add(visualSprite.name, sprite);
                    // Initialise sprite controller and start presenting the object
                    var controller = sprite.GetComponent<SpriteController>();
                    controller.Init(visualSprite);
                    controller.Present();
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
                    controller.DisapperAndDestory();
                }
            }

            // set subgoals
            foreach (var sprite in spritePool)
            {
                var controller = sprite.Value.GetComponent<SpriteController>();
                var flag = subgoalObjectNames.Contains(sprite.Key);
                controller.SetSubgoal(flag);

            }
        }
    }
}