using UnityEngine;
using System.Collections;
using System;

[Serializable]
public class VisualSolutionObject
{
    public VisualStageObject[] visualStages;

    int stageIndex = -1;

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
