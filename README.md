# Planning Visualisation

This is an internal project. The client needs a tool to help them visualise AI planning solution. The tool will enable creates, views and exports animation.


# How to Edit Scene

Open Planning Visualisation folder as an Unity workspace. Drag scenes file to the Hierarchy to start editing the GameObjects in the scene, Scene files are under the Scene folders
in the AnimationProfile and Visualier folders.

# How to Edit Script

Script can be created directly in the Assets directories, simply right click Create -> C# Script. If scripts are going to be attached to a game object, the class should be extending
MonoBehaviour. Unity would recommend using their monoDeveloper to code for the guideword when using Unity.Engine.

# How to Run

Put only the scene you want to test in the Hierarchy and press the play button at the top.

# How to Build WebGL

After Selecting all the scene with the starting Scene being the first one clicked
There is a WebGL module that need to be installed, open the installer again and tick only the WebGL module to be installed.
After the module is loaded, in Files -> Build Setting, select WebGL and click Player Setting, the inspector on your right will show the setting of the web player, select the NewTemplate
as our template, and click Build and Run in the Build Setting window and select the Built file location. This may take a while, after it is finished, the Browser will open the First Scene
of the project. Later, unless we have a new built, we can go to the directory of the built and open the index.html. Notice that Chrome will not allowed to open html file locally, so better
to set up a server or using other Browser to open the index.html.

See the User Guide pdf to get started.

