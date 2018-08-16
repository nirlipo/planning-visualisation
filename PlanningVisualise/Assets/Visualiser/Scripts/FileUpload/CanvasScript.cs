using UnityEngine;
using System.Collections;
using System.Runtime.InteropServices;
using UnityEngine.UI;

// Script for Opening file panel and read file in built using the Java script plugin.
public class CanvasScript : MonoBehaviour {
	[DllImport("__Internal")]
	private static extern void UploaderCaptureClick();
	public GameObject domainbox;
	public GameObject problembox;
	public GameObject animationbox;
	private string type;

	IEnumerator LoadTexture (string url) {
		WWW file = new WWW (url);
		yield return file;
        string data = file.text;
		string name = url.Split('/')[url.Split('/').Length-1];
		//Assigning file to corresponding variable and showing file name on UI
		if (type == "Domain") {
			ScenesCoordinator.Coordinator.setDomain (data);
			domainbox.GetComponent<InputField> ().text = name;

		} else if (type == "Problem") {
			ScenesCoordinator.Coordinator.setProblem (data);
			problembox.GetComponent<InputField> ().text = name;

		} else {
			ScenesCoordinator.Coordinator.setAnimation (data);
			animationbox.GetComponent<InputField> ().text = name;

		}
	}

	//Recieved call from Javascript code
	void FileSelected (string url) {
		StartCoroutine(LoadTexture (url));
	}

	//trigger open file panel
	public void OnButtonPointerDown (string type) {
		this.type = type;
#if UNITY_EDITOR
		string path;
		if (type == "Animation")
			path = UnityEditor.EditorUtility.OpenFilePanel("Open image","","json");
		else
			path = UnityEditor.EditorUtility.OpenFilePanel("Open image","","pddl");
		if (!System.String.IsNullOrEmpty (path))
			FileSelected ("file:///" + path);
#else
			UploaderCaptureClick ();
#endif
	}
}