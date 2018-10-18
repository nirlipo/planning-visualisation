/*
 * File name :SubgoalMapDictionary
 * This file has datastructure for subgoal mapping process
 */



using System;
using Newtonsoft.Json;


// Data structure for subgoal mapping
namespace Visualiser
{
    [JsonObject]
    public class SubgoalMapDictionary 
    {
        public int[] m_keys;
        public string[][] m_values;
    }
}
