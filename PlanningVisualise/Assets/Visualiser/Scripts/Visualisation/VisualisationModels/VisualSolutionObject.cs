using UnityEngine;
using System.Collections;
using System;
using System.Collections.Generic;

namespace Visualiser
{
    [Serializable]
    public class VisualSolutionObject
    {
        public VisualStageObject[] visualStages;
        public int transferType;
        public Dictionary<string, string> imageTable;

        int stageIndex = -1;

        public string FetchImageString(string key)
        {
            if (imageTable.ContainsKey(key))
            {
                return imageTable[key];
            }
            return null;
        }

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

        public VisualStageObject ResetStage()
        {
            stageIndex = -1;
            return NextStage();
        }
    }
}
