using UnityEngine;
using System.Collections;
using UnityEngine.UI;
namespace Visualiser
{

    public class SampleButton : MonoBehaviour
    {

        public Button buttonComponent;
        public Text stepName;
        public int stageIndex;


        private string stage;
        private VisualiserController visualiserController;


        // Use this for initialization
        void Start()
        {
            buttonComponent.onClick.AddListener(HandleClick);
        }

        public void Setup(string stageObject, int index, VisualiserController vc)
        {
            stage = stageObject;
            stageIndex = index;
            stepName.text = index + ". " + stageObject;
            visualiserController = vc;



        }

        public void HandleClick()
        {
            visualiserController.PresentCurrent(stageIndex);
        }
    }
}