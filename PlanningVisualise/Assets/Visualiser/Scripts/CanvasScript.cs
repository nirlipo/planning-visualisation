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
		Debug.Log (data);
		//Assigning file to corresponding variable
		if (type == "Domain") {
			ScenesCoordinator.Coordinator.setDomain (data);
			domainbox.GetComponent<Image> ().color = Color.green;
		} else if (type == "Problem") {
			ScenesCoordinator.Coordinator.setProblem (data);
			problembox.GetComponent<Image> ().color = Color.green;
		} else {
			ScenesCoordinator.Coordinator.setAnimation (data);
			animationbox.GetComponent<Image> ().color = Color.green;
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