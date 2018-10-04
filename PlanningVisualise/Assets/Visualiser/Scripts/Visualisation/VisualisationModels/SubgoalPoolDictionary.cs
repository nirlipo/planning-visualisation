using System;
using Newtonsoft.Json;

namespace Visualiser
{
    [JsonObject]
    public class SubgoalPoolDictionary
    {
        public string[] m_keys;
        public string[][] m_values;
    }
}
