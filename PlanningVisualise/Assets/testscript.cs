using UnityEngine;
using System.Collections;
using PlanVisualizerArchitecture.Entity.ScriptInfoPack;
using UnityEngine.UI;

public class testscript : MonoBehaviour {
	private Script_PredicateItem[] predicates;
	//private Script_ObjectItem[] Objects = new Script_ObjectItem[10];
	private GameObject predicatesObject;
	//private GameObject ConstantObject;
	void Start(){
		gameObject.GetComponent<InputField>().onEndEdit.AddListener(endEdit);
		/*for (int i = 1; i < ConstantObject.GetComponent<Dropdown>().options.Count;i++){
			Objects [i - 1] = new Script_ObjectItem ();
			Objects[i-1].name =ConstantObject.GetComponent<Dropdown> ().options.ToArray () [i];
		}*/
	}
	public void endEdit(string text){
		this.predicatesObject = GameObject.Find ("Predicates");
		this.predicates = predicatesObject.GetComponent<predicates> ().getpredicateItems();
		int predicatevalue = this.predicatesObject.GetComponent<Dropdown> ().value-1;
		if (predicatevalue>=0)
			predicates [predicatevalue].rules = text;
	}
}
