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
                new VisualSpriteObject { prefab = "Block", name = "E",  minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { prefab = "Block", name = "B",  minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray },
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.65f, maxX = 0.75f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.45f, maxX = 0.55f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black }


            }
        };
        var vstage2 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { prefab = "Block", name = "B",  minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.65f, maxX = 0.75f, minY = 0.6f, maxY = 0.7f, color = Color.yellow},
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.65f, maxX = 0.75f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black }
            }
        };
        var vstage3 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.8f, maxX = 0.9f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
            }
        };
        var vstage4 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
           {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.5f, maxX = 0.6f, minY = 0.6f, maxY = 0.7f , color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray },
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "",  minX = 0.5f, maxX = 0.6f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
           }
        };
        var vstage5 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
           {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "B",minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.8f, maxX = 0.9f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
           }
        };
        var vstage6 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
          {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { prefab = "Block", name = "C",  minX = 0.65f, maxX = 0.75f, minY = 0.6f, maxY = 0.7f, color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "B",  minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "",  minX = 0.65f, maxX = 0.75f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
          }
        };
        var vstage7 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
          {
                new VisualSpriteObject { prefab = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.35f, maxX = 0.45f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
          }
        };
        var vstage8 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
         {
                new VisualSpriteObject { prefab = "Block", name = "E",  minX = 0.2f, maxX = 0.3f, minY = 0.6f, maxY = 0.7f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "B",minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "", minX = 0.2f, maxX = 0.3f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
         }
        };
        var vstage9 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
        {
                new VisualSpriteObject { prefab = "Block", name = "E",minX = 0.35f, maxX = 0.45f, minY = 0.5f, maxY = 0.6f, color = Color.red},
                new VisualSpriteObject { prefab = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { prefab = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { prefab = "Block", name = "D",  minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { prefab = "Block", name = "B", minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { prefab = "Claw", name = "",minX = 0.35f, maxX = 0.45f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { prefab = "Board", name = "", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
        }
        };
        var text = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
         {
                new VisualSpriteObject { prefab = "Text", name = "",minX = 0.4f, maxX = 0.5f, minY = 0.5f, maxY = 0.6f, color = Color.red}
        }
        };
        var vsolution = new VisualSolutionObject
        {
            visualStages = new VisualStageObject[] { vstage1, vstage2, vstage3, vstage4, vstage5, vstage6, vstage7, vstage8, vstage9 }
        };
        var json = JsonUtility.ToJson(vsolution);

        Coordinator.PushParameters("Visualisation", json);
        SceneManager.LoadScene("Visualisation");
    }
}