"""This module is designed to help with getting a valid animation profile in JSON format"""
# -----------------------------Authorship-----------------------------------------
# -- Authors  : Gang
# -- Group    : Planning Visualisation
# -- Date     : 10/Sep/2018
# -- Version  : 1.0
# --------------------------------------------------------------------------------
# -----------------------------Reviewer-------------------------------------------
# -- Authors  :
# -- Group    :
# -- Date     :
# -- Version  :
# --------------------------------------------------------------------------------
import re
import sys
import json
import copy
from colour import Color
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"visualiserFile/predicate_solver"))
import custom_functions
#######################################################
# Input File: A animation PDDF file
# Output : A complete animation profile in JSON format
#######################################################

import adapter as adapter
def get_animation_profile(animation_pddl):
    # --------------------------------------------
    # This is just an example
    text_to_parse = animation_pddl



    # --------------------------------------------
    # Patterns that are going to be used for PREDICATE
    pattern_predicate = ":predicate"

    # --------------------------------------------
    # Final result that is going to be returned
    result = {"objects": {"default": {},
                          "predefine": {},
                          "custom": {}},
              "predicates_rules": {},
              "visual": {},
              "imageTable": {"m_keys": [],
                             "m_values": []}}
    parseVisual(copy.copy(text_to_parse),result)

    parseImage(copy.copy(text_to_parse), result)

    parsePredicate(copy.copy(text_to_parse), result)

    transfer(result)
    return json.dumps(result)

def parseVisual(text_to_parse,result):
    # --------------------------------------------
    # Patterns that are going to be used for Visual
    pattern_visual = ":visual"
    pattern_type = ":type"
    pattern_objects = ":objects"
    pattern_properties = ":properties"
    while text_to_parse.find(pattern_visual):
        # Get the value of the visual
        temp_visual_block = text_to_parse[text_to_parse.index(pattern_visual):]
        temp_visual_block = get_one_block(temp_visual_block)

        temp_visual_pattern = re.compile(pattern_visual + "\s[\w\-]+")
        temp_subshape, temp_subshape_value = temp_visual_pattern.findall(temp_visual_block)[0].split()

        sublist = {}

        # Get the value of type
        temp_regex_pattern = re.compile(pattern_type + "\s[\w\-]+")
        temp_subelement, temp_subelement_value = temp_regex_pattern.search(temp_visual_block)[0].split()
        # print(temp_subelement, temp_subelement_value)

        if "objects" in temp_visual_block:
            # Get the value of objects
            temp_objects_pattern = re.compile(pattern_objects + "\s*(\([^\)]+\)|[\w-]+)") # fix -n
            objectsStr=temp_objects_pattern.search(temp_visual_block).group(1)
            if "(" in objectsStr:
                objects_list=parse_objects(objectsStr)
            else:
                objects_list=objectsStr
            # print(objects_list)
            result["objects"][temp_subelement_value][temp_subshape_value]=[]
            if type(objects_list) in (tuple,list):
                result["objects"][temp_subelement_value][temp_subshape_value].extend(objects_list)
            else:
                result["objects"][temp_subelement_value][temp_subshape_value].append(objects_list)
        elif(temp_subelement_value=="default"):
            result["objects"][temp_subelement_value]=temp_subshape_value

        # Get the value of properties
        temp_property_block = temp_visual_block[temp_visual_block.index(pattern_properties) + len(pattern_properties):]
        temp_property_block = get_one_block(temp_property_block)
        temp_properties_pattern = re.compile("\([a-zA-Z0-9_.-]*\s[#a-zA-Z0-9_.-]*\)")
        temp_properties = temp_properties_pattern.findall(temp_property_block)
        # sublist[temp_subshape_value].append({"prefabImage": temp_subshape_value})
        for x in temp_properties:
            x, y = x.replace('(', '').replace(')', '').split()
            # if x != "base64image":
            sublist[x]=y
            # else:
            #     result["imageTable"]["m_keys"].append(temp_subshape_value)
            #     result["imageTable"]["m_values"].append(y)
        result["visual"][temp_subshape_value]=sublist

        # Get the next SHAPE item
        text_to_parse = text_to_parse[text_to_parse.index(pattern_visual) + len(pattern_visual):]

        # Stop if there is no more object to parse
        if(pattern_visual not in text_to_parse):
            break;

    return result;

def parsePredicate(text_to_parse,result):
    pattern_predicate = ":predicate"
    pattern_parameters = ":parameters"
    pattern_custom=":custom"
    pattern_priority=":priority"
    pattern_effect = ":effect"
    while text_to_parse.find(pattern_predicate):
        # Get the value of the predicate
        temp_visual_block = text_to_parse[text_to_parse.index(pattern_predicate):]
        temp_visual_block = get_one_block(temp_visual_block)

        temp_visual_pattern = re.compile(pattern_predicate + "\s[\w\-]+")
        temp_subshape, temp_subshape_value = temp_visual_pattern.findall(temp_visual_block)[0].split()
        # print(temp_visual_pattern.findall(temp_visual_block))
        # print(temp_visual_block)

        if "priority" in temp_visual_block:
            priority_pattern=re.compile(pattern_priority + "\s*(\(\d+\)|[\d]+)")
            priority=priority_pattern.findall(temp_visual_block)


        # Get the value of parameters
        temp_regex_pattern = re.compile(pattern_parameters +" "+ "\((.*?)\)")
        objectList=temp_regex_pattern.findall(temp_visual_block)[0].split()
        # Get the value of custom
        temp_custom_pattern = re.compile(pattern_custom +"\s[\w\-]+") # fix This line need to be changed to adapte array
        custom=temp_custom_pattern.findall(temp_visual_block)
        if custom:
            temp_objects, temp_objects_value = custom[0].split()
            # print(temp_objects,temp_objects_value)

        # Get the value of effect
        temp_effect_block = temp_visual_block[temp_visual_block.index(pattern_effect) + len(pattern_effect):]
        temp_effect_block = get_one_block(temp_effect_block)
        require_dic={}
        result["predicates_rules"][temp_subshape_value]=parse_rules(temp_effect_block,require_dic)
        result["predicates_rules"][temp_subshape_value]["require"]=require_dic
        result["predicates_rules"][temp_subshape_value]["objects"]=objectList
        if "priority" in temp_visual_block:
            result["predicates_rules"][temp_subshape_value]["priority"] = priority[0]
        if custom:
            result["predicates_rules"][temp_subshape_value]["custom_obj"]=[temp_objects_value]
        # result["predicates_rules"]["custom"]

        # Get the next Predicate item
        text_to_parse = text_to_parse[text_to_parse.index(pattern_predicate) + len(pattern_predicate):]

        # Stop if there is no more object to parse
        if(pattern_predicate not in text_to_parse):
            break;


def parseImage(text_to_parse,result):
    pattern_image = ":image"
    temp_image_block = text_to_parse[text_to_parse.index(pattern_image):]
    temp_image_block = get_one_block(temp_image_block)
    patternPare = re.compile(r'\((.*?)\)')
    imagePareList=patternPare.findall(temp_image_block)
    for imagePare in imagePareList:
        name,value=imagePare.split()
        result["imageTable"]["m_keys"].append(name)
        result["imageTable"]["m_values"].append(value)

#delete key and value
# def parseImage(text_to_parse,result):
#     pattern_image = ":image"
#     temp_image_block = text_to_parse[text_to_parse.index(pattern_image):]
#     temp_image_block = get_one_block(temp_image_block)
#     patternPare = re.compile(r'\((.*?)\)')
#     imagePareList=patternPare.findall(temp_image_block)
#     for imagePare in imagePareList:
#         name,value=imagePare.split()
#         result["imageTable"][name]=value

def removebacket(input):
    output = ""
    forward_bracket = 0;
    input=input.rstrip()
    length = len(input)
    if input[0]=="(" and input[length-1]==")":
        for n in range(length):
            if input[n] == "(":
                forward_bracket += 1

            if input[n] == ")":
                forward_bracket -= 1

            if forward_bracket >= 0:
                output += input[n]
            else:
                return False;

    return output[1:length-1]


#######################################################
# Input File: A string that start with "(" and end with ")"
# Output : all the content in between the parentheses
#######################################################
def get_one_block(input):
    output = ""
    forward_bracket = 0;
    for n in range(len(input)):
        if input[n] == "(":
            forward_bracket += 1

        if input[n] == ")":
            forward_bracket -= 1

        if forward_bracket >= 0:
            output += input[n]
        else:
            break;
    return output


def find_parens(s, depth=1):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)

        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            if len(pstack) == depth:
                toret[pstack.pop()] = i
            else:
                pstack.pop()

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret
def get_bracket(text,depth):
    ruleindex=find_parens(text,depth)
    rules=[]
    for start,end in ruleindex.items():
        rules.append(text[start:end+1])
    return rules
def remove_bracket(text):
    return text[1:len(text)-1]


def parse_objects(text):
    text = remove_bracket(text)
    objects = re.split(r'\s+', text)
    return objects


def parse_function(text,require_dic):
    template = {
        "fname": "",
        "obj_indexs": [],
        "settings": {
        }
    }

    name_pattern = re.compile(r'\(function\s*(\w+)\s*\(.*')
    searchName = re.search(name_pattern, text)
    name = searchName.group(1)
    template["fname"] = name
    # (objects a b c)
    objects_pattern = re.compile(r'\(objects\s+([^)]+)\)')
    searchObj = re.search(objects_pattern, text)
    objects = re.split(r'\s+', searchObj.group(1))
    template["obj_indexs"] = objects
    require=custom_functions.customf_controller(name,None,None,None,None,True)
    for key,value in require.items():
        index=int(key)
        for item in value:
            obj_name=objects[index]
            update_require(require_dic,obj_name,item)
    if "settings" in text:
        settings_pattern = re.compile(r'\(settings\s+(\s*\([^)]*\)\s*)+\)')
        searchSetting = re.search(settings_pattern, text)
        SettingStr = searchSetting.group(0)
        settingList = get_bracket(SettingStr, 2)
        for setting in settingList:
            sname, svalue = parse_objects(setting)
            template["settings"][sname] = svalue

    return {"function": template}


def parse_add(text,require_dic):
    template = {
        "add": []
    }
    reference = get_bracket(text, 2)
    if reference:
        for item in reference:
            name, value = parse_objects(item)
            template["add"].append({name: value})
            update_require(require_dic,name,value)
    digital_pattern = re.compile(r'\b\d+\b')
    digital_list = re.findall(digital_pattern, text)
    if digital_list:
        for item in digital_list:
            template["add"].append(item)
    return template


def parse_rule(rule,require_dic):
    # print(rule)
    template = {
        "left": {},
        "value": {}
    }
    rulePattern = re.compile(r'\((\w+)\s+(\([^)]+\))\s*(\(.*\)|[\w#]+)\)')
    divide_rule = re.search(rulePattern, rule)
    rule_type = divide_rule.group(1)
    left_object = divide_rule.group(2)
    right_value = divide_rule.group(3)
    middle = parse_objects(left_object)
    template["left"][middle[0]] = middle[1:]
    if "function" in rule:
        template["value"] = parse_function(right_value,require_dic)
    elif "(" not in right_value:
        value_pattern = re.compile(r'\(equal\s+\([^)]+\)\s*([\w#]+)\)')
        searchValue = re.search(value_pattern, rule)
        value = searchValue.group(1)
        template["value"]["equal"] = value
    elif "add" in right_value:
        template["value"] = parse_add(right_value,require_dic)
    elif "(" in right_value:
        name, value = parse_objects(right_value)
        template["value"]["equal"] = {name: value}
        update_require(require_dic,name,value)
    return template

def update_require(require_dic,name,value):
    if name not in require_dic:
        require_dic[name]=[]
    require_dic[name].append(value)


def parse_actionrule(rule,require_dic):
    # print(rule)
    template = {
        "action": {}
    }
    rulePattern = re.compile(r'\((\w+)\s*(\(.*\))\)')
    divide_rule = re.search(rulePattern, rule)
    rule_type = divide_rule.group(1)
    right_value = divide_rule.group(2)

    if "function" in rule:
        template["action"] = parse_function(right_value,require_dic)
    return template
def parse_rules(text,require_dic):
    template={
        "rules":[]
    }
    rules=get_bracket(text,2)
    for i,rule in enumerate(rules):
        newrule="rule"+str(i+1)
        template["rules"].append(newrule)
        if "equal" in rule or "assign" in rule:
            template[newrule]=parse_rule(rule,require_dic)
        elif "action" in rule:
            template[newrule] = parse_actionrule(rule,require_dic)
    return template





def transfer(result):
    """The function return the animation file in correct format
        Args:
            Dict: animation file json object
        Returns:
            Dict: correct animation profile
        """
    dictget(result)

    return result

def dictget(input):
    """The function transfers all the digital number string into number
     """
    if type(input) is str:
        # print(input)
        return transfer_str(input)

    if type(input) is dict:
        for k, v in input.items():
            if type(v) is dict:
                input[k]=dictget(v)
            elif type(v) is list:
                input[k]=dictget(v)
            else:
                input[k]=transfer_str(v)
    elif type(input) is list:
        for i,item in enumerate(input):
            input[i]=dictget(item)

    return input
def transfer_str(v):
    value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

    result = value.match(v)

    if (result):
        return float(v)
    elif (v.isdigit()):
        return int(v)
    elif (v == "TRUE"):
        return True
    elif (v == "FALSE"):
        return False
        # print(dict1[k])
    elif (v.lower() == "null"):
        return False
        # print(dict1[k])
    elif (check_color(v)):
        # print(v)
        return transfer_Color(v)
    else:
        return v

def transfer_Color(color):
    """
    This function transfer color name into rgba
    """


    c = Color(color).get_rgb()
    rgba = {"r": round(c[0],4),
            "g": round(c[1],4),
            "b": round(c[2],4),
            "a": 1.0
            }

    return rgba


def check_color(color):
    try:
        # Converting 'deep sky blue' to 'deepskyblue'
        color = color.replace(" ", "")
        Color(color)
        # if everything goes fine then return True
        return True
    except ValueError: # The color code was not found
        return False
if __name__ == "__main__":
    get_animation_profile()