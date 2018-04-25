using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class ScreenManager : MonoBehaviour {
	public GameObject title;
	public GameObject AniProfile;
	public GameObject PredicateList;
	// Use this for initialization
	void Start () {
		DontDestroyOnLoad (this);
	}

}
