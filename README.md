# 1. System overview 

This document contains the User Guide for Planning Visualiser.

The Planning Visualiser is an open-source program which visualises solutions to Planning Problems. It is an executable Unity architecture in a browser.


## 1.1 Planning Problems

For information about Planning Problems, see http://planning.domains/


Our application uses one 'Animation Profile' per problem domain. An Animation Profile is a user-written PDDL file which tells the Visualiser how a Domain is to be visualised. See section 3.2 for more information on Animation Profiles.


## 1.2 Scope
Planning Visualiser currently has Animation Profiles for four problem domains; Blocks, Grid, Towers of Hanoi, and Logistics. Other simple problem domains may be added by writing an Animation Profile (see section 3.2).


Planning visualiser can generate a solution using the solver on http://planning.domains/ . Alternatively, the user can provide their own solution from any solver, provided it conforms to the correct format.



# 2. Getting Started


## 2.1 In-browser (recommended)

1. Visit https://planning-visualise.herokuapp.com/index.html


## 2.2 Local server (For Development)

### 2.2.1 Install dependencies
1. **Unity** - Install the Version 2018.2.1f1  from https://unity3d.com/. When installing, select "Include WebGL"
2. **Django REST** - Follow the tutorial at http://www.django-rest-framework.org/tutorial/quickstart/

### 2.2.2 Install project
1. Clone the project from https://bitbucket.cis.unimelb.edu.au:8445/projects/SWEN90013/repos/swen90013-2018-pl/browse


### 2.2.3 Run
1. Run the server with the command 'python manage.py runserver' in the directory of the file manage.py (/swen90013-2018-pl/server)
2. Open the project in Unity.The Unity application will communicate with the local server


## 2.3 Deployment (For Development)

1. Follow the steps to setup the local server in 2.2
2. Build the project from the File menu in Unity
3. Be sure to include all scenes in the build


# 3. Using the system


## 3.1 Visualise Built-in Domains

### 3.1.1 Select Files

1. Select files for the Problem, Domain and Animation Profile. Files for existing domains are located in the bitbucket repository under Test/testfile.
2. Click “√” button.

### 3.1.2 Visualise Solution

The visualisation page has four main parts.
1. Steps Panel: Shows all the steps in the solution 
2. Step Information Panel: show detailed information for each step, including actions.
3. Animation Panel: displays the animation
4. Control Panel: buttons to control the animation. These include changing the speed of the animation, Play/Pause, Step Forward/Backwards, Replay


## 3.2 Visualise a new Domain

This can be done, for many simple domains, with no modification to the system.

To add a new domain:

1. Write or obtain a Domain PDDL file for the problem domain. Many domains can be found at https://bitbucket.org/planning-researchers/classical-domains/src/208a850d2ff2a27068329ad578ad99af9ec7e5c5/classical/?at=master
2. Write an Animation Profile which corresponds to the domain file. For documentation on the Animation Profile Language, see the file 'Animation Profile Language'
3. Follow the steps in 3.1 to view a visualisation with the new Animation Profile.

## 3.3 Video Record a Visualisation 


A video recording of the visualisation can be created so that the final animation can be easily shared or re-reviewed independently of the system. The below recommendations are one way of recording the animation, however many other methods and tools exist to achieve this.  

### 3.3.1 MacOS Users


To video record the visualisation, have the animation you wish to record on your screen, then complete the following steps:
1. Launch the pre-installed QuickTime Player application
2. Select "File" and choose "New Screen Recording"
3. To decide whether mouse clicks and sounds appear in your recording or not, click the small, white arrow and select the appropriate options from the drop-down menu. 
4. When ready, click the red record button. 
5. You will need to select what you want to record. To record the entire screen, click once anywhere. To record only a portion of it, click and drag a box and then click "Start Recording."
6. When finished, navigate to the menu bar and click the stop recording button designated by the square symbol.
7. To save your recording, click "File" and then"Save", and choose an appropriate save location and name for the recording. 
8. View and share file as you would with any other media file. 


* Instructions adapted from https://www.digitaltrends.com/computing/how-to-record-your-computer-screen/


### 3.3.2 Windows Users 


To video record the visualisation, have the animation you wish to record on your screen, then complete the following steps:
1. Press the Windows key and the letter G at the same time to open the Game Bar dialog (this will pop up on your screen).
2. Check the "Yes, this is a game" checkbox to load the Game Bar. This is the procedure regardless of what you are recording.
3. Click on the Start Recording button, or press Win + Alt + R to start screen recording. 
4. Stop the recording by clicking on the red recording button on the pop-up. 
5. The video can be accessed via your Videos folder, inside the Captures folder.  




* Instructions adapted from https://www.laptopmag.com/articles/how-to-video-screen-capture-windows-10

# 4. Extending the system


Planning Visualiser is modular and can be extended in multiple ways.

Many simple domains can be captured in the existing Animation Profile language. For more complex domains, modifications may need to be made to the application. These are detailed in 4.3. and 4.4


## 4.2 Architecture overview

### Simple Overview


![Overview](https://bitbucket.cis.unimelb.edu.au:8445/projects/SWEN90013/repos/swen90013-2018-pl/raw/Docs/images/readme/architecture%20overview.png?at=refs%2Fheads%2Ffeature-userdocs)




### Detailed Overview



![Overview](https://bitbucket.cis.unimelb.edu.au:8445/projects/SWEN90013/repos/swen90013-2018-pl/raw/Docs/images/vfg_overview.png?at=65e3dd12425df98ae934c6aadeef30498d32b132)

## 4.3 Extending the Visualisation File Generator
The Visualisation File Generator (VFG) decides where objects are on the screen and what they look like, based on the three files listed above.

Most domain-related modifications to the system should be made to the VFG. For example, a new domain might require objects to be laid out in a manner which is not captured in the existing Animation Profile language.

Extending the Visualisation File Generator requires only building the project in Django (see section 2.2). 


Modifications or extensions of the VFG need only be carried out only on the Django server (not Unity). For information on the VFG, see the file 'VFG Documentation'.


## 4.4 Extending the Visualiser
Modifying the visualiser is only required when the current visualiser cannot adequately render the domain on-screen. It does not concern the logic of object layout. For example, a user might want to extend the Visualiser to support animated sprites.


Extending the Visualiser requires building the project in Unity and Django (see section 2.2). Modifications or extensions of the Visualiser need only be carried out on Unity (not Django). For information on the Visualiser, see the file 'Visualiser Documentation'.