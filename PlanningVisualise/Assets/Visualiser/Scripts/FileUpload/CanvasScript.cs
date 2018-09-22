﻿///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: The file has fucntionality to Upload files to server
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
using UnityEngine.SceneManagement;
using System.Runtime.InteropServices;
using UnityEngine.UI;

// Script for Opening file panel and read file in built using the Java script plugin.
public class CanvasScript : MonoBehaviour
{
    [DllImport("__Internal")]
    private static extern void UploaderCaptureClick(string extensionptr);
    private InputField textfield;
    private string type;
    private string name;




    IEnumerator LoadTexture(string url)
    {
        WWW file = new WWW(url);
        yield return file;
        string data = file.text;
        textfield = GameObject.Find(type).GetComponent<InputField>();
        textfield.text = name;
        //Assigning file to corresponding variable and showing file name on UI



        if (type == "Domain")
        {
            ScenesCoordinator.Coordinator.setDomain(data);

        }
        else if (type == "Problem")
        {
            ScenesCoordinator.Coordinator.setProblem(data);

        }
        else if (type == "Animation")
        {
            ScenesCoordinator.Coordinator.setAnimation(data);

        }else if (type == "visualisationFile")
        {
        	ScenesCoordinator.Coordinator.PushParameters("Visualisation", data);
        	SceneManager.LoadScene("Visualisation");

        }
        
    }

    //Recieved call from Javascript code
    void FileSelected(string url)
    {

        StartCoroutine(LoadTexture(url));
    }
    //Getting the file name
    void SetFileName(string name)
    {
        this.name = name;
    }
    //Assign customsolver 
    public void setCustomSolver()
    {
        
        string solverAddress;
        solverAddress = solverbox.GetComponent<InputField>().text;
        ScenesCoordinator.Coordinator.setCustomSolver(solverAddress);
    }
   
    //trigger open file panel
    public void OnButtonPointerDown(string type)
    {
        this.type = type;
#if UNITY_EDITOR
		string path;
		if (type == "Animation")
			path = UnityEditor.EditorUtility.OpenFilePanel("Open image","","json");
		else
			path = UnityEditor.EditorUtility.OpenFilePanel("Open image","","pddl");
		if (!System.String.IsNullOrEmpty (path)){
			SetFileName(path.Split('/')[path.Split('/').Length-1]);
			FileSelected ("file:///" + path);
		}
#else
		if (type == "Animation")
        	UploaderCaptureClick(".json");
        else
        	UploaderCaptureClick(".pddl");
#endif
    }
}