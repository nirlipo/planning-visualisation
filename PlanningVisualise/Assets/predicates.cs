using UnityEngine;
using System.Collections;
using PlanVisualizerArchitecture.Entity.ScriptInfoPack;
using UnityEngine.UI;

public class predicates : MonoBehaviour {
	private Script_PredicateItem[] predicatesitems= new Script_PredicateItem[10];
	// Use this for initialization
	void Start () {
		gameObject.GetComponent<Dropdown>().onValueChanged.AddListener(changetext);
		for (int i = 1; i < this.GetComponent<Dropdown>().options.Count;i++){
			predicatesitems[i-1]=new Script_PredicateItem();
			predicatesitems[i-1].name =this.GetComponent<Dropdown> ().options.ToArray () [i].ToString();
			predicatesitems [i - 1].rules = null;
		}
	}
	
	// Update is called once per frame
	public Script_PredicateItem[] getpredicateItems(){
		return this.predicatesitems;
	}
	public void changetext(int index){
		GameObject predicateRule = GameObject.Find ("PredicateRules");
		if (index != 0) {
			if (predicatesitems [index - 1].rules != null)
				predicateRule.GetComponent<InputField> ().text = predicatesitems [index - 1].rules;
			else
				predicateRule.GetComponent<InputField> ().text = "";
		} else {
			predicateRule.GetComponent<InputField> ().text = "";
		}
	}
}
