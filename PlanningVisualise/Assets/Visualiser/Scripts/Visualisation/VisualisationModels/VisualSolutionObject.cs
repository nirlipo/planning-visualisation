

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: The file is the solution object which has data that is sent by the server to Unity application
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
using System.Collections.Generic;

namespace Visualiser
{
	/* This class contains all the information in the Visualisation file, including all stages
	 * and image*/
    [Serializable]
    public class VisualSolutionObject
    {
        public VisualStageObject[] visualStages;
        public int transferType;
        public ImageDictionary imageTable;
        public int numberOfStages;

        int stageIndex = -1;

		// Retrieving the image of the object from the Visualisation file
        public string FetchImageString(string key)
        {
            if (imageTable.ContainsKey(key))
            {
                return imageTable[key];
            }
            return null;
        }

		// Get the next stage of the animation
        public VisualStageObject NextStage()
        {
            if (stageIndex + 1 < visualStages.Length)
            {
                return visualStages[++stageIndex];
            }
            else
            {   
                return null;
            }
        }

		// Get the previous stage of the animation
        public VisualStageObject PreviousStage()
        {
            if (stageIndex > 0)
            {
                return visualStages[--stageIndex];
            }
            else
            {
                return null;
            }
        }

        

        // Get the initial stage of the animation
        public VisualStageObject ResetStage()
        {
            stageIndex = -1;
            return NextStage();
        }
        // Get current index
        public int getCurrentStage()
        {
            return ++stageIndex;
        }
       
        public int getTotalStages()
        {
            return visualStages.Length;
        }
    }
}
