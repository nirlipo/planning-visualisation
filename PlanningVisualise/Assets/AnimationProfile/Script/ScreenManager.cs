/* SceneManager manage the all the scene transaction and destroying non-DetroyOnLoad gameobject
 * when resetting*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;
using System.Linq;
using System.Collections;
using System.Diagnostics;
using Debug = UnityEngine.Debug;
using UnityEngine.EventSystems;

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

	// Load the visualiser File uploading scene 
	public void loadVFGUploadScene()
	{
		Destroy (GameObject.Find ("Coordinator"));
		SceneManager.LoadScene("VFGUploader");
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

		var newURL = "https://immense-bastion-42146.herokuapp.com/help/";
		Application.OpenURL (newURL);

        // get the current URL
        /*var currentURL = Application.absoluteURL;

		if (currentURL != "") {

			// remove the unity port and trailing slash from the url
			var uri = new Uri (currentURL);
			var clean = uri.GetComponents (UriComponents.AbsoluteUri & ~UriComponents.Port,
				                     UriFormat.UriEscaped);
			if (clean [clean.Length - 1] == '/') {
				clean = clean.Remove (clean.Length - 1);
			}
            
			// Add the django port and help directory to the url, and open it
			var newURL = clean + ":8000/help/";
			Application.OpenURL (newURL);
		} else {
			var newURL = "https://immense-bastion-42146.herokuapp.com/help/";
			Application.OpenURL (newURL);
		}*/
    }

}
