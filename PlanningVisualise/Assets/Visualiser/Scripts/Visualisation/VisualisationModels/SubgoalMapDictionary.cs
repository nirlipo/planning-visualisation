using System;
using Newtonsoft.Json;

namespace Visualiser
{
    [JsonObject]
    public class SubgoalMapDictionary 
    {
        public int[] m_keys;
        public string[][] m_values;
    }
}
