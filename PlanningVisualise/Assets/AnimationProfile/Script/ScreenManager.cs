﻿/* SceneManager manage the all the scene transaction and destroying non-DetroyOnLoad gameobject
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

}
