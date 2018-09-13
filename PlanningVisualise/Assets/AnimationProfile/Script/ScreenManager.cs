/* SceneManager manage the all the scene transaction and destroying non-DetroyOnLoad gameobject
 * when resetting*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class ScreenManager : MonoBehaviour
{
	// Use this for initialization, the SceneManager must be a non-DetroyOnLoad gameobject
    void Start()
    {
        DontDestroyOnLoad(this);
    }

	// Load the visualiser uploading scene 
    public void loadVisualiseScene()
    {
		Destroy (GameObject.Find ("Coordinator"));
        SceneManager.LoadScene("Start");
    }
    // Load the visualiser solution uploading scene 
    public void loadVisualiseSolutionScene()
    {
        Destroy(GameObject.Find("Coordinator"));
        SceneManager.LoadScene("StartSolution");
    }
    // Load the index page scene
    public void loadMainScene(){
		Destroy (GameObject.Find ("Coordinator"));
        SceneManager.LoadScene("Landing Page");
    }
	// Load the scene for playing animation
	public void loadAnimationScene()
	{
		SceneManager.LoadScene("Visualisation");
	}
    // Goto user documentation link
    public void gotoDocumentation()
    {
        Application.OpenURL("https://bitbucket.cis.unimelb.edu.au:8445/projects/SWEN90013/repos/swen90013-2018-pl/browse?at=refs%2Fheads%2Ffeature-userdocs");
    }

}
