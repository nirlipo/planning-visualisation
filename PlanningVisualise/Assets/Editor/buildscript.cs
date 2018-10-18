///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
 * 
 * Purpose: Buildscript - run at build time. Ensures correct scenes are loaded.
 * Authors: Tom, Collin, Hugo and Sharukh
 * Date: 14/08/2018
 * 
 * /
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  */

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
public class buildscript{

	static void build(){
		string[] scene = { 
			"Assets/Visualiser/Scenes/Landing Page.unity", 
			"Assets/Visualiser/Scenes/Start.unity",
			"Assets/Visualiser/Scenes/Visualisation.unity",
			"Assets/Visualiser/Scenes/NetworkError.unity"
		};
		string path = "buildweb/";
		BuildPipeline.BuildPlayer (scene, path, BuildTarget.WebGL, BuildOptions.None);
	}
}
