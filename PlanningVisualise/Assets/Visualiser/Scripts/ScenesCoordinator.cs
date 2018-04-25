using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;

public class ScenesCoordinator : MonoBehaviour
{
    public static ScenesCoordinator Coordinator;

    Dictionary<string, object> sceneParameters;

    private void Awake()
    {
        if (Coordinator == null)
        {
            Coordinator = this;
        }
        DontDestroyOnLoad(gameObject);

        sceneParameters = new Dictionary<string, object>();
    }

    public object FetchParameters(string sceneName)
    {
        return sceneParameters[sceneName];
    }

    public void PushParameters(string sceneName, object parameters)
    {
        sceneParameters.Add(sceneName, parameters);
    }

    private void Start()
    {
        var vstage1 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.2f, maxX = 0.4f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.4f, maxX = 0.6f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.6f, maxX = 0.8f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 1.0f, minY = 0.2f, maxY = 0.4f },
            }
        };
        var vstage2 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.2f, maxX = 0.4f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.2f, maxX = 0.4f, minY = 0.4f, maxY = 0.6f },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.6f, maxX = 0.8f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 1.0f, minY = 0.2f, maxY = 0.4f },
            }
        };
        var vstage3 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.2f, maxX = 0.4f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.2f, maxX = 0.4f, minY = 0.4f, maxY = 0.6f },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.6f, maxX = 0.8f, minY = 0.2f, maxY = 0.4f },
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.6f, maxX = 0.8f, minY = 0.4f, maxY = 0.6f },
            }
        };
        var vsolution = new VisualSolutionObject
        {
            visualStages = new VisualStageObject[] { vstage1, vstage2, vstage3 }
        };
        var json = JsonUtility.ToJson(vsolution);

        Coordinator.PushParameters("Visualisation", json);
        SceneManager.LoadScene("Visualisation");
    }
}
