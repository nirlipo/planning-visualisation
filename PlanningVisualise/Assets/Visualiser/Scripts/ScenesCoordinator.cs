using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;
using System.IO;
using System.Text;
using Visualiser;

public class ScenesCoordinator : MonoBehaviour
{
    public static ScenesCoordinator Coordinator;
    Dictionary<string, object> sceneParameters;
	private string domaintxt;
	private string problemtxt;
	private string animationprofile;
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
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E",  minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B",  minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.65f, maxX = 0.75f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.45f, maxX = 0.55f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black }


            }
        };
        var vstage2 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B",  minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.65f, maxX = 0.75f, minY = 0.6f, maxY = 0.7f, color = Color.yellow},
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.65f, maxX = 0.75f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black }
            }
        };
        var vstage3 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
            {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B", minX = 0.5f, maxX = 0.6f, minY = 0.3f, maxY = 0.4f, color = Color.blue },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.8f, maxX = 0.9f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
            }
        };
        var vstage4 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
           {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B", minX = 0.5f, maxX = 0.6f, minY = 0.6f, maxY = 0.7f , color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.gray },
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw",  minX = 0.5f, maxX = 0.6f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
           }
        };
        var vstage5 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
           {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.65f, maxX = 0.75f, minY = 0.3f, maxY = 0.4f, color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B",minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.8f, maxX = 0.9f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
           }
        };
        var vstage6 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
          {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A", minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C",  minX = 0.65f, maxX = 0.75f, minY = 0.6f, maxY = 0.7f, color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B",  minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw",  minX = 0.65f, maxX = 0.75f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
          }
        };
        var vstage7 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
          {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E", minX = 0.2f, maxX = 0.3f, minY = 0.3f, maxY = 0.4f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B", minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.35f, maxX = 0.45f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
          }
        };
        var vstage8 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
         {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E",  minX = 0.2f, maxX = 0.3f, minY = 0.6f, maxY = 0.7f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D", minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B",minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "Claw", minX = 0.2f, maxX = 0.3f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
         }
        };
        var vstage9 = new VisualStageObject
        {
            visualSprites = new VisualSpriteObject[]
        {
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "E",minX = 0.35f, maxX = 0.45f, minY = 0.5f, maxY = 0.6f, color = Color.red},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "A",minX = 0.35f, maxX = 0.45f, minY = 0.3f, maxY = 0.4f, color = Color.green},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "C", minX = 0.35f, maxX = 0.45f, minY = 0.4f, maxY = 0.5f, color = Color.blue},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "D",  minX = 0.8f, maxX = 0.9f, minY = 0.3f, maxY = 0.4f, color = Color.gray},
                new VisualSpriteObject { showName = true, prefabImage = "Block", name = "B", minX = 0.8f, maxX = 0.9f, minY = 0.4f, maxY = 0.5f, color = Color.yellow },
                new VisualSpriteObject { showName = false, prefabImage = "Claw", name = "",minX = 0.35f, maxX = 0.45f, minY = 0.7f, maxY = 0.8f, color = Color.black },
                new VisualSpriteObject { showName = false, prefabImage = "Board", name = "Board", minX = 0.1f, maxX = 0.9f, minY = 0.28f, maxY = 0.32f, color = Color.black },
        }
        };
        var vsolution = new VisualSolutionObject
        {
            visualStages = new VisualStageObject[] { vstage1, vstage2, vstage3, vstage4, vstage5, vstage6, vstage7, vstage8, vstage9 }
        };
        var json = JsonUtility.ToJson(vsolution);

  	
    }

	// Interface for other objects to use 
	public void uploadallfile(){
		StartCoroutine (generateVisualiser ());
	}

	// Make a POST request to the server for the visualiser file
	IEnumerator generateVisualiser(){
		//generate a unique boundary
		byte[] boundary = UnityWebRequest.GenerateBoundary();
		Debug.Log ("test"+domaintxt);
		List<IMultipartFormSection> formData = new List<IMultipartFormSection>();
		formData.Add( new MultipartFormDataSection("domain",domaintxt ));
		formData.Add( new MultipartFormDataSection("problem",problemtxt ));
		formData.Add( new MultipartFormDataSection("animation",animationprofile ));;
		//serialize form fields into byte[] => requires a bounday to put in between fields
		byte[] formSections = UnityWebRequest.SerializeFormSections(formData, boundary);
        UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:8000/upload/pddl", formData);
		www.uploadHandler =  new UploadHandlerRaw(formSections);
		www.SetRequestHeader("Content-Type", "multipart/form-data; boundary="+ Encoding.UTF8.GetString(boundary));
		yield return www.SendWebRequest();

		if(www.isNetworkError || www.isHttpError) {
			Debug.Log(www.error);
		}
		else {
			Debug.Log("Form upload complete!");
			Coordinator.PushParameters ("Visualisation", www.downloadHandler.text);
			SceneManager.LoadScene ("Visualisation");
		}
	}
	public void setDomain(string domain){
		this.domaintxt = domain;
	}
	public void setProblem(string problem){
		this.problemtxt = problem;
	}
	public void setAnimation(string animation){
		this.animationprofile = animation;
	}
}
