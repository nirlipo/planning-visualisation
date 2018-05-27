using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class ScreenManager : MonoBehaviour
{
    // Use this for initialization
    void Start()
    {
        DontDestroyOnLoad(this);
    }
    public void loadVisualiseScene()
    {
		Destroy (GameObject.Find ("Coordinator"));
        SceneManager.LoadScene("Start");
    }
    public void loadMainScene(){
		Destroy (GameObject.Find ("Coordinator"));
        SceneManager.LoadScene("PlanningVisualise");
    }
	public void loadAnimationScene()
	{
		SceneManager.LoadScene("Visualisation");
	}

}
