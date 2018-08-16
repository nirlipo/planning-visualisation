# Visualiser with unity
The Visualiser component of project Planning visualisation deals with rendering visual objects and thier animation for solutions generated for the given problem in selected domain using a custom constraint solver.

The Visulaiser component UI is created using unity to make sure the application performance is at its best. UI and rendering of solution into visual file components is developed in same environment together to keep the flows consistent.
## Overall file structure
This is overall file structure of the Visualiser
```bash


+---Visualiser
|   +---Animations
|   +---Fonts
|   +---Images
|   +---Resources
|   +---Scenes
|   +---Scripts
|   |   +---FileUpload
|   |   \---Visualisation
|   |       +---AnimationControl
|   |       +---TransferPack
|   |       |   \---TransferItemPack
|   |       \---VisualisationModels
|   \---Sprites
\---WebGLTemplates
    \---NewTemplate

```
## Architecture
Glance at file structure represents that all the components are seperated and modular. As the visualiser is rendering the files from different UI elements and generating objects automatically there will always be dependencies involved in it. Before adding new visual components or adding new functionalities understanding of dependencies is required.

## Build instructions 
- [ ] Make sure the unity is above Version 2018.2.1f1
- [ ] Make sure all scenes that are being used in visualisation are added to build settings
- [ ] The visualization solution object information is recived from server. A consistent network connection is necessary for making sure everything works
- [ ] Images are recommended to be in PNG format and should be converted to sprites before implementing them in application.
