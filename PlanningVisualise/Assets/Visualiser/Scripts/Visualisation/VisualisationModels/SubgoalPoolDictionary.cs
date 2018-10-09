
/*
 * File name :SubgoalPoolDictionary
 * This file has datastructure for subgoal mapping process
 */
using System;
using Newtonsoft.Json;

// Data structure for subgoal mapping
namespace Visualiser
{
    [JsonObject]
    public class SubgoalPoolDictionary
    {
        public string[] m_keys;
        public string[][] m_values;
    }
}
