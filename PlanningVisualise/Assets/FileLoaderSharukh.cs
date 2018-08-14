using UnityEngine;
using UnityEngine.SceneManagement;

public class FileLoaderSharukh : MonoBehaviour {

	void OnMouseUp()
    {
        SceneManager.LoadScene("Loading", LoadSceneMode.Single);
    }
   
}
