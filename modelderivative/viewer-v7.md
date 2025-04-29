# About the Viewer SDK

About the Viewer SDK

The Autodesk Platform Services Viewer SDK lets you create applications to view, share, and interact with design models on your own website from a wide variety of products.The Viewer can display files fromAutoCAD,Fusion 360,Revit, and many more. This JavaScript library enables developers to create applications that combine 2D and 3D visualization with business-oriented data.

The Viewer SDK provides an extension framework that allows developers to:

Customize the Viewerâs appearance, controls, and behavior.

Customize the content and location of the Viewer toolbar.

Write custom extensions to further customize the user experience.

Common Uses

Common applications that use this SDK include, but are not limited to:

Project dashboards

Digital twin

Display planning and timelines

Aggregate and coordinate model changes

Generate 2D and 3D markups

Try it out

You can interact with the viewer in the following example. Click the drop-down in the Viewer window to choose different 2D and 3D models.

Tip: To experiment with customizing the Viewer, copy the following snippet and then click EDIT ON CODEPEN at upper right in the example. When CodePen opens, paste the snippet to the end of the original code in theJStab. This snippet isolates all objects that contain the word âconcreteâ in their metadata.

Next Steps

Before you can display a model in the viewer, it must be translated into the SVF or SVF2 format. There are two ways to do this:

If the file is in a BIM 360 or ACC workspace, the SVF/SVF2 file is automatically generated.

Upload the model to the Object Storage Service (OSS). After uploading you can call the Model Derivative APIâsPOST Start Translation Joboperation to perform the translation.

For more information, see the Model Derivative tutorialPrepare a File for the Viewer.

Authentication (OAuth)is required to use Model Derivative. The Model Derivative tutorial guides you through the process of obtaining an access token. You can also refer to theAuthentication Documentation.

Note

The Autodesk Viewer SDK JavaScript must be delivered from an Autodesk hosted URL.

Before you begin, it is advisable to review the content in the Viewer Essentials and Advanced Options sections.

Terms of Service

APS Viewer SDKis subject toAutodesk Platform Services Terms of Service.

```
viewer.addEventListener(Autodesk.Viewing.GEOMETRY_LOADED_EVENT, function () {
 viewer.search('concrete', function (ids) {
     viewer.isolate(ids);
 });
});

```


---

# Controlling Viewer State

Controlling Viewer State

This example adds a button namedToggle Explodeto the UI. The button toggles between an explode value of 0 and a second preset explode value. This example uses a 50% explode value (0.5) for the second value.

This is accomplished by adding a click event listener to the newexplodeButton, which callsviewer.explode(). The click event lets you switch between the specified explode values.

TipOpen the example in CodePen and try different explode scale values.


---

# Handle Viewer Events

Handle Viewer Events

This example implements an event listener for theSELECTION_CHANGED_EVENT.

Selecting an object calls the specified inline function, which asynchronously retrieves the ID of the selected object and displays it in an alert box with the message:The user has selected objects with IDs. The message is followed by the retrieved object ID.

TipOpen the example in CodePen and change the message text.


---

# Querying Model Properties

Querying Model Properties

This example illustrates how to query a model using a property name and then isolate the corresponding element while automatically zooming in to that element. To test it out:

From the drop-down on the top-left, select01_rac_basic_sample_project.rvt.

In the text box next to the drop-down, enterSingle-Flush [422466].

ClickSearch. The specified door will display clearly, with all other elements suppressed.

The script first captures the name of the property from the text box. After that, it queries the modelâs properties to obtain the node ID of the element. It then uses this ID to isolate the element and zoom in on it.


---

# Customizing Viewer UI

Customizing Viewer UI

This example illustrates adding a custom button next to the Viewer toolbar. The event handler for the buttonâs onClick event changes the lighting preset of the Viewer to Snow Field (16).

TipOpen the example in CodePen and experiment with changing the button tooltip text and the lighting value. To turn off the background image for a lighting environment, click the Settings button, Environment tab, and move the control forEnvironment Image Visibleto the left (off) position.


---

# Customizing Viewer Scene

Customizing Viewer Scene

This example illustrates how to add a custom object to a scene such that it is rendered the same way as the model that is loaded.

The button on the top left, titledAdd Sphere, has an event listener associated with it. When clicked, the event handler checks for the existence of a scene named custom-scene, and creates it if it doesnât exist. It then adds a randomly placed sphere to the scene.


---

# Aggregated View

Aggregated View

This example illustrates creating an aggregated view by combining a Revit model and a Fusion 360 model in a single view.

The example implements a function namedaddViewable, which renders a model specified by the URN of a viewable passed as a parameter. It then calls the function to render the two models in the same Viewer object.

For more information about Aggregated View, see theAdvanced OptionsandAPI Referencesections.


---

# Getting Started

Getting Started

Before You Begin

Before you can create a viewer application, there are a few things you need to do.

Create an Autodesk Platform Services (APS) account.

Register an app.

Get the Client ID and Secret.

Provision access in other products.

For more information, see the APSGetting Startedtutorial.

Add Viewer to an HTML Page

The<script>tag in the following HTML snippet loads the bundled Viewer SDK at runtime and creates an instance of the Viewer that covers the entire HTML page.

ThedividentifierforgeViewerwill initialize a Viewer instance. To learn how to initialize a viewer instance, see Part 2:Initialize Viewer.

Note:The Viewer has a hard dependency on three.js R71.

Bundle Size

We recommend including the<script>tag to load the Viewer JavaScript library as late as possible. This allows browsers to render all static HTML content first.

Viewer Versions

The<script>tag specifies the location of the Viewerâs JavaScript code, as well as the version of the library to download. In the example HTML above, the specified version is7.*, which pulls the latest minor version available for the major version 7 release.

For example, if versions7.0,7.1and7.2are available, then requesting Viewer version7.*retrieves version7.2.

Likewise, the specified version can include the minor or patch numbers, too. The following URLs are all valid:

LMV_VIEWER_VERSION

You can validate the fetched viewer version with the help of theglobal variable LMV_VIEWER_VERSION.

Initialize Viewer

Initialization is a 2 step process:

Initialize the page using functionAutodesk.Viewing.Initializer().

Create a Viewer instance and verify that WebGL support is available.

Example

Initializing the Viewer for SVF and SVF2 Support

You enable SVF or SVF2 support by passing theenvandapiparameters when initializing the Viewer. The value you use forenvandapispecifies an SVF derivative or an SVF2 derivative. The following table lists the values to use:

Parameter

SVF

SVF2

env

AutodeskProduction

AutodeskProduction2

api

api

derivativeV2 (for US)

streamingV2 (for US)

derivativeV2_EU (for EU)

streamingV2_EU (for EMEA)

derivativeV2_AUS (for AUS)

streamingV2_AUS (for AUS)

Initializer

The Initializer function needs to be run just once. It makes sure that all subsystems are running before proceeding.
Refer to the Parameters listed under theInitializer Methodfor details of the values supported foroptions.

Create Viewer instance

Once the Initializer callback is invoked, we proceed to create a new instance of the Viewer.

You have to invoke the methodviewer.start()just once. From there, validate that the browser supports WebGL before moving on toLoad a Model.

Destroy Viewer instance

When the Viewer is no longer needed on the page, uninitialize and claim back memory using:

Load a Model

Loading a model is a 2 step process.

Fetch a Manifest JSON fromModel Derivative API.

Instruct the Viewer to load one of the models referenced by the Manifest JSON.

Before you load a model, you must use thePOST jobendpoint of theModel DerivativeAPI to kick off a translation job, which translates the model into the SVF format. The translation job produces a JSON file known as a Manifest. The manifest provides details of the resources (e.g., model geometry, thumbnails, camera views) that were produced by thetranslation job.

See thePrepare a File for the Viewertutorial in the Model Derivative API documentation for more information.

In order to use theModel DerivativeAPI you must have anACCESS_TOKEN. Use the APSAuthenticationAPI to obtain an access token. The Viewer supports both 2-legged and 3-legged tokens.

Step 1: Fetch Manifest

A manifest is a JSON document containing the result of a translation job. As this process takes place, the content in the JSON document is updated to reflect the progress of the translation job. Once the translation process is complete, the JSON document will contain references to all available derivatives, some of which are models that can be loaded into the Viewer.

The Viewer library provides a static method for fetching a manifest for a specified URN string value.

Notes:

ThedocumentIdis a string value of the URN of the model that was translated.

The URN must be encoded as anunpadded Base64 string. See thePrepare a File for the Viewertutorial in the Model Derivative API documentation for more information on Base64 encoding.

The value assigned todocumentIdmust be prefixed with the stringurn:

If you want to reuse the code snippet shown above, replace the value ofdocumentIdwith the URN from your own translation jobs.

In some cases you may need to determine if the URN is from EMEA or US. Start by base64 decoding the URN, then check if it containsurn:adsk.wipemea:xxx(for EMEA) orurn:adsk.wipprod:xxx(for US).

After successfully fetching the manifest, the callbackonDocumentLoadSuccessgets invoked. The callback receives the argumentviewerDocument, which is an instance ofAutodesk.Viewing.Document.

Step 2: Load Model in Manifest

The snippets below assume that aviewerinstance is available.

You have the option to load the default model or to choose from the list of all models in the manifest.

To load the default model in the manifest:

To choose a different model, retrieve the list of all models and use custom code to determine which one to load.

Putting it all together

At this point, developers should have code that looks like this:

```
<head>
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1, user-scalable=no" />
    <meta charset="utf-8">

    <link rel="stylesheet" href="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/style.min.css" type="text/css">
    <script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>

    <style>
        body {
            margin: 0;
        }
        #forgeViewer {
            width: 100%;
            height: 100%;
            margin: 0;
            background-color: #F0F8FF;
        }
    </style>
</head>
<body>

    <div id="forgeViewer"></div>

</body>

```

```
<!-- Fetch exactly version 7.0.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0.0/viewer3D.min.js"></script>

<!-- Fetch latest patch version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0.*/viewer3D.min.js"></script>

<!-- Also fetch latest patch version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.0/viewer3D.min.js"></script>

<!-- Fetch latest minor version for 7.0 -->
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>

```

```
var viewer;
var options = {
    env: 'AutodeskProduction2',
    api: 'streamingV2',  // for models uploaded to EMEA change this option to 'streamingV2_EU'
    getAccessToken: function(onTokenReady) {
        var token = 'YOUR_ACCESS_TOKEN';
        var timeInSeconds = 3600; // Use value provided by APS Authentication (OAuth) API
        onTokenReady(token, timeInSeconds);
    }
};

Autodesk.Viewing.Initializer(options, function() {

    var htmlDiv = document.getElementById('forgeViewer');
    viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv);
    var startedCode = viewer.start();
    if (startedCode > 0) {
        console.error('Failed to create a Viewer: WebGL not supported.');
        return;
    }

    console.log('Initialization complete, loading a model next...');

});

```

```
var htmlDiv = document.getElementById('forgeViewer');
viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv, {});

```

```
viewer.finish();
viewer = null;
Autodesk.Viewing.shutdown();

```

```
var documentId = 'urn:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bXktYnVja2V0L215LWF3ZXNvbWUtZm9yZ2UtZmlsZS5ydnQ';
Autodesk.Viewing.Document.load(documentId, onDocumentLoadSuccess, onDocumentLoadFailure);

function onDocumentLoadSuccess(viewerDocument) {
    // viewerDocument is an instance of Autodesk.Viewing.Document
}

function onDocumentLoadFailure() {
    console.error('Failed fetching Forge manifest');
}

```

```
var defaultModel = viewerDocument.getRoot().getDefaultGeometry();
viewer.loadDocumentNode(viewerDocument, defaultModel);

```

```
var viewables = viewerDocument.getRoot().search({'type':'geometry'});
viewer.loadDocumentNode(viewerDocument, viewables[0]);

```

```
var documentId = 'urn:dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6bXktYnVja2V0L215LWF3ZXNvbWUtZm9yZ2UtZmlsZS5ydnQ';
Autodesk.Viewing.Document.load(documentId, onDocumentLoadSuccess, onDocumentLoadFailure);

function onDocumentLoadSuccess(viewerDocument) {
    var defaultModel = viewerDocument.getRoot().getDefaultGeometry();
    viewer.loadDocumentNode(viewerDocument, defaultModel);
}

function onDocumentLoadFailure() {
    console.error('Failed fetching Forge manifest');
}

```


---

# Reacting to Events

Reacting to Events

Events are a mechanism to notify 3rd party code about changes in the Viewer.
The Viewer actually listens to its own events in order to update the UI state.
See theViewing Namespacetopic of the API Reference for a list of available events.

This topic demonstrates adding listeners for theAutodesk.Viewing.SELECTION_CHANGED_EVENTandAutodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT.  We will change the HTML content to
display how many elements are currently selected and what navigation tool is currently set.

Before You Begin

We recommend the code in this example to be encapsulated in anextension.

Step 1: Add Selection Counter to HTML

Letâs begin by adding an HTML element that displays how many nodes are currently selected.
Add the HTML block after the Viewerâsdiv.

Add the following style.

The content of#MySelectionValuechanges wheneverAutodesk.Viewing.SELECTION_CHANGED_EVENTgets fired.

Step 2: Listen and react to an event

Events are dispatched through theViewer3Dinstance.
Letâs now add a function to handle selection change events.
We will also calladdEventListener()on the extensionâsload()function and callremoveEventListener()on the extensionsâsunload()function.

We usebind()to keep a reference tothiswithinonSelectionEvent().

At this point, every time a node gets selected the counter will change to that number.
Remove the selection by usingESCon your keyboard.  You select additional nodes by usingShift-ClickorCtrl-Click.
Notice that you can also toggle the selection with those commands.

Step 3: Another event

The Viewerâs toolbar features buttons that change the current navigation tool. Tools are responsible for converting user input into actions.
The Navigation tools in particular deal with navigating the camera around the scene.

Letâs now listen toAutodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENTand display the toolâs name onscreen.
Start by modifying the initially added HTML as follows.

We also need to add the event handler and modifyload()andunload()methods.

Notice that for this new event, we are actually consuming theidproperty and assigning it as theinnerText.
Most of the events dispatched have associated data with them.  The same data can be pulled from theViewerinstance as well.
The sameidvalue can be fetched from the viewer by callingthis.viewer.getActiveNavigationTool().

Now that the event is hooked, try clicking through the navigation buttons in the Viewerâs toolbar. Youâll find that the
event handler will pick up the tool change event!

```
<div class="my-custom-ui">
    <div>Items selected: <span id="MySelectionValue">0</span></div>
<div>

```

```
<style>
   .my-custom-ui {
        position: absolute;
        top: 0;
        left: 0;
        z-index: 5;
        margin: .3em;
        padding: .3em;
        font-size: 3em;
        font-family: sans-serif;
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 8px;
    }
    .my-custom-ui span {
        color: red;
    }
</style>

```

```
// Event handler for Autodesk.Viewing.SELECTION_CHANGED_EVENT
EventsTutorial.prototype.onSelectionEvent = function(event) {
    var currSelection = this.viewer.getSelection();
    var domElem = document.getElementById('MySelectionValue');
    domElem.innerText = currSelection.length;
};

EventsTutorial.prototype.load = function() {
    this.onSelectionBinded = this.onSelectionEvent.bind(this);
    this.viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    return true;
};

EventsTutorial.prototype.unload = function() {
    this.viewer.removeEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.onSelectionBinded = null;
    return true;
};

```

```
<div class="my-custom-ui">
  <div>Items selected: <span id="MySelectionValue">0</span></div>
  <div>Navigation tool: <span id="MyToolValue">Unknown</span></div>
<div>

```

```
// New event for handling Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT
// Follows a similar pattern
EventsTutorial.prototype.onNavigationModeEvent = function(event) {
    var domElem = document.getElementById('MyToolValue');
    domElem.innerText = event.id;
};

EventsTutorial.prototype.load = function() {
    this.onSelectionBinded = this.onSelectionEvent.bind(this);
    this.onNavigationModeBinded = this.onNavigationModeEvent.bind(this);
    this.viewer.addEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.viewer.addEventListener(Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT, this.onNavigationModeBinded);
    return true;
};

EventsTutorial.prototype.unload = function() {
    this.viewer.removeEventListener(Autodesk.Viewing.SELECTION_CHANGED_EVENT, this.onSelectionBinded);
    this.viewer.removeEventListener(Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT, this.onNavigationModeBinded);
    this.onSelectionBinded = null;
    this.onNavigationModeBinded = null;
    return true;
};

```

```
// Alternative handler for Autodesk.Viewing.NAVIGATION_MODE_CHANGED_EVENT
EventsTutorial.prototype.onNavigationModeEvent = function(event) {
    var domElem = document.getElementById('MyToolValue');
    domElem.innerText = this.viewer.getActiveNavigationTool(); // same value as event.id
};

```


---

# Customizing the Toolbar

Customizing the Toolbar

Customizing a toolbar is best explained by looking at an example.

This example creates a custom toolbar with two buttons on the Viewer canvas.
Each button has its own tooltip and reacts to click events.
Clicking one button displays the environment background, while clicking the other hides it.

Before You Begin

The customization logic is is implemented as anextension.

Step 1: Detect the Toolbar

In the custom extension, override base class methodonToolbarCreated. The Viewer will invoke this method as soon as the toolbar is available to the extension.

Step 2: Add Buttons

To create a sub-toolbar and add a couple of buttons:

Notice that the code above calls methodaddClass(), which adds a CSS class to
control the appearance of the custom buttons.

For this example, weâll add the style definitions in the HTML file:

When you refresh the HTML page the buttons display. Hovering over them displays tooltips. Click to trigger their actions.

Step 3: Cleanup

Extensions should remove any DOM elements and events they add.
In this case, onlythis.subToolbarmust be removed.

As explained inWriting an Extension, you can verify that the extension works as expected by manually
calling theviewer.loadExtension('ToolbarExtension')andviewer.unload('ToolbarExtension')methods.

```
function ToolbarExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);
}

ToolbarExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
ToolbarExtension.prototype.constructor = ToolbarExtension;

ToolbarExtension.prototype.load = function() {
  // Set background environment to "Infinity Pool"
  // and make sure the environment background texture is visible
  this.viewer.setLightPreset(6);
  this.viewer.setEnvMapBackground(true);

  // Ensure the model is centered
  this.viewer.fitToView();

  return true;
};

ToolbarExtension.prototype.unload = function() {
  // nothing yet
};

Autodesk.Viewing.theExtensionManager.registerExtension('ToolbarExtension', ToolbarExtension);

```

```
ToolbarExtension.prototype.onToolbarCreated = function(toolbar) {

  alert('TODO: customize Viewer toolbar');
};

```

```
ToolbarExtension.prototype.onToolbarCreated = function(toolbar) {
  // alert('TODO: customize Viewer toolbar');

  var viewer = this.viewer;

  // Button 1
  var button1 = new Autodesk.Viewing.UI.Button('show-env-bg-button');
  button1.onClick = function(e) {
      viewer.setEnvMapBackground(true);
  };
  button1.addClass('show-env-bg-button');
  button1.setToolTip('Show Environment');

  // Button 2
  var button2 = new Autodesk.Viewing.UI.Button('hide-env-bg-button');
  button2.onClick = function(e) {
      viewer.setEnvMapBackground(false);
  };
  button2.addClass('hide-env-bg-button');
  button2.setToolTip('Hide Environment');

  // SubToolbar
  this.subToolbar = new Autodesk.Viewing.UI.ControlGroup('my-custom-toolbar');
  this.subToolbar.addControl(button1);
  this.subToolbar.addControl(button2);

  toolbar.addControl(this.subToolbar);
};

```

```
<style>
  .show-env-bg-button {
    background: red;
  }
  .hide-env-bg-button {
    background: blue;
  }
</style>

```

```
ToolbarExtension.prototype.unload = function() {
  if (this.subToolbar) {
      this.viewer.toolbar.removeControl(this.subToolbar);
      this.subToolbar = null;
  }
};

```


---

# Loading glTF 2.0 Models

Loading glTF 2.0 Models

The glTF 2.0 Loader extension provides the ability to load glTF 2.0 models in the viewer.

The extension id is:Autodesk.glTFExtension

Initialization

Using the glTF 2.0 Loader, you can load local glTF models in Viewer SDK. Initialize the page using function Autodesk.Viewing.Initializer().

Usage

The glTF 2.0 Loader supports these features:

glTF2.0 loading, including geometry and basic material.

Basic navigation, including Orbit, Zoom and Pan tool.

Basic selection, including mapping dbID to glTF nodes.

Show node name on property panel and model browser.

Supports only free measurement mode.

The glTF 2.0 Loader does not support these features:
* Property database.
* Measurement tool.

To activate free measurement mode:

Example using glTF 2.0 Loader:

```
var viewer;
var options = {
    env: 'AutodeskProduction2',
    api: 'streamingV2',  // for models uploaded to EMEA change this option to 'streamingV2_EU'
    documentId: 'tests/unittest/models/glTF/duck.gltf'
    getAccessToken: function(onTokenReady) {
        var token = 'YOUR_ACCESS_TOKEN';
        var timeInSeconds = 3600; // Use value provided by APS Authentication (OAuth) API
        onTokenReady(token, timeInSeconds);
    }
};

Autodesk.Viewing.Initializer(options, function() {
    var htmlDiv = document.getElementById('forgeViewer');
    viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv);
    var startedCode = viewer.start();
    if (startedCode > 0) {
        console.error('Failed to create a Viewer: WebGL not supported.');
        return;
    }
});

```

```
var measuretool = NOP_VIEWER.getExtension('Autodesk.Measure');
measuretool.setFreeMeasureMode(true);

```


---

# Using DiffTool to Compare Models

Using DiffTool to Compare Models

The DiffTool extension provides UI controls for comparing 2D and 3D models.

Examples

Usage

Using the DiffTool, you can compare the differences between models in Viewer SDK. The DiffTool shows three kinds of changes to the primary model:

Added: Shows objects that have been added to the primary model.

Removed: Shows objects that have been removed from the primary model.

Modified: Shows objects that have been changed in the primary model

There are three modification types:

Geometry: The geometry data has been modified.

Transformation: The geometry transformation has been modified.

Attribute: One or more properties of the geometry has been modified.

Configuring DiffTool LMV extension

A list of all configuration options for the DiffTool LMV extension:

primaryModels*Autodesk.Viewing.Model

An array of loaded âAutodesk.Viewing.Modelâ instances that are compared by the DiffTool.

diffModels*Autodesk.Viewing.Model

An array of other loadedAutodesk.Viewing.Modelinstances that participate in the diff operation as the previous state. Length must matchprimaryModelsto define pairs of models to be compared.

versionA*string

Version identifier for the primary models, such as â2â, âVersion 2â, or â02/26/2018â. Note that you must provide a localized string if you are using something other than numbers or dates.

versionB*string

Version identifier of the diff models, usually a previous version

mimeType*string

âapplication/vnd.autodesk.revitâ: Revitâapplication/vnd.autodesk.r360â: Revitâapplication/vnd.autodesk.fusion360â: For Fusion 360âapplication/vnd.autodesk.f3dâ: For Fusion 360âapplication/vnd.autodesk.inventor.assemblyâ: For Inventor (IAM)âapplication/vnd.autodesk.navisworksâ`: For Navisworks (NWD)âapplication/vnd.autodesk.cadâ: For IFCâapplication/vnd.autodesk.dxfâ: For DXFâapplication/vnd.autodesk.autocad.dwgâ: For DWG

âapplication/vnd.autodesk.revitâ: Revit

âapplication/vnd.autodesk.r360â: Revit

âapplication/vnd.autodesk.fusion360â: For Fusion 360

âapplication/vnd.autodesk.f3dâ: For Fusion 360

âapplication/vnd.autodesk.inventor.assemblyâ: For Inventor (IAM)

âapplication/vnd.autodesk.navisworksâ`: For Navisworks (NWD)

âapplication/vnd.autodesk.cadâ: For IFC

âapplication/vnd.autodesk.dxfâ: For DXF

âapplication/vnd.autodesk.autocad.dwgâ: For DWG

propertyFilter{Object.<string,Array<string>}

An object representing a category and properties key-value pair to ignore for diff computation. Example: {âDimensionsâ:[âAreaâ,âLengthâ], âMechanical - Flowâ:[âFlowâ]}

Using LMV initialization options

Examples

```
viewer.loadExtension('Autodesk.DiffTool')

```

```
var config = {
    availableDiffModes: ['overlay', 'sidebyside'],
    diffModels: A,
    primaryModels: B,
    mimeType: 'application/vnd.autodesk.revit',
    diffMode: 'overlay',
    versionA: 'A',
    versionB: 'B',
    propertyFilter: { "Category1": [ "Property1", "Property2" ] }
};

viewer.loadExtension("Autodesk.DiffTool", config);

```


---

# Writing an Extension

Writing an Extension

What is an Extension?

An extension is JavaScript code that extends or modifies the Viewerâs behavior. You can use extensions to add specialized functionality to the Viewer SDK.

Many extensions are bundled with the Viewer. For a complete list of included extensions, see the API Reference section forExtensions. If the functionality you need is not included, you can write your own extensions.

Writing extensions is best explained with an example. The following example    creates a Viewer extension namedMyAwesomeExtension.

There will be two HTML buttons that interact with the added extension. They will be placed below and outside the Viewer canvas.

One of the buttons will be used to lock the camera. Once locked you will not be able to orbit (rotate), pan, or zoom.
The next button will be used to unlock the camera, re-enabling mouse and touch interactions.

Step 1: Include extension file

Extensions must be defined after all core classes for the Viewer have been defined.
This example uses a file namedmy-awesome-extension.jsand the following snippet shows how to include it in the HTML.

Step 2: Write the extension code

An extension consists of the following interface points:

Inherits fromAutodesk.Viewing.Extension.

Defines methodload()that returns aboolean.

Defines methodunload()that also returns aboolean.

Registers itself with a uniquestringid.

An extension will successfully get loaded into The Viewerâs lifecycle only ifload()returnstrue.
Likewise, an extension will get successfully unloaded ifunload()returnstrue.

Notice that the string'MyAwesomeExtension'used inregisterExtension()doesnât need to match the
function name declaration.

Note:The extension does not get loaded when refreshing the HTML page.

Step 3: Load the extension

To instruct the Viewer instance to load the extension:

Refreshing the HTML page displays thealert()message found in the extensionâsload()method.

Step 4: Add HTML buttons

Add two simple HTML buttons after the Viewer div:

Step 5: Add button handlers

To enhance the extensionâsload()method to handle the HTML buttonsâ click events:
Notice our extension has propertythis.viewer, the main access point for most of The Viewerâs features and customizations.

Note:The extension propertythis.vieweris the main access point for most of the Viewerâs features and customizations.

Reload the HTML and use the mouse to move the camera around. Then clickLockit!and notice how you can
no longer modify the camera with the mouse. You will notice that some UI buttons get hidden as well.

Now click theUnlockit!button to enable camera interactions once again.

Step 6: Cleanup on unload

Itâs a good practice to remove added event listeners to DOM elements when the extension is unloaded.

To perform all cleanup operations in theunloadmethod:

Step 7: Test the Extension

To fully test that the extension is working as expected, you can manually force the
extension to be loaded and unloaded.

From the browserâs console type the following to check whether your extension is loaded or not.
At this point, the extension should be loaded and the function call should returntrue:

Note the use of the global variableNOP_VIEWER, defined by the Viewer SDK after developers create a Viewer instance.

Now type the following tounloadthe extension:

If all goes as expected, the added buttons should no longer work. Click on them to validate.

You can then load the extension again by calling

Now the added buttons will again work as expected.

```
<script src="https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/viewer3D.min.js"></script>
<script src="my-awesome-extension.js"></script>

```

```
// Content for 'my-awesome-extension.js'

function MyAwesomeExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);
}

MyAwesomeExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
MyAwesomeExtension.prototype.constructor = MyAwesomeExtension;

MyAwesomeExtension.prototype.load = function() {
  alert('MyAwesomeExtension is loaded!');
  return true;
};

MyAwesomeExtension.prototype.unload = function() {
  alert('MyAwesomeExtension is now unloaded!');
  return true;
};

Autodesk.Viewing.theExtensionManager.registerExtension('MyAwesomeExtension', MyAwesomeExtension);

```

```
var config3d = {
  ...
  extensions: ['MyAwesomeExtension'],
  ...
};
var htmlDiv = document.getElementById('forgeViewer')
viewer = new Autodesk.Viewing.GuiViewer3D(htmlDiv, config3d);
viewer.start();
...
viewer.loadModel(...);

```

```
<div id="forgeViewer"></div>
<button id="MyAwesomeLockButton">Lock it!</button>
<button id="MyAwesomeUnlockButton">Unlock it!</button>

```

```
MyAwesomeExtension.prototype.load = function() {
  // alert('MyAwesomeExtension is loaded!');

  var viewer = this.viewer;

  var lockBtn = document.getElementById('MyAwesomeLockButton');
  lockBtn.addEventListener('click', function() {
    viewer.setNavigationLock(true);
  });

  var unlockBtn = document.getElementById('MyAwesomeUnlockButton');
  unlockBtn.addEventListener('click', function() {
    viewer.setNavigationLock(false);
  });

  return true;
};

```

```
function MyAwesomeExtension(viewer, options) {
  Autodesk.Viewing.Extension.call(this, viewer, options);

  // Preserve "this" reference when methods are invoked by event handlers.
  this.lockViewport = this.lockViewport.bind(this);
  this.unlockViewport = this.unlockViewport.bind(this);
}

MyAwesomeExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
MyAwesomeExtension.prototype.constructor = MyAwesomeExtension;

MyAwesomeExtension.prototype.lockViewport = function() {
  this.viewer.setNavigationLock(true);
};

MyAwesomeExtension.prototype.unlockViewport = function() {
  this.viewer.setNavigationLock(false);
};

MyAwesomeExtension.prototype.load = function() {
  // alert('MyAwesomeExtension is loaded!');

  this._lockBtn = document.getElementById('MyAwesomeLockButton');
  this._lockBtn.addEventListener('click', this.lockViewport);

  this._unlockBtn = document.getElementById('MyAwesomeUnlockButton');
  this._unlockBtn.addEventListener('click', this.unlockViewport);

  return true;
};

 MyAwesomeExtension.prototype.unload = function() {
  // alert('MyAwesomeExtension is now unloaded!');

  if (this._lockBtn) {
    this._lockBtn.removeEventListener('click', this.lockViewport);
    this._lockBtn = null;
  }

  if (this._unlockBtn) {
      this._unlockBtn.removeEventListener('click', this.unlockViewport);
      this._unlockBtn = null;
  }

  return true;
};

```

```
NOP_VIEWER.isExtensionLoaded('MyAwesomeExtension');

```

```
NOP_VIEWER.unloadExtension('MyAwesomeExtension');

```

```
NOP_VIEWER.loadExtension('MyAwesomeExtension');

```


---

# Adding Custom Geometry

Adding Custom Geometry

The Viewer lets you to add custom geometry into a scene by using theviewer.overlayapi.

Use this feature to overlay more data to the loaded model. Every custom geometry
added into the overlay scene gets rendered on every frame, even when progressive rendering is on.

Frame rate declines when too many custom geometries are added into overlay scenes.

Custom geometry uses the main scene depth buffer for depth testing, allowing the custom geometry to appear within the loaded model.

Use theSceneBuilderAPI to add objects that can be rendered progressively.

Step 1: Create custom geometry

The Viewer bundles version 71 ofthree.jslibrary and exposes its functionality through the global variableTHREE.
Letâs use it to create a red sphere.

Step 2: Create overlay scene

Custom geometry must be added to an overlay scene. Multiple custom geometries can coexist in the same scene.
Scenes are created and identified by name. Be sure to choose a name that wonât conflict with scenes created by the Viewer.

Step 3: Add custom geometry to overlay scene

Custom geometry must be added into specific overlay scenes. In this example we are adding custom geometrysphereMeshinto the scene named'custom-scene'.

Step 4: Remove custom geometry from overlay scene

You can remove the custom geometry and overlay scenes withremoveMesh()andremoveScene().

The viewer doesnât dispose of the geometry or material used with custom geometry. The application developer can use the following to release the memory.

Whatâs next?

To view an interactive example, check outCustomizing Viewer Scene.

For all available methods, see theOverlayManagerAPI documentation page.

```
var geom = new THREE.SphereGeometry(10, 8, 8);
var material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
var sphereMesh = new THREE.Mesh(geom, material);
sphereMesh.position.set(1, 2, 3);

```

```
if (!viewer.overlays.hasScene('custom-scene')) {
    viewer.overlays.addScene('custom-scene');
}

```

```
viewer.overlays.addMesh(sphereMesh, 'custom-scene');

```

```
viewer.overlays.removeMesh(sphereMesh, 'custom-scene');
viewer.overlays.removeScene('custom-scene');

```

```
// Once the material and geometries are no longer used by any other
// meshes, they need to be disposed to avoid memory leaks.
material.dispose();
geom.dispose();

```


---

# Querying the Property Database

Querying the Property Database

TheProperty Databasecontains all of the BIM data for a construction model and the manufacturing data for manufacturing models. The Property Database is kept on a dedicatedweb workerand accessing it is done via asynchronous messages.

In this example weâll be writing a function that queries the Property Database of the model directly inside the web worker execution context.

Step 1: Writing a custom query function

The query functionmustbe nameduserFunction. Letâs start by writing a trivial query function for the Property Database.

The trivial query function doesnât interact withpdb, the Property Database, yet. Weâll implement rhw interaction in Step 3. For now weâll have it return a fixed value of42.

Step 2: Executing the custom query function

Useviewer.model.getPropertyDb().executeUserFunction(userFunction)which returns aPromisethat resolves with the return value ofuserFunction.

After executing this code snippet, youâll see the messageretValue is: 42in the browserâs developer console.

Step 3: Querying the Property Database

Now itâs time to modify ouruserFunctionto have it interact with the Property Database.

The objective of the custom query function is to return the ids of the heaviest parts in the model. To do this, weâll iterate over all part-ids in the model and check theirMassproperty value.

Due to the Property Database data layout, weâll first need to identify the index for the âMassâ property.
Update the custom query function as follows:

If the value ofattrIdMassis different than-1, then we know that the modelâs Property Database contains âMassâ data for its parts. Next weâll have the function iterate over all parts and their properties, to find out which one is the largest.

And finally, the Promiseâsresolvefunction from Step 2 will have to be updated, too. In this case, weâll have the viewer select and focus (zoom) on the largest part.

Final thoughts

When writing your ownuserFunction, make sure that you avoid referencing objects that live outside the functionâs scope. This is because the function gets serialized when messaged to the web worker.

Whatâs next?

To view an interactive example, seeQuerying Model Properties.

SeeProperty Databasefor  the instance methods available for your custom query function.

```
function userFunction(pdb) {
    return 42;
}

```

```
var thePromise = viewer.model.getPropertyDb().executeUserFunction( userFunction );
thePromise.then(function(retValue){
    console.log('retValue is: ', retValue); // prints 'retValue is: 42'
}).catch(function(err){
  console.log("Something didn't go right...")
  console.log(err);
});

```

```
function userFunction(pdb) {

    //return 42;

    var attrIdMass = -1;

    // Iterate over all attributes and find the index to the one we are interested in
    pdb.enumAttributes(function(i, attrDef, attrRaw){

        var name = attrDef.name;

        if (name === 'Mass') {
            attrIdMass = i;
            return true; // to stop iterating over the remaining attributes.
        }
    });
}

```

```
function userFunction(pdb) {

    //return 42;

    var attrIdMass = -1;

    // Iterate over all attributes and find the index to the one we are interested in
    pdb.enumAttributes(function(i, attrDef, attrRaw){

        var name = attrDef.name;

        if (name === 'Mass') {
            attrIdMass = i;
            return true; // to stop iterating over the remaining attributes.
        }
    });

    // Early return is the model doesn't contain data for "Mass".
    if (attrIdMass === -1)
      return null;

    // Now iterate over all parts to find out which one is the largest.
    var maxValue = 0;
    var maxValId = -1;
    pdb.enumObjects(function(dbId){

        // For each part, iterate over their properties.
        pdb.enumObjectProperties(dbId, function(attrId, valId){

            // Only process 'Mass' property.
            // The word "Property" and "Attribute" are used interchangeably.
            if (attrId === attrIdMass) {

                var value = pdb.getAttrValue(attrId, valId);

                if (value > maxValue) {
                    maxValue = value;
                    maxValId = dbId;
                }

                // Stop iterating over additional properties when "Mass" is found.
                return true;
            }
        });
    });

    // Return results
    return {
      id: maxValId,
      mass: maxValue
    }
}

```

```
var thePromise = viewer.model.getPropertyDb().executeUserFunction( userFunction );
thePromise.then(function(retValue){

    //if (retValue === 42) {
    //  console.log('We got the expected value back.');
    //}

    if (!retValue) {
      console.log("Model doesn't contain property 'Mass'.");
      return;
    }

    var mostMassiveId = retValue.id;
    viewer.select(mostMassiveId);
    viewer.fitToView([mostMassiveId]);
    console.log('Most massive part is', mostMassiveId, 'with Mass:', retValue.mass);
});

```


---

# Using Profile APIs

Using Profile APIs

The Profile API lets you specify thepreferencevalues andextensionsthat you want to load or unload in the Viewer.

Using built-in profiles to apply settings to the Viewer.

Creating a custom profile.

Registering custom profiles with a specific file type.

Overriding the default profile with a custom one.

Using built-in profiles

The Viewer provides built-in, ready-to-use profiles that offer the same user experience as desktop products such as Navisworks and Revit.

For more information, seeProfileSettings

The following snippet shows how to use the Navisworks profile.

The following snippet shows how to use the AEC profile.

Create a custom profile

You can also set a custom profile. A custom profile can override existing preferences, load or unload specific extensions, and set preferences to be persistent.

For more information, seeProfile

The following snippet overrides a couple of preferences, adds new preferences, unloads two extensions, and sets some preferences to be persistent between browser sessions.

Custom profiles can be cloned from existing profile settings. In the following snippet, the profile settings are cloned from the AEC profile settings.
In addition to the AEC profile settings, the properties panel opens when selecting an object and progressive rendering is turned off.

Registering a custom profile for a specific file type

Use the ProfileManager (viewer.profileManager) to register a custom profile with a specific file type.

For more information, seeProfileManager

To use the registered file profiles be sure to set the following config flag:

During initialization, register the custom profile with thedwffile type.

Use custom profile regardless of the file type loaded

You can make a custom profile the default for any file type. The following code sample demonstrates how to override the default profile with the custom profile.

Restore default profile

The following snippet restores the default profile available in the Viewer.

```
const profileSettings = Autodesk.Viewing.ProfileSettings.Navis;
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

```
const profileSettings = Autodesk.Viewing.ProfileSettings.AEC;
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

```
const customProfileSettings = {
    settings: {
        reverseMouseZoomDir: true, // override existing
        reverseHorizontalLookDirection: true, // override existing
        customSettingOne: true, // new preference
        customSettingTwo: 2, // new preference
        customSettingThree: 'test' // new preference
    },
    extensions: {
        unload: ['Autodesk.ViewCubeUi', 'Autodesk.BimWalk']
    }
};
const customProfile = new Autodesk.Viewing.Profile(customProfileSettings);
// Updates viewer settings encapsulated witihn a Profile.
// This method will also load and unload extensions referenced by the Profile.
viewer.setProfile(customProfile);

```

```
const aecProfileSettings = Autodesk.Viewing.ProfileSettings.AEC;
// The custom profile settings are cloned from the AEC profile settings.
const customProfileSettings = Autodesk.Viewing.ProfileSettings.clone(aecProfileSettings);
// Turn off progressive rendering
customProfileSettings.settings.progressiveRendering = false;
// Open the properties panel when selecting an object.
customProfileSettings.settings.openPropertiesOnSelect = true;

const customProfile = new Autodesk.Viewing.Profile(customProfileSettings);
viewer.setProfile(customProfile);

```

```
const config3d = {
    useFileProfile: true
};
const viewer = new Autodesk.Viewing.GuiViewer3D(viewerElement, config3d);

```

```
Autodesk.Viewing.Initializer(initOptions, function() {
    const profileSettings = {
        name: 'DWF',
        settings: {
            // Turn off progressive rendering
            progressiveRendering: false,
            // Open the properties panel when selecting an object.
            openPropertiesOnSelect: true
        }
    };
    viewer.profileManager.registerProfile('dwf', profileSettings);
    viewer.start();
    // The urn should be a bubble node derived from a dwf model.
    Autodesk.Viewing.Document.load(urn, (lmvDocument) => {
        const geometryItems = lmvDocument.getRoot().search({ type: 'geometry' });
        const defaultItem = geometryItems[0];
        viewer.loadDocumentNode(lmvDocument, defaultItem, config3d);
    });
});

```

```
viewer.profileManager.registerProfile('default', profileSettings);

```

```
// Get the registered default profile
const defaultProfile = viewer.profileManager.getProfileOrDefault();
// Set the default profile
viewer.setProfile(defaultProfile);

```


---

# Adding Custom Geometry with Scene Builder

Adding Custom Geometry with Scene Builder

Using the Scene Builder extension, you can create models and add your own objects to Viewer SDK. These objects are treated just like data from a downloaded model with a few restrictions:

Only 3D objects are supported, including 3D lines and other geometry.

Only THREE.BufferGeometry objects can be used.

Lines are not rendered using THREE.Line objects. You must set the propertyisLine:trueon the BufferGeometry.

The same BufferGeometry canât be used for lines and triangles.

Similarly, use the BufferGeometry propertyisPoint:trueto draw points.

The model doesnât have a property database. You can assign database ids and they can be used to collect multiple objects together, but there are no properties associated with the objects.

The model is flat and doesnât have an instance tree.

The only materials that you can use with the Scene Builder are MeshPhong, MeshBasic, LineBasic and Prism.

The objects you add using the SceneBuilder render just like models that are downloaded. Unlike using overlays,
the framerate is not impacted when you add objects. However, it takes longer to fully render the model if you are rendering many objects. It should be noted that the spatial accelerator
hasnât been implemented for the Scene Builder models.

In this tutorial, you will:

Load the Scene Builder extension, which provides access to the ModelBuilder API.

Use the ModelBuilder API to create custom models.

Add custom geometry to your models.

Step 1: Loading the Extension

Like other extensions, the Scene Builder extension is loaded usingloadExtension.

Once the extension is loaded get the extension by usinggetExtension.

Step 2: Creating a Model

After the extension is loaded, you must create a model to hold the objects that you want to display.
To do that, use the extension methodaddNewModel. This method creates the model and returns aModelBuilderAPI you can use to update the model.

Notice the two optional arguments to addNewModel,conserveMemoryandmodelNameOverride. This is the effect of the
arguments on the new model:

conserveMemory: Changes the way LMV stores meshes. This defaults to false and setting it to true will cause lmv to conserve memory by sharing a single mesh object for all of the fragments in the model. If you set this to true, then theaddMesh()method cannot be used to add fragments.

modelNameOverride: Sets a name that you want to display in the model browser panel. If you donât set this option LMV will generate a name -SceneBuilderModeln- where n is the model id of the new model.

Step 3: Adding custom graphics to the model

LMV identifies objects using their property database id. Each object can consist of multiplefragments. Each fragment
has some geometry, a material, and a transform to position the geometry in 3D.

There are three ways to add graphics using the ModelBuilder:

Create and add materials and geometry with THREE separately and then add fragments using the material name and the geometry id.

Create the materials and geometry with THREE and add fragments using the javascript objects.

Create a THREE Mesh and add fragments using the THREE Mesh object.

You can use the different methods separately or together as needed. Methods on the ModelBuilder that require a material accept the
name of a material added to a model or a THREE material. If the THREE material does not exist, it is added to the model.
Similarly, a geometry id or a THREE geometry object can be used interchangeably.

3.1 Adding graphics separately

When you add a material to the model you assign it a name. If the name is already in use or the material was added to a different model, the operation fails to add the material.

When you add geometry to the model, the ModelBuilder assigns and returns an id for the geometry. However, if the geometry was already added to the model, the operation fails.

After the material and geometry are added, you can add a fragment using the material name and geometry id.

TheaddFragmentmethod returns an id that you can use to delete or change the display of the fragment.

3.2 Adding graphics using THREE objects

An alternate mechanism for adding graphics is using THREE objects. ModelBuilder checks to see if the objects have
been added and adds them if they havenât. You canât share THREE objects between models and the operation fails if any of the objects were added to a different
model. ModelBuilder generates a name to use when adding the material. The generated name is!!mtl-n, where n is the value of theidproperty of the material.

3.3 Adding graphics using THREE Mesh

Adding graphics using THREE Mesh is like adding graphics using THREE objects, and the same limitations apply to both. Using THREE Mesh is a good option when you want to hold all of the THREE objects in the THREE mesh. This option only works if the conserveMemory method is not presentâor is set to falseâwhen calling a new model.

Whatâs next?

Check out theModelBuilderAPI documentation page to see all available methods.

```
await viewer.loadExtension('Autodesk.Viewing.SceneBuilder');

```

```
ext = viewer.getExtension('Autodesk.Viewing.SceneBuilder');

```

```
modelBuilder = await ext.addNewModel({
    conserveMemory: false,
    modelNameOverride: 'My Model Name'
});

```

```
purple = new THREE.MeshPhongMaterial({
    color: new THREE.Color(1, 0, 1)
});
modelBuilder.addMaterial('purple', purple);

```

```
box = new THREE.BufferGeometry().fromGeometry(new THREE.BoxGeometry(10, 10, 10));
let id = modelBuilder.addGeometry(box);

```

```
const transform = new THREE.Matrix4().compose(
    new THREE.Vector3(-15, 0, 0),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
modelBuilder.addFragment(1, 'purple', transform);

```

```
red = new THREE.MeshPhongMaterial({
    color: new THREE.Color(1, 0, 0)
});
torus = new THREE.BufferGeometry().fromGeometry(new THREE.TorusGeometry(10, 2, 32, 32));

const transform = new THREE.Matrix4().compose(
    new THREE.Vector3(19, 0, 0),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
modelBuilder.addFragment(torus, red, transform);

```

```
mesh = new THREE.Mesh(torus, purple);
mesh.matrix = new THREE.Matrix4().compose(
    new THREE.Vector3(0, 12, 12),
    new THREE.Quaternion(0, 0, 0, 1),
    new THREE.Vector3(1, 1, 1)
);
mesh.dbId = 100;    // Set the database id for the mesh
modelBuilder.addMesh(mesh);

```


---

# Setting up Edit2D in Your Application

Setting up Edit2D in Your Application

The Edit2D extension provides tools for displaying and editing 2D shapes in Viewer SDK. This tutorial demonstrates how the Edit2D extension works. Tutorials that demonstrate how to use Edit2D, customize Edit2D, and how to manually draw Edit2D shapes with JavaScript are linked at the end of this tutorial.

This tutorial covers:

How to load the Edit2D extension

How to connect your app with Edit2D

Step 1: Load the Extension

To start using Edit2D, you first need to load the extension. In this example, we will register Edit2Dâs default toolset. You can learn how to create your own toolset, along with other customizations, in theCustomizing Edit2Dtutorial.

Step 2: Connect Your App with Edit2D

After youâve loaded the extension, make sure that the Edit2D toolset responds to your Viewer SDK application. Do this by setting up the Edit2D Context and configuring event handling.

2.1 Set Edit2D Context

Registering the default tools sets up anEdit2DContextthat contains an edit layer, tools, and everything the tools need to work.

2.2 Configure Event Handling

Most Edit2D classes support the Viewer SDK EventListener interface. There are a few different ways you can connect your application UI and data model with Edit2D. This step shows two examples:

Synchronizing your data model

Synchronizing selection

Synchronizing your data model

Within your application, shapes may have an application-specific meaning unknown to Edit2D. This means that when you modify the layer with Edit2D tools or undo/redo, your application-specific data model remains unchanged. To keep your data model in sync with changes made to the layer, you can register an event listener withUndoStack. Doing this allows you to be notified consistently, regardless of whether a modification is caused by a tool, Undo, or Redo. Add one of the following lines to your code to notify you before or after the action is taken.

Synchronizing selection

You can also synchronize selection with Edit2D for certain items in your UI usingedit2d.context.selection.

One way to do this is to register a handler. The handler ensures the application is notified if selection changes.

In the following example, weâve set the handler to listen for mouse clicks.

Similarly, you can set the handler to synchronize mouse hovering:

By default, selection and mouse-over highlighting are automatically controlled by Edit2D tools. However, you can also modify selection and hover-highlighting from your application by accessing ctx.selection directly:

Whatâs Next?

Now that youâve set up Edit2D, check out these tutorials:

Using the Edit2D Toolset

Drawing Edit2D Shapes Manually

Customizing Edit2D

```
// Load Edit2D extension
const options = {
    // If true, PolygonTool creates Paths instead of just Polygons. This lets you change segments to arcs.
    enableArcs: true
};

const edit2d = await viewer.loadExtension('Autodesk.Edit2D');

// Register all standard tools in default configuration
edit2d.registerDefaultTools();

```

```
// Code follows example above

const ctx = edit2d.defaultContext;

// {EditLayer} Edit layer containing your shapes
ctx.layer

// {EditLayer} An additional layer used by tools to display temporary shapes (e.g. dashed lines for snapping etc.)
ctx.gizmoLayer

// {UndoStack} Manages all modifications and tracks undo/redo history
ctx.undoStack

// {Selection} Controls selection and hovering highlight
ctx.selection

// {Edit2DSnapper} Edit2D snapper
ctx.snapper

```

```
// Before action
ctx.undoStack.addEventListener(Autodesk.Edit2D.UndoStack.BEFORE_ACTION, beforeAction);

// After action
ctx.undoStack.addEventListener(Autodesk.Edit2D.UndoStack.BEFORE_ACTION, afterAction);

```

```
// Register your handler
ctx.selection.addEventListener(Autodesk.Edit2D.Selection.Events.SELECTION_CHANGED, onSelectionChanged);

```

```
// Update UI state on hover changes
ctx.selection.addEventListener(Autodesk.Edit2D.Selection.Events.SELECTION_HOVER_CHANGED, onHoverChanged);

```

```
// Apply your selection from UI
ctx.selection.selectOnly(myItem.shape);

// Sync Edit2D state on UI-hover events
ctx.selection.setHoverID(shape.id);

```


---

# Using the Edit2D Toolset

Using the Edit2D Toolset

Now that you have integrated Edit2D with your application, you can start using Edit2D tools to create shapes.

This tutorial shows you how to:

Use various Edit2D tools

Display and change labels

Use snapping

Some code samples are provided in this tutorial, but most of the content demonstrates how Edit2D works for end users after being loaded in the Viewer SDK app. Google Chrome is required to complete this tutorial.

You should complete theSetting Up Edit2Dtutorial before using this tutorial. Additional tutorials, which demonstrate how to customize Edit2D and how to manually draw Edit2D shapes using JavaScript, are linked at the end of this tutorial.

Step 1: Run the Edit2D Playground

For this tutorial, you need to set up the Edit2D playground. The Edit2D playground is useful for debugging Edit2D and testing its functionality. To set up the playground, copy this code snippet to your Chrome DevTools snippet collection and run it:

Setting up the Edit2D playground gives you quick access to some Edit2D functions. Note that because the functions are mechanisms for testing, they should not be used for production code or environment. Weâve used them in this tutorial to show you how the Edit2D extension works after loading it in your application.

Step 2: Use Edit2D Tools to Make Shapes

This step demonstrates how to use the following Edit2D tools:

PolygonTool

PolylineTool

PolygonEditTool

InsertSymbolTool

These tools become available when you callregisterDefaultTools(). We did this when we loaded the extension in theSet Up Edit2Dtutorial. Weâll load these tools in the console to demonstrate how each one works.

2.1 PolygonTool: Drawing Polygons and Rectangles

To start using the PolygonTool, enter the following in your console:

The mouse cursor will change to a cross.

WithPolygonToolactivated, you can:

Click to start a new polygon.

Click again to add vertices to the polygon.

Backspaceto remove the most recently added vertex.

Escto discard the new polygon.

HoldShiftto disable snapping. Snapping is active by default.

Double-click to add the final vertex of the polygon. Keyboard shortcuts for finishing the polygon areEnterand theckey.

WithPolygonTool, you can also click and drag to draw a rectangle:

Press and hold your mouse to choose a starting point for your rectangle.

(Optionally) Hold theShiftkey to force the rectangle into a square.

Drag mouse to determine the length and width of the rectangle.

Release the mouse to finish the rectangle.

2.2 PolylineTool: Drawing Polylines

To draw polylines, start the``PolylineTool:

PolylineToolis similar toPolygonTooland allows you to click point-by-point to draw polylines. You can draw simple lines using a single-drag interaction.

2.3 PolygonEditTool: Modify Polygons and Paths

To edit a polygon, startPolygonEditTool.

Shapes in the layer should now respond on mouse-hover with a slightly higher fill opacity. You can now click shapes that you want to edit.

WithPolygonEditTool, you can do the following:

Move a shapeby dragging it.

Move verticesby dragging vertex gizmos.

HoldShiftkey todisable snapping. Snapping is active by default.

Move edgesby dragging edge gizmos. When an edge is moved, neighboring edges get larger or smaller.

Create Protrusionsby dragging edges. If the moved edge is on the same line as its neighbor, the system adds an extra corner. This feature can be used to quickly edit protrusions for shapes with right angles.

Cancel dragging interactionby usingEsckey.

Insert new vertexby right-clicking the edge. This displays the context menu.

Remove verticesby clicking a vertex gizmo and pressingBackspace. You can also right-click the vertex gizmo to display the context menu.

Copy/Pastea shape withCtrl-C/Ctrl-V. Pasting multiple times will create multiple duplicates.

Change lines to Bezier arcsby right-clicking an edge and choosingChange to Arc Segmentin the context menu. As a shortcut, you can select the edge and pressa.

Change arcs back to linesby using the context menu of an arc segment. As a shortcut, you can select the edge and pressl.

Edit tangents of curve segmentsby dragging the tangent gizmos of a selected arc edge.

Change segments into ellipse arcsusing the context menu.

Edit ellipse arcsby selecting an edge and dragging the purple gizmo at the center of the arc.

2.4 InsertSymbolTool

WithInsertSymbolTool, you can click to insert shape instances at the mouse position.

The default shape is a circle. You can replace the default by changing the symbol property of the tool. In the following example, weâll changeInsertSymbolToolso that it creates horizontal lines of length 1 centered at the mouse position:

Step 3: Display Labels

With some basic shapes in place, letâs add meaning to the shapes by creating labels. You can use Labels to display anything you want. For example, we will use a label to display the area and length of a shape.

3.1 Labels for Area and Length

PolygonToolandPolygonEditToolboth have options to display area (polygons) and respective length (polylines).

To display the area of a polygon being edited, call the following:

Similarly, you can display the length of new polylines:

You can use the same functions in PolygonEditTools to display the area and length of a shape.

3.2 Units for Areas and Lengths

Edit 2D uses the same units and length calibration as the MeasureExtension. You can use MeasureExtensionâs calibration panel to specify units and calibration for your Edit2D shapes.

If you use Edit2D without the MeasureExtension, it will display all coordinates in model units. You can customize units by modifying or replacingDefaultUnitHandler. More information is available in theCustomize Edit2Dtutorial.

3.3 Creating Custom Labels

You can also give shapes custom text labels. The following example attaches a custom text label to the first shape in the layer.

Similarly, you can attach a custom label to the edge of a shape.

If you no longer want a label, you can remove it.

3.4 Apply Labels to Multiple Shapes

You can easily apply labels to a whole group of shapes using aShapeLabelRule. AShapeLabelRulewill define a rule for how to apply labels.

ShapeLabelRulehas a few default settings. You can configure or replace any of these settings.

Labels are created when shapes are added, and deleted when shapes are removed.

Labels are created only for visible shapes larger than 5 pixels.

Labels smoothly fade out when the shape becomes smaller than 5 pixels.

WithShapeLabelRule, you can also define a:

Filter: Determines which shapes should be labeled.

Text rule: Determines the text for each shape.

Style rule: (Optional) Determines how to stylize a label.

A simple example is to create aShapeLabelRulethat displays the shape properties. In this example, we will label each shape with its class name.

Step 4: Snapping

When drawing new shapes or moving vertices,PolygonToolandPolylgonEditToolsupport many types of snapping.

Snapping to a sheet geometry

Snapping to edit layer geometry

Snapping to angles

Snapping to combinations of the previous types.

Snapping is active by default but can be suppressed by holdingShift. Geometry snapping and snapping indicators work the same way in Edit2D as with the Measure extension. Snapping to intersections and angles is only supported by Edit2D.

4.1 Geometry Snapping

There are two types of geometry snapping:

Point-Snap: Snap to a unique point. This can be a line vertex, a circle midpoint, or a line intersection. Edit2D displays a square to indicate that you are creating a point-snap.

Segment-Snap: Snap to a segment (for example, a line or circular arc). The position is not fully snapped, but constrained to a certain segment. Edit2D shows a crosshair of three lines to indicate that you are creating a segment-snap.

4.2 Angle Snapping

When usingPolygonToolor moving vertices withPolygonEditTool, angle snapping is indicated by red dashed lines.

By default, we snap to angles that are multiples of 45Â°. You can change this behavior by changing the table of snapping angles inAngleSnapper.

Angle snapping always refers to a ânewâ edge that you are currently modifying.

InPolygonTool, this refers to the new edge that you would get when adding the next vertex at the current mouse position.

InPolyEditTool, when moving a vertex, it refers to the edges that start/end at the vertex being moved.

Angle snapping works if the new edge forms a snapping angle with any other edge in the shape. You can also snap to the perpendicular bisector of another edge.

4.3 Intersection Snapping

Snapping to an angle or line segment only constrains the snap position to one line segment. If there are multiple lines that a mouse position can snap to, the intersection of the closest two points is chosen.

The following cases are possible:

Intersection between two geometry segments (each may be sheet geometry or edit layer geometry)

Intersection between two angle snaplines

Intersection between an angle snapline and line segment.

The following image shows an example of the third case. The intersection of a perpendicular bisector (angle snap) and a line segment on a sheet (geometry snap).

Whatâs Next?

To learn more about Edit2D, check out these tutorials:

Drawing Edit2D Shapes Manually

Customizing Edit2D

```
// Facilitate access to extension and layer
window.edit2d = NOP_VIEWER.getExtension('Autodesk.Edit2D');
window.layer  = edit2d.defaultContext.layer;
window.tools  = edit2d.defaultTools;

// Convenience function for tool switching per console. E.g. startTool(tools.polygonTool)
var startTool = function(tool) {

    var controller = NOP_VIEWER.toolController;

    // Check if currently active tool is from Edit2D
    var activeTool = controller.getActiveTool();
    var isEdit2D = activeTool && activeTool.getName().startsWith("Edit2");

    // deactivate any previous edit2d tool
    if (isEdit2D) {
        controller.deactivateTool(activeTool.getName());
        activeTool = null;
    }

    // stop editing tools
    if (!tool) {
        return;
    }

    controller.activateTool(tool.getName());
}

```

```
startTool(tools.polygonTool);

```

```
startTool(tools.polylineTool)

```

```
startTool(tools.polygonEditTool);

```

```
startTool(tools.insertSymbolTool);

```

```
let line = new Autodesk.Edit2D.Polyline().makeLine(-1, -1, 1, 1);
tools.insertSymbolTool.symbol=line;

```

```
tools.polygonTool.setAreaLabelVisible(true);

```

```
tools.polygonTool.setLengthLabelVisible(true);

```

```
tools.polygonEditTool.setAreaLabelVisible(true);
tools.polygonEditTool.setLengthLabelVisible(true);

```

```
var poly = layer.shapes[0];
var label = new Autodesk.Edit2D.ShapeLabel(poly, layer);
label.setText('MyLabel');

```

```
var poly = layer.shapes[0];
var label = new Autodesk.Edit2D.EdgeLabel(layer);
label.attachToEdge(poly, 0);
label.setText('My Edge Label');

```

```
label.dtor();

```

```
// Label each shape with its className
var classRule = new Autodesk.Edit2D.ShapeLabelRule(layer, shape => shape.constructor.name);

```

```
edit2d.defaultContext.snapper.angleSnapper.snapAngles

```


---

# Drawing Edit2d Shapes Manually

Drawing Edit2d Shapes Manually

With Edit2D loaded in your application, you can begin adding shapes to PDF files and sheets. This tutorial demonstrates how to draw and change shapes using JavaScript, giving you a view into the mechanisms that make up the Edit2D extension. Google Chrome is required to complete this tutorial.

This tutorial covers:
- Drawing polygons and polylines
- Adding and removing shape styles
- Drawing Bezier and ellipse arcs
- Converting your Edit2D shapes to and from SVG

Before you do this tutorial, you should complete theSetting Up Edit2Dtutorial. Tutorials for using and customizing Edit2D are linked at the end of this tutorial.

Step 1: Run the Edit2D Playground

For this tutorial, you need to set up the Edit2D playground. The Edit2D playground is useful for debugging Edit2D and testing its functionality. To set up the playground, copy this code snippet to your Chrome DevTools snippet collection and run it:

Setting up the Edit2D playground gives you quick access to some Edit2D functions. However, because the functions are mechanisms for testing, they should not be used in a production code or environment. They are used in this tutorial to demonstrate how the Edit2D extension works after being loaded in your application.

Step 2: Check Sheet Coordinates

The following steps contain code snippets that let you draw shapes, lines, and arcs. You need to change the coordinates in these snippets so that the items are within visible range of your sheet. By default, Edit2D uses the same coordinate system as the underlying sheet. To find out the visible area for a sheet, you can check the bounding box of the model:

You can now check x/y values withbox.minandbox.max.

Step 3: Draw Polygons and Polylines

Letâs start by drawing a polygon. Enter the following snippet to add a triangle to your sheet. Remember to adjust the coordinates so that the triangle is visible on your PDF or sheet.

You can create polylines using similar code:

Step 4: Add Shape Styles

All Edit2D shapes have astylethat configures their appearance. Letâs modify the style of the polygon we created.

Notice that you must uselayer.update()to show the changes. This is because an edit layer knows the shape it is showing, but the shape does not know which edit layer is using it. If a shape you are modifying is already displayed, as in this example, you must update the layer.

Step 5: Undo Changes

5.1 Remove Shapes

You can remove a single shape usinglayer.removeShape(poly)or clear the entire layer usinglayer.clear().

5.2 Use Undo/Redo

For simplicity, we manipulated the layer directly in our examples. If you are using the Edit2D tools in your application, they track the undo/redo history. Mixing this with manual modifications may cause inconsistencies between the undo history and the actual layer state.

To make sure your manual changes are tracked in the undo/redo history, wrap your modifications into an action.

If you are using Edit2Dâs default toolset, theEdit2DContextprovides shortcuts for tracking your manual changes.

More generally, you can perform an action by calling run on the undoStack. Here is an example for adding multiple shapes in this way:

Step 6: Draw Bezier Arcs

Polygons and polylines can contain only straight line segments. To create shapes that are fully or partially smooth, you can usepathshapes. Path shapes allow you to change straight line segments to Bezier arcs.

This example demonstrates how to create a polypath:

The arc segment is specified by 4 control points P0, P1, P2, P3;

P0 and P3 define the start and end point. These points are specified in advance by the start and end positions of the edgeâs vertex.

P1 and P2 are points that control the start and end tangents of the arc.

As previously noted, you needlayer.update()for shapes that are already visible to show the changes from callingsetBezierArc(..).

Creating a polyline path is similar to creating a polygon path.

Notice that the polyline path requires 4 vertices while the polylgon path only needed 3. This is because the closing segment from c to a is added automatically when using the polygon path. To create the same closed shape with a polyline path, you need to repeatvertex aat the end. Be aware that the number of valid segment indices for polygons isvertexCount-1andvertexCount-2for polylines.

Step 7: Draw Ellipse Arcs

The following example shows how to specify an ellipse arc. All ellipse parameters are 1:1 matching with those in SVG standard.

Step 8: About Edit2D Shapes and SVG Shapes

You can convert SVG shapes to Edit2D shapes or convert Edit2D shapes to SVG shapes.

8.1 Import and Convert SVG Shapes

The following example shows how to import a single SVG shape and convert it to an Edit2D shape.

8.2 Export and Convert Edit2D Shapes

You can also export Edit2D shapes as SVG shapes.

In the following example, we convert the full content of an Edit2D layer to an SVG and show the result in a pop up window.

When you export from Edit2D, you can add style attributes.

Example output: <path d=âM 12.79,21.51 H 18.7 V 18.56 H 12.79 Zâ stroke=ârgb(0,0,128)â fill=ârgb(0,0,128)â stroke-width=â3â fill-opacity=â0.2â/>

You can also serialize Edit2Dâs layer content 1:1 into an xml file and download it.

Whatâs Next?

Now that youâve learned how to draw shapes manually, check out these other Edit2D tutorials:

Using the Edit2D Toolset

Customizing Edit2D

```
// Facilitate access to extension and layer
window.edit2d = NOP_VIEWER.getExtension('Autodesk.Edit2D');
window.layer  = edit2d.defaultContext.layer;
window.tools  = edit2d.defaultTools;

// Convenience function for tool switching per console. E.g. startTool(tools.polygonTool)
var startTool = function(tool) {

    var controller = NOP_VIEWER.toolController;

    // Check if currently active tool is from Edit2D
    var activeTool = controller.getActiveTool();
    var isEdit2D = activeTool && activeTool.getName().startsWith("Edit2");

    // deactivate any previous edit2d tool
    if (isEdit2D) {
        controller.deactivateTool(activeTool.getName());
        activeTool = null;
    }

    // stop editing tools
    if (!tool) {
        return;
    }

    controller.activateTool(tool.getName());
}

```

```
var box = NOP_Viewer.model.getBoundingBox();

```

```
// Create simple triangle
var poly = new Autodesk.Edit2D.Polygon([
    {x: 53, y: 24},
    {x: 62, y: 24},
    {x: 57, y: 34}
]);

// Show it
layer.addShape(poly);

```

```
//Create polyline
var polyline = new Autodesk.Edit2D.Polyline([
    {x: 54, y: 30},
    {x: 54, y: 35},
    {x: 62, y: 35},
    {x: 62, y: 30}
]);

// Show it
layer.addShape(polyline);

```

```
// Configure shape style
var style = poly.style;
style.fillColor = 'rgb(255,0,0)';
style.fillAlpha = 0.3;
style.lineWidth = 1.0;
style.lineStyle = 11;

// show changes
layer.update();

```

```
edit2d.defaultContext.clearLayer();
edit2d.defaultContext.addShape(poly);
edit2d.defaultContext.removeShape(poly);

```

```
const action = new Actions.AddShapes(this.layer, shapes);
this.undoStack.run(action);

```

```
// Create simple PolygonPath
var path = new Autodesk.Edit2D.PolygonPath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}  // c
]);

// Change segment (a,b) from line to arc
path.setBezierArc(
    0,              // segment index (= index of its start vertex)
    54.72, 20.54,   // control point to define start tangent
    60.53, 20.34    // control point to define end tangent
);

// Show it
layer.addShape(path);

```

```
// Create simple PolylinePath
var path = new Autodesk.Edit2D.PolylinePath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}, // c
    {x: 53, y: 24}, // d = a (repeated to close the triangle)
]);

// Change segment (a,b) from line to arc
path.setBezierArc(0, 54.72, 20.54, 60.53, 20.34);

// Show it
layer.addShape(path);

```

```
// Create simple PolygonPath
var path = new Autodesk.Edit2D.PolygonPath([
    {x: 53, y: 24}, // a
    {x: 62, y: 24}, // b
    {x: 57, y: 34}  // c
]);

// Change segment 0 into ellipse arc
var params = new Autodesk.Edit2D.EllipseArcParams();

// ellipse radii along ellipse x/y-axis
params.rx = 4;
params.ry = 6;

// ccw rotation of x/y-axes in degrees.
// rotation 0 means ellipse-x-axis = (1,0)
params.rotation = 0;

// whether to use shorter or longer path around ellipse.
params.largeArcFlag = false;

// Whether to go counterclockwise (true) or clockwise (false) from startAngle.
params.sweepFlag = true;

path.setEllipseArc(0, params);

layer.addShape(path);

```

```
// Create Edit2D shape from SVG string
const svgString = '<path d="M 12.79,21.51 H 18.70 V 18.56 H 12.79 Z"/>';
const shape2    = Autodesk.Edit2D.Shape.fromSVG(svgString);

```

```
// Get SVG string representation from a shape
shape.toSVG();

```

```
function showSvgPopup() {

    // window size
    const width = 400;
    const height = 400;

    // define pixel-scope as box2
    const pixelBox = new THREE.Box2();
    pixelBox.min.set(0, 0);
    pixelBox.max.set(width, height);

    // convert layer to svg element
    const svg = Autodesk.Edit2D.Svg.createSvgElement(
        layer.shapes,
        { dstBox: pixelBox } // rescale to fit pixelBox [0,400]^2
    );

    // show in popup window
    const w = window.open('', '', `width=${width},height=${height}`);
    w.document.body.appendChild(svg);
    w.document.close();
    };

    showSvgPopup();

```

```
shape.toSVG({exportStyle: true});

```

```
function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function downloadLayerAsSvg() {

    // define pixel-scope as box2
    var pixelBox = new THREE.Box2();
    pixelBox.min.set(0, 0);
    pixelBox.max.set(400, 400);

    // get layer content as svg dom element
    var svgElem = Autodesk.Edit2D.Svg.createSvgElement(layer.shapes, {dstBox: pixelBox});

    // Serialize to string and download
    var serializer = new XMLSerializer();
    var xmlText = serializer.serializeToString(svg);

    download('test.svg', xmlText);
};

```


---

# Customizing Your Edit2D Instance

Customizing Your Edit2D Instance

Edit2D defines several defaults when you run it. In theSetting Up Edit2Dtutorial, you looked at an application that runs some of those defaults, including Edit2Dâs default toolset and context. There are several ways to customize Edit2D behavior. This tutorial covers some of them.

This tutorial shows you ho to:

Customize units

Customize your toolset

Customize context menu

Add more layers

Customize the appearance of selection and hover

Before completing this tutorial, you should be familiar with how to set up and use Edit2D in your application. Refer to theSetting Up Edit2Dtutorial to familiarize yourself with these concepts. Tutorials about how to use Edit2D and how to manually draw Edit2D shapes with JavaScript are linked at the end of this tutorial.

Step 1: Customize Units

By default, Edit2Dâs unit handling is configured the same way as theMeasureextension in Viewer SDK. If theMeasureextension is not available, values are displayed 1:1 in layer coordinates without units.

Edit2D sets the default formatting for label text usingDefaultUnitHandler.DefaultUnitHandlerdefines how to translate measurements in layers to the text displayed in labels. This includes:
- The name of the unit
- The way in which lengths and areas in layer-coords are translated to displayed values
- The number of digits displayed in labels.

You can define your own formatting by replacing the default unit handler. Note that you need to setunitHandlerbefore specifying the tools.

Step 2: Customize Your Toolset

In the previous tutorial, we set up Edit2D with the default toolset, using theregisterDefaultTools()method. This method completes a few steps for you in order to quickly set up Edit2D:

Creates a single layer and gizmoLayer

Creates all available tools

Registers tools at ToolController

It is usually sufficient to use the default toolset, as long as you can be sure that you are the only one who is using Edit2D within your application. However, Edit2D can also be used by different software components within the same application. This may happen, for example, if Edit2D is used in another Viewer extension. In this case, it would produce conflicts if different components are all accessing the same tools and EditLayer.

You can avoid conflicts by registering your own toolset. First, youâll want to register your tool, giving your toolset a name unique for your application.

Once youâve registered your tools, you need to define your toolset, context, and tools.

Step 3: Customize Context Menu

When you load Edit2Dâs default toolset, it automatically registers a context menu with features suchaddVertexandremoveVertex. You can add application-specific items by registering acontextMenuCallback. You need to register the callback after updating the Edit2D context menu. This is because the Edit2D context menu replaces Viewer SDKâs default context menu when your user hits an an Edit2D shape.

You can also remove the Edit2D contextMenu altogether.

Step 4: Customize Appearance of Selection and Hover

By default, displayed shape styles are slightly varied when users hover over or select them. For example, when a user selects a shape, the shape will display an increased line width and fill opacity. These responses do not alter the actual styles of the shapes you are editing. Instead, Edit2D uses style modifiers. A style modifier is a callback that temporarily overrides the display style of a shape with another one.

In the following example, we will replace the default style modification behavior with custom highlighting that affects all shapes that pass the filter function(shapeId)=>bool.

A custom highlighting can, but does not have to, replace the default one. A layer supports multiple style modifiers that are applied in the order in which they were added.

Note: The style parameter may either be the original polygon style or the style returned by a previously applied style modifier. Make sure to create a modified copy, rather than change the style itself.

Step 5: Add More Layers

When you register your tools, Edit2D creates a singleEditLayerfor your tools to work onâcontext.layerâ and a second one for temporary overlaysâcontext.gizmoLayer. You can add additional layers to the default setup.

Once youâve created the layer, you can choose how to display it. By default, additional layers are represented as overlays.

More generally,layer.sceneis aThree.Scenewith triangulated shapes that you can use in whatever way you want.

Whatâs Next?

Now that youâve learned how to customize Edit2D, check out these tutorials:

Using the Edit2D Toolset

Drawing Edit2D Shapes Manually

```
const unitHandler = new Autodesk.Edit2D.SimpleUnitHandler(viewer);
unitHandler.layerUnit    = 'in';
unitHandler.displayUnits = 'cm';
unitHandler.digits       = 4;

// Register your tools after defining unitHandler

```

```
edit2d.registerTools(MyToolSetName);

```

```
const toolSet = edit2d.getToolSet(MyToolSetName);
const context = toolSet.context;
const tools   = toolSet.tools;

```

```
const myItem = {
    title: 'My extra menu item',
    target : ()=> {console.log('Hello new item);}
};

const cb = (menu) => {
    menu.push(item);
}

//Let Viewer SDK trigger the callback when building the contextMenu
viewer.registerContextMenuCallback('MyOwnItems', cb);

```

```
const toolset = edit2d.getToolSet(MyToolSetName);
toolset.contextMenu.unregister();

```

```
// Switch-off default highlighting behavior
const selection = edit2d.defaultContext.selection;
layer.removeStyleModifier(selection.modifier);

// Define custom style modifier instead
const myModifier = (shape, style) => {

    // Leave style unaffected if shape does not pass the filter
    if (!myFilter(shape.id)) {
        return undefined;
    }

    // Return modified style copy
    const modified = style.clone();
    modified.fillColor = 'rgb(255, 0, 0)';
    return modified;
};

layer.addStyleModifier(myModifier);

```

```
// Create new layer
const anotherLayer = new Autodesk.Edit2d.EditLayer(viewer);

```

```
this.viewer.impl.addOverlay(OverlayName, layer.scene)

```


---

# Using Aggregated View to Load a Model

Using Aggregated View to Load a Model

AggregatedView implements a viewing application based on Viewer3D. The purpose of Aggregated View is to provide functionality around Viewer3D to facilitate implementation of viewer application workflows like switching between different views or toggling models on or off dynamically.

Examples of AggregatedView functionality include:

React compatibility: You can set an array of nodes from React property and AggregatedView takes care of loading and showing or hiding models as needed.

LRU-Caching of models: Keep models in memory for fast switches, but unload unused models if memory is critical.

Extensions: You can specify which extensions to load or load the following defaults:Autodesk.CrossFadeEffects,Autodesk.AEC.LevelsExtension,Autodesk.ModelStructure,Autodesk.AEC.HyperlinkExtension,Autodesk.AEC.Minimap3DExtension,Autodesk.AEC.CanvasBookmarkExtensionandAutodesk.AEC.DropMeExtension.

Home camera: All models are considered when calculating the shared home view.

Application State management: Facilitates some state management. For example,You can set a camera before or after the model is loaded.You can start Walk-mode before or after the BIMWalk extension loaded.You can toggle visibility of a model regardless of loading state of the model.

You can set a camera before or after the model is loaded.

You can start Walk-mode before or after the BIMWalk extension loaded.

You can toggle visibility of a model regardless of loading state of the model.

GlobalOffsets: Choose globalOffset automatically, but identically for all models to make sure that they are placed consistently.

View Switches: Allow visibility toggling (hide/show) versus full view switches (switchView(nodes)), the latter including proper reset of camera, UI, and extensions.

Diff Setups: Use diffOptions to view changes between aggregated views.

For more information, see:AggregatedView

Initialize and load a model with Aggregated View

Loading a model with Aggregated View follows the same steps as theAutodesk.Viewing.Viewer3Dclass. Initialize and load your document from a URN usingAutodesk.Viewing.InitializerandAutodesk.Viewing.Document.load.

Loading multiple models

AggregatedViewmakes it easy for you to load multiple models. UseAutodesk.Viewing.Document.loadto load each document.

Switching between views

TheswitchViewfunction resets the extension, tools, and camera before loading the specified bubble nodes.

The following snippet finds all 3D bubble nodes from a loaded document and loads a 3D bubble node. This example also gets the model instance that is loaded.

After the first model is loaded, you can switch to other views by using the same method.

The following snippet demonstrates how you can unload a single bubble node.

To unload all current models use:

For an Interactive Example, seeAggregated View.

```
// AggregatedView instance
var view = new Autodesk.Viewing.AggregatedView();

// Initialize and load a document.
Autodesk.Viewing.Initializer(options, function onInitialized() {
    // Get the Viewer DIV
    var htmlDiv = document.getElementById('forgeViewer');

    // Initialize the AggregatedView view
    view.init(htmlDiv, options).then(function () {
        Autodesk.Viewing.Document.load(documentId, (doc) => {
            // Set the nodes from the doc
            var nodes = doc.getRoot().search({ type: 'geometry' });
            // Load the first bubble node. This assumes that a bubbleNode was successfully found
            view.setNodes(nodes[0]);
        }, (errorCode, errorMsg, messages) => {
            // Do something with the failed document.
            // ...
        });
    });
});

```

```
const bubbleNodes = [];
// docs is an array of loaded documents
docs.forEach((doc) => {
    var nodes = doc.getRoot().search({ type: 'geometry' });
    bubbleNodes.push(nodes[0]);
});
view.setNodes(bubbleNodes);

```

```
// Get all of the 3D bubble nodes in a loaded document
const nodes3D = doc.docRoot.search({ role: '3d', type: "geometry" });

// The switchView function will load the model
view.switchView(nodes3D[0]);

// Get the model after it is fully loaded
const model = await view.getModelAndWait(nodes3D[0]);

```

```
// Get all of the 2D bubble nodes in a loaded document
const nodes2D = doc.docRoot.search({ role: '2d', type: "geometry" });

// Now lets load two 2D models
// This will reset the UI, the extensions, the tools and the camera before a new node is loaded
view.switchView([nodes2D[0], nodes2D[1]]);

```

```
// Unload a model
view.unload(nodes2D[1]);

```

```
// Unload all of the loaded models
view.unloadAll();

```


---

# Selective Loading Using Queries

Selective Loading Using Queries

Selective Loading uses spatial and property queries to filter the model geometry and load only what you need.
It allows you to provide a better experience interacting with the 3D scene by:

Improving the load time

Loading only the portion of the model required

Currently, the API focuses on load-time optimizations and only load-time filtering is supported.
Minor, known issues in the progressive rendering and the delay in time-to-first-pixel when using spatial filters will be addressed in future releases.

Example:

The image on the left shows a model without the loading filters applied.
The middle image shows an axis-aligned box (blue) being used as the spatial filter to define the portion of the model to load.
The image on the right shows the model loaded with the filter load-option passed toloadDocumentNode.
The same option can be provided toviewer.loadModel.

Quickstart Example for Load-time Filtering

To restrict model loading to certain areas or types of geometry, use queries to filter what to load usingloadDocumentNodeoptions.
A load-time filter can be set by specifying a spatial and/or a property query using thefilterload-option.

The following example creates a load-time filter using aspatial_query.
It describes a condition for testing an axis-aligned bounding box (aabbox) against the given axis-aligned box (aabox).
Objects that do not fulfill the condition are not loaded and only the objects in the shaded area are loaded.

Try it out

You can interact and experiment with the viewer in the following example (the blue box shows the boundary of a simple, spatial query):

Tip: To experiment with the Viewer click EDIT ON CODEPEN at upper right in the example.

Spatial Query Language

Spatial conditionsare specified using a spatial query language.
A spatial query comprises aspatial condition(<scondition>).

<scondition>

Spatial conditions are composed of building blocks that determine whether an object should be loaded or not. Usually these are an expression, a primitive, an optional proxy, and in some cases additional parameters:

Primitives define what to test objects against. In the example above, all objects are tested against an axis-aligned box.

Proxies define how to represent objects when testing them against the primitive. This could be the objectâs axis-aligned bounding box, or a bounding sphere, for example. The proxy part of a condition is optional and defaults to the objectâs bounding box, which is the only proxy that is currently supported.

Expressions define how to interpret the proxy-primitive check. For example, an object could pass the condition if its bounding box intersects the given primitive, or it could be required to be fully enclosed.

Conditions can be negated, combined and nested as illustrated below.

Condition

Description

{"$intersects":[<sprimitive>]}

True, if the primitive intersects with the objectsâs axis-aligned bounding box.

{"$encloses":[<sprimitive>,<sproxy>?,epsilon?]}

True, if the primitive has a volume and fully encloses the objectsâs axis-aligned bounding box.sproxy(optional) defines the type of the bounding box. Defaults toaabboxif not provided.epsilon(optional) is a scalar that expands each dimension of the primitive. Defaults to 0.0 if not provided.

{"$extent":[<threshold>]}

True, if the volume of the objectsâs axis-aligned bounding box (world space) passes the threshold.

{"$not":<scondition>}

Inverts the given condition.

{"$or":[<scondition1>,<scondition2>,...]}

Any of the given conditions must be fulfilled.

{"$and":[<scondition1>,<scondition2>,...]}

All of the given conditions must be fulfilled.

<sprimitive>

Spatial primitives are basic geometries such as points, lines, planes, spheres, and axis-aligned boxes that can be used to create spatial conditions. Currently, only the axis-aligned box is supported.

Primitive

Specification

Example

aabox

[minx,miny,minz,maxx,maxy,maxz]

{"aabox":[-3.3,1.1,0.4,-1.8,3.9,2.7]}

<sproxy>

Spatial proxies describe the type of asimplified geometrical representations of objectsthat are used for the evaluation of a spatial condition. Currently, only axis-aligned bounding box is supported and the parameter is not explicitly required.

Proxy

Description

aabbox

Axis-Aligned Bounding Box

Spatial Query Examples

Simple Example:

Complex Example:

Immediate Spatial Evaluation

Spatial queries are evaluated per object as soon as all objects and their exact bounding volumes are available.
For large models consisting of lots of individual objects, this can introduce a minor but notable offset to the loading time.
In this case, the spatial evaluation behavior can be changed toimmediate evaluationusing thespatial_behaviorfilter option.
Here, preliminary, approximate bounding volumes are used for spatial evaluation once an object is known to the loader, likely leading to inaccuracies in filter evaluation:

Property Query Language

The property queries use a simplified version of theACC Model Property Service Query Language, but with a reduced feature set.
Only$or,$and,$not,$in,$eq,$ne,$like,$isnull,$notnull, and$coalesceexpressions are currently supported.

Property Query Examples

Simple Example:

Complex Example:

How to Get Property Hashes

Currently, property queries rely on property hashes. There are two ways to acquire these, either directly or indirectly.

Direct Enumeration of Property Hashes: To obtain the available properties and their hashes, you can enumerate them as soon as the property database is loaded using the following command:

Hash Lookup Syntax: Instead of using thes.props.p...syntax, you can utilize a preliminary property lookup syntax to perform implicit property hash lookups:

A hash lookup currently requires an exact match of the property name to produce valid query results. If no objects are loaded, consider modifying the property query for better search outcomes.

Top-level Filter Condition

When bothspatial_queryandproperty_queryare set, an object passes filtering if both conditions are met.
This behavior can be specified in the filter load option by specifying theroot_conditionto be eitherand(default) oror:

Whenandis specified, filtering cannot start immediately but needs to wait until all object bounds are known and properties are loaded.

```
const viewer = new Autodesk.Viewing.GuiViewer3D(document.getElementById('viewer'));
Autodesk.Viewing.Initializer(options, () => {
    viewer.start();
    Autodesk.Viewing.Document.load(documentID, onDocumentLoadSuccess,
        () => console.error('Failed to fetch the manifest.'));
});

function onDocumentLoadSuccess(viewerDocument) {
    const defaultModel = viewerDocument.getRoot().getDefaultGeometry();
    viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
        filter: {
            "spatial_query": {
                "$encloses": [ { "aabox": [ -21.0, 37.0, -4.0, 46.0, 59.0, 21.0 ] } ]
            },
        }
    });
}

```

```
"spatial_query": { "$encloses": [ { "aabox": [ -0.3, -3.3, -4.9, +0.0, -3.2, -2.1 ] } ] }

```

```
"spatial_query": { "$or": [

        /* two regions of interest where objects should be loaded */
        { "$encloses": [ { "aabox": [ -168.99, -226.19, -739.92, -133.78, -192.75, 978.69 ] } ] },
        { "$encloses": [ { "aabox": [ -389.19, -368.12,  836.04,  382.63,  140.48, 978.69 ] } ] },

        { "$and": [

            /* two regions that should remain empty (not intersecting with the scene objects) */
            { "$not": { "$or": [
                    { "$intersects": [ { "aabox": [  -88.49, -331.87, -536.42, 486.78, 350.62, -314.62 ] } ] },
                    { "$intersects": [ { "aabox": [ -285.78, -170.97,  119.58, -10.78, 353.67,  581.08 ] } ] }
                ] } },

            /* objects should pass a minimal world-space volume */
            { "$extent": 100000.0 } ] }
        ] }

```

```
viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
    filter: {
        "spatial_behavior": "immediate", // or "exact" (default)
        "spatial_query": { ... },
    }
});

```

```
"property_query": {
    "$and": [
        { "$notnull": "s.props.p20d8441e" },
        { "$notnull": "s.props.p30db51f9" },
        { "$notnull": "s.props.p13b6b3a0" }
    ] }

```

```
"property_query": [
    { "s.props.p4735026f": "'VALV'" },
    { "s.props.p4735026f": "'FBLI'" },
    { "s.props.p4735026f": "'TUBI'" },
    { "s.props.p4735026f": "'INST'" },
    { "s.props.p4735026f": "'ELBO'" },
    { "s.props.p4735026f": "'REDU'" },
    { "s.props.p4735026f": "'ATTA'" },
    { "s.props.p4735026f": "'FLAN'" } ]

```

```
const propertyHashes = await model.getPropertyHashes();

```

```
// Match basic walls (by name property) and all objects that have CENTRIFUGE in their LTS description
"property_query": [
    // instead of { "s.props.p153cb174": "'Basic Wall'" },
    { "?name": "'Basic Wall'" }, // note the ? indicating a look-up
    { "?Base Constraint": "'Level 1'" } ]

```

```
viewer.loadDocumentNode(viewerDocument, defaultModel, { // ...options
    filter: {
        "root_condition": "or", // or "and" (default)
        "spatial_query": { ... },
        "property_query": { ... },
    }
});

```


---

# Glossary of Terms

Glossary of Terms

Term

Definition

access token

An access token (sometimes just âtokenâ or âbearer tokenâ) is a credential used by an application to access an API.The Authentication API returns an access token at the end of a successful authentication flow.The Viewer requires access tokens that have a scope ofviewables:read.For more information, see theAuthentication API BasicsandScopessections.

canvas

An HTML element used as a target for rendering the Viewer SDK.

dbid

The ID of an object linking it to its metadata in the properties database. The dbid is also needed to call Viewer SDK methods; for example, the function used to hide objects in the model expects a list of dbids as its argument.

document

The file for the model you want to load. The doc gives access to the root and provides a method for finding elements by id. To learn more, seeDocument.

extensions

A piece of JavaScript code that is optionally loaded at runtime to extend or modify Viewer SDKâs behavior.Some extensions are bundled with Viewer SDK, and developers
can write their own extensions for specific use cases.

fragID

The ID for an individual fragment of a Viewer SDK model.

fragment

A part of an object with specific geometry and material; a single object consists of one or more fragments. For example, a door object may consist of a door knob (with brass material) and a door frame (with wood material).

geometry node

The smallest selectable element of a model in Viewer SDK (e.g. a door). This is also known as anobject.

ghosting

A feature that makes selected nodes in a model transparent, allowing other nodes to become more prominent.

headless

Viewer SDK without UI elements; only the 3D render canvas.

highlighting

The act of changing the way an object is drawn to make it standout. The Viewer SDK will highlight objects when they are selected and when the user mouses over them. Theming is another way to highlight objects available to applications.

markup

An extension for annotating viewables.

manifest

The result of a translation process, a structured
collection of resources (e.g., model geometry,
thumbnails, camera views) used by Viewer SDK.Get a manifest using theGET :urn/manifestendpoint.Viewer SDK can only render viewables.

measure

An extension for measuring the distance between two points on the surface of a model.

orbit

A feature that allows users to move the camera up, down, left & right.

overlay

A feature that allows you to add custom geometry to the loaded model. To learn more, see theAdd Custom Geometrytutorial.

profile

A set of preferences and extensions in the Viewer SDK. Developers can create their own custom profiles and there are built-in profiles available in the Viewer SDK to bring the same user experience as Autodesk desktop products like Navisworks and Revit.

property database

Metadata associated with a viewable and its parts. The property database maycontain metadata for each geometry node.

scene

An environment where one more more models are placed. Models, cameras, and lights can be positioned or transformed in the environmentâs coordinate system.

search

A feature for searching the viewableâs metadata, alsocalledproperty database.

section(ing)

An extension for cutting 3D models and seeing inside of them.

seed file

The original file that you want to visualize in Viewer SDK.

selection

A feature that lets users select nodes in a model. You can use selection to specify which nodes users can select and keep track of the selected nodes.

theming

A means to highlight objects by changing their color.

viewable

Either a 3D model or a 2D sheet referenced by the manifest.

viewcube

A tool available for 3D models that helps users orient the cameraâs position.

viewer state

The current view of a model based on the position of the camera systemâs eye.


---

# AggregatedView

AggregatedView

AggregatedView implements a viewing application based on Viewer3D. Its purpose is to provide functionality around Viewer3D to facilitate implementation of viewer application workflows like switching between different views or toggling models on/off dynamically.

Examples of AggregatedView functionality include:

Facilitate use in react: Just set an array of nodes from React property and AggregatedView takes care to make sure that models are loaded and shown/hidden as needed.

LRU-Caching of models: Keep models in memory for fast switches, but unload unused models if memory is critical

Extensions: Setting up a couple of useful default extensions (can be customized or switched off where wanted)

Home camera: Setting a home view camera that considers multiple models.

Application State management: Facilitates some state management, e.g.Setting a camera without having to care whether the model is already loaded or not.Starting Walk-mode without having to care whether BIMWalk extension is already loaded.Allow toggling visibility of a model without having to care about the loading state of the model.

Setting a camera without having to care whether the model is already loaded or not.

Starting Walk-mode without having to care whether BIMWalk extension is already loaded.

Allow toggling visibility of a model without having to care about the loading state of the model.

GlobalOffsets: Choose globalOffset automatically, but identically for all models to make sure that they are placed consistently.

View Switches: Allow visibility toggling (hide/show) versus full view switches (switchView(nodes)), the latter including proper reset of camera, UI, and extensions

Diff Setups: Just set diffOptions to setup change visualization of aggregated views.

new AggregatedView()

Examples

Methods

init(parentDiv, options)

Initializes the AggregatedView and loads the following predefined extensions:Autodesk.CrossFadeEffects,Autodesk.AEC.LevelsExtension,Autodesk.ModelStructure,Autodesk.AEC.HyperlinkExtension,Autodesk.AEC.Minimap3DExtension,Autodesk.AEC.CanvasBookmarkExtensionandAutodesk.AEC.DropMeExtensionThe initialization can also be customized with the options object.

To initialize the viewer without loading the specified extension please referenceinitViewerInstance.

Parameters

parentDiv*HTMLDivElement

The div element in which the viewer will be initialized

optionsObject

Configuration options for aggregated view

viewerConfigObject

Used for initializing GuiViewer3D. This is the options object that is passed into either av.Viewer3D or av.GuiViewer3D

disableBookmarksboolean

Disable display of visual bookmarks

clusterfckObject

Dependency-Injection of clusterfck library (enables clustering of Bookmark icons)

viewerStartOptionsObject

Options passed to the viewer initialization process

ignoreGlobalOffsetboolean

Forces globalOffset to undefined for all loaded models. Effect of this is that all models are auto-centered using the model bbox. Note that this does only work if you never show more than one 3D viewable at once

unloadUnfinishedModelsboolean

By setting unloadUnfinishedModels, when calling hide(bubbleNode), it will unload models that havenât been fully loaded. Used in order to reduce amount of file loaders when switching between models

useDynamicGlobalOffsetboolean

If true, the globalOffset is applied dynamically after loading

cameraValidatorboolean

Called with a (camera, model) when using a model camera as start or home camera. This allows for clients to apply optional custom repairs for models with messy camera data

propagateInputEventTypesArray.<string>

By default, LMV ToolController âeatsâ all handled events so that they donât reach any other widgets. Specify an array of event types that you want this behaviour disabled for. For example [âmouseupâ, âmousedownâ] allows alloy to detect mouse outside clicks to close pending dropdown menus

createModelAlignmentService*function

Factory function to create AlignmentService implementation for loading/saving model transforms. See AlignmentServices above for details

getCustomLoadOptionsfunction

Allows for applying custom options to be used for all model loading. The callback returns an options object that is applied by default in all model-load calls. The signature should look like: function(av.BubbleNode)=>Object

viewerUnitsstring

If specified, all models are re-scaled from model units to this unit. Must be a GNU unit format string, e.g. âmâ.

multiViewerFactoryAutodesk.Viewing.MultiViewerFactory

Optional multi viewer factory. Used to create multiple viewers with shared resources

useConsolidationboolean

Optional flag to enable / disable mesh consolidation. Defaults to true.

Returns

type

description

Promise

returns a promise once all of the specified extensions are loaded.

returns a promise once all of the specified extensions are loaded.

initViewerInstance(parentDiv, options)

Initialize a new viewer instance.

To initialize the viewer and load the default extensions please seeinit.

Parameters

parentDiv*HTMLDivElement

The div element in which the viewer will be initialized

optionsObject

The same options object that is passed into the init method

reset()

Resets tools, UI, camera, and refPoint. This method should be called when an explicit view switch occurred instead of just toggling visibility of models.

getModel(node)

Finds a model for the given bubbleNode or key. To get multiple models referencegetModels. To make sure that the model is loaded referencegetModelAndWait.

Parameters

node*Autodesk.Viewing.BubbleNode

The Bubble node to use to get the model

Returns

type

description

Autodesk.Viewing.Model

The model that corresponds to the bubbleNode

The model that corresponds to the bubbleNode

Examples

getModelAndWait(node, checkIfVisible)

Find a model for given bubbleNode or key. If the model is not available yet, wait until itâs ready.

Parameters

node*Autodesk.Viewing.BubbleNode

The Bubble node to use to get the model

checkIfVisibleBoolean

If true, will wait until model is also visible

Returns

type

description

Promise

the promise resolves once the model is loaded with the model instance

the promise resolves once the model is loaded with the model instance

Examples

isEmpty()

Returns true if there are no visible bubble nodes.

Returns

type

description

Boolean

returns true if all nodes are invisible

returns true if all nodes are invisible

show(bubbleNode, customLoadOptions)

Makes sure that a model is loaded and shown

To get the bubbleNode from a URN please referenceDocument#load.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The node to load and show in the viewer

customLoadOptionsObject

Optional extra loadOptions to override/extend the default ones

Returns

type

description

Promise

Returns a promise which resolves with the model

Returns a promise which resolves with the model

Examples

hide(bubbleNode)

Hides the model associated from the supplied bubble node.

To show the model referenceshow.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The node to hide in the viewer

Examples

isVisible(bubbleNode)

Returns true if the supplied bubble node is currently visible.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The BubbleNode to check the visibility of

Returns

type

description

Boolean

true if the specified node is visible, false otherwise

true if the specified node is visible, false otherwise

hideAll()

Hide all of the models in the viewer.

getVisibleNodes()

Returns all of the visible bubble nodes.

Returns

type

description

Array.<Autodesk.Viewing.BubbleNode>

An array of all of the visible nodes

An array of all of the visible nodes

areAllNodes2D()

Returns true if all of the nodes are 2D.

Returns

type

description

Boolean

returns true if all nodes are 2D, false otherwise.

returns true if all nodes are 2D, false otherwise.

isOtgManifestMissing(bubbleNode)

Checks if the Otg manifest for a 3D viewable is available and complete. If not, it reports an error and returns false.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The BubbleNode

Returns

type

description

Boolean

true if the OTG manifest is missing.

true if the OTG manifest is missing.

load(bubbleNode, customLoadOptions)

Loads the model that is specified by the passed in bubbleNode parameter. Note this function will not show the model once it is loaded. To load and show the model reference theshowmethod.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The BubbleNode

customLoadOptionsObject

Optional extra loadOptions to override/extend the default ones

Returns

type

description

Promise

The promise resolves with the loaded model

The promise resolves with the loaded model

unload(bubbleNode)

Unload the model that corresponds with the passed in bubbleNode.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

The BubbleNode to unload

Examples

unloadAll(itemFilter)

Unload all of the models that are currently in the view.

Parameters

itemFilterfunction

This callback is used to check if a model needs to be unloaded. This callback recieves an object describing the current view item and it should return a boolean

Examples

setCameraGlobal(camera)

Set camera in global coords.

The current global offset is automatically subtracted

You donât have to specify all members, e.g., can leave out up or fov. Only defined values are replaced.

You can call it independent of loading state: If no model is loaded yet, the camera change is applied after first model add

Note that the call only has effect on current view, i.e., is discarded on reset/viewSwitch calls.

Parameters

camera*THREE.Camera

Camera instance that will be used to apply to global camera

setCamera(camera)

Set the view from the passed in camera.

Parameters

camera*THREE.Camera

Camera instance

startBimWalk()

Starts the BIM walk tool. Under the hood this method will activate the BimWalk extension.

stopBimWalk()

Stop the BIM walk tool. Under the hood this method will deactivate the BimWalk extension.

isBimWalkActive()

Returns true if the BimWalk tool is active.

Returns

type

description

Boolean

true if the tool is active, false otherwise.

true if the tool is active, false otherwise.

switchView(bubbleNodes, diffConfig)

Switches between bubble node models. This method will reset the view and then set the passed in nodes.

Use this for explicit view switches. SeesetNodes()for params.

Parameters

bubbleNodes*Autodesk.Viewing.BubbleNode, Array.<Autodesk.Viewing.BubbleNode>

The nodes to be shown

diffConfigObject

see the setNodes method for the diffConfig parameter

Returns

type

description

Promise

The promise resolves with the loaded models

The promise resolves with the loaded models

setNodes(bubbleNodes, diffConfig)

Load/Unload models so that the currently loaded models matches with the given list of svfs.

Note: UseswitchView()to do an explicit view switch (including resetting tools/camera). UsesetModels()to reconfiguring which models are visible in the current view.

Parameters

bubbleNodes*Autodesk.Viewing.BubbleNode, Array.<Autodesk.Viewing.BubbleNode>

The nodes to be shown

diffConfigObject

Options to activate diff views.

primaryBubblesArray.<Autodesk.Viewing.BubbleNode>

A subset of âbubbleNodesâ that participates in the diff. If âbubbleNodesâ contains more, these will be ghosted. These nodes represent the current/as-is state

diffBubblesArray.<Autodesk.Viewing.BubbleNode>

Length must match primaryBubbles. For each node primaryBubbles[i], diffBubbles[i] provides the corresponding âbeforeâ state to compare against

diffAutodesk.Viewing.BubbleNode

If svfs are sheet nodes, diff.supportModels must provide the bubbleNodes for the corresponding 3D support models. { diff, primary }

primaryAutodesk.Viewing.BubbleNode

Primary bubble node to do the diff comparison on

autoDetectboolean

If true, support models are automatically found - works for Revit models with master views

Returns

type

description

Promise

The promise resolves with the loaded models

The promise resolves with the loaded models

isLoadDone()

Returns true if all pending loading is finished. More concrete, it means that there is noâ¦

model-root loading

geometry loading, or

propDbLoading pending or in progress.

ReferencewaitForLoadDone.

Returns

type

description

Boolean

Returns true if all of the models in the view are fully loaded, false otherwise.

Returns true if all of the models in the view are fully loaded, false otherwise.

waitForLoadDone()

Returns a promise that resolves whenisLoadDone()returns true.

Returns

type

description

Promise

resolves when all isLoadDone returns true.

resolves when all isLoadDone returns true.

findDiffSupportModel(sheetNode)

âSupport modelsâ are 3D models that augment 2D diffs for better results: Instead of comparing the 2D objects directly, the correspodning 3D counterparts are compared. This is more reliable and avoids false positives due to irrelevant plotting differences. We use master views as support models, because they contain all objects of a given phase.

Given a bubble node referring to a 2D sheet node, this function returns the bubbleNode of the corresponding 3D master view that belongs to the same phase. This can be used as âsupport modelâ to obtain better results for 2D diff.

Parameters

sheetNode*Autodesk.Viewing.BubbleNode

A 2d bubble node

Returns

type

description

Autodesk.Viewing.BubbleNode

the coresponding 3d bubble node

the coresponding 3d bubble node

findDiffSupportModels(diffConfig)

Find corresponding 3D model for each diff/primary The result will be stored in the passed in diffConfig. The results will be in diffConfig.supportBubbles.diff and diffConfig.supportBubbles.primary.

For the diffConfig parameter referencesetNodes.

Parameters

diffConfig*Object

see the setNodes method for the diffConfig parameter

```
const view = new Autodesk.Viewing.AggregatedView();
// Initialize the aggregatedView with the HTML element and the options object
await view.init(viewerElement, options);

```

```
const nodes = view.getVisibleNodes();
// Get the model of the first bubble node.
const model = view.getModel(nodes[0]);

```

```
const model = await view.getModelAndWait(node);

```

```
// Load a document from a documentId/URN
Autodesk.Viewing.Document.load(documentId, (doc) => {
  // Find all of the 3D bubble nodes
  var nodes3D = doc.docRoot.search({ role: '3d', type: "geometry" });

  // Using aggregated view load and show the model.
  const model = await view.show(nodes3D[0]);
});

```

```
view.hide(node);

```

```
const nodes = view.getVisibleNodes();
// Unload the first model
view.unload(nodes[0]);

```

```
// This example will unload all invisible models.
view.unloadAll((item) => {
  return !item.visible
});

```


---

# AppScreenModeDelegate

AppScreenModeDelegate

ExtendsAutodesk.Viewing.ScreenModeDelegate

new AppScreenModeDelegate(viewer)

Screen mode delegate allowing the viewer to go full screen.

Unlike ViewerScreenModeDelegate class, this delegate doesnât use the full browser state, and it takes the entire page full screen, not just the viewer.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.


---

# BubbleNode

BubbleNode

Wrapper and helper for âbubbleâ data.

Bubble is a container of various 2D or 3D viewables (and additional data) that may be generated from a single seed file. The bubble is a JSON structure of nodes that have different roles, for example, they may represent sheets, nested 2D/3D geometry, etc.

This class wraps the internal representation of the bubble and adds a couple of helper methods.

new BubbleNode(data, parent)

Parameters

data*object

Raw node from the bubble JSON.

parentobject

Parent node from the bubble JSON.

Methods

isSVF2()

Returns

type

description

boolean

True if the bubble is from MD API.

getOtgGraphicsNode()

Returns the OTG viewable from an otg manifest (if available, otherwise undefined)

Returns

type

description

Autodesk.Viewing.BubbleNode, undefined

getPropertyDbManifest(viewableID)

Returns a list of property database files. Previously, for v1, this list was hardcoded in PropWorker/ This function knows about v2 and cross-version sharing of OTG property databases

Parameters

viewableIDstring

The viewable ID to get the property DB manifest for, defaults to this nodeâs GUID

getRootNode()

Returns

type

description

Autodesk.Viewing.BubbleNode

Top-most bubble node.

isForgeManifest()

Whether the manifest comes from APS (modelDerivativeV2) or not (derivativeV2). Applies only to the root node. Used internally.

findPropertyDbPath(viewableID)

Finds shared property DB if there is one.

Parameters

viewableIDstring

The viewable ID to use for looking up the property DB, defaults to this nodeâs GUID

Returns

type

description

string, null

Shared property DB path, or null.

name()

Returns

type

description

string

The nodeâs name.

guid()

Returns

type

description

string

The nodeâs GUID.

type()

Returns

type

description

string

The nodeâs type.

extensions()

Returns

type

description

Array.<string>

Either an Array of extension ids, or undefined.

urn(searchParent)

Retrieves the URN of the node or its closest ancestor.

Parameters

searchParent*boolean

If URN is not available for this node, search through its ancestors, too.

Returns

type

description

string

Viewable URN.

lineageUrn(encode)

Retrieves the lineageUrn of the node. Note that models uploaded to OSS directly (not through WipDM) do not have a lineageUrn.

Parameters

encodeboolean

Whether to return the result base64 encoded or not.

Returns

type

description

string

Viewable lineageUrn, or null in case of an error.

isGeomLeaf()

Returns

type

description

boolean

True if this is a geometry leaf node.

isViewable()

Returns

type

description

boolean

True if this is a viewable node.

getLodNode()

Returns

type

description

BubbleNode

The LOD node.

isGeometry()

Returns

type

description

boolean

True if this is a geometry node.

isViewPreset()

Returns

type

description

boolean

True if this is a view preset/camera definition node.

is2D()

Returns

type

description

boolean

True if this is a 2D node.

is3D()

Returns

type

description

boolean

True if this is a 3D node.

is2DGeom()

Returns

type

description

boolean

True if this is a 2D geometry node.

is3DGeom()

Returns

type

description

boolean

True if this is a 3D geometry node.

useAsDefault()

Returns

type

description

boolean

True if the node is meant to be loaded initially.

getDefaultGeometry(searchMasterview, loadLargestView)

Parameters

searchMasterviewboolean

Search for master view

loadLargestViewboolean

Sort by geometry size

Returns

type

description

BubbleNode

The default geometry if any, and otherwise the full data set. For SVF: A geometry node marked as being the default (for SVF:useAsDefault=true). When none is found, it returns the first element fromthis.search({'type':'geometry'}).

getPlacementTransform()

Returns

type

description

object

Placement transform of the node.

isMetadata()

Returns

type

description

boolean

True if this is a metadata node.

findViewableParent()

Returns

type

description

Autodesk.Viewing.BubbleNode

First parent in the hierarchy that is a viewable. If called on the top level design node, returns the first child of the design node that is a viewable.

findParentGeom2Dor3D(options)

Parameters

optionsobject

Advance usage options

fallbackParentAutodesk.Viewing.BubbleNode

Gets returned when no geometry node is available after iterating through the parent chain.

Returns

type

description

Autodesk.Viewing.BubbleNode

First parent in the hierarchy that is a 2D or 3D geometry.

findAllViewables()

Returns

type

description

Array.<Autodesk.Viewing.BubbleNode>

Array with all of the viewables under this node.

getViewableRootPath(ignoreLeaflet)

Looks for the viewable root path in this node and all its children.

Parameters

ignoreLeaflet*boolean

If set, it will skip any image pyramid sub-nodes and return a path to F2D file if available.

Returns

type

description

string

Viewable root path, or null.

getNamedViews()

Returns all the named view in the viewable. Named views are obtained from the documentâs manifest which contains camera information and a string identifier.

Returns

type

description

array

All named views. Returns empty array if none are found.

findByGuid(guid)

Returns first node from the bubble matching a GUID.

Note that some GUIDs in the bubble are not unique, you have to be sure you are looking for a GUID that is unique if you want correct result from this function. Otherwise use the generic search.

Parameters

guid*string

Node GUID.

Returns

type

description

Autodesk.Viewing.BubbleNode

Matching bubble node, or null.

search(propsToMatch)

Finds nodes from the bubble matching one or more properties.

Parameters

propsToMatch*object

Filter criteria: To match, nodes must have the specified properties and values. Use comma-separated property:value pairs or named preset object. (See comments in examples below.)

Returns

type

description

Array.<BubbleNode>

Matching nodes, or null.

Examples

//   { âpropertyâ:âvalueâ [, âpropertyâ:âvalueâ, â¦] }
// or use named preset objects:
//   BubbleNode.MODEL_NODE           { âroleâ:â3dâ, âtypeâ:âgeometryâ }
//   BubbleNode.GEOMETRY_SVF_NODE    { âroleâ:âgraphicsâ, âmimeâ: âapplication/autodesk-svfâ }
//   BubbleNode.SHEET_NODE           { âroleâ:â2dâ, âtypeâ:âgeometryâ }
//   BubbleNode.LEAFLET_NODE         { âroleâ:âleafletâ }
//   BubbleNode.IMAGE_NODE           { âroleâ:âimageâ }
//   BubbleNode.GEOMETRY_F2D_NODE    { âroleâ:âgraphicsâ, âmimeâ: âapplication/autodesk-f2dâ }
//   BubbleNode.VIEWABLE_NODE        { âroleâ:âviewableâ }
//   BubbleNode.AEC_MODEL_DATA       { âroleâ:âAutodesk.AEC.ModelDataâ}

var singleProps = myBubbleNode.search({ âtypeâ:âgeometryâ });
var multiProps  = myBubbleNode.search({ âroleâ:â3dâ, âtypeâ:âgeometryâ });
var presetProps = myBubbleNode.search( myBubbleNode.SHEET_NODE );

traverse(cb)

Recursively traverses the bubble, calling a callback function for each node, for as long as the callback function keeps returning false.

Parameters

cb*function

Callback function, accepts a bubble node as an argument, and returns true if the traversal should be terminated.

Returns

type

description

boolean

Result of the last callback invocation.

getLevel()

Returns the Revit Level/Floor of this bubble node. Only relevant for 2d sheets coming from Revit at the moment.

getLevelName()

Returns

type

description

string

The Revit level/floor name of this bubble node. Only relevant for 2d sheets coming from Revit at the moment.

```
// Filter criteria syntax:

```


---

# Document

Document

new Document(dataJSON, path, acmsession)

Allows the client to load the model data from the cloud, it gives access to the root and provides a method for finding elements by id.

Typically, you load the document from APS, parse it for the required content (for example, 3d geometries), then pass this on to the viewer to display.  You can also get some information about the document, such as the number of views it contains and its thumbnail image.

Parameters

dataJSON*object

JSON data representing the document.

path*string

Path/URL where dataJSON was fetched from.

acmsessionstring

ACM session ID.

Methods

load(documentId, onSuccessCallback, onErrorCallback, options)

Static method to load the translationâs manifest data from an APS endpoint.

Parameters

documentId*string

The URN of the file.

onSuccessCallback*Autodesk.Viewing.Document~loadSuccessCallback

A function that is called when load succeeds.

onErrorCallback*Autodesk.Viewing.Document~loadErrorCallback

A function that is called when load fails.

optionsobject

An optional object that allows configuring manually the manifest request attributes - such as headers, endpoint etc.

Examples

getRoot()

Returns a BubbleNode instance, encapsulating the current document manifest JSON.

Returns

type

description

Autodesk.Viewing.BubbleNode

```
Autodesk.Viewing.Document.load(
   MY_URN,
   function onSuccessCallback(doc){
       var bubbleRoot = doc.getRoot();
       console.log(bubbleRoot);
       // proceed to load a viewable into the Viewer...
   },
   function onErrorCallback(errCode, errMsg){
       console.error('Failed to load manifest [' + errCode + '] ' + errMsg);
   }
)

```


---

# EventUtils

EventUtils

Contains static utility functions for DOM and viewer events.

new EventUtils()

Methods

isRightClick(event)

Parameters

event*DOMEvent

A browser-triggered event

Returns

type

description

boolean

true when the event matches a secondary-button click.

isMiddleClick(event)

Parameters

event*DOMEvent

A browser-triggered event

Returns

type

description

boolean

true when the event matches a middle-button mouse click.

waitUntilTransitionEnded(viewer)

If thereâs no camera transition, return immediately. Otherwise, resolve when the camera transition is finished.

Parameters

viewer*Autodesk.Viewing.Viewer3D

waitUntilGeometryLoaded(viewer)

If geometry has been loaded, return immediately. Otherwise, resolve when the geometry loaded event is fired.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Model

model - Default is viewer.model, if not provided

waitUntilModelAdded(viewer)

If model has been already added, return immediately. Otherwise, resolve when the model is added.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Model

model - Default is viewer.model, if not provided


---

# Extension

Extension

new Extension(viewer, options)

Base class for extending the functionality of the viewer.

Derive from this class and implement methodsload()andunload().

Register this extension by calling:``Autodesk.Viewing.theExtensionManager.registerExtension(âyour_extension_idâ, YOUR_EXTENSION_CLASS); ``

Extensions are registered and loaded automatically by adding the Extension ID to the config object passed to the viewer constructor.

Parameters

viewer*Autodesk.Viewing.Viewer3D

The viewer to be extended.

options*object

An optional dictionary of options for this extension.

Methods

load()

Override the load method to add functionality to the viewer. Use the Viewerâs APIs to add/modify/replace/delete UI, register event listeners, etc.

Returns

type

description

boolean, Promise

True if the load was successful. Optionally, the function can return a Promise which resolves when load succeeds and rejects in case of failure.

unload()

Override the unload method to perform some cleanup of operations that were done in load.

Returns

type

description

boolean

True if the unload was successful.

activate(mode)

Override the activate method to enable the functionality of the extension.

Parameters

modestring

An optional mode that indicates a different way the extension can function.

Returns

type

description

boolean

True if the extension activation was successful.

deactivate()

Override the deactivate method to disable the functionality of the extension.

Returns

type

description

boolean

True if the extension deactivation was successful.

setActive(enable, mode)

Activates the extension if the enable parameter is set to true. Deactivates the extension if the enable parameter is set to true.

Parameters

enable*boolean

flag to activate or deactivate the extension.

modestring

An optional mode that indicates a different way the extension can function.

getName()

Gets the name of the extension.

Returns

type

description

string

Returns the name of the extension.

getModes()

Gets an array of modes available for the extension.

Returns

type

description

Array

Returns an array of modes.

isActive(mode)

Check if the extension is active and optionally check if the specified mode is active for that extension.

Parameters

mode*

An optional mode that indicates a different way the extension can function.

Returns

type

description

boolean

Default - True if the extension is active. When optional argument mode is specified, returns true if both extension and the mode are active, false otherwise.

getState(viewerState)

Gets the extension state as a plain object. Intended to be called when viewer state is requested.

Parameters

viewerState*object

Object to inject extension values.

restoreState(viewerState, immediate)

Restores the extension state from a given object.

Parameters

viewerState*object

Viewer state.

immediate*boolean

Whether the new view is applied with (true) or without transition (false).

Returns

type

description

boolean

True if restore operation was successful.

extendLocalization(locales)

Add localization strings to the viewer. This method can override localization keys already loaded. There is no API method to remove localization strings added with this method.

Parameters

locales*object

The set of localized strings keyed by language

Returns

type

description

boolean

True if localization was successfully updated

Examples

getCache()

Returns an object that persists throughout an extensionâs unload->load operation sequence. Cache object is kept by theAutodesk.Viewing.Viewer3Dinstance. Cache object lives only in RAM, there is no localStorage persistence.

Returns

type

description

object

The cache object for a given extension.

onToolbarCreated(toolbar)

Invoked after the Toolbar UI gets created. Extensions can extend (or remove) its content from this point forward. The method is invoked afterTOOLBAR_CREATED_EVENTgets fired. It is also invoked right afterAutodesk.Viewing.Extension#loadif the toolbar was already created.

Must be overriden by subclasses.

Parameters

toolbar*Autodesk.Viewing.UI.ToolBar

toolbar instance.

```
var locales = {
      en: { my_tooltip: "CUSTOM_TOOLTIP" },
      de: { my_tooltip: "BENUTZERDEFINIERTE_TOOLTIP" }
 };
 ext.extendLocalization(locales);

```


---

# ExtensionManager

ExtensionManager

The ExtensionManager manages all the extensions available to the viewer. Register, retrieve, and unregister your extension using the singletonAutodesk.Viewing.theExtensionManager.

You can load/unload your registered extension into a Viewer by invokingviewer.loadExtension(id, options)andviewer.unloadExtension(id), respectively.

new ExtensionManager()

Methods

registerExtension(extensionId, extensionClass)

Registers a new extension with the given id.

Parameters

extensionId*string

The string id of the extension.

extensionClass*Extension

The Extension-derived class representing the extension.

Returns

type

description

boolean

True if the extension was successfully registered.

True if the extension was successfully registered.

getExtension(extensionId)

Returns the class representing the extension with the given id.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

Extension, null

The Extension-derived class if one was registered; null otherwise.

The Extension-derived class if one was registered; null otherwise.

unregisterExtension(extensionId)

Unregisters an existing extension with the given id.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

boolean

True if the extension was successfully unregistered.

True if the extension was successfully unregistered.

registerExternalExtension(extensionId, urlPathOrCallback, dependencies)

Registers an extension that needs to be downloaded before using it. The Viewer ships with some extensions that are not bundled, but can be runtime-fetched.

Parameters

extensionId*string

The string id of the extension.

urlPathOrCallback*string, function

The url from where it needs to be pulled from. Can be a relative or an absolute path. Optionally, this can be a callback function that defers the loading to the client application. Useful for webpack import style loading. Callback must return a promise that resolves when loading is finished.

dependencies*Array.<string>

Optional list of extension IDs, whose bundles are needed before this extension can be built.

Returns

type

description

boolean

True if the extension was successfully registered.

True if the extension was successfully registered.

getExternalPath(extensionId)

Returns the url path from where to download the extension; null if not registered through registerExternalExtension().

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

url, null

The url from where to download the extension; null if not download is needed.

The url from where to download the extension; null if not download is needed.

getRegisteredExtensions()

Gets a list of all the extensions that are available for usage. Some are already available in memory, while others may require an additional file to be downloaded prior to its usage.

Returns

type

description

Array.<string>

downloadExtension(extensionId)

Download the extension and return its downloading promise

Parameters

extensionId*string

Returns

type

description

Promise

resolves when the extension class is ready for usage.

isDownloading(extensionId)

Is the extension being downloaded?

Parameters

extensionId*string

isAvailable(extensionId)

Is the extension class available?

Parameters

extensionId*string


---

# FileLoader

FileLoader

new FileLoader(viewer)

Base class for file loaders.

It is highly recommended that file loaders use worker threads to perform the actual loading in order to keep the UI thread free. Once loading is complete, the loader should call viewer.impl.onLoadComplete(). During loading, the loader can use viewer.impl.signalProgress(int) to indicate how far along the process is.

To add geometry to the viewer,viewer.impl.addMeshInstance(geometry,meshId,materialId,matrix)should be used. Geometry must be THREE.BufferGeometry, meshId is a number, materialId is a string, and matrix is the THREE.Matrix4 transformation matrix to be applied to the geometry.

Remember to add draw calls to the BufferGeometry if the geometry has more than 65535 faces.

Parameters

viewer*Autodesk.Viewing.Viewer3D

The viewer instance.

Methods

loadFile(url, options, onSuccess, onError)

Initiates the loading of a file from the given URL.

This method must be overridden.

Parameters

url*string

The url for the file.

optionsobject

An optional dictionary of options.

idsstring

A list of object id to load.

sharedPropertyDbPathstring

Optional path to shared property database.

onSuccessfunction

Callback function when the file begins loading successfully. Takes no arguments.

onErrorfunction

Callback function when an error occurs. Passed an integer error code and a string description of the error.

is3d()

Returns true only for a 3D models FileLoader implementation.


---

# GuiViewer3D

GuiViewer3D

Extends`Autodesk.Viewing.Viewer3D`_

new GuiViewer3D(container, config)

Viewer component based onAutodesk.Viewing.Viewer3Dwith added UI.

Parameters

container*HTMLElement

The viewer container.

config*object

The initial settings object. See base class for details.

Properties

ViewerCount

Need to keep track of viewers in document so we know when it is safe to call clearPropertyWorkerCache()

kDefaultCanvasConfig

Default values passed into#setCanvasClickBehaviorspecifying how the viewer canvas will react to user input as well as other 3d-canvas related options.

Methods

loadExtension(extensionId, options)

Loads the extension with the given id and options.

Parameters

extensionId*string

The string id of the extension.

options*Object

An optional dictionary of options.

Returns

type

description

Promise

Resolves with the extension requested.

Resolves with the extension requested.

getExtension(extensionId, callback)

Returns the loaded extension.

Parameters

extensionId*string

The string id of the extension.

callbackfunction

That receives an extension instance as argument.

Returns

type

description

Object

Extension.

Extension.

getExtensionAsync(extensionId)

Returns a promise with the loaded extension.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

Promise

Resolves with the loaded extension.

Resolves with the loaded extension.

unloadExtension(extensionId)

Unloads the extension with the given id.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

boolean

True if the extension was successfully unloaded.

True if the extension was successfully unloaded.

loadExtensionLocal(extensionId, options)

Loads the extension with the given id and options. For internal use only.

Parameters

extensionId*string

The string id of the extension.

options*Object

An optional dictionary of options.

Returns

type

description

Promise

Resolves with the extension requested.

Resolves with the extension requested.

forEachExtension(callback)

Iterate over each extension that has been successfully loaded and invokes a callback function for them.

Parameters

callback*function

That receives an extension instance as argument.

Examples

start(url, options, onSuccessCallback, onErrorCallback, initOptions)

Initializes the viewer and loads any extensions specified in the constructorâs config parameter. If the optional parameters are specified, the start() function will use an optimized initialization sequence that results in faster model load. The parameters are the same as the ones for Viewer3D.loadModel and you do not need to call loadModel subsequently if the model is loaded via the call to start().

Parameters

urlstring

Optional URN or filepath to load on start.

optionsobject

Optional path to shared property database.

onSuccessCallbackAutodesk.Viewing.Viewer3D~onLoadModelSuccess

Method that gets called when initial loading is done and streaming starts.

onErrorCallbackAutodesk.Viewing.Viewer3D~onLoadModelFailure

Method that gets called when initial loading ends with an error.

initOptionsobject

Optional: Options forwarded to viewer.initialize()

Returns

type

description

number

0 if the viewer has started, an error code (same as that returned by initialize()) otherwise.

setUp(config)

Loading extensions and initializing canvas interactions. Invoked automatically byAutodesk.Viewing.Viewer3D#startmethod.

Parameters

configobject

configuration values

extensionsArray.<string>

List of extension ids to load with the model.

canvasConfigobject

Overrides for click/tap events on the 3D canvas. Refer to#setCanvasClickBehaviorfor details.

tearDown(isUnloadModelsWanted)

Unloads extensions and the loaded models. Invoked automatically byAutodesk.Viewing.Viewer3D#finishmethod.

Parameters

isUnloadModelsWantedboolean

Whether to unload models at the end. Default is true.

_onAggregatedSelectionChanged()

When selection has changed set the pivot point to be in the middle, if Autodesk.Viewing.Private.Prefs3D.SELECTION_SETS_PIVOT is true

run()

Triggers the Viewerâs render loop. Invoked automatically byAutodesk.Viewing.Viewer3D#startmethod. Refer toViewerConfig.startOnInitializeto change startâs method behavior.

localize()

Localize the viewer. This method can be overwritten so that the subclasses can localize any additional elements. Invoked internally during initialization.

uninitialize()

Removes all created DOM elements, performs GL uninitialization that is needed and removes event listeners.

finish()

Unloads any loaded extensions and then uninitializes the viewer.

loadModel(url, options, onSuccessCallback, onErrorCallback)

Loads a model into the viewer. Can be used sequentially to load multiple 3D models into the same scene.

Parameters

url*string

The url to the model.

optionsobject

Dictionary of options.

fileLoaderAutodesk.Viewing.FileLoader

The file loader to use for this url. Required for unsupported file types.

keepCurrentModelsboolean

Flag indicating whether viewer should keep or unload all other models.

loadOptionsobject

May contain params that are specific for certain loaders/filetypes.

sharedPropertyDbPathstring

Optional path to shared property database.

idsstring

A list of object IDs to load.

loadAsHiddenboolean

By default, a new model is instantly shown and triggers viewer refreshes during loading. Setting this option avoids that. The model can then be shown later by calling showModel().

modelNameOverridestring

Allows host application to override model name used in UI.

placementTransformLmvMatrix4

Applied to the model during loading.

applyScalingstring, Object

Unit-Scaling that is applied to the model on load, e.g. { from: âftâ, to: âmâ }. If âfromâ is not set, it is determined from model metadata (if provided). If only âtoâ is set, you can just assign a string directly, e.g. applyScaling = âmâ is the same as applyScaling = { to: âmâ }.

applyPlacementInModelUnitsboolean

Only relevant if options.placementTransform and options.applyScaling are both used at once. In this way, it controls the order in which placement and scaling happen: - False: Placement happens in viewer world-units. That is, applyScaling is done first, then the custom placementMatrix is applied. (Default behavior) - True: Placement happens in model units. That is, custom placementMatrix is applied first, then the unit scaling.

onSuccessCallbackAutodesk.Viewing.Viewer3D~onLoadModelSuccess

A method that gets called when modelâs metadata loading is done and geometry streaming starts.

onErrorCallbackAutodesk.Viewing.Viewer3D~onLoadModelFailure

A method that gets called when loading fails.

isLoadDone(include)

Check whether models are completely loaded This method checks all models in the model queue and load requests that havenât loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if present is loaded and no textures are being loaded.

Parameters

includeObject

Optional object to set the scope of the wait

geometryBoolean

Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent geometry from being considered. Defaults to true.

propDbBoolean

Set to false to exclude the property data base loading from consideration. Defaults to true.

texturesBoolean

Set to false to exclude the texture loading from consideration. Defaults to true.

hiddenBoolean

Set to true to include hidden models for consideration. Defaults to false.

onlyModelsModel, Array.<Model>

Limits the check to the model or models in this property. Note that checking for textures loaded cannot be limited to models.

Returns

type

description

Boolean

True if all models are completely loaded, otherwise false

waitForLoadDone(include)

Wait for models to be completely loaded This method checks all models in the model queue and load requests that havenât loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if there is one, is loaded and no textures are being loaded. If this method is called before the viewer is started, then it will wait until the viewer starts and at least one model start loading to check for the load completing

Parameters

includeObject

Optional object to set the scope of the wait

geometryBoolean

Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent waiting for geometry to load. Defaults to true.

propDbBoolean

Set to false to exclude the property data base loading from consideration. Defaults to true.

texturesBoolean

Set to false to exclude the texture loading from consideration. Defaults to true.

hiddenBoolean

Set to true to include hidden models for consideration. Defaults to false.

onlyModelsModel, Array.<Model>

Limits the wait to the model or models in this property. Note that waiting for textures loaded cannot be limited to models.

Returns

type

description

Promise

resolves when all models are loaded. This promise can be rejected by a LOADER_LOAD_ERROR_EVENT event.

unloadModel(model)

Unloads the specified model. ReferenceAutodesk.Viewing.Viewer3D#hideModelto hide the model.

Parameters

model*Autodesk.Viewing.Model

The model to unload.

loadDocumentNode(avDocument, manifestNode, options)

Parameters

avDocument*Autodesk.Viewing.Document

The Document instance, which owns the model being loaded

manifestNode*Autodesk.Viewing.BubbleNode

The specific manifest node to load (within the Document)

optionsViewerConfig

Options to pass toAutodesk.Viewing.Viewer3D#loadModel. Will be initialized internally if not specified. The options object will be augmented by automatically determined load parameters.

Returns

type

description

Promise

Resolves with an object representing the model.

Resolves with an object representing the model.

unloadDocumentNode(manifestNode)

Unloads a model previously loaded by loadDocumentNode().

ReferenceAutodesk.Viewing.Viewer3D#loadDocumentNode

Parameters

manifestNode*Autodesk.Viewing.BubbleNode

The specific manifest node to unload (within the Document)

Returns

type

description

boolean

true on success

true on success

getDimensions()

Returns the dimensions of the WebGL canvas.

Returns

type

description

object

Client rectangle bounds object { width:Number, height: Number }

resize()

Resizes the viewer. Required when wrapping div changes dimensions due to CSS changes.

getHotkeyManager()

Returns

type

description

Autodesk.Viewing.HotkeyManager

The hotkey manager.

getCamera()

Gets the camera so it can be modified by the client.

Returns

type

description

THREE.Camera

The active camera.

getState(filter)

Gets the view state as a plain object. A viewer state contains data for the viewport, selection and isolation.

ReferenceAutodesk.Viewing.Viewer3D#restoreState

Parameters

filterobject

Specifies which viewer values to get.

Returns

type

description

object

Viewer state.

restoreState(viewerState, filter, immediate)

Restores the viewer state from a given object.

ReferenceAutodesk.Viewing.Viewer3D#getState

Parameters

viewerState*Object

filterObject

Similar in structure to viewerState used to filter out values that should not be restored.

immediateboolean

Whether the new view is applied with (true) or without transition (false).

Returns

type

description

boolean

True if restore operation was successful.

setView(viewNode, options)

Loads a view specified in the Manifest JSON. For 3D models it will use the camera values. For 2D models it will use the viewBox values.

Notice that in order that the view will be properly set according to the modelâs transformation, the model has to be loaded first.

Parameters

viewNode*Autodesk.Viewing.BubbleNode

bubble node representing the view

optionsObject

skipTransitionboolean

true to apply instanstly instead of lerping.

useExactCameraboolean

whether any up vector adjustment is to be done (to keep head up view)

skipViewpointExtraboolean

true to skip using extra viewpoint information

Returns

type

description

boolean

true, if the view is applied.

setViewFromArray(params)

Sets the view from an array of parameters.

To get the view array of the current camera use:getViewArrayFromCamera. To get the camera object from the view array usegetCameraFromViewArray.

Parameters

params*Array.<Number>

View parameters: [position-x, position-y, position-z, target-x, target-y, target-z, up-x, up-y, up-z, aspect, fov (radians), orthoScale, isPerspective (0=perspective, 1=ortho)]

getCameraFromViewArray(params, model)

Returns an object representing a Camera from an unintuitive array of number. Note: To use this function in multi-model scenarios, you must pass the model parameter.

To get the view array of the current camera use:getViewArrayFromCamera.

Parameters

params*Array.<Number>

Array with 13 elements describing different aspects of a camera.

modelAutodesk.Viewing.Model

Camera is transformed in the same way as the model. Default is this.model (only sufficient for single-view scenarios).

Returns

type

description

Object, null

Camera object, or null if argument is invalid or missing.

Camera object, or null if argument is invalid or missing.

getViewArrayFromCamera()

Returns an Array of values that could be inserted back into a manifest to represent a view. To get the camera object from the view array usegetCameraFromViewArray.

Returns

type

description

Array.<Number>

Array with 13 elements describing different aspects of the current camera.

Array with 13 elements describing different aspects of the current camera.

setViewFromViewBox(viewbox, name, skipTransition)

Sets the view from an array representing a view box.

Not applicable to 3D.

Parameters

viewbox*Array.<Number>

View parameters: [min-x, min-y, max-x, max-y]

namestring

Optional named view name to also set the layer visibility state associated with this view.

skipTransitionboolean

true to apply instanstly instead of lerping.

activateLayerState(stateName)

Changes the active layer state. Layers is a feature usually available on 2D models and some 3D models.

ReferenceAutodesk.Viewing.Viewer3D#getLayerStates

Parameters

stateName*string

Name of the layer state to activate.

getLayerStates()

Returns information for each layer state: name, description, active. Activate a state throughAutodesk.Viewing.Viewer3D#activateLayerState.

Returns

type

description

Array.<Object>, null

Array of layer states. If layers donât exist or are hidden, this methods returns null.

Array of layer states. If layers donât exist or are hidden, this methods returns null.

setViewFromFile(model)

Sets the view using the default view in the source file.

Parameters

modelAutodesk.Viewing.Model

The model, defaults to the loaded model.

getProperties(dbid, onSuccessCallback, onErrorCallback)

Gets the properties for an ID.

Parameters

dbid*number

The database identifier.

onSuccessCallbackCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbackCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

getObjectTree(onSuccessCallback, onErrorCallback)

Gets the viewer model object tree. Once the tree is received it will invoke the specified callback function.

You can use the model object tree to get information about items in the model.  The tree is made up of nodes, which correspond to model components such as assemblies or parts.

Parameters

onSuccessCallbackCallbacks#onObjectTreeSuccess

Success callback invoked once the object tree is available.

onErrorCallbackCallbacks#onGenericError

Error callback invoked when the object tree is not found available.

setCanvasClickBehavior(config)

Sets the click behavior on the canvas to follow config. This is used to change the behavior of events such as selection or Center-of-Interest changed.

Parameters

config*object

Parameter object that meets the above layout.

Examples

Actions can be any of the following: âselectOnlyâ, âselectToggleâ, âdeselectAllâ, âisolateâ, âshowAllâ, âsetCOIâ, âfocusâ, âhideâ

search(text, onSuccessCallback, onErrorCallback, attributeNames, options)

Searches the elements for the given text. When the search is complete, the callback onResultsReturned(idArray) is invoked.

Parameters

text*string

The search term (not case sensitive).

onSuccessCallback*Callbacks#onSearchSuccess

Invoked when the search results are ready.

onErrorCallback*Callbacks#onGenericError

Invoke when an error occured during search.

attributeNamesArray.<string>

Restricts search to specific attribute names.

optionsObject

Search options.

searchHiddenboolean

Set to true to also search hidden properties

includeInheritedboolean

Set to true to include nodes that inherit the property

getHiddenNodes(model)

Returns an array of the IDs of the currently hidden nodes. When isolation is in place, there are no hidden nodes returned because all nodes that are not isolated are considered hidden.

Parameters

modelAutodesk.Viewing.Model

Model object, if passed in the hidden nodes of the model are returned

Returns

type

description

Array.<number>

Array of nodes that are currently hidden, when no isolation is in place.

getIsolatedNodes(model)

Returns an array of the IDs of the currently isolated nodes.

Not yet implemented for 2D.

Parameters

modelAutodesk.Viewing.Model

Model object, if passed in the isolated nodes of the model are returned

Returns

type

description

Array.<number>

Array of nodes that are currently isolated.

isolate(node, model)

Isolates one of many sub-elements. You can pass in a node or an array of nodes to isolate. Pass in null to reset isolation.

Parameters

node*Array.<number>, number

A node ID or array of node IDs from the model treeBaseViewer#getObjectTree.

modelAutodesk.Viewing.Model

the model that contains the node id. Defaults to the first loaded model.

setBackgroundColor(red, green, blue, red2, green2, blue2)

Sets the background colors, which will be used to create a gradient. Values are in the range [0..255]

Parameters

red*number

green*number

blue*number

red2*number

green2*number

blue2*number

setBackgroundOpacity(opacity)

Sets the background opacity.

Parameters

opacity*number

Value is in the range [0.0..1.0]

toggleSelect(dbid, model, selectionType)

Toggles the selection for a given dbid. If it was unselected, it is selected. If it was selected, it is unselected.

Currently three ways of node selection are supported:

Autodesk.Viewing.SelectionType.MIXEDLeaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Autodesk.Viewing.SelectionType.REGULARNodes are tinted with the selection color.

Nodes are tinted with the selection color.

Autodesk.Viewing.SelectionType.OVERLAYEDNodes are tinted with the selection color and shown on top of the not selected geometry.

Nodes are tinted with the selection color and shown on top of the not selected geometry.

Not yet implemented for 2D.

Parameters

dbid*number

modelAutodesk.Viewing.Model

the model that contains the dbId. Uses the initial model loaded by default.

selectionType*number

a member of Autodesk.Viewing.SelectionMode.

select(dbids, model, selectionType)

Selects the array of ids. You can also pass in a single id instead of an array.

Currently three ways of node selection are supported:

Autodesk.Viewing.SelectionType.MIXEDLeaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Autodesk.Viewing.SelectionType.REGULARNodes are tinted with the selection color.

Nodes are tinted with the selection color.

Autodesk.Viewing.SelectionType.OVERLAYEDNodes are tinted with the selection color and shown on top of the not selected geometry.

Nodes are tinted with the selection color and shown on top of the not selected geometry.

Parameters

dbids*Array.<number>, number

element or array of elements to select.

modelAutodesk.Viewing.Model

the model instance containing the ids.

selectionTypenumber

a member ofAutodesk.Viewing.SelectionType.

clearSelection()

Clears the selection. Seeselect()

getSelectionVisibility()

Returns information about the visibility of the current selection.

Returns

type

description

object

{hasVisible:boolean,hasHidden:boolean}

getSelectionCount()

Returns the number of nodes (dbIds) in the current selection.

Returns

type

description

number

number of selected nodes

number of selected nodes

setSelectionMode(mode)

Sets selection granularity mode. Supported values are:

Autodesk.Viewing.SelectionMode.LEAF_OBJECT: Always select the leaf objects in the hierarchy.

Autodesk.Viewing.SelectionMode.FIRST_OBJECT: For a given node, selects the first non-composite (layer, collection, model) on the path from the root to the given node, and all children.

Autodesk.Viewing.SelectionMode.LAST_OBJECT: For a given node, selects the nearest ancestor composite node and all children. Selects the input node itself in case there is no composite node in the path to the root node.

Parameters

mode*number

The selection mode.

getSelection()

Returns the current selection.

Returns

type

description

Array.<number>

Array of the nodes (dbIds) of the currently selected nodes.

lockSelection(dbIds, lock, model)

Locks the selection of specificnodes(dbIds) in a given model. Thenodeswill be unselected if thelockis set to true and the nodes are already selected. The locked nodes will not be selectable.

Parameters

dbIds*Number, Array.<Number>

dbIds to lock

lock*Boolean

true to lock, false otherwise

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

unlockSelection(dbIds, model)

This function will unlock the specifiednodes(dbIds) for a specificmodel. If thenodesparameter is omitted then the specifiedmodelâs locked nodes will be unlocked. If themodelparameter is omitted then the specifiednodeswill be unlocked for the viewer.model. If both parameters are omitted then all of the models in the viewer will release their locked nodes.

Parameters

dbIdsArray.<Number>

dbIds to unlock

modelAutodesk.Viewing.Model

The model associated to the nodes parameters

isSelectionLocked(dbId, model)

Checks whether selection is locked for a node

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

Returns

type

description

boolean

True is the visibility is locked

getAggregateSelection(callback)

Returns the selected items from all loaded models.

Parameters

callbackfunction

Optional callback to receive enumerated pairs of model and dbId for each selected object. If no callback is given, an array of objects is returned.

Returns

type

description

Array.<object>

An array of objects with a model and selectionSet properties for each model that has selected items in the scene.

setAggregateSelection(selection, fireEvent)

Selects ids from different models. Choose this api instead of select() when selecting across many models

Parameters

selection*Array.<SelectionDef>

Array of selection objects defining what to select

fireEventBoolean

Whether an event is fired at the end

getAggregateIsolation()

Returns the isolated items from all loaded models.

Returns

type

description

Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}>

An array of objects with amodeland the isolatedidsin that model.

setAggregateIsolation(isolation)

Isolate ids from different models. Choose this api instead of isolate() when isolating across many models. It will hide all other models.

Parameters

isolation*Array.<{model: Autodesk.Viewing.Model, ids: (Array.<number>|number)}>

An array of objects with amodeland theidsto isolate in that model

getAggregateHiddenNodes()

Returns the hidden nodes for all loaded models.

Returns

type

description

Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}>

An array of objects with amodeland the hiddenidsin that model.

hide(node, model)

Ensures the passed in nodes (dbIds) are hidden.

Parameters

node*Array.<number>, number

An array of nodes (dbids) or just a single node.

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

show(node, model)

Ensures the passed in nodes (dbIds) are shown.

Parameters

node*Array.<number>, number

An array of nodes (dbids) or just a single node.

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

showAll()

Ensures everything is visible. Clears all node isolation (3D) and turns on all layers (2D).

hideAll()

Ensures all objects are hidden. Clears all nodes.

toggleVisibility(dbId, model)

Toggles the visibility of the given node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

areAllVisible()

Returns true if every node (dbId) is visible.

Returns

type

description

boolean

True if every node is visible, false otherwise.

True if every node is visible, false otherwise.

isNodeVisible(nodeId, model)

Returns true if the specified node is visible. The model argument is required only when in multi-model scenarios.

Parameters

nodeId*number

Geometry node to check if visible.

modelAutodesk.Viewing.Model

The model that contains the specifiednodeId.

Returns

type

description

boolean

toggleLockVisible(dbId, model)

Toggles the visibility lock of the given node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

isVisibleLocked(dbId, model)

Checks whether visibility is locked for a node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

Returns

type

description

boolean

True is the visibility is locked

explode(scale, options)

Explodes the model from the center of gravity.

Not applicable to 2D.

Parameters

scale*number

A value from 0.0-1.0 to indicate how much to explode.

options*Object

Additional setting for STRATEGY_HIERARCHY.

magnitude*Number

Controls the spread of explode.

depthDampening*Number

Controls the reduction of the explode effect with depth of the object in the hierarchy.

getExplodeScale()

Returns the explode scale.

Not applicable to 2D.

Returns

type

description

number

A value from 0.0-1.0 indicating how exploded the model is.

A value from 0.0-1.0 indicating how exploded the model is.

getExplodeOptions()

Returns the explode options.

Not applicable to 2D.

Returns

type

description

object

{magnitude:Number,depthDampening:Number}

lockExplode(dbids, lock, model)

Lock node (dbid) so that it doesnât explode

Not applicable to 2D.

Parameters

dbids*Array.<number>, number

The dbids to lock or unlock

lock*boolean

Set to true to prevent dbids from exploding. Set to false to allow dbids to explode.

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if any dbids were changed.

isExplodeLocked(dbid, model)

Check whether a dbid is locked so it doesnât explode.

Not applicable to 2D.

Parameters

dbid*number

The dbid to check

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if dbid is locked to prevent explode

toggleLockExplode(dbid, model)

Toggle dbid lock so it doesnât explode

Not applicable to 2D.

Parameters

dbid*number

The dbid to lock or unlock

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if any dbids were changed.

setQualityLevel(useSAO, useFXAA)

Enables or disables the high quality rendering settings.

Not applicable to 2D.

Parameters

useSAO*boolean

True or false to enable screen space ambient occlusion.

useFXAA*boolean

True or false to enable fast approximate anti-aliasing.

setGhosting(value)

Toggles ghosting during search and isolate.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether ghosting is on or off.

setGroundShadow(value)

Toggles ground shadow.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether shadow is on or off.

setGroundReflection(value)

Toggles ground reflection.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether reflection is on or off.

setEnvMapBackground(value)

Toggles environment map for background.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether environment map for background is on or off.

setFirstPersonToolPopup(value)

Toggles first person tool popup.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether first person tool popup is showed or not.

getFirstPersonToolPopup()

Returns the state of First Person Walk tool popup.

Not applicable to 2D.

Returns

type

description

boolean

true if the First Person Walk tool popup appears, false if the First Person Walk tool popup does not appear.

setBimWalkToolPopup(value)

Toggles the bimwalk tool popup.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether first person tool popup is showed or not.

getBimWalkToolPopup()

Returns the state of First Person Walk tool popup

Not applicable to 2D.

Returns

type

description

boolean

true if the First Person Walk tool popup appears, false if the First Person Walk tool popup does not appear.

setProgressiveRendering(value)

Toggles whether progressive rendering is used. Warning: turning progressive rendering off will have serious performance implications.

Parameters

value*boolean

whether it is on or off

setGrayscale(value)

Overrides line colors in 2D models to render in shades of gray. Applies only to 2D models.

Parameters

value*boolean

whether it is on or off

setSwapBlackAndWhite(value)

AutoCAD drawings are commonly displayed with white lines on a black background. Setting reverse swaps (just) these two colors.

Parameters

value*boolean

whether it is on or off

setOptimizeNavigation(value)

Toggles whether the navigation should be optimized for performance. If set to true, anti-aliasing and ambient shadows will be off while navigating.

Not applicable to 2D.

Parameters

value*boolean

whether it is on or off

setNavigationLock(value)

Locks or unlocks navigation controls.

When navigation is locked, certain operations (for example, orbit, pan, or fit-to-view) are disabled.

ReferenceAutodesk.Viewing.Viewer3D#setNavigationLockSettings

Parameters

value*boolean

True if the navigation should be locked.

Returns

type

description

boolean

The previous state of the lock (this may be used to restore the lock to itâs previous state).

getNavigationLock()

Gets the current state of the navigation lock.

Returns

type

description

boolean

True if the navigation controls are currently locked.

setNavigationLockSettings(settings)

Updates the configuration of the navigation lock, i.e., which actions are available when navigation is locked.

The configurable actions are âorbitâ, âpanâ, âzoomâ, ârollâ, âfovâ, âwalkâ, or âgotoviewâ. By default, none of the actions are enabled when the navigation is locked.

ReferenceAutodesk.Viewing.Viewer3D#setNavigationLock

Parameters

settings*object

Map of : pairs specifying whether the given action is enabled even when the navigation is locked.

getNavigationLockSettings()

Gets the current configuration of the navigation lock.

Returns

type

description

object

Map of : pairs specifying whether the given action is enabled even when the navigation is locked.

setActiveNavigationTool(toolName)

Swaps the current navigation tool for the tool with the provided name. Will trigger NAVIGATION_MODE_CHANGED event if the mode actually changes.

ReferencegetActiveNavigationTool()

Parameters

toolNamestring

The name of the tool to activate. By default it will switch to the default tool.

Returns

type

description

boolean

True if the tool was set successfully. False otherwise.

True if the tool was set successfully. False otherwise.

getActiveNavigationTool()

Returns the name of the active navigation tool.

ReferencesetActiveNavigationTool()

Returns

type

description

string

The toolâs name.

The toolâs name.

setDefaultNavigationTool(toolName)

Sets the default navigation tool. This tool will always sit beneath the navigation tool on the tool stack.

Parameters

toolName*string

The name of the new default navigation tool.

getDefaultNavigationToolName()

Returns the default navigation tool

Returns

type

description

Object

The default navigation tool.

The default navigation tool.

getFOV()

Gets the current camera vertical field of view.

Returns

type

description

number

the field of view in degrees.

the field of view in degrees.

setFOV(degrees)

Sets the current cameras vertical field of view.

Parameters

degrees*number

Field of view in degrees.

getFocalLength()

Gets the current camera focal length.

Returns

type

description

number

the focal length in millimetres.

the focal length in millimetres.

setFocalLength(mm)

Sets the current cameras focal length.

Parameters

mm*number

Focal length in millimetres

hideLines(hide)

Hides all lines in the scene.

Parameters

hide*boolean

hidePoints(hide)

Hides all points in the scene.

Parameters

hide*boolean

setDisplayEdges(show)

Turns edge topology display on/off (where available).

Parameters

show*boolean

true to turn edge topology display on, false to turn edge topology display off.

applyCamera(camera, fit)

Parameters

camera*THREE.Camera

the camera to apply.

fitboolean

Do a fit to view after transition.

fitToView(objectIds, model, immediate)

Fits camera to objects by ID. It fits the entire model if no ID is provided. Operation will fit to the modelâs bounding box when its object tree is not available.

Parameters

objectIdsArray.<number>, null

array of Ids to fit into the view. Avoid passing this value to fit the entire model.

modelAutodesk.Viewing.Model, null

The model containing theobjectIds. If falsey, the viewerâs current model will be used.

immediateboolean

true to avoid the default transition.

setClickConfig(what, where, newAction)

Modifies a click action configuration entry.

Parameters

what*string

which click config to modify (one of âclickâ, âclickAltâ, âclickCtrlâ, âclickShiftâ, âclickCtrlShiftâ).

where*string

hit location selector (one of âonObjectâ, âoffObjectâ).

newAction*Array.<string>

action list (containing any of âsetCOIâ, âselectOnlyâ, âselectToggleâ, âdeselectAllâ, âdeselectAllâ, âisolateâ, âshowAllâ, âhideâ, âfocusâ).

Returns

type

description

boolean

False if specified entry is not found, otherwise true.

getClickConfig(what, where)

Fetch a click action configuration entry.

Parameters

what*string

which click config to fetch (one of âclickâ, âclickAltâ, âclickCtrlâ, âclickShiftâ, âclickCtrlShiftâ).

where*string

hit location selector (one of âonObjectâ, âoffObjectâ).

Returns

type

description

array

action list for the given entry or null if not found.

setClickToSetCOI(state, updatePrefs)

Modify the default click behaviour for the viewer.

Parameters

state*boolean

If true the default is to set the center of interest. If false the default is single select.

updatePrefsboolean

If true, the user preferences will be updated.

setProfile(profile, override)

Updates viewer settings encapsulated witihn a Profile. This method will also load and unload extensions referenced by the Profile.

Parameters

profile*Autodesk.Viewing.Profile

profile containing settings.

overrideboolean

If set to true this will override all existing preference with the new profile preference. Default: true

Examples

setLightPreset(index)

Sets the Light Presets (Environments) for the Viewer.

Not applicable to 2D.

Sets the preference in the UI

Parameters

index*Number

The index mapping looks like this: 0 -> Simple Grey, 1 -> Sharp Highlights, 2 -> Dark Sky, 3 -> Grey Room, 4 -> Photo Booth, 5 -> Tranquility, 6 -> Infinity Pool, 7 -> Simple White, 8 -> Riverbank, 9 -> Contrast, 1 ->0 Rim Highlights, 1 ->1 Cool Light, 1 ->2 Warm Light, 1 ->3 Soft Light, 1 ->4 Grid Light, 1 ->5 Plaza, 1 ->6 Snow Field

setUsePivotAlways(value)

Set or unset a view navigation option which requests that orbit controls always orbit around the currently set pivot point.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to request use of the pivot point. When false some controls may pivot around the center of the view. (Currently applies only to the view-cube orbit controls.)

setReverseZoomDirection(value)

Set or unset a view navigation option to reverse the default direction for camera dolly (zoom) operations.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setReverseHorizontalLookDirection(value)

Set or unset a view navigation option to reverse the default direction for horizontal look operations.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setReverseVerticalLookDirection(value)

Set or unset a view navigation option to reverse the default direction for vertical look operations.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setZoomTowardsPivot(value)

Get the state of the view navigation option that requests the default direction for camera dolly (zoom) operations to be towards the camera pivot point.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for towards the pivot, false for default

setOrbitPastWorldPoles(value)

Set or unset a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction). In other words, when set the orbit control will allow the camera to rotate into an upside down orientation. When unset orbit navigation should stop when the camera view direction reaches the up/down direction.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to allow orbiting past the poles.

setUseLeftHandedInput(value)

Set or unset a view navigation option which requests that mouse buttons be reversed from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa).

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to request reversal of mouse button assignments.

setDisplayUnits(value)

Set units for quantities displayed in the property panel. Only setting linear (distance) quantity units are supported

Parameters

value*string

display units to set. The units can be ââ (file units), âmmâ, âcmâ, âmâ, âinâ, âftâ, âft-and-fractional-inâ, âft-and-decimal-inâ, âdecimal-inâ, âdecimal-ftâ, âfractional-inâ, âm-and-cmâ,

setDisplayUnitsPrecision(value)

Set the precision for quantities displayed in the property panel.

Parameters

value*number

precision for the units The value is the number of decimal values after the â.â. For e.g., a value of 5 would be either 0.12345 or 1/32 (2^5) for fraction type units Values greater than 6 is not supported If value is not specified, it defaults to the precision in the file

setLayerVisible(nodes, visible, isolate)

Set visibility for a single layer, or for all layers.

Parameters

nodes*Array

An array of layer nodes, or a single layer node, or null for all layers

visible*boolean

true to show the layer, false to hide it

isolateboolean

true to isolate the layer

isLayerVisible(node)

Returns true if the layer is visible.

Parameters

node*Object

Layer node

Returns

type

description

boolean

true if the layer is visible

anyLayerHidden()

Returns true if any layer is hidden.

Returns

type

description

boolean

true if any layer is hidden

allLayersHidden()

Returns true if all layers are hiden.

Returns

type

description

boolean

true if all layers are hidden

hideHiddenObjects()

setGroundShadowColor(color)

If enabled, set ground shadow color

Not applicable to 2D

Parameters

color*THREE.Color

setGroundShadowAlpha(alpha)

If enabled, set ground shadow alpha

Not applicable to 2D

Parameters

alpha*float

setGroundReflectionColor(color)

If enabled, set ground reflection color. This is reset to default when reflections toggled off.

Not applicable to 2D

Parameters

color*THREE.Color

setGroundReflectionAlpha(alpha)

If enabled, set ground reflection alpha. This is reset to default when reflections toggled off.

Not applicable to 2D

Parameters

alpha*number

getCutPlanes()

Returns a list of active cut planes

Not applicable to 2D

Returns

type

description

Array.<THREE.Vector4>

List of Vector4 plane representation {x:a, y:b, z:c, w:d}

setCutPlanes(planes)

Apply a list of cut planes

Not applicable to 2D

Parameters

planes*Array.<THREE.Vector4>

List of Vector4 plane representation: {x:a, y:b, z:c, w:d} Plane general equation: ax + by + cz + d = 0 where a, b, and c are not all zero Passing an empty list or null is equivalent to setting zero cut planes

getScreenShot(w, h, cb, overlayRenderer)

Captures the current screen image as Blob URL Blob URL can be used like a regular image url (e.g., window.open, img.src, etc) If width and height are 0, returns asynchronously and calls the callback with an image as Blob URL with dimensions equal to current canvas dimensions If width and height are given, returns asynchronously and calls the callback with the resized image as Blob URL If no callback is given, displays the image in a new window. Optional overlayRenderer can be supplied, in order to render an overlay on top of the renderer image.

Parameters

wnumber

width of the requested image

hnumber

height of the requested image

cbfunction

callback

overlayRendererfunction

overlayRenderer

Returns

type

description

DOMString

screenshot image Blob URL, if no parameters are given

worldToClient(point, camera)

Calculates the pixel position in client space coordinates of a point in world space.
See alsoclientToWorld().

Parameters

point*THREE.Vector3

Point in world space coordinates.

camera*THREE.Camera

Optional camera to use - default is the viewerâs native camera.

Returns

type

description

THREE.Vector3

Point transformed and projected into client space coordinates. Z value is 0.

clientToWorld(clientX, clientY, ignoreTransparent, ignore2dModelBounds, ignore2dModelsOn3d)

Given coordinates in pixel screen space it returns information of the underlying geometry node. Hidden nodes will not be taken into account. Returns null if there is no geometry in the specified location. For 2d models, it will return null outside the paper, unless ignore2dModelBounds is true.
See alsoworldToClient().

Parameters

clientX*Number

X coordinate where 0 is left

clientY*Number

Y coordinate where 0 is top

ignoreTransparentBoolean

Ignores transparent materials

ignore2dModelBoundsboolean

For 2d models - whether to return a result outside of the modelâs bounds.

ignore2dModelsOn3dboolean

Whether to ignore 2d models when in 3d mode.

Returns

type

description

Object, null

contains point attribute. 3d models have additional attributes.

modelHasTopology()

Expose if the model has topology information downloaded. Only applicable to 3D models.

Returns

type

description

boolean

value - Indicates whether the model has topology information.

setSelectionColor(color, selectionType)

Changes the color of the selection for a particular selection type.

Autodesk.Viewing.SelectionType.MIXEDSets the same color for regular and overlayed selection.

Sets the same color for regular and overlayed selection.

Autodesk.Viewing.SelectionType.REGULARSets the color of regular selection.

Sets the color of regular selection.

Autodesk.Viewing.SelectionType.OVERLAYEDSets the color of overlayed selection.

Sets the color of overlayed selection.

Parameters

color*THREE.Color

selectionType*number

a member of Autodesk.Viewing.SelectionMode.

Examples

set2dSelectionColor(color, opacity)

Changes the color of the selection for 2D drawings.

Parameters

color*THREE.Color

opacity*number

Examples

setTheme(name)

Sets the current UI theme of the viewer. Supported values are âlight-themeâ and âdark-themeâ, which is the default.

Parameters

name*string

Name of the theme, it will be added to the viewerâs container class list.

setThemingColor(dbId, color, model, recursive)

Highlight an object with a theming color that is blended with the original objectâs material.

Parameters

dbId*number

color*THREE.Vector4

(r, g, b, intensity), all in [0,1].

modelAutodesk.Viewing.Model

For multi-model support.

recursiveboolean

Should apply theming color recursively to all child nodes.

clearThemingColors(model)

Restore original colors for all themed shapes.

Parameters

modelAutodesk.Viewing.Model

For multi-model support.

setMaterialsToDefaults(model)

Restore original materials of a model if they were overwritten, e.g. by Autodesk.Viewing.Viewer3D#setView.â

Parameters

modelAutodesk.Viewing.Model

For multi-model support.

hideModel(model)

Temporarily remove a model from the Viewer, but keep loaders, materials, and geometry alive.

ReferenceAutodesk.Viewing.Viewer3D#showModel

Parameters

model*number,Autodesk.Viewing.Model

model id or Model object

Returns

type

description

boolean

true indicates success, i.e., modelId referred to a visible model that is now hidden

showModel(model, preserveTools)

Make a previously hidden model visible again.

ReferenceAutodesk.Viewing.Viewer3D#hideModel

Parameters

model*number,Autodesk.Viewing.Model

model id or Model object

preserveTools*boolean

disable automatic activation of default tool

Returns

type

description

boolean

true indicates success, i.e.,modelreferred to a hidden model that is now visible

getVisibleModels()

Returns

type

description

Array.<Autodesk.Viewing.Model>

getHiddenModels()

Returns

type

description

Array.<Autodesk.Viewing.Model>

getAllModels()

Returns all models loaded in the viewer.

Returns

type

description

Array.<Autodesk.Viewing.Model>

An array of visible and hidden models

An array of visible and hidden models

getFirstModel()

Returns the first model, according to the environment. If we are in 2D, returns the first sheet. If we are in 3D, returns the first 3D model, regardless if a 2D sheet was loaded before. Note: If thereâs only 2D models in a 3D environment it will return null.

Returns

type

description

Autodesk.Viewing.Model

A model

A model

getUnderlayRaster(bubbleNode)

When loading a PDF document we optionally add a raster preview. This function returns the preview corresponding to the passed bubbleNode.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

Returns

type

description

Array.<Autodesk.Viewing.Model>

disableHighlight(disable)

Disables roll-over highlighting.

Parameters

disable*boolean

Indicates whether highlighting should be on or off. True to disable highlights, false to enable them.

disableSelection(disable)

disable the selection of a loaded model.

Parameters

disable*boolean

true to disable selection, false to enable selection.

isHighlightDisabled()

check if the mouse-over highlight is disabled or not

isHighlightPaused()

check if the mouse-over highlight is paused or not

isHighlightActive()

check if the mouse-over highlight is active or not

isSelectionDisabled()

check if the selection of the loaded model is disabled or not

activateExtension(extensionID, mode)

Activates the extension based on the extensionID and mode given. By default it takes the first available mode in getmodes();

Parameters

extensionID*string

The extension id.

modestring

deactivateExtension(extensionID)

Dectivates the extension based on the extensionID specified.

Parameters

extensionID*string

the extension ID

Returns

type

description

boolean

true if the extension was deactivated false otherwise

true if the extension was deactivated false otherwise

isExtensionActive(extensionID, mode)

Check if the extension is active or not by passing the extensionID.

Parameters

extensionID*string

the extension ID

mode*string

The model of the extension

Returns

type

description

boolean

True if the extension is active, false otherwise

True if the extension is active, false otherwise

isExtensionLoaded(extensionID)

Check if the extension is loaded or not by passing the extensionID.

Parameters

extensionID*string

the extension ID

Returns

type

description

boolean

returns true if the extension was loaded, false otherwise

returns true if the extension was loaded, false otherwise

getLoadedExtensions()

Get a list of all the extensions that are currently loaded.

Returns

type

description

Array.<string>

returns the IDs of all of the loaded extensions

returns the IDs of all of the loaded extensions

getExtensionModes(extensionID)

Get a list of all the modes that are available for the given extensionID.

Parameters

extensionID*string

the extension ID

Returns

type

description

Array.<string>

array of the extensionâs modes.

array of the extensionâs modes.

hitTest(x, y, ignoreTransparent)

Returns the intersection information for point x,y. If no intersection is found this function will return null.

Parameters

x*number

X-coordinate, i.e., horizontal distance (in pixels) from the left border of the canvas.

y*number

Y-coordinate, i.e., vertical distance (in pixels) from the top border of the canvas.

ignoreTransparentboolean

ignores any transparent objects that might intersect x,y

Returns

type

description

Intersection, null

Intersection information about closest hit point.

Intersection information about closest hit point.

refresh(clear)

Clears the screen and redraws the overlays if clear is set to true. Only the overlays will be redrawn if clear is set to false. Should only be called when absolutely needed.

Parameters

clear*boolean

clears the screen and redraws the overlays.

chooseProfile()

Function that decides whichAutodesk.Viewing.Profileto use when a model is loaded for the first time.

Override this method to implement a different logic.

Returns

type

description

Autodesk.Viewing.Profile, null

a Profile

```
forEachExtension(function(ext){
    console.log(ext.id);
 })

```

```
 {
     "click": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickCtrl": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickShift": {
         ...
     },
     "clickCtrlShift": {
         ...
     },
     "disableSpinner": BOOLEAN
     "disableMouseWheel": BOOLEAN,
     "disableTwoFingerSwipe": BOOLEAN
}

```

```
const profileSettings = {
   name: "mySettings",
   settings: {
       ambientShadows: false,
       groundShadows: true
   }
   extensions: {
       load: [],   // Extension IDs
       unload: []  // Extension IDs
   }
}
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

```
viewer.setSelectionColor(new THREE.Color(0xFF0000), Autodesk.Viewing.SelectionType.MIXED); // red color

```

```
viewer.set2dSelectionColor(new THREE.Color(0xFF0000), 0.1); // red color, opacity of 0.1

```


---

# HotkeyManager

HotkeyManager

new HotkeyManager()

Management of hotkeys for the viewer.

Methods

getNames()

Return name of the tool returned as an array

Returns

type

description

Array.<string>

[âhotkeysâ]

getName()

Return name of HotkeyManager tool

Returns

type

description

string

âhotkeysâ

pushHotkeys(id, hotkeys, options)

Pushes new hotkeys onto the stack.

Parameters

id*string

The id for this hotkey set.

hotkeys*Array.<Autodesk.Viewing.HotkeyManager~Hotkey>

The list of hotkeys.

optionsobject

An optional dictionary of options for this hotkey set.

tryUntilSuccessboolean

When true, the onPress callback will be called until it returns true or the hotkey state changes. The onRelease callback will be called until it returns true or until the combination is reengaged. Stops propagation through the stack. Non-blocking.

Returns

type

description

boolean

True if the hotkeys were successfully pushed.

popHotkeys(id)

Removes hotkeys associated with an ID from the stack.

Parameters

id*string

The id associated with the hotkeys.

Returns

type

description

boolean

True if the hotkeys were successfully popped.

handleKeyDown(event, keyCode)

Parameters

event*

Event to handle

keyCode*

Key code

handleKeyUp(event, keyCode)

Parameters

event*

Event to handle

keyCode*

Key code

handleBlur()

Handle blur by releasing all current keys

activate()

No-op

deactivate()

No-op


---

# Model

Model

Core class representing the geometry.

new Model()

Methods

getInstanceTree()

Returns

type

description

InstanceTree

Instance tree of the model if available, otherwise null.

getFuzzyBox(options)

Computes Bounding box of all fragments, but excluding outliers.

Parameters

optionsObject

quantilfloat

in [0,1]. Relative amount of fragments that we consider computation. By default, we consider the 75% of fragments that are closest to the center.

centerfloat

Center from which we collect the closest shapes. By default, we use the center of mass.

ignoreTransformsboolean

Ignore modelMatrix and animation transforms

allowlistArray.<number>

Fragments to include in fuzzybox, by index.

Returns

type

description

THREE.Box3

getBoundingBox(ignoreTransform, excludeShadow)

Parameters

ignoreTransformboolean

Set to true to return the original bounding box in model space coordinates.

excludeShadowboolean

Remove shadow geometry (if exists) from model bounds.

Returns

type

description

THREE.Box3

Bounding box of the model if available, otherwise null.

is2d()

Returns

type

description

boolean

Whether the model is 2D.

is3d()

Returns

type

description

boolean

Whether the model is 3D.

isSVF2()

Returns

type

description

boolean

True if the model is an SVF2 file - which supports sharing of materials and geometry.

isPdf(onlyPdfSource)

Parameters

onlyPdfSource*boolean

Set to true in order to verify that the source file of the model is PDF. Some design files can get extracted to PDFs for example, and in that case, when using the flag, weâll get false as a result.

Returns

type

description

boolean

True if the model is created from a PDF file.

isRevitPdf()

Returns

type

description

boolean

True if the model is a PDF that was created from a Revit source file.

isSmartPdf()

Returns

type

description

boolean

True if the model is a Smart PDF that was created by our translation pipeline.

isLeaflet()

Returns

type

description

boolean

True if the model is created from an image file.

isPageCoordinates()

By default, Leaflet documents are being loaded in a normalized coordinate system. Only when usingfitPaperSizeload option, the model will be loaded in page coordinates, like every other 2D model.

Returns

type

description

boolean

True if the model is loaded in page coordinates.

isSceneBuilder()

Returns

type

description

boolean

True if the model is created using Autodesk.Viewing.SceneBuilder extension

getData()

Returns the geometry data.

Returns

type

description

Object

Data that represents the geometry.

getDocumentNode()

Returns an object wrapping the bubble/manifest entry for the loaded geometry. Contains data such as the viewableID, guid, roleâ¦

Returns

type

description

Autodesk.Viewing.BubbleNode

getRoot()

Returns the root of the geometry node graph.

Returns

type

description

object

The root of the geometry node graph. Null if it doesnât exist.

getRootId()

Returns the root of the geometry node graph.

Returns

type

description

number

The ID of the root or 0 if it doesnât exist.

getUnitData(unit)

Returns an object that contains the standard unit string (unitString) and the scale value (unitScale).

Parameters

unit*string

Unit name from the metadata

Returns

type

description

object

This object contains the standardized unit string (unitString) and a unit scaling value (unitScale)

getUnitScale()

Returns the scale factor of modelâs distance unit to meters.

Returns

type

description

number

The scale factor of the modelâs distance unit to meters or unity if the units arenât known.

getUnitString()

Returns a standard string representation of the modelâs distance unit.

Returns

type

description

string

Standard representation of modelâs unit distance or null if it is not known.

getDisplayUnit()

Returns a standard string representation of the modelâs display unit.

Returns

type

description

string

Standard representation of modelâs display unit or null if it is not known.

getMetadata(itemName, subitemName, defaultValue)

Return metadata value.

Parameters

itemName*string

Metadata item name.

subitemNamestring

Metadata subitem name.

defaultValue

Default value.

Returns

type

description

Metadata value, or defaultValue if no metadata or metadata item/subitem does not exist.

getDefaultCamera()

Returns the default camera.

isAEC()

Returns

type

description

boolean

True when the âAECâ loader settings were used when loading the model

hasPageShadow()

Returns

type

description

boolean

True when a 2D model has a page shadow

getUpVector()

Returns up vector as an array of 3.

getNorthVector()

Returns north vector as an array of 3.

getFrontVector()

Returns front vector as an array of 3.

geomPolyCount()

Returns the polygon count.

Returns

type

description

number

instancePolyCount()

Returns the instanced polygon count.

Returns

type

description

number

isLoadDone(checkTextures)

Returns true if the model with all its geometries has loaded.

Parameters

checkTexturesboolean

Ensures that the modelâs textures were completely loaded.

Returns

type

description

boolean

isObjectTreeCreated()

Returns

type

description

boolean

True if the frag to node id mapping is done.

getPropertyDb()

Returns an instance ofPropertyDatabase Loader, responsible for communicating with the PropertyDatabase instance hosted in a browser worker thread.

Returns

type

description

Autodesk.Viewing.Private.PropDbLoader

getPropertyHashes(nameRE, categoryRE)

Enumerates all attributes (types of properties) used for the given model. If the property database is available, for each property a triple with the propertyâs hash, name, and category is created and added to the result array. In addition, regular expression can be used to filter by name and/or category.

Parameters

nameRE*RegExp

Regular expression to use for filtering properties by their name.

categoryRE*RegExp

Regular expression to use for filtering properties by their category.

Returns

type

description

Array

Array with triples of the propertiesâ hashes, names, and categories.

Examples

getProperties(dbId, onSuccessCallback, onErrorCallback)

Asynchronous method that gets object properties

Parameters

dbId*number

The database identifier.

onSuccessCallbackCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbackCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

getProperties2(dbId, onSuccessCallback, onErrorCallback, options)

Asynchronous method that gets object properties

Parameters

dbId*number

The database identifier.

onSuccessCallbackCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbackCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

optionsObject

needsExternalIdboolean

Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds.

getBulkProperties(dbIds, options, onSuccessCallback, onErrorCallback)

Returns properties for multiple objects with an optional filter on which properties to retrieve.

Parameters

dbIds*Array.<number>

IDs of the nodes to return the properties for.

options*object, undefined

Dictionary with options.

propFilterArray.<string>

Array of property names to return values for. Use null for no filtering. Filter applies to ânameâ and âexternalIdâ fields also.

ignoreHiddenboolean

Ignore hidden properties

onSuccessCallback*function

This method is called when request for property db succeeds.

onErrorCallback*function

This method is called when request for property db fails.

getBulkProperties2(dbIds, options, onSuccessCallback, onErrorCallback)

Returns properties for multiple objects with an optional filter on which properties to retrieve.

Parameters

dbIds*Array.<int>

IDs of the nodes to return the properties for.

options*object, undefined

Dictionary with options.

propFilterArray.<string>

Array of property names to return values for. Use null for no filtering. Filter applies to ânameâ and âexternalIdâ fields also.

categoryFilterArray.<string>

Array of category names to return values for. Use null for no filtering.

ignoreHiddenboolean

Ignore hidden properties

needsExternalIdboolean

Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds.

onSuccessCallback*function

This method is called when request for property db succeeds.

onErrorCallback*function

This method is called when request for property db fails.

getPropertySetAsync(dbIds, options)

Returns a Promise that resolves withPropertySetfor multiple objects. An optional filter can be passed in to specify which properties to retrieve.

Parameters

dbIds*Array.<int>

IDs of the nodes to return the properties for.

optionsObject

Dictionary with options.

propFilterArray.<string>

Array of property names to return values for. Use null for no filtering. Filter applies to ânameâ and âexternalIdâ fields also.

ignoreHiddenboolean

Ignore hidden properties

needsExternalIdboolean

Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds.

Returns

type

description

Promise (PropertySet)

A promise that resolves with an instance of a Autodesk.Viewing.PropertySet

getPropertySet(dbIds, onSuccessCallback, onErrorCallback, options)

Gets the propertyPropertySetfor multiple objects. An optional filter can be passed in to specify which properties to retrieve.

For the async version seegetPropertySetAsync

Parameters

dbIds*Array.<int>

IDs of the nodes to return the properties for.

onSuccessCallback*function

This method is called when request for property db succeeds.

onErrorCallback*function

This method is called when request for property db fails.

optionsObject

Dictionary with options.

propFilterArray.<string>

Array of property names to return values for. Use null for no filtering. Filter applies to ânameâ and âexternalIdâ fields also.

ignoreHiddenboolean

Ignore hidden properties

needsExternalIdboolean

Ensures loading of externalID table if necessary. This may consume a lot of memory. Only use if you really need externalIds.

Returns

type

description

Promise (PropertySet)

Returns a promise that resolves with an instance of a Autodesk.Viewing.PropertySet

Returns a promise that resolves with an instance of a Autodesk.Viewing.PropertySet

getExternalIdMapping(onSuccessCallback, onErrorCallback)

Returns an object with key values being dbNodeIds and values externalIds. Useful to map LMV node ids to Fusion node ids.

Parameters

onSuccessCallback*function

This method is called when request for property db succeeds.

onErrorCallback*function

This method is called when request for property db fails.

getLayerToNodeIdMapping(onSuccessCallback, onErrorCallback)

Returns an object with key values being layer names, pointing to Arrays containing dbIds.

Parameters

onSuccessCallback*function

This method is called when request for property db succeeds.

onErrorCallback*function

This method is called when request for property db fails.

getObjectTree(onSuccessCallback, onErrorCallback)

Asynchronous operation that gets a reference to the object tree.

You can use the model object tree to get information about items in the model.  The tree is made up of nodes, which correspond to model components such as assemblies or parts.

Parameters

onSuccessCallbackCallbacks#onObjectTreeSuccess

Success callback invoked once the object tree is available.

onErrorCallbackCallbacks#onGenericError

Error callback invoked when the object tree is not found available.

isObjectTreeLoaded()

Returnstrueonly when the object tree is loaded into memory. Will returnfalsewhile the object tree is still loading, or when the object tree fails to load.

Returns

type

description

boolean

search(text, onSuccessCallback, onErrorCallback, attributeNames, options)

Async operation to search the object property database.

Parameters

text*string

The search term (not case sensitive).

onSuccessCallback*Callbacks#onSearchSuccess

Invoked when the search results are ready.

onErrorCallback*Callbacks#onGenericError

Invoke when an error occured during search.

attributeNamesArray.<string>

Restricts search to specific attribute names.

optionsObject

Search options. Currently only supported option is searchHidden

searchHiddenboolean

Set to true to also search hidden properties

findProperty(propertyName)

Searches the property database for all dbIds that contains a specific property name.

Parameters

propertyName*string

The property name to search for (case sensitive).

Returns

type

description

Promise (number[])

The promise, which resolves with an array of dbIds containing the specified property.

getTopology(index)

Return topology data of one fragment.

Requires topology data to have been fetched withfetchTopology().

Parameters

index*number

Topology index.

Returns

type

description

object

Topology data.

hasTopology()

See alsofetchTopology().

Returns

type

description

boolean

true if topology data has been downloaded and is available in memory

fetchTopology(maxSizeMB)

Downloads the topology file, if one is available. The file may not get downloaded if the topology content size in memory is bigger than a specified limit (100 MB by default, 20 MB for mobile).

Parameters

maxSizeMBnumber

Maximum uncompressed topology size allowed (in MegaBytes).

Returns

type

description

Promise

A Promise that resolves with the topology object.

hasGeometry()

Returns

type

description

boolean

True if the model loaded contains at least 1 fragment.

getFragmentPointer(fragId)

Returns the FragmentPointer of the specified fragId in the model. This method returns null if the fragId is not passed in.

Parameters

fragId*number

fragment id in the model

Returns

type

description

Autodesk.Viewing.Private.FragmentPointer

The FragmentPointer

clone()

Returns a shallow copy of the model. All the inner state (Fragments, Geometries etc.) are shared.

Returns

type

description

Autodesk.Viewing.Model

A shallow copy of the model.

```
 const properties = await model.getPropertyHashes(/category/i);
// -> Array(8) [ (3) [â¦], (3) [â¦], (3) [â¦], (3) [â¦], (3) [â¦], (3) [â¦], (3) [â¦], (3) [â¦] ]
//     0: Array(3) [ "p5eddc473", "Category", "__category__" ]
//     1: Array(3) [ "pa7275c45", "CategoryId", "__categoryId__" ]
//     2: Array(3) [ "p3ed85946", "Subcategory", "Identity Data" ]
//     ...

```


---

# Navigation

Navigation

new Navigation(camera)

This is the core interface to camera controls and navigation. The active navigation object can normally be obtained from the ânavigationâ property of the Viewer3D instance. Client implementations should not normally instantiate this class directly.

Parameters

camera*THREE.Camera

The main camera object used to render the scene.

Methods

setCamera(camera)

Set or unset the current camera used for navigation. Normally set via the constructor. The camera should be of type Autodesk.Viewing.UnifiedCamera.

Parameters

camera*Autodesk.Viewing.UnifiedCamera

the current camera object.

getCamera()

Returns

type

description

THREE.Camera

the current camera object.

the current camera object.

setScreenViewport(viewport)

Set the current canvas viewport in screen coordinates. Invoked internally on canvas resize.

Parameters

viewport*object

Rectangle with properties left, top, width, height.

getScreenViewport()

Get the current canvas viewport in screen coordinates.

Returns

type

description

object

with properties left, top, width, height.

setView(from, to, up)

Sets the current view to the given LookAt, while keeping other camera properties as is. Jumps to the new location, without camera path animation.

Parameters

from*THREE.Vector3

The desired camera position in world space.

to*THREE.Vector3

The desired camera target in world space.

upTHREE.Vector3

The desired camera up direction in world space.

orientCameraUp(force)

Orient the cameraâs up direction with the current world up direction

Parameters

force*boolean

if true, will orient camera up direction regardless of navigation lock

getPivotPoint()

Returns

type

description

THREE.Vector3

the world space position of the pivot point for orbit navigation.

setPivotPoint(pivot)

Sets the Vector3 world space position of the pivot point for orbit navigation.

Parameters

pivot*THREE.Vector3

the new pivot position.

getPosition()

Returns

type

description

THREE.Vector3

the world space position of the camera.

setPosition(pos)

Sets the Vector3 world space position of camera.

Parameters

pos*THREE.Vector3

the new camera position.

setTarget(target)

Sets the Vector3 world space position towards which the camera should be pointing.

Parameters

target*THREE.Vector3

the new camera look at point.

getTarget()

Returns

type

description

THREE.Vector3

the world space position towards which the camera is pointing.

getEyeVector()

Get the current camera view vector. This vector is not normalized and its length is the distance between the camera position and the camera look at point.

Returns

type

description

THREE.Vector3

the current camera view vector in world space.

getEyeToCenterOfBoundsVec(bounds)

Get a vector from the camera location to the center of the input bounding box.

Parameters

bounds*THREE.Box3

Bounding box.

Returns

type

description

THREE.Vector3

The vector from the camera location to the center of the input bounds.

The vector from the camera location to the center of the input bounds.

getFovMin()

Returns

type

description

number

the minimum allowed vertical field of view in degrees.

getFovMax()

Returns

type

description

number

the maximum allowed vertical field of view in degrees.

setZoomInLimitFactor(factor)

Limits zoom in to show 1/factor-th of the entire 2D page. Applies only on 2D vectorized models.

Parameters

factor*number

getZoomInLimitFactor()

Returns

type

description

number

the current limit when zooming into 2D vectorized models.

setZoomOutLimitFactor(factor)

Limits zoom out to a multiplier of the modelâs bounding box dimensions. Applies only on 2D vectorized models.

Parameters

factor*number

getZoomOutLimitFactor()

Returns

type

description

number

the current limit when zooming out 2D vectorized models.

isPointVisible(point)

Returns true if the point is visible.

Parameters

point*THREE.Vector3

The point in world coordinates.

Returns

type

description

boolean

True if the point is within the cameraâs frustum.

True if the point is within the cameraâs frustum.

setVerticalFov(fov, adjustPosition)

Set the current vertical field of view.

Parameters

fov*number

the new field of view in degrees (value is clamped to the minimum and maximum field of view values).

adjustPosition*boolean

If true, the camera position will be modified to keep either the world space area of the view at the pivot point unchanged (if it is set and visible) or the world space area of view at the camera look at point unchanged.

applyRotation(point, angle, pivot, viewVec)

Applies a rotation on a single point

Parameters

point*THREE.Vector3

Point to rotate

angle*number

Angle of rotation (in radians)

pivot*THREE.Vector3

Pivot of rotation

viewVec*THREE.Vector3

Front vector

getSignedAngle(v1, v2, viewVec)

Computes a signed angle between two vectors

Parameters

v1*THREE.Vector3

Vector #1

v2*THREE.Vector3

Vector #2

viewVec*THREE.Vector3

Front vector

Returns

type

description

number

Signed angle between two vectors

computeFit(oldpos, oldcoi, fov, bounds, aspect)

Compute camera position and look at point which will fit the given bounding box in the view frustum at the given field of view angle.

Parameters

oldpos*THREE.Vector3

existing camera position

oldcoi*THREE.Vector3

existing camera look at point

fov*number

field of view (in degrees) to use for fit calculation in degrees

bounds*THREE.Box3

bounding box to fit

aspect*number

optional aspect ratio of window, horizontal/vertical

Returns

type

description

object

Object with properties âpositionâ and âtargetâ.

computeOrthogonalUp(pos, coi)

Compute a vector which is orthogonal to the given view and aligned with the world up direction.

Parameters

pos*THREE.Vector3

view position

coi*THREE.Vector3

center of interest (view look at point)

Returns

type

description

THREE.Vector3

up direction orthogonal to the given view

fitBounds(immediate, bounds, reorient, force)

Causes the current camera position to be changed in order to fit the given bounds into the current view frustum.

Parameters

immediate*boolean

if false the camera position will animate to the new location.

bounds*THREE.Box3

bounding box to fit

reorient*boolean

if true the camera up direction will be reoriented with the world up.

force*boolean

if true will perform regardless of gotoview enabled or not.

Returns

type

description

object

Object with properties âpositionâ and âtargetâ.

updateCamera()

Update the current camera projection matrix and orient the camera to the current look at point. Invoked internally prior to rendering a new frame with the current camera.

setConstraints2D(viewRegion, maxPixelPerUnit)

Applies zooming and panning restrictions when viewing 2D models. Invoke without parameters to clear any previous setting.

Parameters

viewRegionTHREE.Box3

in world space. If specified, navigation is restricted so that this region always spans >= half of the screen extent in x and y.

maxPixelPerUnitnumber

Restrict zoom-In, so that a single unit in world-space never exceeds maxPixelPerUnit on screen.


---

# NullScreenModeDelegate

NullScreenModeDelegate

ExtendsAutodesk.Viewing.ScreenModeDelegate

new NullScreenModeDelegate(viewer)

Screen mode delegate with no full screen functionality.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.


---

# OverlayManager

OverlayManager

Provides a mechanism for adding custom meshes. These meshes are added into their own overlay scenes, which are always rendered after the main scene.

new OverlayManager()

Methods

addScene(name)

Creates a scene that is always rendered after the main scene. It is rendered into a separate buffer when each frame of the main scene is drawn. The buffer is then composited over the main scene. If it is enabled, the overlay scenes use the main scene depth buffer for the depth testing, to allow the overlay to appear in the main scene.

Parameters

name*string

scene identifier

Returns

type

description

boolean

true if the overlay was added or already exists, false otherwise

true if the overlay was added or already exists, false otherwise

removeScene(name)

Removes a scene along with all the meshes in it.

Parameters

name*string

scene identifier

Returns

type

description

boolean

true if the overlay was removed or if it doesnât exist

true if the overlay was removed or if it doesnât exist

clearScene(name)

Removes all meshes from a scene.

Parameters

name*string

scene identifier

hasScene(name)

Checks whether a scene already exists

Parameters

name*string

scene identifier

Returns

type

description

boolean

true the scene exists

true the scene exists

addMesh(mesh, sceneName)

Inserts one or more custom THREE.Mesh into an existing scene.

Parameters

mesh*THREE.Mesh, Array

A mesh instance or an Array of them.

sceneName*string

Name of an existing scene.

Returns

type

description

boolean

true if the mesh was added to the scene

true if the mesh was added to the scene

Examples

removeMesh(mesh, sceneName)

Removes one or more custom THREE.Mesh from an existing scene. Developers are responsible for disposing the material and geometry after the mesh is removed.

Parameters

mesh*THREE.Mesh, Array

A mesh instance or an Array of them.

sceneName*string

Name of the scene the mesh(es) belong to.

Returns

type

description

boolean

true if the mesh (or meshes) was removed.

true if the mesh (or meshes) was removed.

hasMesh(mesh, sceneName)

Checks whether a mesh is already part of a scene.

Parameters

mesh*THREE.Mesh

The mesh instance.

sceneName*string

Name of the scene to check against.

Returns

type

description

boolean

true if the mesh belongs to the scene.

true if the mesh belongs to the scene.

```
// Create a new mesh
   const geometry = new THREE.SphereGeometry(10, 8, 8);
   const material = new THREE.MeshBasicMaterial({ color: 0x336699 });
   const mesh = new THREE.Mesh(geometry, material);
   mesh.position.x = 1.0; mesh.position.y = 2.0; mesh.position.z = 3.0;
   // Add scene and mesh
   addScene('my_scene');
   addMesh([mesh], 'my_scene');

```


---

# Profile

Profile

new Profile(profileSettings)

Profiles encapsulate viewer settings, extensions to unload, and extensions to load.

TheprofileSettings.settingsparameter will override the existingpreferencesupon calling theapplymethod. TheprofileSettings.extensions.loadandprofileSettings.extensions.unloadarrays are used to load and unload extensions. Make sure to set the profile by using theAutodesk.Viewing.Viewer3D#setProfilemethod.

Parameters

profileSettings*ProfileSettings

the profile settings.

Examples

};
const profile = new Autodesk.Viewing.Profile(profileSettings);

Methods

apply(prefs, override)

Applies the profileâs settings to the viewer preferences. To make the viewer react to the updated preferences please referenceAutodesk.Viewing.Viewer3D#setProfile.

Parameters

prefs*Autodesk.Viewing.Private.Preferences

preferences instance.

overrideboolean

Override all existing preferences with the profileâs preferences.

```
const profileSettings = {
 name: "mySettings",
 description: "My personal settings.",
 settings: {
     ambientShadows: false,
     groundShadows: true
 }
 persistent: ['ambientShadows'],
 extensions: {
     load: ["Autodesk.BimWalk"],   // Extensions to load
     unload: ["Autodesk.ViewCubeUi"]  // Extensions to unload and to not load
 }

```


---

# ProfileManager

ProfileManager

The ProfileManager provides a mechanism for registeringprofile settingswith a specific file type. Any of the registered profiles can be set by usingviewer.setProfile().

new ProfileManager()

Examples

Methods

registerProfile(fileExt, profileSettings)

Registers a profile. The profile will be overridden if a profile was already registered with the ProfileManager.

Parameters

fileExt*String

file extension to register the profile settings with.

profileSettings*ProfileSettings,Autodesk.Viewing.Profile

profile settings object or profile instance to register

unregisterProfile(fileExt)

Unregister the profile associated with a file type

Parameters

fileExt*String

file type

getProfileOrDefault(fileExt)

Returns a profile that is registered with the specific file type. If the file type is not registered, then the default profile is returned.

Parameters

fileExt*String

file extension

Returns

type

description

Autodesk.Viewing.Profile

Profile associated with the file extension.

Profile associated with the file extension.

```
const profileManager = new Autodesk.Viewing.ProfileManager();
// or
// const profileManger = viewer.profileManager;
const profileSettings = {
   name: "DWF",
   settings: {
       swapBlackAndWhite: true
   },
   // ...
}
// Registers the specified profile settings for dwf models.
profileManager.registerProfile('dwf', profileSettings);
const profile = profileManager.getProfile('dwf'); // others: 'default', 'nwc', 'nwd', 'rvt', 'ifc'
viewer.setProfile(profile);

```


---

# PropertySet

PropertySet

The PropertySet class allows for aggregation of properties with the same names and categories. To get an instance of this class useAutodesk.Viewing.Model#getPropertySet.

new PropertySet(result)

Parameters

result*Object

Examples

Methods

forEach(callback)

Iterates over all of the common properties. The callback is invoked on each key in the property map.

Parameters

callback*forEachCallback

Called for each entry in the map

getAggregation(properties)

Returns an object containing aggregated values. seeAutodesk.Viewing.PropertySet#forEach

Parameters

properties*Array.<Object>, String

either the key in the object or an array of properties

Returns

type

description

AggregatedResult

Object with all aggregated values

Object with all aggregated values

Examples

getValue2PropertiesMap(properties)

Returns an object with a key representing the propertyâs displayValue and the value being all of the property names associated with it.

seeAutodesk.Viewing.PropertySet#forEachseePropertyResult

Parameters

properties*Array.<Object>, String

either the key in the object or an array of properties

Returns

type

description

Object

The key representing a common displayValue and the value representing all of the PropertyResult sharing that displaValue

The key representing a common displayValue and the value representing all of the PropertyResult sharing that displaValue

Examples

getValidIds(displayName, displayCategory)

Searches all of the keys in the map object and returns all valid keys that either match the displayName or categoryName.

Parameters

displayName*String

the display name

displayCategory*String

the category name

Returns

type

description

Array.<String>

an array of valid map ids

an array of valid map ids

getDbIds()

Get the dbIds that are associated with the propertySet

Returns

type

description

Array.<number>

an array of dbids associated with the PropertySet

an array of dbids associated with the PropertySet

getVisibleKeys()

Returns an array of keys that contain visible properties

Returns

type

description

Array.<string>

array of keys

array of keys

getKeysWithCategories()

Returns an array of keys that have properties with displayCategories

Returns

type

description

Array.<string>

array of keys

array of keys

merge(propertySet)

Merges the passed in PropertySet map with the current PropertySetâs map.

Parameters

propertySet*Autodesk.Viewing.PropertySet

A PropertySet instance

Returns

type

description

Autodesk.Viewing.PropertySet

returns from the passed in propertySet merged

returns from the passed in propertySet merged

```
const dbIds = viewer.getSelection();
// Use the model's getPropertySet to get the PropertySet instance for the specified dbIds
viewer.model.getPropertySet(dbIds).then((propSet) => {
   // iterate, aggregate, etc
});

```

```
propertySet.forEach((key, properties) => {
  const aggregation = propertySet.getAggregation(key);
});

```

```
propertySet.forEach((name, properties) => {
  const commonValues = propertySet.getValue2PropertiesMap(key);
});

```


---

# ScreenModeDelegate

ScreenModeDelegate

new ScreenModeDelegate(viewer)

Virtual base class for screen mode manipulation.

Derive from this class and use it to allow viewer to go full screen.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.


---

# ToolController

ToolController

new ToolController(viewerImpl, viewerApi, autocam, utilities, defaultHandler)

Core interface to add and remove canvas interactions to the viewer.

This class is created internally by the Viewer api and is available via the âtoolControllerâ property of the Viewer3D api object. Client implementations should not normally instantiate this class directly.

Parameters

viewerImpl*object

The viewer implementation object.

viewerApi*object

The viewer api object.

autocam*object

The Autocam interface object.

utilities*object

The ViewingUtilities object.

defaultHandler*object

The default event handling tool.

Methods

registerTool(tool, onStateChanged)

This method registers an event handling tool with the controller. This makes the tool available for activation and deactivation. Tools are registered under one or more names which must be provided via their âgetNamesâ method. The tools âgetNamesâ method must return an array of one or more names. Typically a tool will only have one name but if it wishes to operate in different modes it can use different names to activate the modes. Registered tools have the properties named âutilitiesâ and âcontrollerâ added to them which refer to the ViewingUtilities object and this controller respectively. Tools may not use the name âdefaultâ which is reserved.

Parameters

tool*object

The tool to be registered.

onStateChanged*function

callback to be called when disabling the tool through the modality map

deregisterTool(tool)

This method deregisters an event handling tool with the controller afterwhich it will no longer be available for activation and deactivation. All names that the tool is registered under will be deregistered. If any tool is active at the time of deregistration will first be deactivated and itâs âdeactivateâ method will be called.

Parameters

tool*object

The tool to be deregistered.

getTool(name)

This method returns the tool registered under the given name.

Parameters

name*string

The tool name to look up.

Returns

type

description

object

The tool registered under the given name or undefined if not found.

getActiveToolName()

This method returns the name of the topmost tool on the tool stack. If no tools are active the name of the default tool is returned (which is âdefaultâ).

Returns

type

description

string

The tool name to look up.

getActiveTool()

This method returns the name of the topmost tool on the tool stack. If no tools are active the name of the default tool is returned (which is âdefaultâ).

Returns

type

description

string

The tool name to look up.

getActiveTools()

Return the current tool stack.

Returns

type

description

Array

list of tools in the tool stack

list of tools in the tool stack

rearrangeByPriorities()

Sorts the toolStack according to the toolsâ priority. Useful when a toolâs priority gets changed after activation.

activateToolModality(toolName)

Disables or enables tools in the toolâs modality map

Parameters

toolName*string

Name of the tool

activateTool(toolName)

Activates the tool registered under the given name. Activation implies pushing the tool on a stack of âactiveâ tools, each of which (starting from the top of the stack) is given the opportunity to handle incoming events. Tools may âconsumeâ events by returning true from their event handling methods, or they may allow events to be passed down to the next tool on the stack by returning false from the handling methods. Upon activation the tools âactivateâ method is called with the name under which it has been activated. Activation is not allowed while the controller is in a âlockedâ state (see the methods âsetIsLockedâ and âgetIsLockedâ). Tools must be registered prior to activation (see the methods âregisterToolâ and âderegisterToolâ). Each tool has its own priority property (default 0), such that a tool with higher priority will get events first.

Parameters

toolName*string

The name of the tool to be activated.

Returns

type

description

boolean

True if activation was successful.

deactivateTool(toolName)

The first tool found on the active stack with the given name is removed and its âdeactivateâ method is called. Once deactivated the tool will no longer receive events via its handler methods. Deactivation is not allowed while the controller is in a âlockedâ state (see the methods âsetIsLockedâ and âgetIsLockedâ).

Parameters

toolName*string

The name of the tool to be deactivated.

Returns

type

description

boolean

True if deactivation was successful.

getToolNames()

Obtain a list of all the currently registered tool names.

Returns

type

description

Array

List of all registered tool names.

setDefaultTool(tool)

Set the tool which will be requested to handle events if no other active tool handles them.

Parameters

tool*object

The tool to be registered as the default.

getDefaultTool()

Get the tool which handle events if no other active tool handles them.

Returns

type

description

object

The tool to be registered as the default.

setIsLocked(state)

Set the controller into a locked or unlocked state. While locked, tool activation and deactivation is not allowed. Locking the controller is sometimes necessary to force an interaction to remain active until it is fully completed.

Parameters

state*boolean

The state of the controller lock.

Returns

type

description

boolean

The previous state of the lock (this may be used to restore the lock to itâs previous state).

getIsLocked()

Get the current state of the controller lock.

Returns

type

description

boolean

The state of the lock.

handleCmdKeyEvent(cmdEvent, eventType)

Catches a CMD event and generate a Control one instead.

Parameters

cmdEvent*object

Event generated by CMD key

eventType*string

Event type

setMouseWheelInputEnabled(isEnabled)

Whether mouse scroll wheel (and/or two-finger vertical swipe) will trigger a camera zoom operation.

Parameters

isEnabled*boolean

setModalityMap(map)

Set the modality map for each tool. This function will clear any existing modality map. The map object consists of a key which represents the tool name and a value which is an object that represents which tools to enable and disable. To get the tool names @seeAutodesk.Viewing.ToolController#getToolNames

Parameters

map*object

Object describing each toolâs modality with other tools.

Examples

// When enabling the section tool the pan tool will be disabled.
toolController.setModalityMap({

measure: { explode: false, bimwalk: false, section: false },
section: { pan: false }

});

getModalityMap()

Get the modality map.

Returns

type

description

object

returns a copy of the tool modality.

returns a copy of the tool modality.

getToolModality(name)

Get a specific toolâs modality map.

Parameters

name*string

tool name

Returns

type

description

object

an object describing the toolâs modality map.

an object describing the toolâs modality map.

setToolModality(name, map)

Parameters

name*string

Tool name that is associated with the modality map.

map*object

Object containing the name of the tool as the key and a boolean that describes if the tool can be enabled or disabled.

```
// When enabling the measure tool the explode, bimwalk and section tools will be disabled.

```


---

# ToolInterface

ToolInterface

new ToolInterface()

Base class for new interaction tools.

Can also be used simply as a template for creating a new tool.

Methods

getNames()

This method should return an array containing the names of all tools implemented by this class. Often this would be a single name but it is possible to support multiple interactions with a single tool. When this tool is registered with the ToolController each name gets registered as an available tool.

Returns

type

description

Array

Array of strings. Should not be empty.

getName()

This is an optional convenience method to obtain the first name of this tool.

Returns

type

description

string

The tools default name.

getPriority()

This method should return the priority of the tool inside the tool stack. A tool with higher priority will get events first.

Returns

type

description

number

The toolâs priority.

register()

This method is called byAutodesk.Viewing.ToolController#registerTool. Use this for initialization.

deregister()

This method is called byAutodesk.Viewing.ToolController#deregisterTool. Use this to clean up your tool.

activate(name, viewerApi)

The activate method is called by the ToolController when it adds this tool to the list of those to receive event handling calls. Once activated, a toolâs âhandle*â methods may be called if no other higher priority tool handles the given event. Each active toolâs âupdateâ method also gets called once during each redraw loop.

Parameters

name*string

The name under which the tool has been activated.

viewerApi*Autodesk.Viewing.Viewer3D

Viewer instance.

deactivate(name)

The deactivate method is called by the ToolController when it removes this tool from the list of those to receive event handling calls. Once deactivated, a toolâs âhandle*â methods and âupdateâ method will no longer be called.

Parameters

name*string

The name under which the tool has been deactivated.

update(highResTimestamp)

The update method is called by the ToolController once per frame and provides each tool with the oportunity to make modifications to the scene or the view.

Parameters

highResTimestamp*number

The process timestamp passed to requestAnimationFrame by the web browser.

Returns

type

description

boolean

A state value indicating whether the tool has modified the view or the scene and a full refresh is required.

handleSingleClick(event, button)

This method is called when a single mouse button click occurs.

Parameters

event*MouseEvent

The event object that triggered this call.

button*number

The button number that was clicked (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleDoubleClick(event, button)

This method is called when a double mouse button click occurs.

Parameters

event*MouseEvent

The event object that triggered this call.

button*number

The button number that was clicked (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleSingleTap(event)

This method is called when a single tap on a touch device occurs.

Parameters

event*Event

The triggering event. For tap events the canvasX, canvasY properties contain the canvas relative device coordinates of the tap and the normalizedX, normalizedY properties contain the tap coordinates in the normalized [-1, 1] range. The event.pointers array will contain either one or two touch events depending on whether the tap used one or two fingers.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleDoubleTap(event)

This method is called when a double tap on a touch device occurs.

Parameters

event*Event

The triggering event. For tap events the canvasX, canvasY properties contain the canvas relative device coordinates of the tap and the normalizedX, normalizedY properties contain the tap coordinates in the normalized [-1, 1] range. The event.pointers array will contain either one or two touch events depending on whether the tap used one or two fingers.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleKeyDown(event, keyCode)

This method is called when a keyboard button is depressed.

Parameters

event*KeyboardEvent

The event object that triggered this call.

keyCode*number

The numerical key code identifying the key that was depressed. Note that the keyCode parameter value may be different that the value indicated in the event object due to key re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleKeyUp(event, keyCode)

This method is called when a keyboard button is released.

Parameters

event*KeyboardEvent

The event object that triggered this call.

keyCode*number

The numerical key code identifying the key that was released. Note that the keyCode parameter value may be different that the value indicated in the event object due to key re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleWheelInput(delta)

This method is called when a mouse wheel event occurs.

Parameters

delta*number

A numerical value indicating the amount of wheel motion applied. Note that this value may be modified from the orignal event values so as to provide consistent results across browser families.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleButtonDown(event, button)

This method is called when a mouse button is depressed.

Parameters

event*MouseEvent

The event object that triggered this call.

button*number

The button number that was depressed (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleButtonUp(event, button)

This method is called when a mouse button is released.

Parameters

event*MouseEvent

The event object that triggered this call.

button*number

The button number that was released (0, 1, 2 for Left, Middle, Right respectively). Note that the button parameter value may be different that the button value indicated in the event object due to button re-mapping preferences that may be applied. This value should be respected over the value in the event object.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleMouseMove(event)

This method is called when a mouse motion event occurs.

Parameters

event*MouseEvent

The event object that triggered this call.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleGesture(event)

This method is called when a touch gesture event occurs.

Parameters

event*Event

The event object that triggered this call. The event.type attribute will indicate the gesture event type. This will be one of: dragstart, dragmove, dragend, panstart, panmove, panend, pinchstart, pinchmove, pinchend, rotatestart, rotatemove, rotateend, drag3start, drag3move, drag3end. The event.canvas[XY] attributes will contain the coresponding touch position. The event.scale and event.rotation attributes contain pinch scaling and two finger rotation quantities respectively. The deltaX and deltaY attributes will contain drag offsets.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleBlur(event)

This method is called when the canvas area loses focus.

Parameters

event*FocusEvent

The event object that triggered this call.

Returns

type

description

boolean

True if this tool wishes to consume the event and false to continue to pass the event to lower priority active tools.

handleResize()

This method is called on every active tool whenever the screen area changes. The new canvas area can be obtained from the Navigation interface via the getScreenViewport method.


---

# Viewer3D

Viewer3D

new Viewer3D(container, config)

Base class for all viewer implementations. It contains everything that is needed to connect to the Autodesk Platform Services and display 2D and 3D models. It also includes basic navigation support, context menu and extension APIs.

Parameters

container*HTMLElement

The viewer container.

config*ViewerConfig

The initial settings object.

startOnInitializeboolean

Set this to false if you want to defer the run to a later time by calling run() explicitly.

themestring

Set this to âlight-themeâ if you want to use the light ui theme. Themes can be changed during execution by calling setTheme() and passing the themeâs name.

localStoragePrefixstring

The local storage prefix for viewer.

profileSettingsSettings

settings object to override the default viewer settings:Autodesk.Viewing.ProfileSettings.Default.

useFileProfileboolean

if set to true one of the registered file profiles will be used to set the profile. Otherwise, the viewer uses the default profile.

Properties

ViewerCount

Need to keep track of viewers in document so we know when it is safe to call clearPropertyWorkerCache()

kDefaultCanvasConfig

Default values passed into#setCanvasClickBehaviorspecifying how the viewer canvas will react to user input as well as other 3d-canvas related options.

scene

The extra scene that gets rendered after the background and before any models are rendered. SeeViewer3DExtraScene

sceneAfter

The extra scene that gets rendered after all models are rendered. SeeViewer3DExtraScene

Methods

loadExtension(extensionId, options)

Loads the extension with the given id and options.

Parameters

extensionId*string

The string id of the extension.

options*Object

An optional dictionary of options.

Returns

type

description

Promise

Resolves with the extension requested.

Resolves with the extension requested.

getExtension(extensionId, callback)

Returns the loaded extension.

Parameters

extensionId*string

The string id of the extension.

callbackfunction

That receives an extension instance as argument.

Returns

type

description

Object

Extension.

Extension.

getExtensionAsync(extensionId)

Returns a promise with the loaded extension.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

Promise

Resolves with the loaded extension.

Resolves with the loaded extension.

unloadExtension(extensionId)

Unloads the extension with the given id.

Parameters

extensionId*string

The string id of the extension.

Returns

type

description

boolean

True if the extension was successfully unloaded.

True if the extension was successfully unloaded.

loadExtensionLocal(extensionId, options)

Loads the extension with the given id and options. For internal use only.

Parameters

extensionId*string

The string id of the extension.

options*Object

An optional dictionary of options.

Returns

type

description

Promise

Resolves with the extension requested.

Resolves with the extension requested.

forEachExtension(callback)

Iterate over each extension that has been successfully loaded and invokes a callback function for them.

Parameters

callback*function

That receives an extension instance as argument.

Examples

start(url, options, onSuccessCallback, onErrorCallback, initOptions)

Initializes the viewer and loads any extensions specified in the constructorâs config parameter. If the optional parameters are specified, the start() function will use an optimized initialization sequence that results in faster model load. The parameters are the same as the ones for Viewer3D.loadModel and you do not need to call loadModel subsequently if the model is loaded via the call to start().

Parameters

urlstring

Optional URN or filepath to load on start.

optionsobject

Optional path to shared property database.

onSuccessCallbackAutodesk.Viewing.Viewer3D~onLoadModelSuccess

Method that gets called when initial loading is done and streaming starts.

onErrorCallbackAutodesk.Viewing.Viewer3D~onLoadModelFailure

Method that gets called when initial loading ends with an error.

initOptionsobject

Optional: Options forwarded to viewer.initialize()

Returns

type

description

number

0 if the viewer has started, an error code (same as that returned by initialize()) otherwise.

setUp(config)

Loading extensions and initializing canvas interactions. Invoked automatically byAutodesk.Viewing.Viewer3D#startmethod.

Parameters

configobject

configuration values

extensionsArray.<string>

List of extension ids to load with the model.

canvasConfigobject

Overrides for click/tap events on the 3D canvas. Refer to#setCanvasClickBehaviorfor details.

tearDown(isUnloadModelsWanted)

Unloads extensions and the loaded models. Invoked automatically byAutodesk.Viewing.Viewer3D#finishmethod.

Parameters

isUnloadModelsWantedboolean

Whether to unload models at the end. Default is true.

_onAggregatedSelectionChanged()

When selection has changed set the pivot point to be in the middle, if Autodesk.Viewing.Private.Prefs3D.SELECTION_SETS_PIVOT is true

run()

Triggers the Viewerâs render loop. Invoked automatically byAutodesk.Viewing.Viewer3D#startmethod. Refer toViewerConfig.startOnInitializeto change startâs method behavior.

localize()

Localize the viewer. This method can be overwritten so that the subclasses can localize any additional elements. Invoked internally during initialization.

uninitialize()

Removes all created DOM elements, performs GL uninitialization that is needed and removes event listeners.

finish()

Unloads any loaded extensions and then uninitializes the viewer.

loadModel(url, options, onSuccessCallback, onErrorCallback)

Loads a model into the viewer. Can be used sequentially to load multiple 3D models into the same scene.

Parameters

url*string

The url to the model.

optionsobject

Dictionary of options.

fileLoaderAutodesk.Viewing.FileLoader

The file loader to use for this url. Required for unsupported file types.

keepCurrentModelsboolean

Flag indicating whether viewer should keep or unload all other models.

loadOptionsobject

May contain params that are specific for certain loaders/filetypes.

sharedPropertyDbPathstring

Optional path to shared property database.

idsstring

A list of object IDs to load.

loadAsHiddenboolean

By default, a new model is instantly shown and triggers viewer refreshes during loading. Setting this option avoids that. The model can then be shown later by calling showModel().

modelNameOverridestring

Allows host application to override model name used in UI.

placementTransformLmvMatrix4

Applied to the model during loading.

applyScalingstring, Object

Unit-Scaling that is applied to the model on load, e.g. { from: âftâ, to: âmâ }. If âfromâ is not set, it is determined from model metadata (if provided). If only âtoâ is set, you can just assign a string directly, e.g. applyScaling = âmâ is the same as applyScaling = { to: âmâ }.

applyPlacementInModelUnitsboolean

Only relevant if options.placementTransform and options.applyScaling are both used at once. In this way, it controls the order in which placement and scaling happen: - False: Placement happens in viewer world-units. That is, applyScaling is done first, then the custom placementMatrix is applied. (Default behavior) - True: Placement happens in model units. That is, custom placementMatrix is applied first, then the unit scaling.

onSuccessCallbackAutodesk.Viewing.Viewer3D~onLoadModelSuccess

A method that gets called when modelâs metadata loading is done and geometry streaming starts.

onErrorCallbackAutodesk.Viewing.Viewer3D~onLoadModelFailure

A method that gets called when loading fails.

isLoadDone(include)

Check whether models are completely loaded This method checks all models in the model queue and load requests that havenât loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if present is loaded and no textures are being loaded.

Parameters

includeObject

Optional object to set the scope of the wait

geometryBoolean

Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent geometry from being considered. Defaults to true.

propDbBoolean

Set to false to exclude the property data base loading from consideration. Defaults to true.

texturesBoolean

Set to false to exclude the texture loading from consideration. Defaults to true.

hiddenBoolean

Set to true to include hidden models for consideration. Defaults to false.

onlyModelsModel, Array.<Model>

Limits the check to the model or models in this property. Note that checking for textures loaded cannot be limited to models.

Returns

type

description

Boolean

True if all models are completely loaded, otherwise false

waitForLoadDone(include)

Wait for models to be completely loaded This method checks all models in the model queue and load requests that havenât loaded the root model yet. A model is completely loaded when the root model is loaded, all of the geometry is loaded, the property database, if there is one, is loaded and no textures are being loaded. If this method is called before the viewer is started, then it will wait until the viewer starts and at least one model start loading to check for the load completing

Parameters

includeObject

Optional object to set the scope of the wait

geometryBoolean

Set to false to exclude the geometry loading from consideration. Because textures are loaded with geometry, include.textures must also be set to false to prevent waiting for geometry to load. Defaults to true.

propDbBoolean

Set to false to exclude the property data base loading from consideration. Defaults to true.

texturesBoolean

Set to false to exclude the texture loading from consideration. Defaults to true.

hiddenBoolean

Set to true to include hidden models for consideration. Defaults to false.

onlyModelsModel, Array.<Model>

Limits the wait to the model or models in this property. Note that waiting for textures loaded cannot be limited to models.

Returns

type

description

Promise

resolves when all models are loaded. This promise can be rejected by a LOADER_LOAD_ERROR_EVENT event.

unloadModel(model)

Unloads the specified model. ReferenceAutodesk.Viewing.Viewer3D#hideModelto hide the model.

Parameters

model*Autodesk.Viewing.Model

The model to unload.

loadDocumentNode(avDocument, manifestNode, options)

Parameters

avDocument*Autodesk.Viewing.Document

The Document instance, which owns the model being loaded

manifestNode*Autodesk.Viewing.BubbleNode

The specific manifest node to load (within the Document)

optionsViewerConfig

Options to pass toAutodesk.Viewing.Viewer3D#loadModel. Will be initialized internally if not specified. The options object will be augmented by automatically determined load parameters.

Returns

type

description

Promise

Resolves with an object representing the model.

Resolves with an object representing the model.

unloadDocumentNode(manifestNode)

Unloads a model previously loaded by loadDocumentNode().

ReferenceAutodesk.Viewing.Viewer3D#loadDocumentNode

Parameters

manifestNode*Autodesk.Viewing.BubbleNode

The specific manifest node to unload (within the Document)

Returns

type

description

boolean

true on success

true on success

getDimensions()

Returns the dimensions of the WebGL canvas.

Returns

type

description

object

Client rectangle bounds object { width:Number, height: Number }

resize()

Resizes the viewer. Required when wrapping div changes dimensions due to CSS changes.

getHotkeyManager()

Returns

type

description

Autodesk.Viewing.HotkeyManager

The hotkey manager.

getCamera()

Gets the camera so it can be modified by the client.

Returns

type

description

THREE.Camera

The active camera.

getState(filter)

Gets the view state as a plain object. A viewer state contains data for the viewport, selection and isolation.

ReferenceAutodesk.Viewing.Viewer3D#restoreState

Parameters

filterobject

Specifies which viewer values to get.

Returns

type

description

object

Viewer state.

restoreState(viewerState, filter, immediate)

Restores the viewer state from a given object.

ReferenceAutodesk.Viewing.Viewer3D#getState

Parameters

viewerState*Object

filterObject

Similar in structure to viewerState used to filter out values that should not be restored.

immediateboolean

Whether the new view is applied with (true) or without transition (false).

Returns

type

description

boolean

True if restore operation was successful.

setView(viewNode, options)

Loads a view specified in the Manifest JSON. For 3D models it will use the camera values. For 2D models it will use the viewBox values.

Notice that in order that the view will be properly set according to the modelâs transformation, the model has to be loaded first.

Parameters

viewNode*Autodesk.Viewing.BubbleNode

bubble node representing the view

optionsObject

skipTransitionboolean

true to apply instanstly instead of lerping.

useExactCameraboolean

whether any up vector adjustment is to be done (to keep head up view)

skipViewpointExtraboolean

true to skip using extra viewpoint information

Returns

type

description

boolean

true, if the view is applied.

setViewFromArray(params)

Sets the view from an array of parameters.

To get the view array of the current camera use:getViewArrayFromCamera. To get the camera object from the view array usegetCameraFromViewArray.

Parameters

params*Array.<Number>

View parameters: [position-x, position-y, position-z, target-x, target-y, target-z, up-x, up-y, up-z, aspect, fov (radians), orthoScale, isPerspective (0=perspective, 1=ortho)]

getCameraFromViewArray(params, model)

Returns an object representing a Camera from an unintuitive array of number. Note: To use this function in multi-model scenarios, you must pass the model parameter.

To get the view array of the current camera use:getViewArrayFromCamera.

Parameters

params*Array.<Number>

Array with 13 elements describing different aspects of a camera.

modelAutodesk.Viewing.Model

Camera is transformed in the same way as the model. Default is this.model (only sufficient for single-view scenarios).

Returns

type

description

Object, null

Camera object, or null if argument is invalid or missing.

Camera object, or null if argument is invalid or missing.

getViewArrayFromCamera()

Returns an Array of values that could be inserted back into a manifest to represent a view. To get the camera object from the view array usegetCameraFromViewArray.

Returns

type

description

Array.<Number>

Array with 13 elements describing different aspects of the current camera.

Array with 13 elements describing different aspects of the current camera.

setViewFromViewBox(viewbox, name, skipTransition)

Sets the view from an array representing a view box.

Not applicable to 3D.

Parameters

viewbox*Array.<Number>

View parameters: [min-x, min-y, max-x, max-y]

namestring

Optional named view name to also set the layer visibility state associated with this view.

skipTransitionboolean

true to apply instanstly instead of lerping.

activateLayerState(stateName)

Changes the active layer state. Layers is a feature usually available on 2D models and some 3D models.

ReferenceAutodesk.Viewing.Viewer3D#getLayerStates

Parameters

stateName*string

Name of the layer state to activate.

getLayerStates()

Returns information for each layer state: name, description, active. Activate a state throughAutodesk.Viewing.Viewer3D#activateLayerState.

Returns

type

description

Array.<Object>, null

Array of layer states. If layers donât exist or are hidden, this methods returns null.

Array of layer states. If layers donât exist or are hidden, this methods returns null.

setViewFromFile(model)

Sets the view using the default view in the source file.

Parameters

modelAutodesk.Viewing.Model

The model, defaults to the loaded model.

getProperties(dbid, onSuccessCallback, onErrorCallback)

Gets the properties for an ID.

Parameters

dbid*number

The database identifier.

onSuccessCallbackCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbackCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

getObjectTree(onSuccessCallback, onErrorCallback)

Gets the viewer model object tree. Once the tree is received it will invoke the specified callback function.

You can use the model object tree to get information about items in the model.  The tree is made up of nodes, which correspond to model components such as assemblies or parts.

Parameters

onSuccessCallbackCallbacks#onObjectTreeSuccess

Success callback invoked once the object tree is available.

onErrorCallbackCallbacks#onGenericError

Error callback invoked when the object tree is not found available.

setCanvasClickBehavior(config)

Sets the click behavior on the canvas to follow config. This is used to change the behavior of events such as selection or Center-of-Interest changed.

Parameters

config*object

Parameter object that meets the above layout.

Examples

Actions can be any of the following: âselectOnlyâ, âselectToggleâ, âdeselectAllâ, âisolateâ, âshowAllâ, âsetCOIâ, âfocusâ, âhideâ

search(text, onSuccessCallback, onErrorCallback, attributeNames, options)

Searches the elements for the given text. When the search is complete, the callback onResultsReturned(idArray) is invoked.

Parameters

text*string

The search term (not case sensitive).

onSuccessCallback*Callbacks#onSearchSuccess

Invoked when the search results are ready.

onErrorCallback*Callbacks#onGenericError

Invoke when an error occured during search.

attributeNamesArray.<string>

Restricts search to specific attribute names.

optionsObject

Search options.

searchHiddenboolean

Set to true to also search hidden properties

includeInheritedboolean

Set to true to include nodes that inherit the property

getHiddenNodes(model)

Returns an array of the IDs of the currently hidden nodes. When isolation is in place, there are no hidden nodes returned because all nodes that are not isolated are considered hidden.

Parameters

modelAutodesk.Viewing.Model

Model object, if passed in the hidden nodes of the model are returned

Returns

type

description

Array.<number>

Array of nodes that are currently hidden, when no isolation is in place.

getIsolatedNodes(model)

Returns an array of the IDs of the currently isolated nodes.

Not yet implemented for 2D.

Parameters

modelAutodesk.Viewing.Model

Model object, if passed in the isolated nodes of the model are returned

Returns

type

description

Array.<number>

Array of nodes that are currently isolated.

isolate(node, model)

Isolates one of many sub-elements. You can pass in a node or an array of nodes to isolate. Pass in null to reset isolation.

Parameters

node*Array.<number>, number

A node ID or array of node IDs from the model treeBaseViewer#getObjectTree.

modelAutodesk.Viewing.Model

the model that contains the node id. Defaults to the first loaded model.

setBackgroundColor(red, green, blue, red2, green2, blue2)

Sets the background colors, which will be used to create a gradient. Values are in the range [0..255]

Parameters

red*number

green*number

blue*number

red2*number

green2*number

blue2*number

setBackgroundOpacity(opacity)

Sets the background opacity.

Parameters

opacity*number

Value is in the range [0.0..1.0]

toggleSelect(dbid, model, selectionType)

Toggles the selection for a given dbid. If it was unselected, it is selected. If it was selected, it is unselected.

Currently three ways of node selection are supported:

Autodesk.Viewing.SelectionType.MIXEDLeaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Autodesk.Viewing.SelectionType.REGULARNodes are tinted with the selection color.

Nodes are tinted with the selection color.

Autodesk.Viewing.SelectionType.OVERLAYEDNodes are tinted with the selection color and shown on top of the not selected geometry.

Nodes are tinted with the selection color and shown on top of the not selected geometry.

Not yet implemented for 2D.

Parameters

dbid*number

modelAutodesk.Viewing.Model

the model that contains the dbId. Uses the initial model loaded by default.

selectionType*number

a member of Autodesk.Viewing.SelectionMode.

select(dbids, model, selectionType)

Selects the array of ids. You can also pass in a single id instead of an array.

Currently three ways of node selection are supported:

Autodesk.Viewing.SelectionType.MIXEDLeaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Leaf nodes are selected using the overlayed selection type, and inner nodes are selected using regular selection type.

Autodesk.Viewing.SelectionType.REGULARNodes are tinted with the selection color.

Nodes are tinted with the selection color.

Autodesk.Viewing.SelectionType.OVERLAYEDNodes are tinted with the selection color and shown on top of the not selected geometry.

Nodes are tinted with the selection color and shown on top of the not selected geometry.

Parameters

dbids*Array.<number>, number

element or array of elements to select.

modelAutodesk.Viewing.Model

the model instance containing the ids.

selectionTypenumber

a member ofAutodesk.Viewing.SelectionType.

clearSelection()

Clears the selection. Seeselect()

getSelectionVisibility()

Returns information about the visibility of the current selection.

Returns

type

description

object

{hasVisible:boolean,hasHidden:boolean}

getSelectionCount()

Returns the number of nodes (dbIds) in the current selection.

Returns

type

description

number

number of selected nodes

number of selected nodes

setSelectionMode(mode)

Sets selection granularity mode. Supported values are:

Autodesk.Viewing.SelectionMode.LEAF_OBJECT: Always select the leaf objects in the hierarchy.

Autodesk.Viewing.SelectionMode.FIRST_OBJECT: For a given node, selects the first non-composite (layer, collection, model) on the path from the root to the given node, and all children.

Autodesk.Viewing.SelectionMode.LAST_OBJECT: For a given node, selects the nearest ancestor composite node and all children. Selects the input node itself in case there is no composite node in the path to the root node.

Parameters

mode*number

The selection mode.

getSelection()

Returns the current selection.

Returns

type

description

Array.<number>

Array of the nodes (dbIds) of the currently selected nodes.

lockSelection(dbIds, lock, model)

Locks the selection of specificnodes(dbIds) in a given model. Thenodeswill be unselected if thelockis set to true and the nodes are already selected. The locked nodes will not be selectable.

Parameters

dbIds*Number, Array.<Number>

dbIds to lock

lock*Boolean

true to lock, false otherwise

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

unlockSelection(dbIds, model)

This function will unlock the specifiednodes(dbIds) for a specificmodel. If thenodesparameter is omitted then the specifiedmodelâs locked nodes will be unlocked. If themodelparameter is omitted then the specifiednodeswill be unlocked for the viewer.model. If both parameters are omitted then all of the models in the viewer will release their locked nodes.

Parameters

dbIdsArray.<Number>

dbIds to unlock

modelAutodesk.Viewing.Model

The model associated to the nodes parameters

isSelectionLocked(dbId, model)

Checks whether selection is locked for a node

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

Returns

type

description

boolean

True is the visibility is locked

getAggregateSelection(callback)

Returns the selected items from all loaded models.

Parameters

callbackfunction

Optional callback to receive enumerated pairs of model and dbId for each selected object. If no callback is given, an array of objects is returned.

Returns

type

description

Array.<object>

An array of objects with a model and selectionSet properties for each model that has selected items in the scene.

setAggregateSelection(selection, fireEvent)

Selects ids from different models. Choose this api instead of select() when selecting across many models

Parameters

selection*Array.<SelectionDef>

Array of selection objects defining what to select

fireEventBoolean

Whether an event is fired at the end

getAggregateIsolation()

Returns the isolated items from all loaded models.

Returns

type

description

Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}>

An array of objects with amodeland the isolatedidsin that model.

setAggregateIsolation(isolation)

Isolate ids from different models. Choose this api instead of isolate() when isolating across many models. It will hide all other models.

Parameters

isolation*Array.<{model: Autodesk.Viewing.Model, ids: (Array.<number>|number)}>

An array of objects with amodeland theidsto isolate in that model

getAggregateHiddenNodes()

Returns the hidden nodes for all loaded models.

Returns

type

description

Array.<{model: Autodesk.Viewing.Model, ids: Array.<number>}>

An array of objects with amodeland the hiddenidsin that model.

hide(node, model)

Ensures the passed in nodes (dbIds) are hidden.

Parameters

node*Array.<number>, number

An array of nodes (dbids) or just a single node.

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

show(node, model)

Ensures the passed in nodes (dbIds) are shown.

Parameters

node*Array.<number>, number

An array of nodes (dbids) or just a single node.

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

showAll()

Ensures everything is visible. Clears all node isolation (3D) and turns on all layers (2D).

hideAll()

Ensures all objects are hidden. Clears all nodes.

toggleVisibility(dbId, model)

Toggles the visibility of the given node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

areAllVisible()

Returns true if every node (dbId) is visible.

Returns

type

description

boolean

True if every node is visible, false otherwise.

True if every node is visible, false otherwise.

isNodeVisible(nodeId, model)

Returns true if the specified node is visible. The model argument is required only when in multi-model scenarios.

Parameters

nodeId*number

Geometry node to check if visible.

modelAutodesk.Viewing.Model

The model that contains the specifiednodeId.

Returns

type

description

boolean

show(dbId, locked, model)

Ensures the passed in nodes (dbIds) are shown.

Parameters

dbId*Array.<number>, number

array of nodes or a single node

locked*boolean

Set to true to lock the nodes visible. Set to false to allow the nodes to be hidden.

modelAutodesk.Viewing.Model

The model that contains the dbId. By default uses the initial model loaded into the scene.

toggleLockVisible(dbId, model)

Toggles the visibility lock of the given node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

isVisibleLocked(dbId, model)

Checks whether visibility is locked for a node (dbId).

Not yet implemented for 2D.

Parameters

dbId*number

the objectâs identifier.

modelAutodesk.Viewing.Model

the model that contains the dbId. By default uses the initial model loaded into the scene.

Returns

type

description

boolean

True is the visibility is locked

explode(scale, options)

Explodes the model from the center of gravity.

Not applicable to 2D.

Parameters

scale*number

A value from 0.0-1.0 to indicate how much to explode.

options*Object

Additional setting for STRATEGY_HIERARCHY.

magnitude*Number

Controls the spread of explode.

depthDampening*Number

Controls the reduction of the explode effect with depth of the object in the hierarchy.

getExplodeScale()

Returns the explode scale.

Not applicable to 2D.

Returns

type

description

number

A value from 0.0-1.0 indicating how exploded the model is.

A value from 0.0-1.0 indicating how exploded the model is.

getExplodeOptions()

Returns the explode options.

Not applicable to 2D.

Returns

type

description

object

{magnitude:Number,depthDampening:Number}

lockExplode(dbids, lock, model)

Lock node (dbid) so that it doesnât explode

Not applicable to 2D.

Parameters

dbids*Array.<number>, number

The dbids to lock or unlock

lock*boolean

Set to true to prevent dbids from exploding. Set to false to allow dbids to explode.

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if any dbids were changed.

isExplodeLocked(dbid, model)

Check whether a dbid is locked so it doesnât explode.

Not applicable to 2D.

Parameters

dbid*number

The dbid to check

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if dbid is locked to prevent explode

toggleLockExplode(dbid, model)

Toggle dbid lock so it doesnât explode

Not applicable to 2D.

Parameters

dbid*number

The dbid to lock or unlock

modelAutodesk.Viewing.Model

The model containing the dbids. Defaults to this.model

Returns

type

description

boolean

True if any dbids were changed.

setQualityLevel(useSAO, useFXAA)

Enables or disables the high quality rendering settings.

Not applicable to 2D.

Parameters

useSAO*boolean

True or false to enable screen space ambient occlusion.

useFXAA*boolean

True or false to enable fast approximate anti-aliasing.

setGhosting(value)

Toggles ghosting during search and isolate.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether ghosting is on or off.

setGroundShadow(value)

Toggles ground shadow.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether shadow is on or off.

setGroundReflection(value)

Toggles ground reflection.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether reflection is on or off.

setEnvMapBackground(value)

Toggles environment map for background.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether environment map for background is on or off.

setFirstPersonToolPopup(value)

Toggles first person tool popup.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether first person tool popup is showed or not.

getFirstPersonToolPopup()

Returns the state of First Person Walk tool popup.

Not applicable to 2D.

Returns

type

description

boolean

true if the First Person Walk tool popup appears, false if the First Person Walk tool popup does not appear.

setBimWalkToolPopup(value)

Toggles the bimwalk tool popup.

Not applicable to 2D.

Parameters

value*boolean

Indicates whether first person tool popup is showed or not.

getBimWalkToolPopup()

Returns the state of First Person Walk tool popup

Not applicable to 2D.

Returns

type

description

boolean

true if the First Person Walk tool popup appears, false if the First Person Walk tool popup does not appear.

setProgressiveRendering(value)

Toggles whether progressive rendering is used. Warning: turning progressive rendering off will have serious performance implications.

Parameters

value*boolean

whether it is on or off

setGrayscale(value)

Overrides line colors in 2D models to render in shades of gray. Applies only to 2D models.

Parameters

value*boolean

whether it is on or off

setSwapBlackAndWhite(value)

AutoCAD drawings are commonly displayed with white lines on a black background. Setting reverse swaps (just) these two colors.

Parameters

value*boolean

whether it is on or off

setOptimizeNavigation(value)

Toggles whether the navigation should be optimized for performance. If set to true, anti-aliasing and ambient shadows will be off while navigating.

Not applicable to 2D.

Parameters

value*boolean

whether it is on or off

setNavigationLock(value)

Locks or unlocks navigation controls.

When navigation is locked, certain operations (for example, orbit, pan, or fit-to-view) are disabled.

ReferenceAutodesk.Viewing.Viewer3D#setNavigationLockSettings

Parameters

value*boolean

True if the navigation should be locked.

Returns

type

description

boolean

The previous state of the lock (this may be used to restore the lock to itâs previous state).

getNavigationLock()

Gets the current state of the navigation lock.

Returns

type

description

boolean

True if the navigation controls are currently locked.

setNavigationLockSettings(settings)

Updates the configuration of the navigation lock, i.e., which actions are available when navigation is locked.

The configurable actions are âorbitâ, âpanâ, âzoomâ, ârollâ, âfovâ, âwalkâ, or âgotoviewâ. By default, none of the actions are enabled when the navigation is locked.

ReferenceAutodesk.Viewing.Viewer3D#setNavigationLock

Parameters

settings*object

Map of : pairs specifying whether the given action is enabled even when the navigation is locked.

getNavigationLockSettings()

Gets the current configuration of the navigation lock.

Returns

type

description

object

Map of : pairs specifying whether the given action is enabled even when the navigation is locked.

setActiveNavigationTool(toolName)

Swaps the current navigation tool for the tool with the provided name. Will trigger NAVIGATION_MODE_CHANGED event if the mode actually changes.

ReferencegetActiveNavigationTool()

Parameters

toolNamestring

The name of the tool to activate. By default it will switch to the default tool.

Returns

type

description

boolean

True if the tool was set successfully. False otherwise.

True if the tool was set successfully. False otherwise.

getActiveNavigationTool()

Returns the name of the active navigation tool.

ReferencesetActiveNavigationTool()

Returns

type

description

string

The toolâs name.

The toolâs name.

setDefaultNavigationTool(toolName)

Sets the default navigation tool. This tool will always sit beneath the navigation tool on the tool stack.

Parameters

toolName*string

The name of the new default navigation tool.

getDefaultNavigationToolName()

Returns the default navigation tool

Returns

type

description

Object

The default navigation tool.

The default navigation tool.

getFOV()

Gets the current camera vertical field of view.

Returns

type

description

number

the field of view in degrees.

the field of view in degrees.

setFOV(degrees)

Sets the current cameras vertical field of view.

Parameters

degrees*number

Field of view in degrees.

getFocalLength()

Gets the current camera focal length.

Returns

type

description

number

the focal length in millimetres.

the focal length in millimetres.

setFocalLength(mm)

Sets the current cameras focal length.

Parameters

mm*number

Focal length in millimetres

hideLines(hide)

Hides all lines in the scene.

Parameters

hide*boolean

hidePoints(hide)

Hides all points in the scene.

Parameters

hide*boolean

setDisplayEdges(show)

Turns edge topology display on/off (where available).

Parameters

show*boolean

true to turn edge topology display on, false to turn edge topology display off.

applyCamera(camera, fit)

Parameters

camera*THREE.Camera

the camera to apply.

fitboolean

Do a fit to view after transition.

fitToView(objectIds, model, immediate)

Fits camera to objects by ID. It fits the entire model if no ID is provided. Operation will fit to the modelâs bounding box when its object tree is not available.

Parameters

objectIdsArray.<number>, null

array of Ids to fit into the view. Avoid passing this value to fit the entire model.

modelAutodesk.Viewing.Model, null

The model containing theobjectIds. If falsey, the viewerâs current model will be used.

immediateboolean

true to avoid the default transition.

setClickConfig(what, where, newAction)

Modifies a click action configuration entry.

Parameters

what*string

which click config to modify (one of âclickâ, âclickAltâ, âclickCtrlâ, âclickShiftâ, âclickCtrlShiftâ).

where*string

hit location selector (one of âonObjectâ, âoffObjectâ).

newAction*Array.<string>

action list (containing any of âsetCOIâ, âselectOnlyâ, âselectToggleâ, âdeselectAllâ, âdeselectAllâ, âisolateâ, âshowAllâ, âhideâ, âfocusâ).

Returns

type

description

boolean

False if specified entry is not found, otherwise true.

getClickConfig(what, where)

Fetch a click action configuration entry.

Parameters

what*string

which click config to fetch (one of âclickâ, âclickAltâ, âclickCtrlâ, âclickShiftâ, âclickCtrlShiftâ).

where*string

hit location selector (one of âonObjectâ, âoffObjectâ).

Returns

type

description

array

action list for the given entry or null if not found.

setClickToSetCOI(state, updatePrefs)

Modify the default click behaviour for the viewer.

Parameters

state*boolean

If true the default is to set the center of interest. If false the default is single select.

updatePrefsboolean

If true, the user preferences will be updated.

setProfile(profile, override)

Updates viewer settings encapsulated witihn a Profile. This method will also load and unload extensions referenced by the Profile.

Parameters

profile*Autodesk.Viewing.Profile

profile containing settings.

overrideboolean

If set to true this will override all existing preference with the new profile preference. Default: true

Examples

setLightPreset(index)

Sets the Light Presets (Environments) for the Viewer.

Not applicable to 2D.

Sets the preference in the UI

Parameters

index*Number

The index mapping looks like this: 0 -> Simple Grey, 1 -> Sharp Highlights, 2 -> Dark Sky, 3 -> Grey Room, 4 -> Photo Booth, 5 -> Tranquility, 6 -> Infinity Pool, 7 -> Simple White, 8 -> Riverbank, 9 -> Contrast, 1 ->0 Rim Highlights, 1 ->1 Cool Light, 1 ->2 Warm Light, 1 ->3 Soft Light, 1 ->4 Grid Light, 1 ->5 Plaza, 1 ->6 Snow Field

setUsePivotAlways(value)

Set or unset a view navigation option which requests that orbit controls always orbit around the currently set pivot point.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to request use of the pivot point. When false some controls may pivot around the center of the view. (Currently applies only to the view-cube orbit controls.)

setReverseZoomDirection(value)

Set or unset a view navigation option to reverse the default direction for camera dolly (zoom) operations.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setReverseHorizontalLookDirection(value)

Set or unset a view navigation option to reverse the default direction for horizontal look operations.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setReverseVerticalLookDirection(value)

Set or unset a view navigation option to reverse the default direction for vertical look operations.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for reverse, false for default

setZoomTowardsPivot(value)

Get the state of the view navigation option that requests the default direction for camera dolly (zoom) operations to be towards the camera pivot point.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true for towards the pivot, false for default

setOrbitPastWorldPoles(value)

Set or unset a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction). In other words, when set the orbit control will allow the camera to rotate into an upside down orientation. When unset orbit navigation should stop when the camera view direction reaches the up/down direction.

Not applicable to 2D.

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to allow orbiting past the poles.

setUseLeftHandedInput(value)

Set or unset a view navigation option which requests that mouse buttons be reversed from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa).

Sets the preference in the UI

Parameters

value*boolean

value of the option, true to request reversal of mouse button assignments.

setDisplayUnits(value)

Set units for quantities displayed in the property panel. Only setting linear (distance) quantity units are supported

Parameters

value*string

display units to set. The units can be ââ (file units), âmmâ, âcmâ, âmâ, âinâ, âftâ, âft-and-fractional-inâ, âft-and-decimal-inâ, âdecimal-inâ, âdecimal-ftâ, âfractional-inâ, âm-and-cmâ,

setDisplayUnitsPrecision(value)

Set the precision for quantities displayed in the property panel.

Parameters

value*number

precision for the units The value is the number of decimal values after the â.â. For e.g., a value of 5 would be either 0.12345 or 1/32 (2^5) for fraction type units Values greater than 6 is not supported If value is not specified, it defaults to the precision in the file

setLayerVisible(nodes, visible, isolate)

Set visibility for a single layer, or for all layers.

Parameters

nodes*Array

An array of layer nodes, or a single layer node, or null for all layers

visible*boolean

true to show the layer, false to hide it

isolateboolean

true to isolate the layer

isLayerVisible(node)

Returns true if the layer is visible.

Parameters

node*Object

Layer node

Returns

type

description

boolean

true if the layer is visible

anyLayerHidden()

Returns true if any layer is hidden.

Returns

type

description

boolean

true if any layer is hidden

allLayersHidden()

Returns true if all layers are hiden.

Returns

type

description

boolean

true if all layers are hidden

hideHiddenObjects()

setGroundShadowColor(color)

If enabled, set ground shadow color

Not applicable to 2D

Parameters

color*THREE.Color

setGroundShadowAlpha(alpha)

If enabled, set ground shadow alpha

Not applicable to 2D

Parameters

alpha*float

setGroundReflectionColor(color)

If enabled, set ground reflection color. This is reset to default when reflections toggled off.

Not applicable to 2D

Parameters

color*THREE.Color

setGroundReflectionAlpha(alpha)

If enabled, set ground reflection alpha. This is reset to default when reflections toggled off.

Not applicable to 2D

Parameters

alpha*number

getCutPlanes()

Returns a list of active cut planes

Not applicable to 2D

Returns

type

description

Array.<THREE.Vector4>

List of Vector4 plane representation {x:a, y:b, z:c, w:d}

setCutPlanes(planes)

Apply a list of cut planes

Not applicable to 2D

Parameters

planes*Array.<THREE.Vector4>

List of Vector4 plane representation: {x:a, y:b, z:c, w:d} Plane general equation: ax + by + cz + d = 0 where a, b, and c are not all zero Passing an empty list or null is equivalent to setting zero cut planes

getScreenShot(w, h, cb, overlayRenderer)

Captures the current screen image as Blob URL Blob URL can be used like a regular image url (e.g., window.open, img.src, etc) If width and height are 0, returns asynchronously and calls the callback with an image as Blob URL with dimensions equal to current canvas dimensions If width and height are given, returns asynchronously and calls the callback with the resized image as Blob URL If no callback is given, displays the image in a new window. Optional overlayRenderer can be supplied, in order to render an overlay on top of the renderer image.

Parameters

wnumber

width of the requested image

hnumber

height of the requested image

cbfunction

callback

overlayRendererfunction

overlayRenderer

Returns

type

description

DOMString

screenshot image Blob URL, if no parameters are given

worldToClient(point, camera)

Calculates the pixel position in client space coordinates of a point in world space.
See alsoclientToWorld().

Parameters

point*THREE.Vector3

Point in world space coordinates.

camera*THREE.Camera

Optional camera to use - default is the viewerâs native camera.

Returns

type

description

THREE.Vector3

Point transformed and projected into client space coordinates. Z value is 0.

clientToWorld(clientX, clientY, ignoreTransparent, ignore2dModelBounds, ignore2dModelsOn3d)

Given coordinates in pixel screen space it returns information of the underlying geometry node. Hidden nodes will not be taken into account. Returns null if there is no geometry in the specified location. For 2d models, it will return null outside the paper, unless ignore2dModelBounds is true.
See alsoworldToClient().

Parameters

clientX*Number

X coordinate where 0 is left

clientY*Number

Y coordinate where 0 is top

ignoreTransparentBoolean

Ignores transparent materials

ignore2dModelBoundsboolean

For 2d models - whether to return a result outside of the modelâs bounds.

ignore2dModelsOn3dboolean

Whether to ignore 2d models when in 3d mode.

Returns

type

description

Object, null

contains point attribute. 3d models have additional attributes.

modelHasTopology()

Expose if the model has topology information downloaded. Only applicable to 3D models.

Returns

type

description

boolean

value - Indicates whether the model has topology information.

setSelectionColor(color, selectionType)

Changes the color of the selection for a particular selection type.

Autodesk.Viewing.SelectionType.MIXEDSets the same color for regular and overlayed selection.

Sets the same color for regular and overlayed selection.

Autodesk.Viewing.SelectionType.REGULARSets the color of regular selection.

Sets the color of regular selection.

Autodesk.Viewing.SelectionType.OVERLAYEDSets the color of overlayed selection.

Sets the color of overlayed selection.

Parameters

color*THREE.Color

selectionType*number

a member of Autodesk.Viewing.SelectionMode.

Examples

set2dSelectionColor(color, opacity)

Changes the color of the selection for 2D drawings.

Parameters

color*THREE.Color

opacity*number

Examples

setTheme(name)

Sets the current UI theme of the viewer. Supported values are âlight-themeâ and âdark-themeâ, which is the default.

Parameters

name*string

Name of the theme, it will be added to the viewerâs container class list.

setThemingColor(dbId, color, model, recursive)

Highlight an object with a theming color that is blended with the original objectâs material.

Parameters

dbId*number

color*THREE.Vector4

(r, g, b, intensity), all in [0,1].

modelAutodesk.Viewing.Model

For multi-model support.

recursiveboolean

Should apply theming color recursively to all child nodes.

clearThemingColors(model)

Restore original colors for all themed shapes.

Parameters

modelAutodesk.Viewing.Model

For multi-model support.

setMaterialsToDefaults(model)

Restore original materials of a model if they were overwritten, e.g. by Autodesk.Viewing.Viewer3D#setView.â

Parameters

modelAutodesk.Viewing.Model

For multi-model support.

hideModel(model)

Temporarily remove a model from the Viewer, but keep loaders, materials, and geometry alive.

ReferenceAutodesk.Viewing.Viewer3D#showModel

Parameters

model*number,Autodesk.Viewing.Model

model id or Model object

Returns

type

description

boolean

true indicates success, i.e., modelId referred to a visible model that is now hidden

showModel(model, preserveTools)

Make a previously hidden model visible again.

ReferenceAutodesk.Viewing.Viewer3D#hideModel

Parameters

model*number,Autodesk.Viewing.Model

model id or Model object

preserveTools*boolean

disable automatic activation of default tool

Returns

type

description

boolean

true indicates success, i.e.,modelreferred to a hidden model that is now visible

getVisibleModels()

Returns

type

description

Array.<Autodesk.Viewing.Model>

getHiddenModels()

Returns

type

description

Array.<Autodesk.Viewing.Model>

getAllModels()

Returns all models loaded in the viewer.

Returns

type

description

Array.<Autodesk.Viewing.Model>

An array of visible and hidden models

An array of visible and hidden models

getFirstModel()

Returns the first model, according to the environment. If we are in 2D, returns the first sheet. If we are in 3D, returns the first 3D model, regardless if a 2D sheet was loaded before. Note: If thereâs only 2D models in a 3D environment it will return null.

Returns

type

description

Autodesk.Viewing.Model

A model

A model

getUnderlayRaster(bubbleNode)

When loading a PDF document we optionally add a raster preview. This function returns the preview corresponding to the passed bubbleNode.

Parameters

bubbleNode*Autodesk.Viewing.BubbleNode

Returns

type

description

Array.<Autodesk.Viewing.Model>

disableHighlight(disable)

Disables roll-over highlighting.

Parameters

disable*boolean

Indicates whether highlighting should be on or off. True to disable highlights, false to enable them.

disableSelection(disable)

disable the selection of a loaded model.

Parameters

disable*boolean

true to disable selection, false to enable selection.

isHighlightDisabled()

check if the mouse-over highlight is disabled or not

isHighlightPaused()

check if the mouse-over highlight is paused or not

isHighlightActive()

check if the mouse-over highlight is active or not

isSelectionDisabled()

check if the selection of the loaded model is disabled or not

activateExtension(extensionID, mode)

Activates the extension based on the extensionID and mode given. By default it takes the first available mode in getmodes();

Parameters

extensionID*string

The extension id.

modestring

deactivateExtension(extensionID)

Dectivates the extension based on the extensionID specified.

Parameters

extensionID*string

the extension ID

Returns

type

description

boolean

true if the extension was deactivated false otherwise

true if the extension was deactivated false otherwise

isExtensionActive(extensionID, mode)

Check if the extension is active or not by passing the extensionID.

Parameters

extensionID*string

the extension ID

mode*string

The model of the extension

Returns

type

description

boolean

True if the extension is active, false otherwise

True if the extension is active, false otherwise

isExtensionLoaded(extensionID)

Check if the extension is loaded or not by passing the extensionID.

Parameters

extensionID*string

the extension ID

Returns

type

description

boolean

returns true if the extension was loaded, false otherwise

returns true if the extension was loaded, false otherwise

getLoadedExtensions()

Get a list of all the extensions that are currently loaded.

Returns

type

description

Array.<string>

returns the IDs of all of the loaded extensions

returns the IDs of all of the loaded extensions

getExtensionModes(extensionID)

Get a list of all the modes that are available for the given extensionID.

Parameters

extensionID*string

the extension ID

Returns

type

description

Array.<string>

array of the extensionâs modes.

array of the extensionâs modes.

hitTest(x, y, ignoreTransparent)

Returns the intersection information for point x,y. If no intersection is found this function will return null.

Parameters

x*number

X-coordinate, i.e., horizontal distance (in pixels) from the left border of the canvas.

y*number

Y-coordinate, i.e., vertical distance (in pixels) from the top border of the canvas.

ignoreTransparentboolean

ignores any transparent objects that might intersect x,y

Returns

type

description

Intersection, null

Intersection information about closest hit point.

Intersection information about closest hit point.

refresh(clear)

Clears the screen and redraws the overlays if clear is set to true. Only the overlays will be redrawn if clear is set to false. Should only be called when absolutely needed.

Parameters

clear*boolean

clears the screen and redraws the overlays.

chooseProfile()

Function that decides whichAutodesk.Viewing.Profileto use when a model is loaded for the first time.

Override this method to implement a different logic.

Returns

type

description

Autodesk.Viewing.Profile, null

a Profile

```
forEachExtension(function(ext){
    console.log(ext.id);
 })

```

```
 {
     "click": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickCtrl": {
         "onObject": [ACTIONS],
         "offObject": [ACTIONS]
     },
     "clickShift": {
         ...
     },
     "clickCtrlShift": {
         ...
     },
     "disableSpinner": BOOLEAN
     "disableMouseWheel": BOOLEAN,
     "disableTwoFingerSwipe": BOOLEAN
}

```

```
const profileSettings = {
   name: "mySettings",
   settings: {
       ambientShadows: false,
       groundShadows: true
   }
   extensions: {
       load: [],   // Extension IDs
       unload: []  // Extension IDs
   }
}
const profile = new Autodesk.Viewing.Profile(profileSettings);
viewer.setProfile(profile);

```

```
viewer.setSelectionColor(new THREE.Color(0xFF0000), Autodesk.Viewing.SelectionType.MIXED); // red color

```

```
viewer.set2dSelectionColor(new THREE.Color(0xFF0000), 0.1); // red color, opacity of 0.1

```


---

# ViewingUtilities

ViewingUtilities

new ViewingUtilities(viewerImplIn, autocam, navapi)

Variety of utilities convenient to navigation and tool development.

This class is instantiated internally and made available to all registered interaction tools via their âutilitiesâ property.

Parameters

viewerImplIn*object

The viewer implementation object.

autocam*object

The Autocam interface object.

navapi*object

The Navigation interface object.

Methods

transitionView(pos, coi, fov, up, worldUp, reorient, pivot)

This method triggers a camera view transition as specified by the parameters.

Parameters

pos*THREE.Vector3

The new world space position of the camera.

coi*THREE.Vector3

The new center of interest (look at point).

fov*number

The new field of view for the camera in degrees.

up*THREE.Vector3

The new camera up direction.

worldUp*THREE.Vector3

The new world up direction.

reorient*boolean

If true the given camera up parameter is ignored and a new up direction will be calculated to be aligned with the given world up direction.

pivot*THREE.Vector3

The new pivot point.

goHome()

This method triggers a camera view transition to the registered home view for the current scene.

getHitPoint(x, y)

This method performs a hit test with the current model using a ray cast from the given screen coordinates.

Parameters

x*number

The normalized screen x coordinate in [0, 1].

y*number

The normalized screen y coordinate in [0, 1].

Returns

type

description

THREE.Vector3

The world space hit position or null if no object was hit.

activatePivot(fadeIt)

This method activates the in scene pivot indicator. The pivot is positioned at the current cameraâs pivot point.

Parameters

fadeIt*boolean

If true the indicator will be displayed and then fade away after a short period.

pivotActive(state, fadeIt)

This method changes the display state of the in scene pivot indicator. If the current scene is 2D this method has no effect.

Parameters

state*boolean

The requested display state for the indicator.

fadeIt*boolean

If true and âstateâ is also true, the indicator will be displayed and then fade away after a short period.

pivotUpdate()

Invoke this method to refresh the pivot indicator and continue its fading action if required.

setPivotPoint(newPivot, preserveView, isset)

Set the current pivot point and pivot set flag. If the pivot indicator is active its position will be updated accordingly. If a temporary pivot was previously applied, its saved state will be cleared.

Parameters

newPivot*THREE.Vector3

The world space position of the new pivot point.

preserveView*boolean

If false the cameraâs view direction will change to look at the new pivot point. If true the cameraâs view will not be changed.

isset*boolean

The new state of the pivot set flag.

savePivot(name)

Save a copy of the current pivot point and pivot set flag.

Parameters

name*string

Optional unique name of the saved location.

restorePivot(name)

Restore the saved copy of the current pivot point and pivot set flag. Once restored the saved value is erased.

Parameters

name*string

Optional unique name of the saved location.

setTemporaryPivot(newPivot)

Allows the caller to save the current pivot and replace it with a new location. If while the temporary pivot is active a new pivot is set via the setPivotPoint method, the saved pivot will be cleared to avoid restoring an out of date pivot location.

Parameters

newPivot*THREE.Vector3

The new pivot to be assigned or null to clear any previously saved pivot.

removeTemporaryPivot()

Restore a pivot value that was saved by a call to setTemporary Pivot.

setPivotSize(scale)

Changes the pivot graphic size.

Parameters

scale*number

Default size value is 1

setPivotColor(color, opacity)

Change pivot color and opacity. Example, to get red 100% solid (non-transparent) use setPivotColor(0xFF0000, 1)

Parameters

color*number

RBG Hex color.

opacitynumber

Opacity value from 0 (transparent) to 1 (opaque).

getBoundingBox(ignoreSelection)

Return the bounding box of the current model or model selection.

Parameters

ignoreSelection*boolean

If true the current selection is ignored and the model bounds is returned.

Returns

type

description

THREE.Box3

fitToView(immediate)

Request a camera transition to fit the current model or model selection into the view frustum.

Parameters

immediate*boolean

If true the transition will be immediate, otherwise animated over a short time period.


---

# Button

Button

ExtendsAutodesk.Viewing.UI.Control

new Button(id, options)

Button control that can be added to toolbars.

Parameters

idstring

The ID for this button. Optional.

optionsobject

An optional dictionary of options.

collapsibleboolean

Whether this button is collapsible.

Properties

StateNumber

Enum for button states

Methods

setState(state)

Sets the state of this button.

Parameters

state*Autodesk.Viewing.UI.Button.State

The state.

Returns

type

description

boolean

True if the state was set successfully.

setIcon(iconClass)

Sets the icon for the button.

Parameters

iconClass*string

The CSS class defining the appearance of the button icon (e.g. image background).

getState()

Returns the state of this button.

Returns

type

description

Autodesk.Viewing.UI.Button.State

The state of the button.

onClick(event)

Override this method to be notified when the user clicks on the button.

Parameters

event*MouseEvent

onMouseOver(event)

Override this method to be notified when the mouse enters the button.

Parameters

event*MouseEvent

onMouseOut(event)

Override this method to be notified when the mouse leaves the button.

Parameters

event*MouseEvent

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

setCollapsed(collapsed)

Sets the collapsed state of this control.

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if the controlâs collapsed state changes.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

STATE_CHANGED

Event fired when state of the button changes.

Properties

buttonIdstring

The ID of the button that fired this event.

stateAutodesk.Viewing.UI.Button.State

The new state of the button.

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# ComboButton

ComboButton

Extends`Autodesk.Viewing.UI.Button`_

new ComboButton(id, options)

ComboButton with submenu that can be added to toolbars.

Parameters

idstring

The id for this comboButton. Optional.

optionsobject

An optional dictionary of options.

Methods

addControl(button)

Adds a new control to the combo fly-out.

Parameters

button*Autodesk.Viewing.UI.Button

removeControl(button)

Removes a control from the combo fly-out.

Parameters

button*Autodesk.Viewing.UI.Button

setState(state)

Sets the state of this combo button.

Parameters

state*Autodesk.Viewing.UI.Button.State

The state.

saveAsDefault()

Copies tooltip (if any), icon and click handler into an internal attribute. Can be restored through#restoreDefault.

restoreDefault()

Restores visual settings previously stored through#saveAsDefault.

setIcon(iconClass)

Sets the icon for the button.

Parameters

iconClass*string

The CSS class defining the appearance of the button icon (e.g. image background).

getState()

Returns the state of this button.

Returns

type

description

Autodesk.Viewing.UI.Button.State

The state of the button.

onClick(event)

Override this method to be notified when the user clicks on the button.

Parameters

event*MouseEvent

onMouseOver(event)

Override this method to be notified when the mouse enters the button.

Parameters

event*MouseEvent

onMouseOut(event)

Override this method to be notified when the mouse leaves the button.

Parameters

event*MouseEvent

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

setCollapsed(collapsed)

Sets the collapsed state of this control.

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if the controlâs collapsed state changes.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

STATE_CHANGED

Event fired when state of the button changes.

Properties

buttonIdstring

The ID of the button that fired this event.

stateAutodesk.Viewing.UI.Button.State

The new state of the button.

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# Control

Control

new Control(id, options)

Base class for UI controls.

It is abstract and should not be instantiated directly.

Parameters

idstring

The id for this control.

optionsobject

Dictionary with options.

collapsibleboolean

Whether this control is collapsible.

Properties

EventString

Enum for control event IDs.

containerHTMLElement

The HTMLElement representing this control.

Methods

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

setCollapsed(collapsed)

Sets the collapsed state of this control.

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if the controlâs collapsed state changes.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# ControlGroup

ControlGroup

Extends`Autodesk.Viewing.UI.Control`_

new ControlGroup(id, options)

Class for grouping controls.

Parameters

idstring

The id for this control group.

optionsobject

An optional dictionary of options.

collapsibleboolean

Whether this control group is collapsible.

Methods

addControl(control, options)

Adds a control to this control group.

Parameters

control*Autodesk.Viewing.UI.Control

The control to add.

optionsobject

An option dictionary of options.

indexobject

The index to insert the control at.

Returns

type

description

boolean

True if the control was successfully added.

indexOf(control)

Returns the index of a control in this group. -1 if the item isnât found.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to find.

Returns

type

description

number

Index of a successfully removed control, otherwise -1.

removeControl(control)

Removes a control from this control group.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to remove.

Returns

type

description

boolean

True if the control was successfully removed.

getControl(controlId)

Returns the control with the corresponding ID if it is in this control group.

Parameters

controlId*string

The ID of the control.

Returns

type

description

Autodesk.Viewing.UI.Control

The control or null if it doesnât exist.

getControlId(index)

Returns the control ID with for corresponding index if it is in this control group.

Parameters

index*number

Index of the control.

Returns

type

description

string

The ID of the control or null if it doesnât exist.

getNumberOfControls()

Returns the number of controls in this control group.

Returns

type

description

number

The number of controls.

setCollapsed(collapsed)

Sets the collapsed state of this control group. Iterates over the child controls and calls child.setCollapsed(collapsed).

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if at least one collapsible childâs state changes.

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

CONTROL_ADDED

Event fired a control is added to the control group.

Properties

controlstring

The control that was added.

indexnumber

The index at which the control was added.

CONTROL_REMOVED

Event fired when a control is removed from the control group.

Properties

controlstring

The control that was removed.

indexnumber

The index at which the control was removed.

SIZE_CHANGED

Event fired when the size of the control group changes.

Properties

childEventobject

The event that the child fired.

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# DataTable

DataTable

new DataTable(dockingPanel)

UI component in LMV that can be added into the DockingPanels to create custom tables

Parameters

dockingPanel*Autodesk.Viewing.UI.DockingPanel

Instance of the Docking Panel

Methods

setData(rowdata, columndata)

Sets the table data

Parameters

rowdata*Array.<Array.<Array>>

The dataset in array of arrays and represents a set of rows

columndata*Array

The dataset in array and represents the column data

destroyTable()

Destroys the table instance

setSortFunction(sortFunc)

API to set the custom sorting function

Parameters

sortFunc*function

custom sort function for the table dataset

getSortFunction()

API to get the custom sorting function

Returns

type

description

function

custom sort function set by the setSortFunction method

restoreDefaultSortFunction()

API to set the default sorting function

getGroupByColumn(col)

Get the group by given column

Parameters

col*number

column index

Returns

type

description

Array.<number>

rowGroups - an array of grouped data, where each group contains numbers that represent the row-indices of the original table dataset.

groupByColumn(col)

Group by given column

Parameters

col*number

column index

getAggregate(type, col)

Get aggregation based on the type for the given column

Parameters

type*string

type of aggregation

col*number

column index

Returns

type

description

string

the final result of the aggregation

aggregate(type, col)

Aggregate based on the type for the given column

Parameters

type*string

type of aggregation

col*number

column index

clearAggregates()

Clears all the aggregations


---

# DockingPanel

DockingPanel

new DockingPanel(parentContainer, id, title, options)

UI panel that is movable and resizable within the bounds of its parent container.

Parameters

parentContainer*HTMLElement

The container for this panel.

id*string

The id to assign this panel.

title*string

The title of this panel.

optionsobject

An optional dictionary of options.

localizeTitleboolean

When true, localization is attempted for the given title.

addFooterboolean

When true, adds a footer to the panel with resizing handler.

Examples

```
// Example of a simple DockingPanel that displays the given content.
// The titlebar and move behavior are overridden in initialize(), which also
// creates a custom close button.
//
SimplePanel = function(parentContainer, id, title, content, x, y)
{
    this.content = content;
    Autodesk.Viewing.UI.DockingPanel.call(this, parentContainer, id, '');

    // Auto-fit to the content and don't allow resize.  Position at the coordinates given.
    //
    this.container.style.height = "auto";
    this.container.style.width = "auto";
    this.container.style.resize = "none";
    this.container.style.left = x + "px";
    this.container.style.top = y + "px";
};

SimplePanel.prototype = Object.create(Autodesk.Viewing.UI.DockingPanel.prototype);
SimplePanel.prototype.constructor = SimplePanel;

SimplePanel.prototype.initialize = function()
{
    // Override DockingPanel initialize() to:
    // - create a standard title bar
    // - click anywhere on the panel to move
    // - create a close element at the bottom right
    //
    this.title = this.createTitleBar(this.titleLabel || this.container.id);
    this.container.appendChild(this.title);

    this.container.appendChild(this.content);
    this.initializeMoveHandlers(this.container);

    this.closer = this.getDocument().createElement("div");
    this.closer.className = "simplePanelClose";
    this.closer.textContent = "Close";
    this.initializeCloseHandler(this.closer);
    this.container.appendChild(this.closer);
};

```


---

# Filterbox

Filterbox

new Filterbox(id, options)

A text input that invokes a callback when the text changes.

Parameters

idstring

The id for this control.

optionsobject

An optional dictionary of options.

filterFunctionfunction

Invoked when the text changes, receives 1 string argument.


---

# ModelStructurePanel

ModelStructurePanel

ExtendsAutodesk.Viewing.UI.DockingPanel

new ModelStructurePanel(parentContainer, id, title, options)

The Model Structure Panel allows users to explore and set the visibility and selection states of the nodes defined in the loaded model.

Parameters

parentContainer*HTMLElement

The container for this panel.

id*string

The id for this panel.

title*string

The initial title for this panel.

optionsobject

An optional dictionary of options.

startCollapsedboolean

When true, collapses all of the nodes under the root.


---

# ObjectContextMenu

ObjectContextMenu

new ObjectContextMenu(viewer)

Context Menu object is the base class for the viewerâs context menus.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.


---

# PropertyPanel

PropertyPanel

ExtendsAutodesk.Viewing.UI.DockingPanel

new PropertyPanel(parentContainer, id, title, options)

The Property Panel displays properties from the whole model or specific parts of it.

Parameters

parentContainer*HTMLElement

The container for this panel.

id*string

The id for this panel.

title*string

The initial title for this panel.

optionsobject

An optional dictionary of options. Currently unused.


---

# RadioButtonGroup

RadioButtonGroup

ExtendsAutodesk.Viewing.UI.ControlGroup

new RadioButtonGroup(id, options)

Group of controls that act like a radio group.

I.e., only one button may be active at a time. Only acceptsAutodesk.Viewing.UI.Button.

Parameters

id*string

The id for this control group.

optionsobject

An optional dictionary of options.

collapsibleboolean

Whether this control group is collapsible.

Methods

addControl(control, options)

Adds a control to this radio button group. The control must be abutton.

Parameters

control*Autodesk.Viewing.UI.Button

The button to add.

optionsobject

An option dictionary of options.

indexobject

The index to insert the control at.

Returns

type

description

boolean

True if the button was successfully added.

removeControl(control)

Removes a control from this control group.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to remove.

Returns

type

description

boolean

True if the control was successfully removed.

getActiveButton()

Returns the active button in this radio button group.

Returns

type

description

Autodesk.Viewing.UI.Button

The active button. Null if no button is active.

indexOf(control)

Returns the index of a control in this group. -1 if the item isnât found.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to find.

Returns

type

description

number

Index of a successfully removed control, otherwise -1.

getControl(controlId)

Returns the control with the corresponding ID if it is in this control group.

Parameters

controlId*string

The ID of the control.

Returns

type

description

Autodesk.Viewing.UI.Control

The control or null if it doesnât exist.

getControlId(index)

Returns the control ID with for corresponding index if it is in this control group.

Parameters

index*number

Index of the control.

Returns

type

description

string

The ID of the control or null if it doesnât exist.

getNumberOfControls()

Returns the number of controls in this control group.

Returns

type

description

number

The number of controls.

setCollapsed(collapsed)

Sets the collapsed state of this control group. Iterates over the child controls and calls child.setCollapsed(collapsed).

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if at least one collapsible childâs state changes.

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

ACTIVE_BUTTON_CHANGED

Event fired when active button for this radio group changes.

Properties

buttonAutodesk.Viewing.UI.Button

The button whose state is changing.

isActiveButtonboolean

Is the event target the currently active button.

CONTROL_ADDED

Event fired a control is added to the control group.

Properties

controlstring

The control that was added.

indexnumber

The index at which the control was added.

CONTROL_REMOVED

Event fired when a control is removed from the control group.

Properties

controlstring

The control that was removed.

indexnumber

The index at which the control was removed.

SIZE_CHANGED

Event fired when the size of the control group changes.

Properties

childEventobject

The event that the child fired.

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# SettingsPanel

SettingsPanel

ExtendsAutodesk.Viewing.UI.SettingsPanel

new SettingsPanel(parentContainer, id, title, options)

UI panel specifically designed for application settings.

The user can add new options to each of the tabs.

Parameters

parentContainer*HTMLElement

The container for this panel.

id*string

The id to assign this panel.

title*string

The title of this panel.

optionsobject

An optional dictionary of options.

widthnumber

Override panelâs minimum width

heightAdjustmentnumber

Override panelâs extra content height, to account for non-scrolling elements.

Methods

setVisible(show)

Sets the new visibility state of this SettingsPanel.

Parameters

show*boolean

The desired visibility state.

addTab(tabId, tabTitle, options)

Adds a new tab to the panel.

Parameters

tabId*string

id for the tab (DOM element will have an extended ID to ensure uniqueness).

tabTitle*string

optionsobject

optional parameter that allows for additional options for the tab: * tabClassName - class name for the Dom elements* minWidth - min width for the tab* index - index if the tab should be inserted instead of added at the end.

Returns

type

description

boolean

True if the tab was added to the panel, false otherwise.

removeTab(tabId)

Removes the given tab from the panel.

Parameters

tabId*string

Tab to remove.

Returns

type

description

boolean

True if the tab was successfully removed, false otherwise.

hasTab(tabId)

Returns true if a tab with given id exists.

Parameters

tabId*string

Tab id.

Returns

type

description

boolean

True if the tab with given id exists, false otherwise.

selectTab(tabId)

Makes a given tab visible and hides the other ones.

Parameters

tabId*string

Tab to select.

Returns

type

description

boolean

True if the tab was selected, false otherwise.

isTabSelected(tabId)

Returns true if the given tab is selected (visible).

Parameters

tabId*string

Tab to check.

Returns

type

description

boolean

True if the tab is selected, false otherwise.

addLabel(tabId, name)

Adds a label to the panel.

Parameters

tabId*string

Id of the tab that will contain the button.

name*string

User facing text.

Returns

type

description

object

the label control

addButton(tabId, label)

Adds a button to the panel.

Parameters

tabId*string

Id of the tab that will contain the button.

label*string

User facing text.

Returns

type

description

string

ID of a new control.

addCheckbox(tabId, caption, initialState, onchange, description, options)

Creates a checkbox control and adds it to a given tab.

Parameters

tabId*string

Tab to which to add a new checkbox.

caption*string

The text associated with the checkbox.

initialState*boolean

Initial value for the checkbox (checked or not).

onchange*function

Callback that is called when the checkbox is changed.

description*

options*object, undefined

Additional options: * insertAtIndex - index at which to insert a new checkbox* i18nOptions - additional translation options forwarded to i18n.t

Returns

type

description

string

ID of a new control.

addRow(tabId, caption, description, options)

Creates a row control and adds it to a given tab. A row only contains a caption and a descriptions

Parameters

tabId*string

Tab to which to add a new row.

caption*string

The text associated with the row.

description*string

Description

options*object, undefined

Additional options: * insertAtIndex - index at which to insert a new row

Returns

type

description

string

ID of a new control.

addSlider(tabId, caption, min, max, initialValue, onchange, options)

Creates a slider control and adds it to a given tab.

Parameters

tabId*string

Tab to which to add a new slider.

caption*string

The text associated with the slider

min*number

Min value of the slider.

max*number

Max value of the slider.

initialValue*number

Initial value for the slider.

onchange*function

Callback that is called when the slider value is changed.

options*object, undefined

Additional options: * insertAtIndex - index at which to insert a new slider

Returns

type

description

string

ID of a new control.

addSliderV2(tabId, caption, description, min, max, initialValue, onchange, options)

Creates a row control and a slider control and adds it to a given tab. The slider does not contain the caption or the stepper.

Parameters

tabId*string

Tab to which to add a new slider.

caption*string

The text associated with the slider

description*string

The description for the slider

min*number

Min value of the slider.

max*number

Max value of the slider.

initialValue*number

Initial value for the slider.

onchange*function

Callback that is called when the slider value is changed.

options*object, undefined

Additional options: * insertAtIndex - index at which to insert a new slider

Returns

type

description

Array.<string>

an array of control ids

an array of control ids

addDropDownMenu(tabId, caption, items, initialItemIndex, onchange, options)

Parameters

tabId*string

Tab to which to add a new slider.

caption*string

The text associated with the slider.

items*Array

List of items for the menu.

initialItemIndex*number

Initial choice.

onchange*function

Callback that is called when the menu selection is changed.

options*object, undefined

Additional options: * insertAtIndex - index at which to insert a new drop down menu

Returns

type

description

string

ID of a new control.

addControl(tabId, control, options)

Adds a new control to a given tab.

Parameters

tabId*string

Tab to which to add a new.

control*object, HTMLElement

Control to add to the given tab.

options*object, undefined

Additional parameters: * insertAtIndex - index at which to insert a new control* caption - caption for the control

Returns

type

description

string

ID of the added control.

removeButton(buttonId)

Removes a given button from the settings panel.

Parameters

buttonId*string,Autodesk.Viewing.UI.Control

button, or button id, to remove.

Returns

type

description

boolean

True if the button was removed, false otherwise.

removeCheckbox(checkboxId)

Removes a given checkbox from the settings panel.

Parameters

checkboxId*string,Autodesk.Viewing.UI.Control

Checkbox to remove.

Returns

type

description

boolean

True if the checkbox was removed, false otherwise.

removeSlider(sliderId)

Removes a given slider from the settings panel.

Parameters

sliderId*string,Autodesk.Viewing.UI.Control

Slider control to remove.

Returns

type

description

boolean

True if the slider control was removed, false otherwise.

removeDropdownMenu(dropdownMenuId)

Removes a given dropdown menu from the settings panel.

Parameters

dropdownMenuId*string,Autodesk.Viewing.UI.Control

Dropdown to remove.

Returns

type

description

boolean

true if the dropdown was removed, false if the dropdown was not removed.

removeControl(controlId)

Removes a given control from the settings panel.

Parameters

controlId*string,Autodesk.Viewing.UI.Control

The control ID or control instance to remove.

Returns

type

description

boolean

true if the control was removed, false if the control was not removed.

getControl(controlId)

Returns a control with a given id.

Parameters

controlId*string

Checkbox id to return.

Returns

type

description

object

Control object if found, null otherwise.

getContentSize()

Returns the width and height to be used when resizing the panel to the content.

Returns

type

description

object

{height:number,width:number}.

sizeToContent(container)

Resizes panel vertically to wrap around the content. It will always leave some room at the bottom to display the toolbar.

Parameters

container*HTMLElement

parent container of settings panel


---

# ToolBar

ToolBar

Extends`Autodesk.Viewing.UI.ControlGroup`_

new ToolBar(id, options)

Core class representing a toolbar UI.

It consists ofAutodesk.Viewing.UI.ControlGroupthat group controls by functionality.

Parameters

id*string

The id for this toolbar.

optionsobject

An optional dictionary of options.

collapsibleboolean

Whether this toolbar is collapsible.

alignVerticallyboolean

Whether this toolbar should be vertically positioned on the right side.

Methods

addControl(control, options)

Adds a control to this control group.

Parameters

control*Autodesk.Viewing.UI.Control

The control to add.

optionsobject

An option dictionary of options.

indexobject

The index to insert the control at.

Returns

type

description

boolean

True if the control was successfully added.

indexOf(control)

Returns the index of a control in this group. -1 if the item isnât found.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to find.

Returns

type

description

number

Index of a successfully removed control, otherwise -1.

removeControl(control)

Removes a control from this control group.

Parameters

control*string,Autodesk.Viewing.UI.Control

The control ID or control instance to remove.

Returns

type

description

boolean

True if the control was successfully removed.

getControl(controlId)

Returns the control with the corresponding ID if it is in this control group.

Parameters

controlId*string

The ID of the control.

Returns

type

description

Autodesk.Viewing.UI.Control

The control or null if it doesnât exist.

getControlId(index)

Returns the control ID with for corresponding index if it is in this control group.

Parameters

index*number

Index of the control.

Returns

type

description

string

The ID of the control or null if it doesnât exist.

getNumberOfControls()

Returns the number of controls in this control group.

Returns

type

description

number

The number of controls.

setCollapsed(collapsed)

Sets the collapsed state of this control group. Iterates over the child controls and calls child.setCollapsed(collapsed).

Parameters

collapsed*boolean

The collapsed value to set.

Returns

type

description

boolean

True if at least one collapsible childâs state changes.

getId()

Gets this controlâs ID.

Returns

type

description

string

The controlâs ID.

setVisible(visible)

Sets the visibility of this control.

Parameters

visible*boolean

The visibility value to set.

Returns

type

description

boolean

True if the controlâs visibility changed.

isVisible()

Gets the visibility of this control.

Returns

type

description

boolean

True if the this control is visible.

setToolTip(toolTipText)

Sets the tooltip text for this control.

Parameters

toolTipText*string

The text for the tooltip.

Returns

type

description

boolean

True if the tooltip was successfully set.

getToolTip()

Returns the tooltip text for this control.

Returns

type

description

string

The tooltip text. Null if itâs not set.

isCollapsed()

Gets the collapsed state of this control.

Returns

type

description

boolean

True if this control is collapsed.

isCollapsible()

Returns whether or not this control is collapsible.

Returns

type

description

boolean

True if this control can be collapsed.

addClass(cssClass)

Adds a CSS class to this control.

Parameters

cssClass*string

The name of the CSS class.

removeClass(cssClass)

Removes a CSS class from this control.

Parameters

cssClass*string

The name of the CSS class.

getPosition()

Returns the position of this control relative to the canvas.

Returns

type

description

object

Thetopandleftvalues of the toolbar.

getDimensions()

Returns the dimensions of this control.

Returns

type

description

object

Thewidthandheightof the toolbar.

setDisplay(value)

Sets the CSSdisplaystyle value.

Parameters

value*string

CSS display value

removeFromParent()

Removes current control from its parent container.

Returns

type

description

boolean

True if the control was successfully removed.

Events

CONTROL_ADDED

Event fired a control is added to the control group.

Properties

controlstring

The control that was added.

indexnumber

The index at which the control was added.

CONTROL_REMOVED

Event fired when a control is removed from the control group.

Properties

controlstring

The control that was removed.

indexnumber

The index at which the control was removed.

SIZE_CHANGED

Event fired when the size of the control group changes.

Properties

childEventobject

The event that the child fired.

VISIBILITY_CHANGED

Event fired when the visibility of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isVisibleboolean

True if the control is now visible.

COLLAPSED_CHANGED

Event fired when the collapsed state of the control changes.

Properties

controlIdstring

The ID of the control that fired this event.

isCollapsedboolean

True if the control is now collapsed.


---

# Tree

Tree

new Tree(delegate, root, parentContainer, options)

Tree view control

Parameters

delegate*object

TreeDelegate instance

root*object

A node in the model Document

parentContainer*HTMLElement

options*object

Methods

destroy()

Remove tree from DOM.

show(show)

Show/hide the tree control

Parameters

show*boolean

true to show the tree control, false to hide it

getRootContainer()

Get the root container

Returns

type

description

string

getElementForNode(node)

Get DOM element for a given logical tree node (or its integer id)

Parameters

node*object

Tree node element

Returns

type

description

HTMLElement

delegate()

Get the tree delegate

Returns

type

description

object

TreeDelegate instance

isCollapsed(group)

Is the given group node in the tree collapsed?

Parameters

group*object

The group node

Returns

type

description

boolean

true if group node is collapsed, false if expanded

setCollapsed(group, collapsed, recursive)

Collapse/expand the given group node in the tree

Parameters

group*object

the group node

collapsed*boolean

Set to true to collapse the group node, false to expand it

recursive*boolean

Set to true to make it recursive

setAllCollapsed(collapsed)

Collapse/expand all group nodes in the tree

Parameters

collapsed*boolean

true to collapse tree, false to expand it

addToSelection(nodes)

Add the given nodes to the current selection

Parameters

nodes*Array.<object>

nodes to add to the current selection

removeFromSelection(nodes)

Remove the given nodes from the current selection

Parameters

nodes*Array.<object>

The nodes to remove from the current selection

setSelection(nodes)

Set the current selection

Parameters

nodes*Array.<object>

nodes to make currently selected

getSelection()

Get the current selection

Returns

type

description

Array.<object>

selected nodes.

clearSelection()

Clear the current selection

isSelected(node)

Is the given node selected?

Parameters

node*object

The tree node

Returns

type

description

boolean

true if node is selected, false otherwise

true if node is selected, false otherwise

scrollTo(node)

Scrolls the container to reveal the nodeâs DOM element.

Parameters

node*object

the Tree node

addClass(node, className, recursive)

Add a CSS class to a node

Parameters

node*number, object

The tree node

className*string

recursive*

Returns

type

description

boolean

true if the class was added, false otherwise

true if the class was added, false otherwise

removeClass(node, className, recursive)

Remove a class from a node

Parameters

node*number, object

The tree node or its dbId

className*string

Class name

recursive*boolean

Set to true to make it recursive

Returns

type

description

boolean

true if the class was removed, false otherwise

true if the class was removed, false otherwise

hasClass(node, className)

Does the node have the given class?

Parameters

node*number, object

The node or its dbId

className*string

Returns

type

description

boolean

true if the node has the given class, false otherwise

clear()

Clears the contents of the tree

iterate(node, callback)

Iterates through nodes in the tree in pre-order.

Parameters

node*object, number

node at which to start the iteration.

callback*function

invoked for each iterated node with (Object, HTMLElement)


---

# AnimationExtension

AnimationExtension

new AnimationExtension(viewer, options)

AnimationExtension adds a toolbar with buttons (play/pause/forward/backward/goto start/end) and timeline scrubber to control animation playback. The extension provides api methods that will be reflected by the animation toolbar.

The extension id is:Autodesk.Fusion360.Animation

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Adds a toolbar button and hooks animation listeners.

unload()

Removes toobar button and unhooks animation listeners.

play()

Plays the animation. Invoke pause() to stop the animation.

pause()

Pauses an active animation. Can resume by invoking play()

isPlaying()

Whether the animation is currently playing. Always returns the opposite of isPaused()

Returns

type

description

boolean

isPaused()

Wether the animation is currently paused. Always returns the opposite of isPlaying()

Returns

type

description

boolean

rewind()

Rewinds and pauses the animation.

setTimelineValue(scale)

Sets the animation at the very beginning (0), at the end(1) or anywhere in between. For example, use value 0.5 to set the animation half way through itâs completion. Will pause a playing animation.

Parameters

scale*number

value between 0 and 1

prevKeyframe()

Sets animation onto the previous keyframe. Will pause the animation if playing.

nextKeyframe()

Sets animation onto the next keyframe. Will pause the animation if playing.

getDuration()

Returns how many seconds does the animation take to complete.

Returns

type

description

number

getDurationLabel()

Returns duration as a formatted String h:mm:ss (hours:minutes:seconds)

Returns

type

description

string

getCurrentTime()

Returns the elapsed time (in seconds) of the animation.

Returns

type

description

number

getCurrentTimeLabel()

Returns the current animation time as a formatted String h:mm:ss (hours:minutes:seconds)

Returns

type

description

string

setFollowCamera(followCam)

Whether a playing animation updates the camera position.

Parameters

followCam*boolean

true to allow animation to update camera position (default behavior).

Returns

type

description

boolean

true if the operation was successful.

isFollowingCamera()

Returns

type

description

boolean

Whether animations will update the cameraâs position (true) or not (false)

setSpeedModifier(value)

Changes the speed at which the animation is played. Use value 1 to run the animation at default speed, use value 2 to run it at double the speed, use value 0.5 to run it at half the speed.

Parameters

value*number

A multiplier for the animationâs elapsed time.

getSpeedModifier()

Returns

type

description

number

The playback speed multiplier.

setLooping(loop)

Sets whether the animation rewinds and plays as soon as the animation finishes playing.

Parameters

loop*boolean

true to have the animation loop continuously.

isLooping()

Returns

type

description

boolean

Whether the animation will loop continuously.

onToolbarCreated(toolbar)

Invoked by the viewer when the toolbar UI is available.

Parameters

toolbar*Autodesk.Viewing.UI.ToolBar

toolbar instance.

openPanel()

Opens a panel with options to configure the animation extension.

activate()

Plays the animation.

deactivate()

Pauses the animation.

isActive()

Returns

type

description

boolean

true when the animation is playing.

```
// When ANIMATION_READY_EVENT is fired, object tree has been created and animation data has been processed
viewer.addEventListener(Autodesk.Viewing.ANIMATION_READY_EVENT, function () {
  const animationExt = viewer.getExtension('Autodesk.Fusion360.Animation');
  animationExt.play();
});

```


---

# BimWalkExtension

BimWalkExtension

new BimWalkExtension(viewer, options)

First Person navigation tool, similar to those found in videogames. Supports keyboard and mouse input.

The extension id is:Autodesk.BimWalk

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate()

Enables the walk tool.

deactivate()

Deactivates the walk tool.

```
viewer.loadExtension('Autodesk.BimWalk')

```


---

# CrossFadeEffects

CrossFadeEffects

CrossFadeEffects extension provides API for implementing smooth fading effects in LMV, e.g.

CrossFading between models or model configurations (e.g. color theming, hiding objects etc.)

Image-based âghostingâ effect, i.e. showing a semitransparent snapshot of a model on top of another one.

The extension id is:Autodesk.CrossFadeEffects

Note:

Note that CrossFadeEffects require 2 extra RenderTargets. So, they should only be used for optional effects that can be skipped on weak devices.

CrossFade effects can only be used for one purpose at a time. When using them for a new feature, you have to make sure that they donât conflict with existing features.

new CrossFadeEffects()

Examples

Methods

load()

Enables cross frade effects.

unload()

Disables cross frade effects.

acquireControl(clientId, onClientChanged)

Fading targets may be used by different clients for different purposes. Thatâs okay as long as it does not happen concurrently.

In case of conflicts, the last caller takes precedence.

If you start an effect using this extension, always call this function to notify client code that was using it before. Vice versa, provide an onClientChanged() callback to handle the case that someone else overtakes.

Example: If start a fading effect while the ghost floors of the LevelsExtension are fading out, the LevelsExtension will be notified to skip the fade-out anim to avoid conflicts.

Parameters

clientId*string

Some identifier unique for the code component using the effect, e.g. the name of an extension.

onClientChangedfunction

Will be called if another client called acquireControl.

setModelTargetIndex(modelId, targetIndex)

Only allowed if modelCrossFade is enabled. Determines to which target a RenderModel will be rendered.

Parameters

modelId*number

The model id

targetIndex*undefined, 0, 1

index of the crossFade target or undefined (default) to use default color buffer

setModelTargetIndexForAll(index)

Only allowed if modelCrossFade is enabled. Determines to which target a RenderModel will be rendered.

Parameters

index*undefined, 0, 1

index of the crossFade target or undefined (default) to use default color buffer

setCrossFadeOpacity(targetIndex, opacity)

Only allowed if modelCrossFade is enabled. Assigns a blending opacity to a cross-fading extra target.

Parameters

targetIndex*number

must be >0

opacity*number

in [0,1]

setCrossFadeEnabled(enable)

Enable/Disable model cross-fading. Must be enabled in order to render models to different render targets for cross-fading effects (see below). If no cross-fading effects are used, it should be disabled to save GPU memory and performance.

Parameters

enable*boolean

Whether to enable(true) or disable(false) cross fade effects.

fadeTarget(targetIndex, startOpacity, endOpacity, duration, onFinished)

Runs a fading-animation on a cross-fading target.

Parameters

targetIndex*number

see setModelTargetIndex()

startOpacity*number

in [0,1]

endOpacity*number

in [0,1]

durationnumber

in seconds

onFinishedfunction

optional callback triggered when animation is finished

Returns

type

description

object

AnimControl instance

fadeToViewerState(applyState, duration)

Runs a static image fade between the current view and a modified view. (e.g. with changed model/fragment visiblity, ghosting etc.) The modified view is specified via function applyState.

Parameters

applyState*function

applied after rendering the fading start image.

duration*number

in seconds

```
viewer.loadExtension('Autodesk.CrossFadeEffects')

```


---

# DocumentBrowser

DocumentBrowser

Adds a toolbar button that opens a Panel displaying all models and views available from the loaded Document. The panel allows navigating to any model referenced by the Document.

The extension id is:Autodesk.DocumentBrowser

new DocumentBrowser()

Examples

Methods

loadNextModel(viewerConfig, loadOptions)

Unloads the current model and then loads the next model in the Document. It may reload the same model if the Document contains only 1 model.

Parameters

viewerConfigobject

loadOptionsobject

loadPrevModel(viewerConfig, loadOptions)

Unloads the current model and then loads the previous model in the Document. It may reload the same model if the Document contains only 1 model.

Parameters

viewerConfigobject

loadOptionsobject

```
viewer.loadExtension('Autodesk.DocumentBrowser')

```


---

# Edit2DExtension

Edit2DExtension

Edit2D extension provides API for implementing 2D vector editing. Loading the extension does not add UI or changes behavior in the viewer. Its purpose is only to provide a basis for other extensions and client applications.

The extension id is:Autodesk.Edit2D

new Edit2DExtension()

Examples

```
viewer.loadExtension('Autodesk.Edit2D')

```


---

# ExplodeExtension

ExplodeExtension

Use itsactivate()method to enable the explode UI.

The extension id is:Autodesk.Explode

new ExplodeExtension(viewer, options)

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Initializes and registers the ExplodeTool.

unload()

Deactivate the extension, deregister the ExplodeTool, and remove the UI from the toolbar.

onToolbarCreated(toolbar)

Invoked by the viewer when the toolbar UI is available.

Parameters

toolbar*Autodesk.Viewing.UI.ToolBar

toolbar instance.

activate()

Activates the tool and UI.

deactivate()

Hides the explode UI and deactivates the ExplodeTool (resets the explode scale).

isActive()

Returns

type

description

boolean

true if the ExplodeTool is active.

getScale()

Returns

type

description

number

Between 0 and 1.

setScale(value)

Sets scale of the explode and applies an explode operation.

Parameters

value*number

Between 0 and 1.

getMagnitude()

Returns

type

description

number

0 - +inf.

setMagnitude(value)

Sets magnitude of the explode and applies an explode operation.

Parameters

value*number

0 - +inf.

getDepthDampening()

Returns

type

description

number

1 - +inf.

setDepthDampening(value)

Sets depth dampening of the explode and applies an explode operation.

Parameters

value*number

0 - +inf.

setStrategy(strategy)

Specifies the algorithm used for exploding models.

Parameters

strategy*string

Either âhierarchyâ or âradialâ.

getStrategy()

Returns an identifier for the algorithm used for exploding models.

Returns

type

description

string

setUIEnabled(enable)

Enable / Disable the explode button & slider. Doesnât affect the state of the explode scale itself.

Parameters

enable*boolean

enable / disable the UI.

```
viewer.loadExtension('Autodesk.Explode')

```


---

# FullScreenExtension

FullScreenExtension

new FullScreenExtension(viewer, options)

Use itsactivate()method to enter fullscreen mode. It performs the same action as the toolbarâs fullscreen button.

The extension id is:Autodesk.FullScreen

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate()

Enters fullscreen mode.

deactivate()

Exits fullscreen mode.

```
viewer.loadExtension('Autodesk.FullScreen')

```


---

# FusionOrbitExtension

FusionOrbitExtension

new FusionOrbitExtension(viewer, options)

Provides a customization to the orbit tool.

The extension id is:Autodesk.Viewing.FusionOrbit

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate(mode)

Activates the extensionâs tool.

Parameters

modestring

Either âfusionorbitâ (default) or âfusionfreeorbitâ.

deactivate()

Deactivates the extensionâs tool.

```
viewer.loadExtension('Autodesk.Viewing.FusionOrbit')

```


---

# GeolocationExtension

GeolocationExtension

Provides functions for converting GPS coordinates in WGS-84 format { x: Longitude, y: Latitude, z: Height(m) } into Viewer scene coordinates, and back. Supports a single model loaded into the scene.

The extension id is:Autodesk.Geolocation

new GeolocationExtension(viewer, options)

Parameters

viewer*Autodesk.Viewing.Viewer3D

The Viewer instance

optionsobject

Not used

Examples

Methods

activate()

When active, the extension will detect clicks on the model and will place a marker on the model. A panel will be displayed containing vertices clicked on the model. Each point-entry will also contain GPS its associated GPS position.

deactivate()

Stops detecting click events on the canvas and closes the Panel.

isActive()

Whether the extension is active. When the extension is active, click events will be processed and added into a Panel.

Returns

type

description

boolean

True if the extension is active.

hasGeolocationData()

Returns

type

description

boolean

true when the model contains geolocation data.

lmvToLonLat(lmvPoint)

Converts viewer coordinates (obtained with something likeviewer.clientToWorld()) into { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format.

Parameters

lmvPoint*THREE.Vector3

3D point in the scene

Returns

type

description

THREE.Vector3

GPS coordinate in WGS-84 format: { x: Longitude, y: Latitude, z: Height }

lonLatToLmv(lonLat)

Converts coordinates from { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format into viewer scene coordinates.

Parameters

lonLat*THREE.Vector3

GPS coordinate in WGS-84 format: { x: Longitude, y: Latitude, z: Height }

Returns

type

description

THREE.Vector3

3D point in the scene

openGoogleMaps(pointLL84)

Returns a Google Maps URL with a PIN on the specified GPS location. When no argument is provided, the URL will use the Modelâs geolocation if available.

Parameters

pointLL84THREE.Vector3

GPS location in WGS-84 format: { x: Longitude, y: Latitude }. Height is ignored.

getCurrentPositionLmv()

Returns a Promise that resolves with a position in Viewer-space coordinates based on the deviceâs real world GPS position.

Returns

type

description

Promise

that resolves with a THREE.Vector3 containing Viewer-space coordinates. It rejects if deviceâs real world GPS position is not available.

```
viewer.loadExtension('Autodesk.Geolocation')

```


---

# GestureDocumentNavigationExtension

GestureDocumentNavigationExtension

Provide an option to switch sheets and documents, using gestures.

The extension id is:Autodesk.BIM360.GestureDocumentNavigation

new GestureDocumentNavigationExtension()

Examples

Methods

load()

Load the GestureDocumentNavigation extension.

Returns

type

description

boolean

True if measure extension is loaded successfully.

unload()

Unload the measure extension.

Returns

type

description

boolean

True if measure extension is unloaded successfully.

prepareChange(cb)

Prepare current document before switching sheet / document.

Parameters

cb*function

This callback is called after current document is ready to switch.

changeSheetRequired(guid)

Change a sheet.

Parameters

guid*number

The guid of the desired sheet.

changeSheetRequired(urn, guid)

Change a document.

Parameters

urn*number

The urn of the desired document.

guid*number

The guid of the desired sheet.

```
viewer.loadExtension('Autodesk.BIM360.GestureDocumentNavigation')

```


---

# glTF

glTF

Extension description

The glTF extension lets you view glTF 2.0 models in the Viewer. This extension lets you have efficient glTF 2.0 models in your application.

The extension id is: âAutodesk.glTFâ

new glTF(viewer, options)

Autodesk.glTFExtension constructor

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.

optionsObject

Options for the glTFExtension

someOptionboolean

This is how options should be documented

Examples

Methods

activate(mode)

Override the activate method to enable the functionality of the extension.

Parameters

mode

An optional mode that indicates a different way the extension can function.

Returns

type

description

boolean

True if the extension activation was successful.

deactivate()

Override the deactivate method to disable the functionality of the extension.

Returns

type

description

boolean

True if the extension deactivation was successful.

```
 // Use this viewer option to load the glTF extension
 var options = {
 env: 'AutodeskProduction',
 api: 'derivativeV2',
 documentId: 'tests/unittest/models/gltf/duck.gltf'
}

```


---

# GoHomeExtension

GoHomeExtension

new GoHomeExtension(viewer, options)

Use itsactivate()method to animate the camera back to its default, home view. The extension doesnât provide any UI.

The extension id is:Autodesk.GoHome

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate()

Animates the camera back to its home location.

activate()

It doesnât do anything.

```
viewer.loadExtension('Autodesk.GoHome')

```


---

# HyperlinkExtension

HyperlinkExtension

new HyperlinkExtension(viewer, options)

Enhances 2D models by adding in-canvas tooltips that on click will navigate the user to another 2D or 3D model.

The extension id is:Autodesk.Hyperlink

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Registers the hyperlink tool that will intercept pointer events to provide hyperlinks next to specific nodes in the model.

unload()

Unregisters the hyperlink tool.

```
viewer.loadExtension('Autodesk.Hyperlink')

```


---

# LayerManagerExtension

LayerManagerExtension

new LayerManagerExtension(viewer, options)

Use itsactivate()method to open the LayersPanel UI. Layers are usually present in 2D models, but some 3D models may support layers as well, for example: AutoCAD.

The extension id is:Autodesk.LayerManager

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate()

Opens the Layers Panel UI.

deactivate()

Closes the Layers Panel UI.

isActive()

Checks whether the Layers Panel UI is opened.

Returns

type

description

boolean

true if the Layers Panel UI is currently opened.

```
viewer.loadExtension('Autodesk.LayerManager')

```


---

# MarkupsCore

MarkupsCore

new MarkupsCore(viewer, options)

Extension that allows end users to draw 2D markups on top of 2D and 3D models.

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance used to operate on.

options*object

Same Dictionary object passed intoViewer3Dâs constructor.

markupDisableHotkeysboolean

Disables hotkeys for copy, cut, paste, duplicate, undo, redo and deselect.

markupToolClassAutodesk.Viewing.ToolInterface

Class override for input handling. Use it to override/extend default hotkeys and/or mouse/gesture input.

Methods

enterEditMode(layerId)

Enables mouse interactions and mobile device gestures over the Viewer canvas to create or draw markups.

Exit Edit mode by callingleaveEditMode().

See alsoshow()

Parameters

layerId*string

[optional] Identifier for the layer of markups to be edited. Example âLayer1â.

Returns

type

description

boolean

Returns true if editMode is active

leaveEditMode()

Exits Edit mode.

See alsoenterEditMode().

Returns

type

description

boolean

Returns true if Edit mode has been deactivated

toggle()

Toggle between visible markups, i.e., show() and hidden markups, i.e., hide().

show()

Enables loading of previously saved markups. Exit Edit mode by callinghide().

See alsoenterEditMode().

Returns

type

description

boolean

Whether it successfully entered view mode or not.

hide()

Removes any markup currently overlaid on the viewer. It exits Edit mode if it is active.

See alsoshow()

Returns

type

description

boolean

Whether it successfully left view mode or not.

clear()

Removes newly created markups in the current editing layer. Markups that were created in a specific layer will not be removed.

Markups should have been added while inenterEditMode().

generateData()

Returns an SVG string with the markups created so far. The SVG string can be reloaded usingloadMarkups().

Markups should have been added while inenterEditMode().

Returns

type

description

string

Returns an SVG element with all of the created markups in a string format.

changeEditMode(editMode)

Changes the active drawing tool. For example, from the Arrow drawing tool to the Rectangle drawing tool. Only applicable while inEdit Mode.

Supported values are:

newAutodesk.Viewing.Extensions.Markups.Core.EditModeArrow(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModeRectangle(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModeCircle(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModeCloud(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModeText(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModeFreehand(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModePolyline(MarkupsCoreInstance)

newAutodesk.Viewing.Extensions.Markups.Core.EditModePolycloud(MarkupsCoreInstance)

This function fires eventAutodesk.Viewing.Extensions.MarkupsCore.EVENT_EDITMODE_CHANGED.

Parameters

editMode*object

Object instance for the drawing tool

isNavigationAllowed()

Check whether a user can perform camera navigation operations on the current loaded model. While the extension is active, the user can still draw markups. Panning and zooming are only supported for orthographic cameras.

Returns

type

description

boolean

WhetherallowNavigation()can succeed.

allowNavigation(allow)

Enables click, tap, and swipe behavior to allow camera zoom and panning operations. It is only available inEdit mode.

Parameters

allow*boolean

Whether camera navigation interactions are active or not.

disableMarkupInteractions(disable)

Sets mouse interactions and mobile device gestures with markups. Only applicable inEdit mode.

Parameters

disable*boolean

true to disable interactions with markups; false to enable interactions with markups; default false.

copy()

Standard copy operation. Applies to any selected markup.
See alsocut()andpaste().

cut()

Standard cut operation. Applies to any selected markup, which gets removed from the screen at call time.
See alsocopy()andpaste().

paste()

Standard paste operation. This function will paste any previously copied or cut markup. Can be called repeatedly after a single copy or cut operation.
See alsocopy()andcut().

undo()

Will undo the previous operation.
The Undo/Redo stacks will track any change done to the existing markups.
See alsoredo()andisUndoStackEmpty().

redo()

Will redo any previously undo operation.
See alsoundo(),isRedoStackEmpty().

isUndoStackEmpty()

Returns true whenundo()produces no changes.

Returns

type

description

boolean

true if there are no changes to undo; false if there are changes to undo.

isRedoStackEmpty()

Returns true whenredo()produces no changes.

Returns

type

description

boolean

true if there are no changes to redo; false if there are changes to redo.

getId()

Helper function for generating unique markup ids.

Returns

type

description

number

getMarkup(id)

Returns a markup with the specified ID. Returns null when not found. The ID can be retrieved from the return value of getSelection().
See alsogetSelection().

Parameters

id*string

Markup identifier.

Returns

type

description

Autodesk.Viewing.Extensions.Markups.Core.Markup

Returns markup object.

selectMarkup(markup)

Selects or deselects a markup. A selected markup gets an overlayed UI that allows you to perform transformations such as resizing, rotations, and translations. To deselect a markup, send a null value.
See alsogetMarkup().

Parameters

markup*Autodesk.Viewing.Extensions.Markups.Core.Markup, null

The markup instance to select. Set the value to null to deselect a markup.

getSelection()

Returns the currently selected markup. A selected markup has a custom UI overlayed that allows you to perform resizing, rotations and translations.
See alsoselectMarkup().

Returns

type

description

Autodesk.Viewing.Extensions.Markups.Core.Markup, null

Returns selected markup object; null if no markup is selected.

deleteMarkup(markup, dontAddToHistory)

Deletes a markup from the canvas. Only applies while inEdit mode.

Parameters

markup*Autodesk.Viewing.Extensions.Markups.Core.Markup

Markup object.

dontAddToHistoryboolean

Whether delete action can beundone.

loadMarkups(markupString, layerId)

Loads data (SVG string) for all markups in a specified layer (layerId) to the Viewerâs canvas.

See alsounloadMarkups(), andhideMarkups().

Parameters

markupString*string

SVG string with markups. See alsogenerateData().

layerId*string

Identifier for the layer where the markup should be loaded to. Example âLayer1â.

Returns

type

description

boolean

Whether the markup string was able to be loaded successfully

revertLayer(layerId)

Revert any changes made to the specific layer.

See alsoloadMarkups()andenterEditMode().

Parameters

layerId*string

ID of the layer to revert any changes that were made to it.

Returns

type

description

boolean

true if the layer was unloaded, false if the layer was not unloaded.

unloadMarkups(layerId)

Removes markups from the DOM (Document Object Model). This is helpful for freeing up memory.

See alsoloadMarkups(),unloadMarkupsAllLayers(),clear(),hide(), andhideMarkups().

Parameters

layerId*string

ID of the layer containing all markups to unload (from the DOM).

Returns

type

description

boolean

Whether the operation succeeded or not.

unloadMarkupsAllLayers()

Removes all markups loaded so far. Great for freeing up memory.

See alsoloadMarkups(),unloadMarkups(),clear(),hide(), andhideMarkups().

hideMarkups(layerId)

Hides all markups in a specified layer. Note that hidden markups will not be unloaded. Use theshowMarkups()method to make them visible again; no additional parsing is required.

See alsoshowMarkups(),unloadMarkups(), andloadMarkups().

Parameters

layerId*string

ID of the layer containing all markups that should be hidden (in the DOM).

Returns

type

description

boolean

Whether the operation succeeded or not.

showMarkups(layerId)

Unhides a layer of hidden markups (hideMarkups()).

Parameters

layerId*string

ID of the layer containing all markups to unload (from the DOM).

Returns

type

description

boolean

Whether the operation succeeded or not.

Events

EVENT_EDITMODE_CHANGED

Fired whenever the drawing tool changes. For example, when the Arrow drawing tool changes into the Rectangle drawing tool.

EVENT_EDITMODE_ENTER

Fired when Edit mode has been enabled, which allows the end user to start drawing markups over the Viewer canvas.

EVENT_EDITMODE_LEAVE

Fired when Edit mode has been disabled, preventing the end user from drawing markups over the Viewer canvas.

EVENT_MARKUP_SELECTED

Fired when a drawn markup has been selected by the end user with a click command.

Properties

markupMarkup

The selected markup

EVENT_MARKUP_DRAGGING

Fired when a drawn markup is being dragged over the Viewer canvas.

EVENT_HISTORY_CHANGED

Fired whenever a new undo or redo action is available.

Properties

dataEventHistoryChangedData

The event data to identify the action and target

EVENT_EDITMODE_CREATION_BEGIN

Fired when a markup creation begins. For example, as soon as the user starts dragging with the mouse to draw an arrow on the screen.

EVENT_EDITMODE_CREATION_END

Fired when a markup has been created. For example, as soon as the user stops dragging and releases the mouse button to finish drawing an arrow on the screen

EVENT_MARKUP_DESELECT

Fired when a markup is no longer selected.

Properties

markupIdnumber

The id of the selected markup

EVENT_EDITFRAME_EDITION_START

The selected markup is being modified, i.e, resizing, rotating, moving around

EVENT_EDITFRAME_EDITION_END

The selected markup is no longer being modified


---

# MeasureExtension

MeasureExtension

new MeasureExtension(viewer, options)

Provides UI controls to perform distance and angle measurements for 2D and 3D models.

The extension id is:Autodesk.Measure

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Load the measure extension.

Returns

type

description

boolean

True if measure extension is loaded successfully.

unload()

Unload the measure extension.

Returns

type

description

boolean

True if measure extension is unloaded successfully.

getMeasurement(unitType, precision)

Get the current measurement in the measure tool.

Parameters

unitTypestring

Either: âdecimal-ftâ, âftâ, âft-and-decimal-inâ, âdecimal-inâ, âfractional-inâ, âmâ, âcmâ, âmmâ or âm-and-cmâ.

precisionnumber

precision index (0: 0, 1: 0.1, 2: 0.01, 3: 0.001, 4: 0.0001, 5: 0.00001). When units type is âftâ, âinâ or âfractional-inâ, then the precisions are 0: 1, 1: 1/2, 2: 1/4, 3: 1/8, 4: 1/16, 5: 1/32, 6: 1/64.

Returns

type

description

object, null

Object with properties of the current measurement, or null.

getMeasurementList(unitType, precision)

Get a list of all the measurements that are currently on the screen.

Parameters

unitTypestring

Either: âdecimal-ftâ, âftâ, âft-and-decimal-inâ, âdecimal-inâ, âfractional-inâ, âmâ, âcmâ, âmmâ or âm-and-cmâ.

precisionnumber

precision index (0: 0, 1: 0.1, 2: 0.01, 3: 0.001, 4: 0.0001, 5: 0.00001). When units type is âftâ, âinâ or âfractional-inâ, then the precisions are 0: 1, 1: 1/2, 2: 1/4, 3: 1/8, 4: 1/16, 5: 1/32, 6: 1/64.

Returns

type

description

Array.<object>

An array of measurement objects with properties of the measurement.

setMeasurements(measurements)

Restores existing measurements. Themeasurementsobject should be generated by either thegetMeasurementListor thegetMeasurementmethods.

Parameters

measurements*Array.<object>, object

An array of measurement objects

activate(mode, type)

Activates the tool and UI to start measuring.

Parameters

modestring

Either âdistanceâ, âangleâ, âareaâ (2D only), âarcâ (2D only), âcalibrateâ or âcustomâ. Default is âdistanceâ.

typestring

Custom measurement type. Required when mode is âcustomâ.

deactivate()

Deactivates measuring tool and UI.

Returns

type

description

boolean

setIsolateMeasure(enable)

When enabled, the Viewer will only render model parts that are included in measurements.

Parameters

enable*boolean

true to render only nodes being measured.

deleteAllMeasurements()

Delete all measurements.

deleteCurrentMeasurement()

Deletes the selected measurement.

setFreeMeasureMode(allow, useLastViewport)

Enable measuring on non snapped locations.

Parameters

allow*boolean

true to allow measuring on non snapped locations, otherwise false;

useLastViewport*boolean

override the free measurementâs viewport with a previously created measurementâs viewport.

isFreeMeasureMode()

Checks whether measuring can be performed from non snapped locations.

Returns

type

description

boolean

true is users can measure from any location.

```
viewer.loadExtension('Autodesk.Measure')

```


---

# MinimapExtension

MinimapExtension

Provides a 2d Minimap to show the view of the current document.

The extension id is:Autodesk.BIM360.Minimap

new MinimapExtension()

Examples

Methods

load()

Load the minimap extension.

Returns

type

description

boolean

True if minimap extension is loaded successfully.

unload()

Unload the minimap extension.

Returns

type

description

boolean

True if minimap extension is unloaded successfully.

onCameraChange(withTransition)

Occurs when camera changes

Parameters

withTransition*boolean

True if cameara changed with a transition.

destroyUI()

Destroys minimapâs UI

```
viewer.loadExtension('Autodesk.BIM360.Minimap')

```


---

# ModelBuilder

ModelBuilder

Class that implements the API for building models dynamically. An instance of this class can be obtained after the Promise returned byAutodesk.Viewing.Extensions.SceneBuilder#addNewModelis resolved.

new ModelBuilder(model, options)

The constructor is invoked automatically byAutodesk.Viewing.Extensions.SceneBuilder.

Parameters

model*Autodesk.Viewing.Model

The model this build works on

optionsobject

Options for the ModelBuilder

conserveMemoryboolean

Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.ModelBuilder#addMesh </en/docs/viewer/v7/reference/Extensions/ModelBuilder/#addMesh/>`_ is not available because a single mesh is shared among all of the fragments in the model.

Methods

isConservingMemory()

Returns

type

description

boolean

true when the model being manipulated is using the memory-optimized code path.

addGeometry(geometry, numFragments)

Add geometry to the model.

Parameters

geometry*THREE.BufferGeometry

The geometry to add. This can be null or undefined to allocate a geometry id without geometry.

numFragmentsnumber

The number of fragments you expect this geometry to be used in. Default is 1. This is used to prioritize placing geometry on the GPU. Geometry used by more fragments gets a higher priority.

Returns

type

description

number

The id of the added geometry, or 0 if there was an error.

changeGeometry(existingGeom, geometry, numFragments)

Change geometry in a model.

Parameters

existingGeom*number, THREE.BufferGeometry

The geometry or the id of the geometry to change

geometry*THREE.BufferGeometry

Geometry that replaces the existing geometry

numFragmentsnumber

The number of fragments using this geometry. If not given, then we will count the number in the model. This is used to prioritize placing geometry on the GPU. Geometry used by more fragments gets a higher priority.

Returns

type

description

boolean

True if the existing geometry is valid and the geometry was changed.

findGeometryFragments(geometry)

Find fragments using a specific geometry.

Parameters

geometry*number, THREE.BufferGeometry, Array.<(number|THREE.BufferGeometry)>

The geometry or id(s) of the geometry to use in the search

Returns

type

description

Array.<number>

An array with the fragment ids for all fragments that were using the geometry. Null is returned if any geometry is invalid.

removeGeometry(geometry)

Remove geometry from the model.

Parameters

geometry*number, THREE.BufferGeometry, Array.<(number|THREE.BufferGeometry)>

The geometry or id(s) of the geometry to remomve

Returns

type

description

boolean

True if all of the ids are valid and the geometry is removed.

addMaterial(name, material)

Add a material that can be used by a mesh in the model.

Parameters

name*string

The name used for the material. This name must not be used for an existing material in the model.

material*THREE.Material

The material to add. This material must not be used in the model.

Returns

type

description

boolean

True if the material was added.

changeMaterial(existingMaterial, material)

Replaces an existing material with another one.

Parameters

existingMaterial*string, THREE.Material

The material or name of the material to change. The material must be in the model.

material*THREE.Material

The material to replace the existing material. This material must not be used in the model.

Returns

type

description

boolean

True if the material is valid and the material was changed.

findMaterial(name)

Find a material

Parameters

name*string

The name of the material

findMaterialFragments(materials)

Return the fragments that are using materials.

Parameters

materials*string, THREE.Material, Array.<(string|THREE.Material)>

The materials or names of the materials to use in the search.

Returns

type

description

Array.<number>

An array with the fragment ids for all fragments that were using the materials. Null is returned if any material name is invalid or all of the materials were not removed.

removeMaterial(materials)

Remove a material from the model. The caller should dispose the material if needed.

Parameters

materials*string, THREE.Material, Array.<(string|THREE.Material)>

The materials or names of the materials to remove. All of the names must be used for materials in the model.

Returns

type

description

boolean

True if all of the names are valid and all of the materials are removed.

addMesh(mesh)

Add a fragment to the model using a mesh. Meshes can only be added to the model whenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis false. Note the following restrictions:

A mesh cannot be used multiple times.

The geometry for a mesh cannot be used in different models.

The material for a mesh cannot be used in different models.

Parameters

mesh*THREE.Mesh

The mesh to be added.

isLineboolean

Optional bool to mark line geometry

isWideLineboolean

Optional bool to mark wide line geometry

isPointboolean

Optional bool to mark point geometry

fragIdnumber

The fragment id for the mesh. This must not be defined when addMesh() is called and the Viewer sets this property to the new fragment id.

modeIdnumber

The id of the model. This must not be defined when addMesh() is called and the Viewer will set this to the id of the model for this ModelBuilder.

dbIdnumber

An optional object id for the mesh. Meshes with the same object id are selected as a unit. Internal tables are maintained to link fragments and dbIds. If a mesh is in the scene you shouldnât change this value direcly. CallAutodesk.Viewing.Extensions.ModelBuilder#changeFragmentsDbIdto change it to insure the tables are updated.

Returns

type

description

boolean

True if the mesh was added.

removeMesh(meshes)

Remove a mesh from the model. Meshes can only be removed from the model whenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis false.

Parameters

meshes*THREE.Mesh, Array.<THREE.Mesh>

The meshes to be removed.

Returns

type

description

boolean

True if the mesh was removed.

updateMesh(meshes, skipGeom, skipTransform)

Use this method to inform the Viewer when you directly update a mesh you added to the model. If you change a mesh directly without calling this method, it may not display properly. You donât need to call this if you use the ModelBuilder API to update a mesh.

Parameters

meshes*THREE.Mesh, Array.<THREE.Mesh>

The meshes that were changed.

skipGeomboolean

Set to true if the geometry in the meshes wasnât updated

skipTransformboolean

Set to true if the tranforms in the meshes werenât update

Returns

type

description

boolean

True if the viewer was updated

sceneUpdated(objectsMoved, skipRepaint)

Signal viewer that scene was modified.

Parameters

objectsMovedboolean

True if transforms or geometry was changed

skipRepaintboolean

True to skip repainting because of this change

addFragment(geometry, material, transform, bbox)

Add a fragment to a model. A fragment is the combination of a geometry, a material, and a transform.

Parameters

geometry*number, THREE.BufferGeometry

The geometry or the id of the geometry for the fragment. Use a falsey value if the geometry for the fragment isnât ready. If the geometry hasnât been added to the model, this method will add it. Geometry must not be used in a different model.

material*string, THREE.material

The material or the name of the material instance for the fragment. A material name must be used by a material in the model, but a material will be added to the model if it hasnât already.

transformTHREE.Matrix, Array.<number>

The transform for the fragment. Default is the identity transform. If an array is used it is a 4x3 matrix in column major order.

bboxTHREE.Box3, Array.<number>

Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. WhenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z.

Returns

type

description

number

The fragment id added or 0 if there was an error.

changeFragmentGeometry(fragment, geometry, transform, bbox)

Change the geometry and transform for a fragment.

Parameters

fragment*number, THREE.Mesh

The mesh or fragment id whose geometry is to be set.

geometry*number, THREE.BufferGeometry

The geometry or the id of the geometry for the fragment. Use a falsey value if the geometry for the fragment isnât ready. If the geometry hasnât been added to the model, this method will add it. Geometry must not be used in a different model.

transformTHREE.Matrix, Array.<number>

The transform for the fragment. If not present the transform isnât changed. If an array is used it is a 4x3 matrix in column major order.

bboxTHREE.Box3, Array.<number>

Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. WhenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z.

Returns

type

description

boolean

True if the geometry id is valid and the fragment is changed.

changeFragmentMaterial(fragment, material)

Change the material for a fragment.

Parameters

fragment*number, THREE.Mesh

The mesh or fragment id whose material is to be set.

material*string, THREE.material

The material or the name of the material for the fragment. A material name must be used by a material in the model, but a material will be added to the model if it hasnât been.

Returns

type

description

boolean

True if the material id is valid and the fragment is changed.

changeFragmentTransform(fragment, transform, bbox)

Change the transform for a fragment.

Parameters

fragment*number, THREE.Mesh

The mesh or fragment id whose material is to be set.

transform*THREE.Matrix, Array.<number>

The transform for the fragment. If an array is used it is a 4x3 matrix in column major order.

bboxTHREE.Box3, Array.<number>

[bbox] Bounding box for the fragment. Default is calculated from the geometry bounding box and the transform. WhenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis true then this argument is ignored and the default is used. If an array is used it contains the minimum x, y, z followed by the maximum x, y, z.

Returns

type

description

boolean

True if the fragId is valid and the transform was changed.

changeFragmentsDbId(fragments, dbId)

Change the dbId of one or more fragments

Parameters

fragments*number, THREE.Mesh, Array.<(number|THREE.Mesh)>

The meshes or ids of the fragments to be changed

dbId*number

The new dbId of the fragments. A 0 dbId will prevent an object from being selected. All fragments with the same dbId are selected as a single object. Changing the dbids on fragments will not change the display of objects that are already selected.

Returns

type

description

boolean

True if all of the fragment ids were valid and all of the fragments were changed.

removeFragment(fragments)

Remove fragments from the model

Parameters

fragments*number, THREE.Mesh, Array.<(number|THREE.Mesh)>

The meshes or ids of the fragments to be removed

Returns

type

description

boolean

True if all of the fragment ids were valid and all of the fragments were removed.

packNormals(geometry)

Pack normals for geometry. Utility method automatically used whenAutodesk.Viewing.Extensions.ModelBuilder#isConservingMemoryis true.

Parameters

geometry*THREE.BufferGeometry

Returns

type

description

THREE.BufferGeometry

The geometry argument is returned


---

# ModelStructureExtension

ModelStructureExtension

new ModelStructureExtension(viewer, options)

Adds a toolbar button for accessing the Model Browser panel.

Use itsactivate()method to open the Model Browser panel. The Model Browser is only available to 3D models.

The extension id is:Autodesk.ModelStructure

Autodesk.Viewing.GuiViewer3Dloads this extension by default.

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Invoked automatically when the extension is loaded.

unload()

Invoked automatically when the extension is unloaded.

onToolbarCreated(toolbar)

Invoked after the Toolbar UI gets created. Adds toolbar button.

Parameters

toolbar*Autodesk.Viewing.UI.ToolBar

toolbar instance.

activate()

Opens the Model Browser UI.

deactivate()

Closes the Model Browser UI.

isActive()

Returns

type

description

boolean

true when the panel is visible.

setModelStructurePanel(modelStructurePanel)

Sets the panel instance to open when clicking the toolbar button. Use the API to override the default panel with a custom one.

Parameters

modelStructurePanel*Autodesk.Viewing.UI.ModelStructurePanel

The model structure panel to use, or null.

Returns

type

description

boolean

True if the panel, or null, was set successfully; false otherwise.

restoreDefaultPanel()

Removes custom panel and restores the default one.

```
viewer.loadExtension('Autodesk.ModelStructure')

```


---

# NavToolsExtension

NavToolsExtension

new NavToolsExtension(viewer, options)

Adds toolbar buttons to Orbit, Pan and Dolly. It also adds camera interaction buttons for Fit to View, Focal Length and Roll

The extension id is:Autodesk.DefaultTools.NavTools

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate(mode)

Performs the corresponding button action.

Parameters

mode*string

one of the supported modes, see getModes().

deactivate()

Deactivates the current mode and activates the default viewerâs navigation tool.

Returns

type

description

boolean

true when deactivation is successful.

isActive(mode)

Checks whether a specific supported mode is currently active.

Parameters

mode*string

one of the supported modes.

Returns

type

description

boolean

true is the mode queried is currently active.

```
viewer.loadExtension('Autodesk.DefaultTools.NavTools')

```


---

# NPR

NPR

new NPR(viewer, options)

Provides UI controls for NPR settings

The extension id is:Autodesk.NPR

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.

options*Object

Not used.

Examples

Methods

onToolbarCreated()

Invoked by the viewer when the toolbar UI is available. Adds a button to the Settings panel.

openPanel()

Opens the NPR Render Options panel.

setParameter(param, value)

Changes post-processing setting parameters. The supported param/value combinations are:

âstyleâ: either âedgingâ, âcelâ, âgraphiteâ, âpencilâ ornullto turn post-processing off.

âedgesâ:boolean

âidEdgesâ:boolean

ânormalEdgesâ:boolean

âdepthEdgesâ:boolean

âbrightnessâ:Number

âcontrastâ:Number

âgrayscaleâ:boolean

âpreserveColorâ:boolean

âlevelsâ:Number

ârepeatsâ:Number

ârotationâ:Numberbetween 0 and 1, around circle (e.g. 0.5 == pi radians, 1.0 == 2*pi)

Fires eventRENDER_OPTION_CHANGED_EVENT.

Parameters

param*string

Either âstyleâ, âedgesâ, âidEdgesâ, ânormalEdgesâ, âdepthEdgesâ, âbrightnessâ, âcontrastâ, âgrayscaleâ, âpreserveColorâ, âlevelsâ, ârepeatsâ or ârotationâ.

value*

type depends on the specifiedparam.

```
viewer.loadExtension('Autodesk.NPR');

```


---

# PDFExtension

PDFExtension

Registers a FileLoader to enhanceviewer.loadModel()to allow loading of PDF files. The viewer will render a single page at a time.

The extension id is:Autodesk.PDF

new PDFExtension()

Examples

var viewer = new Autodesk.Viewing.Viewer3D(div,config3d);
viewer.start();
viewer.loadExtension(âAutodesk.PDFâ).then(function() {

// URL parameterpagewill override value passed to loadModel
viewer.loadModel(âpath/to/file.pdfâ, { page: 1 });

});

});

```
// Create Viewer instance and load PDF file on page 1

```


---

# PopoutExtension

PopoutExtension

Extension to popout the viewer into child windows

The extension id is:Autodesk.Viewing.Popout

new PopoutExtension(viewer, options)

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.

options*object

Not used.

Examples

Methods

load()

Extension interface method - loads the extension

Returns

type

description

boolean

unload()

Extension interface method - unloads the extension

Returns

type

description

boolean

popoutToChild(child, elementid, copyStyles, setupStyleObserver)

Use this to pop the viewer out to an existing window

Parameters

child*object

Already open window created with window.open()

elementid*string

The dom element id in the child where the viewer will be moved to

copyStylesboolean

Flag to copy the styles from the current window to the child. Set this to false if you intend to copy the styles yourself

setupStyleObserverboolean

Style observers clone dynamically added  (from extensions loading) into child. This is required for extensions to work. Set this to false if you intend to set up the cloning with mutation observers yourself

popoutToBlank(options, onBeforeUnload, onClose, onBlocked)

Use this to pop the viewer out to a new blank window

Parameters

optionsobject

windowFeature options

onBeforeUnloadfunction

Called before the popout window is unloaded

onClosefunction

Called when popout window is closed

onBlockedfunction

Called when popup blockers block creating child window

popin()

Closes the popout window and moves the viewer back to the main window

```
viewer.loadExtension('Autodesk.Viewing.Popout');

```


---

# PropertiesManagerExtension

PropertiesManagerExtension

new PropertiesManagerExtension(viewer, options)

Use itsactivate()method to open the Properties UI.

The extension id is:Autodesk.PropertiesManager

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Invoked when the extension gets loaded.

Returns

type

description

boolean

true when the extension loaded successfully.

unload()

Invoked when the extension gets unloaded.

activate()

Opens the Properties UI.

deactivate()

Closes the Properties UI.

isActive()

Returns

type

description

boolean

true is the properties panel is open.

setPanel(propertyPanel)

Overrides the property panel instance.

Parameters

propertyPanel*

Returns

type

description

boolean

True if the panel or null was set successfully, and false otherwise.

setDefaultPanel()

Resets the panel to its default instance.

getPanel()

Gets the property panel instance.

Returns

type

description

object

The panel instance.

```
viewer.loadExtension('Autodesk.PropertiesManager')

```


---

# RollCameraExtension

RollCameraExtension

Provides UI controls to perform rotation of camera view.

The extension id is:Autodesk.BIM360.RollCamera

new RollCameraExtension()

Examples

Methods

load()

Load the roll camera extension.

unload()

Unload the roll camera extension.

onToolbarCreated(toolbar)

Invoked by the viewer when the toolbar UI is available.

Parameters

toolbar*Autodesk.Viewing.UI.ToolBar

toolbar instance.

roll(clockwise)

Roll the camera 90 degrees.

Parameters

clockwise*boolean

True to rotate clockwise, false to rotate counter clockwise.

```
viewer.loadExtension('Autodesk.BIM360.RollCamera')

```


---

# SceneBuilder

SceneBuilder

Scene Builder extension provides an API for building scenes without loading them from a URL.

The extension id is:Autodesk.Viewing.SceneBuilder

new SceneBuilder(viewer, options)

Parameters

viewer*Autodesk.Viewing.Viewer3D

The viewer instance loading the extension

optionsobject

Default options used when calling addNewModel

conserveMemoryboolean

Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.SceneBuilder#addMesh <#fixMe/>`_ is not available because a single mesh is shared among all of the fragments in the model.

Examples

Methods

load()

Extension interface method - loads the extension

Returns

type

description

boolean

unload()

Extension interface method - unloads the extension MethodAutodesk.Viewing.Extensions.SceneBuilder#addNewModelwill fail if the extension is unloaded.

addNewModel(options)

Add a new empty model into the scene. The model can be manipulated only by its associated ModelBuilder instance.

Parameters

optionsobject

Options combined with the options used  when the extension is loaded with loadExtension(). The combined options are put in the loadOptions property in the object returned by model.getData().

conserveMemoryboolean

Set to true to turn on memory conservation mode. In this mode [addMesh()]`Autodesk.Viewing.Extensions.SceneBuilder#addMesh <#fixMe/>`_ is not available because a single mesh is shared among all of the fragments in the model.

createWireframeboolean

Set to true to turn on edge generation for geometry.

Returns

type

description

Promise (ModelBuilder)

A Promise that resolves with a ModelBuilder instance for the new model.

```
viewer.loadExtension('Autodesk.Viewing.SceneBuilder');

```


---

# SectionExtension

SectionExtension

new SectionExtension(viewer, options)

The SectionExtension provides ways to cut the geometry using planes or a cube. The extension adds a toolbar button to access the feature.

The extension id is:Autodesk.Section

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

toggle()

Toggles activeness of section planes.

Returns

type

description

boolean

Whether the section plane is active or not.

getSectionStyle()

Returns the current type of plane that will cut-though the geometry.

Returns

type

description

null, string

Either âXâ or âYâ or âZâ or âBOXâ or null.

setSectionStyle(style, preserveSection)

Sets the Section plane style.

Parameters

style*string

Accepted values are âXâ, âYâ, âZâ and âBOXâ (in Caps)

preserveSectionboolean

Whether sending the current style value resets the cut planes.

getState(viewerState)

Gets the extension state as a plain object. Invoked automatically by viewer.getState()

Parameters

viewerState*object

Object to inject extension values.

restoreState(viewerState)

Restores the extension state from a given object. Invoked automatically by viewer.restoreState()

Parameters

viewerState*object

Viewer state.

Returns

type

description

boolean

True if restore operation was successful.

setSectionBox(box)

Set a section box around the passed in THREE.Box3. This method will also enable the section tool.

Parameters

box*THREE.Box3

used to set the section box.

setSectionPlane(normal, point, enableRotationGizmo)

Place a section plane on the Intersection. This method will also enable the section tool.

Parameters

normal*THREE.Vector3

plane normal.

point*THREE.Vector3

position to place the plane.

enableRotationGizmo*

activate(mode)

Activates a section plane for user to interact with. It performs the same action as the UI button.

Parameters

mode*string

Accepted values are âxâ, âyâ, âzâ and âboxâ (in lowercase)

Returns

type

description

boolean

true if the activation was successful.

true if the activation was successful.

deactivate(keepCutPlanes)

Removes the section plane/box from the 3D canvas.

Parameters

keepCutPlanes*

keep existing cut planes when deactivating the tool. Default is false.

Returns

type

description

boolean

returns true if deactivated, false otherwise.

returns true if deactivated, false otherwise.

```
viewer.loadExtension('Autodesk.Section')

```


---

# SnappingExtension

SnappingExtension

Utility extension that provides access to theAutodesk.Viewing.Extensions.Snapping.Snappertool.

The extension id is:Autodesk.Snapping

new SnappingExtension(viewer, options)

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

load()

Load the extension.

Returns

type

description

Promise

that resolves when dependent extension finishes loading.

unload()

Unloads the extension. It does not unload dependent extensions.

Returns

type

description

boolean

Always returns true

activate()

Unused method.

Returns

type

description

boolean

Always returns true

deactivate()

Unused method.

Returns

type

description

boolean

Always returns false

```
viewer.loadExtension('Autodesk.Snapping')

```


---

# SplitScreenExtension

SplitScreenExtension

new SplitScreenExtension(viewer, options)

This extension subdivides the LMV canvas into between 2 and 4 (inclusive) separate subcanvases.

The extension id is:Autodesk.SplitScreen

For each sub-canvas, you can specify a separate model filter function to control in which canvases each model shall appear. The canvases are numbered as follows: 0  1 2  3

By default (no modelFilter), all models are rendered to each subcanvas. Overlays are rendered into both canvases (unless selection highlighting proxies - which are associated with models)

Limitations: Most core features of LMV keep working (2D/3D render, mouse-over, selection, directional zoom etc.). However, there are currently some known limitations/tradeoffs:

All canvases must use the same camera. Overcoming this requires to introduce a separate scene graph evaluation too.

Subcanvas configuration is currently limited to subcanvases with the same aspect ratio. Extending that will (among others) require support for separate cameras.

ZoomToolExtension, SectionTool, and Measure tool are disabled SplitScreen (we hide the UI)

GroundShadow is supported, but doesnât apply model filter yet when refreshing the shadow

GroundReflection in SplitScreen is not supported yet.

We currently use only a single background for both. This is hardly noticeable for discreet backgrounds like the AEC default or fixed colors, but may disturb when using more detailed environments.

Parameters

viewer*Viewer3D

Viewer instance

optionsobject

viewportsArray.<?Autodesk.Viewing.Extensions.SplitScreenExtension~modelFilterFunction>

Filter functions that returns true for models to be rendered for the viewport at that index. Falsy values render everything.

Examples

viewports: [
function(id) { return id === 1; },
function(id) { return id !== 1; }
]
};
viewer.loadExtension(âAutodesk.SplitScreenâ, options);

```
var options = {

```


---

# ViewCubeUi

ViewCubeUi

new ViewCubeUi(viewer, options)

Create the UI for the view cube.

The extension id is:Autodesk.ViewCubeUi

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.

options*object

Not used.

Examples

Methods

setVisible(show)

Show or hide the view cube element. This also applies to the home button.

Parameters

show*boolean

If set to false, the view cube and the home button will become invisible.

showTriad(show)

Show the x,y,z axes of the view cube.

Parameters

show*boolean

if set to true, the view cube axes will be shown.

setViewCube(face)

Set the face of ViewCube and apply camera transformation according to it.

Parameters

face*string

The face name of ViewCube. The name can contain multiple face names, the format should be"[front/back],[top/bottom],[left/right]".

Examples

displayHomeButton(show)

Hides the Home button next to the ViewCube.

Parameters

show*boolean

displayViewCube(display, updatePrefs)

Display the view cube. This will not effect the home button.

Parameters

display*boolean

if set to false the view cube element will be invisible

updatePrefs*boolean

update the view cube preference

localize()

Localize the view cube

refreshCube()

Refresh the view cube

```
viewer.loadExtension('Autodesk.ViewCubeUi');

```

```
viewer.setViewCube('front top right');
 viewer.setViewCube('bottom left');
 viewer.setViewCube('back');

```


---

# ViewerSettingsExtension

ViewerSettingsExtension

new ViewerSettingsExtension(viewer, options)

Use itsactivate()method to open the Settings UI.

The extension id is:Autodesk.ViewerSettings

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Examples

Methods

activate()

Opens the Settings UI.

deactivate()

Closes the Settings UI.

```
viewer.loadExtension('Autodesk.ViewerSettings')

```


---

# WireframesExtension

WireframesExtension

Provides the ability of rendering the model in wireframe mode. The method implemented is not very performant, so itâs best to avoid using it with large models.

The extension id is:Autodesk.Viewing.Wireframes

new WireframesExtension()

Examples

Methods

activate()

Enters wireframe mode.

deactivate()

Exits wireframe mode.

showSolidMaterial(show)

Whether to replace the standard materials with a solid one, or not.

Parameters

show*boolean

showLines(show)

Whether to render line edges or not.

Parameters

show*boolean

setSolidMaterial(material)

Replaces the solid material.

Parameters

material*THREE.Material

setLinesMaterial(material)

Replaces the line material.

Parameters

material*THREE.Material

setLightPreset(name)

Specifies the light preset to use when wireframe mode is activated.

Parameters

name*string

the name of the light preset

```
viewer.loadExtension('Autodesk.Viewing.Wireframes')

```


---

# ZoomWindow

ZoomWindow

Extends the dolly (zoom) button on the toolbar with a tool for end users to specify a rectangular section for the camera to zoom into and adjust accordingly.

The extension id is:Autodesk.Viewing.ZoomWindow

new ZoomWindow()

Examples

Methods

activate(mode)

Activates either ZoomWindow or dolly/zoom tool.

Parameters

modestring

Either âzoomwindowâ or âdollyâ

deactivate()

Deactivates the tool and resets the navigation tool.

```
viewer.loadExtension('Autodesk.Viewing.ZoomWindow')

```


---

# Snapper

Snapper

new Snapper(viewer, options)

A tool that lets users attach pointer events to vertices and edges. It supports 2D and 3D models.

Parameters

viewer*Viewer3D

Viewer instance

options*object

Configurations for the extension

Methods

isActive()

Returns

type

description

boolean

true when the tool is active

activate()

Starts intercepting pointer events. Invoked automatically by theToolController.

deactivate()

Stops intercepting pointer events. Invoked automatically by theToolController.

getSnapResult()

Returns

type

description

SnapResult

The snapping status of the last pointer event performed.

isSnapped()

Checks whether the toolâs last update resulted on a snap.

Returns

type

description

boolean

true when the last pointer event got snapped.

snapping3D(result)

3D Snapping

Parameters

result*

Result of Hit Test.

extractLineGeometry(edge, geometry)

Get Edge geometry for the case that the hittest result contained a 3D lines. For this case, we have no Face3, so that faceSnapping and edgeSnapping donât work.

Parameters

edge*Object

{a, b} with vertex indices a,b of lineStart/lineEnd vertex

geometry*GeometryBuffer

Returns

type

description

THREE.Geometry, THREE.BufferGeometry

Geometry with simple line

faceIsCurved(face)

Checks if the given geometry is curved

Parameters

face*THREE.BufferGeometry

The geometry

Returns

type

description

boolean

True if the any of the faces composing the geometry is curved

snapping2D(hitResult, options)

Snap to a 2D model.

Parameters

hitResult*object

a result of a ray intersection.

optionsobject

Options object.

enumSegmentsfunction

Enumerates all segments within a given bbox in model-space.


---

# SnapResult

SnapResult

new SnapResult()

Encapsulates the result of a Snap operation performed by theSnapper.

Methods

clear()

Resets the object to its non-snapping state.

copyTo(destiny)

Copies the current state of the object into another.

Parameters

destiny*SnapResult

target for the copy operation.

clone()

Creates a new instance and copies the current state into it.

Returns

type

description

SnapResult

isEmpty()

Returns

type

description

boolean

true only when snapping information is available.

getFace()

Gets the snapped face, when available.

getEdge()

Gets the snapped edge, when available.

getVertex()

Gets the snapped vertex, when available.

getGeometry()

Gets the snapped element, which differs depending on what kind of element it was snapped to, seeSnapType.


---

# InstanceTree

InstanceTree

new InstanceTree(nodeAccess, objectCount, maxDepth)

Parameters

nodeAccess*

objectCount*

maxDepth*

Methods

isNodeHidden(dbId)

Whether a node id is hidden.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

boolean

isNodeVisibleLocked(dbId)

Whether a node idâs visiblitly is locked.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

boolean

isNodeExplodeLocked(dbId)

Whether a node idâs explode is locked.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

boolean

getNodeType(dbId)

Gets the type associated with the node, such as assmebly, layer, model, geometry, etc.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

number

one ofNODE_TYPE

isNodeSelectable(dbId)

Whether the node is a selectable entity.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

boolean

getNodeParentId(dbId)

Gets the database id of the nodeâs parent.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

number

getRootId()

Gets the modelâs root database id.

Returns

type

description

number

getNodeName(dbId, includeCount)

Gets the name associated to the id.

Parameters

dbId*number

The nodeâs database id

includeCount*boolean

True if must include count

Returns

type

description

string

getChildCount(dbId)

Get number of children under the specified id.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

number

getFragmentCount(dbId)

Get number of fragments under the specified id.

Parameters

dbId*number

The nodeâs database id

Returns

type

description

number

getNodeBox(dbId, dst)

Sets the bounding box values for a particular id on the 2nd argument provided. There is no return value.

Parameters

dbId*number

The nodeâs database id

dst*Float32Array

An array holding 6 number values: (min-x, min-y, min-z, max-x, max-y, max-z)

enumNodeFragments(node, callback, recursive)

Parameters

node*number

The id of a node.

callback*Autodesk.Viewing.Private.InstanceTree~onEnumNodeFragments

The function that will be called for each fragment. Note that if the callback function returns a truthy value, a loop over the fragments and child nodes will be interrupted and the callback result will be forwarded back to the caller.

recursiveboolean

Whether the callback function gets called for child nodes, too.

enumNodeChildren(node, callback, recursive)

Parameters

node*number

The id of a node.

callback*Autodesk.Viewing.Private.InstanceTree~onEnumNodeChildren

The function that will be called for each child node. Note that if the callback function returns a truthy value, a loop over the child nodes will be interrupted and the callback result will be forwarded back to the caller.

recursiveboolean

Whether the callback function gets called for indirect child nodes, too.

search(text)

Search the tree for nodes whose names match the given string.

Parameters

text*string

The search term (not case sensitive).

Returns

type

description

Array.<number>

The dbIds of all nodes in the tree matching the search text.

The dbIds of all nodes in the tree matching the search text.


---

# Preferences

Preferences

Application preferences.

Optionally uses web storage.

Each preference value can have tags associated to them. Developer supported tags are:

âignore-producerâ

âno-storageâ

âshared-storageâ

â2dâ

â3dâ

Use tag âignore-producerâ in extensions to avoid having developer-defined render settings overridden by the loaded file.

Use tag âno-storageâ in extensions to avoid having User Preferences (from Settings Panel) override default or developer-defined preferences. Useful for render settings.

Use tag âshared-storageâ to always store the preference in a shared storage instead of the current profile storage. This is useful for preferences that should be shared across different storage profiles.

Preferences may apply to all model types, only 2D models (with tag â2dâ) or 3D models only (with tag â3dâ).

new Preferences(options)

Parameters

options*object

Contains configuration parameters used to do initializations.

localStorageboolean

Whether values get stored and loaded back from localStorage. Defaults totrue.

prefixstring

A string to prefix preference names in web storage. Defaults to'Autodesk.Viewing.Preferences.'.


---

# PropDbLoader

PropDbLoader

Per model property database interface, talks to the worker thread behind the scenes.

new PropDbLoader(sharedDbPath, model, eventTarget)

Parameters

sharedDbPath*

model*

eventTarget*

Methods

getAttributeDefinitions(force)

Gets a list of all available attributes in the property database

Parameters

forceboolean

fetch the attribute definitions afresh (and update the cache)

Returns

type

description

Promise ({category: string, dataTypeContext: (string|undefined), description: (string|undefined), flags: number, name: string, precision: number, propertyHash: string}[])

getProperties(dbId, onSuccess, onError)

Gets the properties for an ID.

Parameters

dbId*number

The database identifier.

onSuccessCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

getProperties2(dbId, onSuccess, onError, options)

Gets the properties for an ID. New version of getProperties() that avoids loading of externalId table unless really needed.

Parameters

dbId*number

The database identifier.

onSuccessCallbacks#onPropertiesSuccess

Callback for when the properties are fetched.

onErrorCallbacks#onGenericError

Callback for when the properties are not found or another error occurs.

optionsobject

needsExternalIdboolean

If true, we enforce loading of externalIDs if necessary. ExternalIds may significantly increase memory consumption and should only be loaded if unavoidable.

getBulkProperties(dbIds, propFilter, onSuccess, onError, ignoreHidden)

Bulk property retrieval with property name filter.

Parameters

dbIds*Array.<number>

array of object dbIds to return properties for.

propFilterobject

array of property names to retrieve values for. If empty, all properties are returned.

onSuccess*function

Callback function for when results are ready.

onError*function

Callback function for when something went wrong.

ignoreHiddenboolean

true to ignore hidden properties.

getBulkProperties2(dbIds, options, onSuccess, onError)

Bulk property retrieval with property name filter.

Parameters

dbIds*Array.<number>

array of object dbIds to return properties for.

optionsobject

propFilterArray.<string>

array of property names to retrieve values for. If empty, all properties are returned.

categoryFilterArray.<string>

array of category names to retrieve values for. If empty, all properties are returned.

ignoreHiddenboolean

true to ignore hidden properties.

needsExternalIdboolean

If true, it is ensured that externalId table is loaded before doing the property query.

onSuccess*function

Callback function for when results are ready.

onError*function

Callback function for when something went wrong.

getPropertySet(dbIds, options, onSuccess, onError)

Retrieves properties related to the specified dbIds. The results object that is passed into the onSuccess callback contains the displayName and displayCategory separated by a â/â as the key and all of the related properties as the entryâs value. The results can be used to create a newPropertySetinstance.

Parameters

dbIds*Array.<number>

array of object dbIds to return properties for.

optionsObject

propFilterArray.<string>

array of property names to retrieve values for. If empty, all properties are returned.

ignoreHiddenboolean

true to ignore hidden properties.

needsExternalIdboolean

If true, it is ensured that externalId table is loaded before doing the property query.

onSuccess*function

Callback function for when results are ready.

onError*function

Callback function for when something went wrong.

executeUserFunction(code, userData)

Allows executing user supplied function code on the worker thread against thePropertyDatabaseinstance. The returned value from the supplied function will be used to resolve the returned Promise. The function must be nameduserFunction.

Parameters

code*function, string

Function takes 1 argument, thePropertyDatabaseinstance.

userData*

A value that will get passed to thecodefunction when run in the property worker context. it needs to be serializable.

Returns

type

description

Promise

Resolves with the return value of user function.

Resolves with the return value of user function.

Examples

This example, however, only works on non-minfied/non-uglified code. Minification or other
obfuscation techniques that change the function name will cause an error, with the userFunction
not found. In that cases, a string must be used.

getLoadProgress()

Estimated load progress in percent.

Returns

type

description

number

in the range 0..100

isLoadDone()

Returns true if loading is finished (either with success or with error)

Returns

type

description

boolean

```
function userFunction(pdb, userData) {
       const dbId = 1;
       pdb.enumObjectProperties(dbId, function(propId, valueId) {
             // do stuff
       });
       return 42 * userData; // userData will be 2 in this example
  }
  executeUserFunction(userFunction, 2).then(function(result) {
       console.log(result); // result === 84 === 42 * 2
  })

```

```
await executeUserFunction('function userFunction(pdb, userData) { ... }');

```


---

# ViewerPreferences

ViewerPreferences

Viewer preferences.

extends Autodesk.Viewing.Private.Preferences

new ViewerPreferences(viewer, options)

Parameters

viewer*Autodesk.Viewing.Viewer3D

Viewer instance.

options*object

Contains configuration parameters used to do initializations.

localStorageboolean

Whether values get stored and loaded back from localStorage. Defaults totrue.

prefixstring

A string to prefix preference names in web storage. Defaults to'Autodesk.Viewing.ViewerPreferences.'.


---

# ErrorCodes

ErrorCodes

Error code constants These constants will be used inCallbacks#onGenericErrorfunctions.

Constants

UNKNOWN_FAILURE

An unknown failure has occurred.

type

type

number

BAD_DATA

Bad data (corrupted or malformed) was encountered.

type

type

number

NETWORK_FAILURE

A network failure was encountered.

type

type

number

NETWORK_ACCESS_DENIED

Access was denied to a network resource (HTTP 403)

type

type

number

NETWORK_FILE_NOT_FOUND

A network resource could not be found (HTTP 404)

type

type

number

NETWORK_SERVER_ERROR

A server error was returned when accessing a network resource (HTTP 5xx)

type

type

number

NETWORK_UNHANDLED_RESPONSE_CODE

An unhandled response code was returned when accessing a network resource (HTTP âeverything elseâ)

type

type

number

BROWSER_WEBGL_NOT_SUPPORTED

Browser error = webGL is not supported by the current browser

type

type

number

BAD_DATA_NO_VIEWABLE_CONTENT

There is nothing viewable in the fetched document

type

type

number

BROWSER_WEBGL_DISABLED

Browser error = webGL is supported, but not enabled

type

type

number

BAD_DATA_MODEL_IS_EMPTY

There is no geometry in loaded model

type

type

number

UNSUPORTED_FILE_EXTENSION

The extension of the loaded file is not supported

type

type

number

VIEWER_INTERNAL_ERROR

Viewer error: wrong or forbidden usage of the viewer

type

type

number

WEBGL_LOST_CONTEXT

WebGL error while loading a model, typically due to IE11 limitations

type

type

number

LOAD_CANCELED

Viewer error because loading a resource was canceled

type

type

number


---

# ProfileSettings

ProfileSettings

ProfileSettings are used to set the viewerâs profile.

To generate a profile from the supplied profile settings, please referenceAutodesk.Viewing.Profile. To set the viewerâs profile, useviewer.setProfile(profile).

Properties

clonefunction

This function is used to clone an existing ProfileSetting.

Constants

Default

Default profile settings. It uses the preferences described inAutodesk.Viewing.DefaultSettings. The following preferences will be persisted: alwaysUsePivot, zoomTowardsPivot, reverseHorizontalLookDirection, reverseVerticalLookDirection, orbitPastWorldPoles, clickToSetCOI, ghosting, optimizeNavigation, ambientShadows, antialiasing, groundShadows, groundReflections, firstPersonToolPopup, bimWalkToolPopup, swapBlackAndWhite, openPropertiesOnSelect, reverseMouseZoomDir, leftHandedMouseSetup, wheelSetsPivot

type

type

ProfileSettings

AEC

AEC profile settings. It inherits the settings fromAutodesk.Viewing.ProfileSettings.Default. The following preferences differ from the Default settings: { edgeRendering: true, // on desktop, false on mobile. lightPreset: âBoardwalkâ, envMapBackground: true }

type

type

ProfileSettings

Fluent

Design Collaboration profile settings. Inherits the settings fromAutodesk.Viewing.ProfileSettings.AEC. The following preferences differ from the AEC settings: { reverseMouseZoomDir: true, wheelSetsPivot: true, alwaysUsePivot: true, enableCustomOrbitToolCursor: false }

type

type

ProfileSettings

Navis

Navisworks profile settings. Inherits the settings fromAutodesk.Viewing.ProfileSettings.AEC. The following preferences differ from the AEC settings: { bimWalkToolPopup: false, bimWalkNavigatorType: âaecâ, defaultNavigationTool3D: âextractor_definedâ }

type

type

ProfileSettings


---

# onSetGlobalManager

onSetGlobalManager

Classes can override this method to pass the instance to other objects See DockingPanel.js for an example

Parameters

globalManager*GlobalManager

GlobalManager instance


---

# SearchResults

SearchResults

Parameters

parent*HTMLElement

HTMLElement where the search result will be inserted

excludeRoot*boolean

Flag indicating whether to exclude the root in the search

container*GuiViewer3D, HTMLElement

Viewer container element


---

# create

create

Initialize the view cube and the home button. This method is called when the extension is loaded.


---

# setViewType

setViewType

Set the viewCube view type.

Parameters

viewType*string

1 for orthographic, 2 for perspective, 3 for orthoFaces


---

# showCompass

showCompass

Parameters

showboolean

show the compass


---

# setCompassRotation

setCompassRotation

Parameters

radiansnumber

// Angle of north in radians wrt front


---

# LMV_VIEWER_VERSION

LMV_VIEWER_VERSION

Contains the Viewerâs version.


---

# LMV_THIRD_PARTY_COOKIE

LMV_THIRD_PARTY_COOKIE

When true, requests to APS are authenticated with a cookie. When false, requests to APS are authenticated with an Authentication header. When undefined, the viewer will first try authentication via cookie, if that doesnât work it will fallback to using an Authentication header.


---

# LMV_VECTOR_PDF

LMV_VECTOR_PDF

When true, the viewer will favor loading the PDF file over the Leaflet derivative, ignoring the manifest value fortotalRasterPixels. A true value will take precedence overLMV_RASTER_PDF.


---

# LMV_RASTER_PDF

LMV_RASTER_PDF

When true, the viewer will favor loading the Leaflet derivative over the PDF file, ignoring the manifest value fortotalRasterPixels. WhenLMV_RASTER_PDFis true, this value is ignored.


---

# AttributeType

AttributeType

Numeric values and their meanings associated toPropertyResult.type.


---

# PropertyDatabase

PropertyDatabase

new PropertyDatabase(dbjsons)

The Property Database contains property information for each part of a model. The data is read-only, since it has been packed to optimize memory footprint. Itâs implemented as an Entity-Atribute-Value (EAV) set of tables. LMV keeps the PropertyDatabase in a browser worker thread to prevent compute-intensive methods to block the main browser UI thread. Words âAttributeâ and âPropertyâ are use interchangeably.

Parameters

dbjsons*

Properties

enumObjectProperties

Iterates over all properties for a given database id and invokes the supplied callback function.

getPropertiesSubsetWithInheritance

Given an object ID, returns the corresponding value IDs for the given list of attribute Ids. Takes into account instance_of inheritance of properties.

Methods

getObjectCount()

Obtains the number of database ids (dbIds) available. These ids range betwee 1 (inclusive) up to getObjectCount() (exclusive).

Returns

type

description

number

getAttrValue(attrId, valId, integerHint)

Obtains the actual value of a property.

Parameters

attrId*number

The attribute id

valId*number

The value id

integerHintboolean

If true the return value will be casted to integer.

Returns

type

description

getObjectProperties(dbId, propFilter, ignoreHidden, propIgnored)

Obtains all properties for a given database id.

Parameters

dbId*number

The database id

propFilterArray.<string>

Array of property names to return values for. Use null for no filtering.

ignoreHiddenboolean

true to ignore hidden properties.

propIgnoredArray.<string>

Array of property names to not include in the return value.

Returns

type

description

object

consisting of attributesname,dbId,propertiesandexternalId.

getExternalIdMapping(extIdFilter)

Obtains a map between each database id (dbId) and their corresponding external-id. The external-id is the identifier used by the source file. Example: A translated Revit file has a wall with dbId=1, but in Revit (desktop application) the identifier of that wall is âWall-06-some-guid-hereâ.

Parameters

extIdFilterArray.<number>

Limits the result to only contain the ids in this array.

Returns

type

description

object

map from dbId into external-id.

getSearchTerms(searchText)

Given a text string, returns an array of individual words separated by white spaces. Will preserve white spacing within double quotes.

Parameters

searchText*string

Text to search

bruteForceFind(propertyName)

Given a property name, it returns an array of ids that contain it.

Parameters

propertyName*string

Property name

getLayerToNodeIdMapping()

Specialized function that returns: { âlayer-name-1â: [id1, id2, â¦, idN], âlayer-name-2â: [idX, idY, â¦, idZ], â¦ }

getAttributeDef(attrId)

Unpacks an attribute value into all available components.

Parameters

attrId*number

The attribute id.

Returns

type

description

object

containingname,category,dataType,dataTypeContext,description,displayNameandflags.

enumAttributes(cb)

Invokes a callback function for each attribute-id in the model.

Parameters

cb*function

Callback invoked

Examples

findLayers()

Iterates over the property database and finds all layers.

Returns

type

description

object

enumObjects(cb, fromId, toId)

Iterates over all database ids and invokes a callback function.

Parameters

cb*function

callback function. Receives a single parameter: the database-id. Have the function return true to abort iteration.

fromId*number

starting id (inclusive)

toId*number

end id (exclusive)

attributeHidden(attrId)

Checks whether an attribute is hidden or not.

Parameters

attrId*number

The attribute id.

Returns

type

description

boolean

true if the attribute is a hidden one.

true if the attribute is a hidden one.

_ignoreAttribute(propertyFilter, attrId)

Checks whether an attribute must be excluded from Diff comparison.

Parameters

propertyFilter*Object

A key-value pair of category and property names to ignore from Diff

attrId*number

The attribute id.

numberOfAttributes()

Returns count of the number of attributes

Returns

type

description

number

numberOfValues()

Returns count of the number of values

Returns

type

description

number

```
pdb.enumAttributes(function(attrId, attrDef) {
        // attrDef is an object
        if (attrDef.name === 'name') {
            return true; // return true to stop iteration.
        }
   })

```


---

# FeatureFlags

FeatureFlags

Static class that manages feature flags. Feature flags are used to enable or disable certain features of the viewer. After initialization, the flags become immutable.

new FeatureFlags()

Examples

Methods

set(name, value)

Sets the value of a given feature flag. If the flag does not exist, nothing happens.

Parameters

name*string

Feature flag identifier

value*boolean

New value of the feature flag

isEnabled(name)

Returns whether a given feature flag is enabled.

Parameters

name*string

Feature flag identifier

Returns

type

description

boolean, undefined

Feature flag value or undefined if the flag does not exist.

print()

Prints all public feature flags and their values to the console

```
FeatureFlags.set('EXAMPLE_FEATURE', true);

```


---

# NavToolsConfig

NavToolsConfig

Configuration object for the navigation tools

Properties

dollyScrollScalenumber

The dolly (zoom) scale of the scroll wheel which is used to calculate the camera distance. The default is set to 0.6.

dollyDragScalenumber

The dolly (zoom) scale for the zoom tool which is used to calculate the camera distance. The default is set to 100.


---

# InitOptions

InitOptions

Properties

envstring

Can beAutodeskProduction(default),AutodeskStaging, orAutodeskDevelopment.

apistring

Can be undefined (default), usestreamingV2(SVF2) orderivativeV2(SVF) for US data center,derivativeV2_EUfor European data center, andstreamingV2_AUSorderivativeV2_AUSfor Australian data center

getAccessTokenfunction

A function that provides an access token asynchronously. The function signature isgetAccessToken(onSuccess), where onSuccess is a callback that getAccessToken function should invoke when a token is granted, with the token being the first input parameter for the onSuccess function, and the token expire time (in seconds) being the second input parameter for the function. Viewer relies on both getAccessToken and the expire time to automatically renew token, so it is critical that getAccessToken must be implemented as described here.

languagestring

Preferred language code as defined in RFC 4646, such asen,de,fr, etc. If no language is set, viewer will pick it up from the browser. If language is not as defined in RFC, viewer will fall back toenbut the behavior is undefined.

logLevelnumber

Specifies which types of messages will be logged into the console. Values are: 5 Debug, 4 Logs, 3 Info, 2 Warnings, 1 Errors, 0 None. Defaults to (1) for Errors only. All values can be found in Autodesk.Viewing.Private.LogLevels.

webGLHelpLinkstring

A link url to a help page on webGL if itâs disabled. Supported only when using the GuiViewer3D instance; not supported in headless mode.


---

# GetPropertiesResult

GetPropertiesResult

Object with properties associated with a dbId.

Properties

dbIdnumber

the id passed intogetPropertiesfunction.

externalIdstring

an identifier that can be used in the un-translated version of the model. Can be used for desktop application integrations.

namestring

The elementâs name.

propertiesArray.<PropertyResult>

list of associated properties


---

# PropertyResult

PropertyResult

Element type forGetPropertiesResult.properties.

Properties

attributeNamestring

The property identifying name.

displayCategorystring, null

Category the attribute belongs into.

displayNamestring

A user facing label for the property. It could contain the same value as attributeName.

displayValuestring, number, boolean

The value for the property.

hiddenboolean

Whether the property is meant to be user facing or not.

precisionnumber

Applies only to numerical displayValues.

typeobject

An enumeration value of type AttributeType indicating how to interpret displayValue.

unitsstring, null

The units associated with displayValue.


---

# Prefs3D

Prefs3D

Contains viewer setting preference names for 3D models.

Properties

VIEW_CUBEstring

Sets the visibility of the viewcube.

VIEW_CUBE_COMPASSstring

Sets the visibility of the viewcube compass. The compass will only be displayed if model contains orientation data.

VIEW_TYPEstring

Sets the view to orthographic or perspective.

ALWAYS_USE_PIVOTstring

Orbit controls always orbit around the currently set pivot point.

ZOOM_TOWARDS_PIVOTstring

Default direction for camera dolly (zoom) operations to be towards the camera pivot point.

SELECTION_SETS_PIVOTstring

Sets selection / un-selection action to automatically reset the orbit pivot to be the center of the multiple selection.

REVERSE_HORIZONTAL_LOOK_DIRECTIONstring

Sets a view navigation option to reverse the default direction for horizontal look operations.

REVERSE_VERTICAL_LOOK_DIRECTIONstring

Sets a view navigation option to reverse the default direction for vertical look operations.

ORBIT_PAST_WORLD_POLESstring

Set a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction).

CLICK_TO_SET_COIstring

Modify the default click behavior for the viewer.

GHOSTINGstring

Toggles ghosting during search and isolate.

OPTIMIZE_NAVIGATIONstring

Toggles whether the navigation should be optimized for performance.

AMBIENT_SHADOWSstring

Enables or disables ambient shadows.

ANTIALIASINGstring

Enables or disables antialiasing.

GROUND_SHADOWstring

Toggles ground shadow.

GROUND_REFLECTIONstring

Toggles ground reflection.

LINE_RENDERINGstring

Hides all lines in the scene.

EDGE_RENDERINGstring

Turns edge topology display on/off (where available).

LIGHT_PRESETstring

Sets the Light Presets (Environments) for the Viewer.

ENV_MAP_BACKGROUNDstring

Toggles environment map for background.

FIRST_PERSON_TOOL_POPUPstring

Toggles first person tool popup.

BIM_WALK_TOOL_POPUPstring

Toggles the bimwalk tool popup.

BIM_WALK_NAVIGATOR_TYPEstring

Identifier for the bimWalkNavigatorType preference. This is used to set the BimWalk tool navigator.

BIM_WALK_GRAVITYstring

Identifier for the bimWalkGravity preference. This is used to toggle the BimWalk toolâs gravity.

DEFAULT_NAVIGATION_TOOL_3Dstring

identifier for the toolToUse preference. This is used to set which navigation tool will be used.

SELECTION_MODEstring

identifier for the selectionMode preference. This is used to set which selection mode (Leaf, First, Last object) wil be used by the viewer.

ENABLE_CUSTOM_ORBIT_TOOL_CURSORstring

identifier for whether the OrbitDollyPanTool will customize the cursor visuals.

EXPLODE_STRATEGYstring

Specifies which algorithm is used when exploding the model. Supported values are âhierarchyâ (default) and âradialâ. Other values are treated as âradialâ.

FORCE_DOUBLE_SIDEDstring

Forces the viewer to render materials as double sided. Otherwise it uses the model specified value.


---

# Prefs2D

Prefs2D

Contains viewer setting preference names for 2D models.

Properties

GRAYSCALEstring

Overrides line colors in 2D models to render in shades of gray.

SWAP_BLACK_AND_WHITEstring

Will switch to white lines on a black background.

FORCE_PDF_CALIBRATIONstring

Force PDF calibration before measuring.

FORCE_LEAFLET_CALIBRATIONstring

Force Leaflet calibration before measuring.

VECTOR_VIEWINGstring

Vector viewing of PDF.


---

# Prefs

Prefs

Contains viewer setting preference names that are available to both 3D and 2D models.

Properties

PROGRESSIVE_RENDERINGstring

Toggles whether progressive rendering is used.

PROGRESSIVE_FPS_TARGETstring

Sets the target for number of frames per second when progressive rendering is used.

OPEN_PROPERTIES_ON_SELECTstring

Open property panel when selecting an object. (Only for GuiViewer3D)

POINT_RENDERINGstring

Hides all points in the scene.

BACKGROUND_COLOR_PRESETstring

Sets a color to the background.

REVERSE_MOUSE_ZOOM_DIRstring

Reverse the default direction for camera dolly (zoom) operations.

LEFT_HANDED_MOUSE_SETUPstring

Reverse mouse buttons from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa).

FUSION_ORBITstring

Sets the orbit to fusion orbit.

FUSION_ORBIT_CONSTRAINEDstring

Sets the the orbit to the contrained fusion orbit.

WHEEL_SETS_PIVOTstring

Sets wheel-zoom action to automatically reset the orbit pivot to the location under the cursor.

RESTORE_SESSION_MEASUREMENTSstring

When opening the measure tool restore any existing measurements that where created during the session.

DISPLAY_UNITSstring

Units for quantities displayed in the property panel

DISPLAY_UNITS_PRECISIONstring

Precision for quantities displayed in the property panel

KEY_MAP_CMDstring

CMD key mapping to CTRL key in Mac


---

# VIEW_TYPES

VIEW_TYPES

ViewCube view types.

Properties

DEFAULTnumber

Sets the default view and enables the view preferences.

ORTHOGRAPHICnumber

Sets the orthographic view and enables the view preferences.

PERSPECTIVEnumber

sets the perspective view and enables the view preferences.

PERSPECTIVE_ORTHO_FACESnumber

sets the perspective with orthographic faces view and enables the view preferences


---

# _TARGET_MODES

_TARGET_MODES

Modes to set the FPS target when progressive rendering is enabled.

Properties

LOWnumber

sets the FPS target to 6.

MODERATEnumber

sets the FPS target to 15.

MEDIUMnumber

sets the FPS target to 30.

HIGHnumber

sets the FPS target to 60.


---

# Settings

Settings

Object used to apply the preferences by a Profile

Properties

viewCubeboolean

Sets the visibility of the viewcube.

viewCubeCompassboolean

Sets the visibility of the viewcube compass. The compass will only be displayed if model contains orientation data.

viewTypenumber

Sets the view to default (0), orthographic (1), perspective (2) or perspective with ortho faces (3).

alwaysUsePivotboolean

Orbit controls always orbit around the currently set pivot point.

zoomTowardsPivotboolean

default direction for camera dolly (zoom) operations to be towards the camera pivot point.

reverseHorizontalLookDirectionboolean

Sets a view navigation option to reverse the default direction for horizontal look operations.

reverseVerticalLookDirectionboolean

Sets a view navigation option to reverse the default direction for vertical look operations.

orbitPastWorldPolesboolean

Set a view navigation option to allow the orbit controls to move the camera beyond the north and south poles (world up/down direction).

clickToSetCOIboolean

Modify the default click behavior for the viewer.

ghostingboolean

Toggles ghosting during search and isolate.

optimizeNavigationboolean

Toggles whether the navigation should be optimized for performance.

ambientShadowsboolean

Enables or disables ambient shadows.

antialiasingboolean

Enables or disables antialiasing.

groundShadowboolean

Toggles ground shadow.

groundReflectionboolean

Toggles ground reflection.

lineRenderingboolean

Hides all lines in the scene.

edgeRenderingboolean

Turns edge topology display on/off (where available).

lightPresetnumber, string

Sets the Light Presets (Environments) for the Viewer.

envMapBackgroundboolean

Toggles environment map for background.

firstPersonToolPopupboolean

Toggles first person tool popup.

bimWalkToolPopupboolean

Toggles the bimwalk tool popup.

grayscaleboolean

Overrides line colors in 2D models to render in shades of gray.

swapBlackAndWhiteboolean

Will switch to white lines on a black background.

progressiveRenderingboolean

Toggles whether progressive rendering is used.

openPropertiesOnSelectboolean

Open property panel when selecting an object (Only for GuiViewer3D).

pointRenderingboolean

Hides all points in the scene.

backgroundColorPreset

Sets a color to the background.

reverseMouseZoomDirboolean

Reverse the default direction for camera dolly (zoom) operations.

leftHandedMouseSetupboolean

Reverse mouse buttons from their default assignment (i.e. Left mouse operation becomes right mouse and vice versa).

fusionOrbitboolean

Sets the orbit to fusion orbit.

fusionOrbitConstrainedboolean

Sets the the orbit to the contrained fusion orbit.

wheelSetsPivotboolean

Sets wheel-zoom action to automatically reset the orbit pivot to the location under the cursor.

selectionSetsPivotboolean

Sets selection / un-selection action to automatically reset the orbit pivot to be the center of the multiple selection.

bimWalkNavigatorTypestring

Sets the BimWalk tool navigator.

bimWalkGravityboolean

Toggles the BimWalk toolâs gravity.

defaultNavigationTool3Dstring

Sets which navigation tool will be used by the viewer. (ie: âextractor_definedâ || âbimwalkâ)

explodeStrategystring

Sets which algorithm is used when exploding a model. Supported values are âhierarchyâ (default) and âradialâ. Other values are treated as âradialâ.

loadingAnimationboolean

Toggles loading animation for 2D Models.

forcePDFCalibrationboolean

Force PDF calibration before measuring.

forceLeafletCalibrationboolean

Force Leaflet calibration before measuring.

restoreMeasurementsboolean

When opening the measure tool restore any existing measurements that where created during the session.

forceDoubleSidedboolean

Force the render to use double sided materials.

keyMapCmdboolean

Force mapping CMD key to Ctrl in Mac.

displaySectionHatchesboolean

Display the hatch pattern for planes in the section tool. This does not apply to the section box.


---

# Extensions

Extensions

Contains information about which extension should or should not be loaded.

Properties

loadArray.<string>

An array of extension ids that should be loaded.

unloadArray.<string>

An array of extension ids that should not be loaded.


---

# ProfileSettings

ProfileSettings

Object used for setting a viewer profile.

Properties

namestring

Name of the profile settings.

labelstring

Optional. An end-user string to use instead of the name.

descriptionstring

Optional. A description about the profile.

settingsSettings

Used by the Profile to apply to the viewer preferences.

persistentArray.<String>

An array of setting ids to keep in localStorage.

sharedStorageArray.<String>

An array of setting ids that share the persisted values across profiles.

extensionsExtensions

Extensions that should or should not be loaded.


---

# forEachCallback

forEachCallback

This callback is displayed as a global member.

Parameters

key*string

string with a propertyâs name and category separated by â/â

properties*Array.<Object>

an array of property objects associated with the key


---

# AggregatedResult

AggregatedResult

Properties

averageNumber

Average of all displayValues

countNumber

The number of properties

maxNumber

The max of all displayValues

medianNumber

The median of all displayValues

minNumber

The min of all displayValues

modeArray.<Number>

An array of possible modes

rangeNumber

The range (max-min) of all of the displayValues

sumNumber

The sum of all displayValues


---

# Viewer3DExtraScene

Viewer3DExtraScene

LMV has two extra scene it renders along with the models. One is rendered before the models, and the other is rendered after the models. These scenes are THREE.Scene objects and you can add custom meshes to be rendered to either of the scenes.

The objects you add to these scenes will be drawn using the same multiple render targets that are used when drawing the models. You may choose to either support multiple render targets or disable them.

To support multiple render targets you can only use Prism, MeshPhongMaterial, MeshBasicMateiral or LineBasicMaterial materials, and you must add all the materials to LMV.

To disable multiple render targets you can set theskipIdTargetandskipDepthTargetproperties totrue. If you disable multiple render targets your objects will not have rollover highlighting and will not contribute to ambient occlusion.

Properties

skipIdTargetboolean

Set to true to prevent the id target from being rendered.

skipDepthTargetboolean

Set to true to prevent the ambient occlusion depth target from being rendered.


---

# SelectionDef

SelectionDef

Properties

modelAutodesk.Viewing.Model

The model from which to select

idsArray.<number>

array of ids to select

selectionTypenumber

a member ofAutodesk.Viewing.SelectionType


---

# Intersection

Intersection

Object that is returned by the ray cast and hit test methods for each scene object under the given canvas coordinates.

Properties

dbIdnumber

Internal ID of the scene object.

distancenumber

Distance of the intersection point from camera. All intersections returned by the ray casting method are sorted from the smallest distance to the largest.

faceTHREE.Face3

THREE.Face3 object representing the triangular mesh face that has been intersected.

faceIndexnumber

Index of the intersected face, if available.

fragIdnumber

ID of Viewer SDK fragment that was intersected.

pointTHREE.Vector3

THREE.Vector3 point of intersection.

modelAutodesk.Viewing.Model

Model instance the dbId belongs to.


---

# EventHistoryChangedData

EventHistoryChangedData

The event data to identify the action and target for MarkupCore.EVENT_HISTORY_CHANGED event.

Properties

actionstring

A string identifier for the action taken, like redo, undo, cancel, execute, clear

targetIdnumber

A number targetId based on the action.


---

# Migration Guide v6 to v7

Migration Guide v6 to v7

Description

This guide is intended for developers who have been usingv6and are upgrading tov7.

The tables indicate changes fromv6tov7. Developers should review the changes and update their code based on the changes noted inv7. Refer to the final column for instructions and description of the changes.

The code below assumes that symbolavstands forAutodesk.Viewingnamespace global variable.

API Changes

Changes inoptionsobject passed intoav.Initializer(options,callback):

v6

varoptions=av.createInitializerOptions()

v7

varoptions={env:'AutodeskProduction'};

Developers need to create the object themselves.

v6

options.loglevel=1oroptions.logLevel=1

v7

options.logLevel=1

Only uppercaseLevelis supported.

Viewerrelated changes:

v6

varconfig3d=av.createViewerConfig()

v7

varconfig3d={};

Developers need to create the object themselves. Empty object yields the same result.

v6

av.Private.GuiViewer3D

v7

av.GuiViewer3D

Class is now available from outside the Private namespace.

v6

viewer.load(svfURN, sharedPropertyDbPath, onSuccess, onError, acmSessionId, loadOptions)

v7

var options = {sharedPropertyDbPath,
acmSessionId,
loadOptions};viewer.loadModel(svfURN,options,onSuccess,onError);

sharedPropertyDbPath,
acmSessionId,
loadOptions

};

viewer.loadModel(svfURN,options,onSuccess,onError);

Replace with new method.

v6

viewer.loadModel(...):bool

v7

viewer.loadModel(...):Promise

The function now returns aPromisewhich resolves with theboolreturned in v6.

v6

viewer.isolateById(idArray)

v7

viewer.isolate(idArray)

Replace with new method.

v6

viewer.getMemoryInfo()

v7

viewer.getExtension('Autodesk.MemoryLimited').getMemoryInfo()

Functionality has been encapsulated into an extension.

The ViewCube apis have been moved out ofViewer3Dinstance and into theAutodesk.ViewCubeUiextension.

v6

viewer.displayViewCubeUI(display)

v7

extension.setVisible(display);

Functionality available in extension.

v6

viewer.displayViewCube(display)

v7

extension.displayViewCube(display);

Functionality available in extension.

v6

viewer.setViewCube(display)

v7

extension.setViewCube(display);

Functionality available in extension.

v6

viewer.showViewCubeUI(show)

v7

extension.setVisible(show);

Functionality available in extension.

v6

viewer.showViewCubeTriad(show)

v7

extension.showTriad(show);

Functionality available in extension.

v6

viewer.displayHomeButton(show)

v7

extension.displayHomeButton(show);

Functionality available in extension.

Changes toDocumentclass:

v6

Document.getSubitemsWithProperties(...)

v7

BubbleNode.search(...)

Replaced by member function inBubbleNode.

v6

getItemById(id)

v7

bubbleNode.findByGuid(id)

Replaced by member function inBubbleNode.

v6

getRootItem():Object

v7

bubbleNode.getRoot():BubbleNode

Replaced by member function inBubbleNode. The return value also changes. Get the raw object by usingbubbleNode.data.

v6

getViewableItems():Array

v7

bubbleNode.getRoot().findAllViewables():Array

Replaced by member function inBubbleNode. Make sure to use the root node before using the function.

v6

Document.getPropertyDbPath():string

v7

Document.getFullPath(bubbleNode.getRoot().findPropertyDbPath())

Use in case you are callingViewer3D.loadModeldirectly and not usingViewer3D.loadDocuementNode, which populates the property automatically.

Changes toViewingApplicationclass:

v6

ViewingApplication

v7

viewer.loadDocumentNode()

TheViewingApplicationclass provided a way to keep a reference to theDocumentinstance and provided methods to change the model in the scene. The class is no longer required now that theViewer3Dinstance provides the same functionality. Refer toloadDocumentNode()documentation for usage details.

If you are not ready to move out of usingViewingApplication, you may still continue using it with version 7 by fetching the code from<scriptsrc=https://developer.api.autodesk.com/modelderivative/v2/viewers/7.*/legacy/ViewingApplication.js>.

On-Demand Loadingis the feature that allows to visualize models that require more memory than the available in the browser. The trade off is that loading times will be longer. This feature has been repackaged into theAutodesk.MemoryLimitedextension.

v6

Enabledby default

v7

Disabledby default

To enable memory limited mode you must configure LMV to use theAutodesk.MemoryLimitedextension
to load large SVF models on memory limited devices.
This is done by adding an object to the options you pass the Viewer3D or GuiViewer3D constructor.

Example:

v6

GEOMETRY_LOADED_EVENTmay include propertyonDemandLoad

v7

GEOMETRY_LOADED_EVENTno longer includes propertyonDemandLoad

The eventâs payload no longer contains propertyonDemandLoad. UsegetMemoryInfo()on theAutodesk.MemoryLimitedextension to determine whether a model is using on demand loading.

Detecting Toolbar creation:

v6

viewer.getToolbarPromise():Promise

v7

Extension.prototype.onToolbarCreated(toolbar)

Extensions may now override methodonToolbarCreatedto be notified when the toolbar is instantiated.
TheTOOLBAR_CREATED_EVENTis still present without modifications.

Animation API changes:

v6

viewer.playAnimation(callback)

v7

viewer.addEventListener(av.ANIMATION_TRACK_UPDATE_EVENT,callback)viewer.getExtension('Autodesk.Fusion360.Animation').play()

Animation API is not concentrated in theAutodesk.Fusion360.Animationextension.

Non-Photorealistic Rendering (NPR) changes:

v6

viewer.impl.setPostProcessParameter('style','cel')

v7

viewer.loadExtension('Autodesk.NPR');varext=viewer.getExtension('Autodesk.NPR');ext.setParameter('style','cel')

ExtensionAutodesk.NPRprovides the API method.

v6

viewer.impl.preloadPostProcessStyle('style')

v7

No replacement

The functionality has been folded intoext.setParameter().

Autodesk.BIM360.Extension.PushPinchanges:

v6

extension.createItem(data)

v7

extension.loadItems([data])

Replacement wraps data into an Array.

Moved symbols from between namespaces:

v6

av.getScreenShot()

v7

av.ScreenShot.getScreenShot()

Screenshot-related static functions have been moved into their own namespace.

v6

av.Viewer3D.ScreenMode

v7

av.ScreenMode

Moved into theAutodesk.Viewingnamespace.

FunctionBubbleNode.prototype.getAecModelData()may require an additional server request to fetch the data.

v6

varaecData=bubbleNode.getAecModelData()

v7

av.Document.getAecModelData(bubbleNode).then(aecData=>...)

The addded static function inDocumentguarantees that an additional server request will be performed (when needed) before attempting to access the modelâs AEC data.

Version global variable.

v6

LMV_VIEWER_PATCH

v7

LMV_VIEWER_VERSION

The value ofLMV_VIEWER_PATCHhas been folded intoLMV_VIEWER_VERSION, which will contain a proper Semanic Version string value.

```
var config3d = {
    ...
    loaderExtensions = {
        svf: "Autodesk.MemoryLimited"
    }
}
var viewer = new av.Viewer3D(domCanvasContainer, config3d); // or
var viewer = new av.GuiViewer3D(domCanvasContainer, config3d);

```


---

# V6 Changelog

V6 Changelog

IMPORTANT

Next major release: LMV 7.0

BREAKING CHANGES:  The next major release, LMV 7.0 is expected to contain breaking changes to better accommodate upstream merges, specify new file loaders, reduce package size, and improve performance.

We strongly recommend that you specify the version of Viewer code you are using for web applications deployed in production. By including a specific version number, you can update your application as necessary to accommodate breaking changes and dictate when to migrate to the next version. To learn how to load version-specific Viewer libraries, refer to the section âGetting the Codeâ inDeveloperâs Guide Basics.

6.6.4

Release Date: 2019-06-12

Fixed

LMV-4744 Non-photoreal Rendering causes black screen in Chrome v75

6.6.3

Release Date: 2019-06-07

Fixed

LMV-2958  2D annotations obscured by opaque selection highlight.

Changed

LMV-2958  2D selection opacity is now configurable through argument in existing Viewer APIset2dSelectionColor()

6.6.2

Release Date: 2019-06-05

Fixed

LMV-4720 Hyperlinks do not work in 6.6.1

6.6.1

Release Date: 2019-05-20

Fixed

LMV-4634 Objects are not isolating properly in large NWD models

6.6.0

Release Date: 2019-04-23

Changed

LMV-4399: Section tool will now take into account the cameraâs viewport during initialization

Added

Support forAutodesk.AEC.LevelsExtensionon mobile platforms.

Support forAutodesk.BIM360.Extension.PushPin(pushpins) andAutodesk.PDF(vector PDF).

Pushpin thumbnail & screenshots enhancements.

MethodrearrangeByPrioritiestotoolControllerAPI.

Handler for swipe gesture.

LMV-4218:config3d.modelBrowserIsolateSelectedNodesto configure the Model Browser to isolate the selected nodes or not (default is set to not isolate it).

DockingPanel.bringToFront()

Removed

LMV-4218: Transparent selection highlighting

Fixed

LMV-2958: Selection highlights for 2D are not transparent and obscured annotations

LMV-4308: Section tool cuts plane partially if state was saved withviewer.getState()

LMV-4338: Rendering of rotated images in PDF Extension

LMV-4308: Section tool cuts plane partially after usingviewer.restoreState()

LMV-4150: Dialog title gets truncated

LMV-4140: The camera cannot be tilted in first person mode if the initial point of view is looking straight down or up at the model

LMV-4428: Reduce hitTest when mouse hovering on the canvas

6.5.0

Release Date: 2019-03-04

Changed

LMV-4003: To properly support models with animation,on-demand-loadingisdisabledinviewer.loadDocumentNode()whenAutodesk.Fusion360.Animationis present in BubbleNodeâs extensions.

LMV-3886: UI code for the Explode slider has been moved out ofGuiViewer3Dand into extensionAutodesk.Explode.

LMV-4069: Settings Panel (which had been locked in a fixed location since being updated in 4.1.0) is now floating and can again be moved around the canvas.

BLMV-3048: Code for section planes fromLevelsExtensionwas moved out ofviewerState.cutplanesand intoviewerState.floorGuid.

Added

Model Browser displays child element count in parentheses.New child element countOriginal behavior

New child element count

Original behavior

WebGLRenderer can now use a WebGL2 context

LMV-4201: New methods to Fusion Animation extensionAutodesk.Fusion360.Animationto optionally decouple cameras from animation:

setFollowCamera(bool)

isFollowingCamera():bool

When setFollowCamera(false) is invoked, playing an animation will not affect the camera state. Likewise, the animation will not stop when the user orbits the model.  The default behavior remains unchanged. The UI also remains unchanged, so the feature can only be activated via javascript.

recursive flag to viewer.setThemingColor function:setThemingColor(dbId,color[,model[,recursive]])

setThemingColor(dbId,color[,model[,recursive]])

dbId

number

color

THREE.Vector4

(r, g, b, intensity), all in [0,1].

model

Autodesk.Viewing.Model

<optional>

NEW!

recursive

boolean

<optional>

Should apply theming color recursively to all child nodes.

LMV-3934:model.getPropertyDb().executeUserFunction():Promise

Allows executing user supplied function code on the worker thread against thePropertyDatabaseinstance. The returned value from the supplied function will be used to resolve the returned Promise.

Example:

Get started with the step-by-stepProperty Database Queriestutorial.

LMV-4174: newtotalRasterPixelsproperty to decide when to render PDFs using the new vector renderer.  (Once this property is enabled in Derivative Services,) PDF pages that contain less than about 1 megapixel of raster images will be rendered with the vector renderer; otherwise the Leaflet renderer is still used.

Removed

None

Fixed

LMV-4064: Screenshot includes overlays, SAO and antialiasing

BLMV-2790: Icons get mixed with lowercase letter font in IE/Edge

BLMV-2918: Use DPI data embedded in markups/pushpins to scale them according to the DPI of the current version

LMV-4131: shadow maps which were broken after 3.3

BLMV-2978: Shift+Click selects object while selector is disabled

LMV-3886: Explode slider doesnât work on Android mobile devices

LMV-4004: Improper selection color on theming colored items

BLMV-2977: navigation lock race condition with touch devices.

DropMeTool logic to resolve overlapping viewports

Viewcube triad sometimes vanishes when aligned to axis

fitBoundsnow takes into account camera rotation (roll)

6.4.2

Release Date: 2019-02-06

Fixed

LMV-4237: Runtime error when invokingviewer.finish()

6.4.1

Release Date: 2019-01-23

Fixed

LMV-4064: Include overlays and SAO in screen shot

6.4.0

Release Date: 2019-01-22

Added

LMV-4020: Danish locale support

Leaflet support to viewer.impl.getScreenshotProgressive

Support ghosted object in getScreenshotProgressive

LMV-3511: Support for undo in the markups extension to automatically select the next markup item available to undo.

Support different dpi leaflet-pdf file compare

BIM color theme via viewer.setTheme(âbim-themeâ).

LMV-4123: Method BubbleNode.useAsDefault():Boolean

CrossFadeEffects extension

CrossFade effects are an optional LMV feature that supports rendering into multiple color targets and blending between them. This addition moves the implementation from the viewer core to a new extension âCrossFadeEffectsâ.

The extension id is:Autodesk.CrossFadeEffects

Example:

Geolocation extension

Provides functions for converting GPS coordinates in WGS-84 format { x: Longitude, y: Latitude, z: Height(m) } into
Viewer scene coordinates and back. Supports a single 3D model loaded into the scene.

The extension id is:Autodesk.Geolocation

Example:

viewer.loadExtension('Autodesk.Geolocation')

Functions:

hasGeolocationData()

Does the model contain geolocation data?

returnsboolean(true when the model contains geolocation data)

lmvToLonLat(lmvPoint)

Converts viewer coordinates (obtained with something like viewer.clientToWorld()) into { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format.

returns{THREE.Vector3}:  (GPS coordinate in WGS-84 format: { x: Longitude, y: Latitude, z: Height } )

lonLatToLmv(lonLat)

Converts coordinates from { x: Longitude, y: Latitude, z: Height (meters) } in WGS-84 format into viewer scene coordinates.

returns{THREE.Vector3}:  (3D point in the scene)

openGoogleMaps([pointLL84])

Returns a Google Maps URL with a PIN on the specified GPS location. When no argument is provided, the URL will use the Modelâs geolocation if available.

activate()

Click the model to set points and see optional panel UI for testing and debugging

Changed

Redesigned Environments UI in Settings Panel.

BLMV-2115: [PushPin extension] Save external IDs along with LMV IDs

BLMV-2525: [PushPin extension] Save globalOffset to viewerState

FloorSelector: Avoid using crossFade effects when running on mobile

Fixed

LMV-3606: Restore topology highlight in measure tool for Fusion models

LMV-3196: Transparent object loses transparency and becomes opaque on focus.

LMV-3722: Selected transparent objects become opaque when the view is orbited, panned or zoomed.

LMV-3967: First Person extension does not properly initialize FOV from ortho view

LMV-3975: Crash with F2D files missing rcv_offsets and rcvs property DB files

Improve bubbleNode.search docs

BLMV-2644: [Markups extension] Fix canvg import on IE11 and Edge

BLMV-2685: [Pixel Compare] sensitivity of threshold

Some PDF text characters failing to get filled

LMV-4067: JsDocs search function

LMV-4076: Animation scrub for opacity

LMV-4043: DocumentBrowser extension lists an empty âfolderâ entry

LMV-4133: Inconsistent appearance of Phong material with mirror transform. Backfacing normals now face the camera in this case

Version 6.3.5

Release Date: 2018-12-14

Fixed

LMV-4075: Issue with loading models from manifests where the view-node isnât a child of a geometry node.

Version 6.3.4

Release Date: 2018-12-05

Fixed

LMV-4049: Issue of MarkupCoreâsrenderToCanvas()displaying upside-down.

Version 6.3.3

Release Date: 2018-11-27

Fixed

Issue in 6.1 and later where incompatible libraries caused 2D sheets to render black. URLs for dependencies are now set to load matching versions.

Version 6.3.2 BROKEN

Release Date: 2018-11-26

Broken

Regression error introduced in version number handling when attempting to prevent issue where incompatible libraries caused 2D sheets to render black. SEE FIX IN PATCH 6.3.3.

Version 6.3.1

Release Date: 2018-11-20

Changed

Restore functionAutodesk.Viewing.Private.getHtmlTemplatefor compatibility.

Version 6.3.0

Release Date: 2018-11-19

Added

LMV-3766 Support for leaflet pyramid output with missing levels

Autodesk.PDF extension

Prototype vector rendering loader for PDF files.

Sample code:

Autodesk.DocumentBrowser extension

Toolbar button and panel for viewing all 2D and 3D models available in a JSON manifest.

Document Browser Extension

viewer.loadDocumentNode

New model loading API:viewer.loadDocumentNode(lmvDocument,bubbleNode,options)

lmvDocument

The Document instance, which owns the model being loaded

bubbleNode

The specific manifest node to load (within the Document)

options<optional>

Options to pass to Autodesk.Viewing.Viewer3D#loadModel. Will be initialized internally if not specified. Leave empty in most cases.

loadOptions

loadOptions.skipHiddenFragments:boolto skip initially hidden meshes

Changed

Property Panel

Property Panelâs title will now display the name of the selected node.

Properties: Older versions

Properties: 6.3 updated title

Other:

Default value for BlendShaderâs AO opacity

Default values for SAOShaderâs radius and intensity.

All documentation URLs referencingforge.autodesk.comare now referencingforge.developer.com

Model loading UI will now be removed as soon as geometry is ready for rendering

Fixed

SplitScreen: Fix pan speed in SplitScreen when using 3 or 4 viewports

SplitScreen: Roll tool no longer jumps when dragging across viewports

LMV-3823: MissingUint8Array.prototype.slicein IE11 while loading Leaflet PDFs

Keep View Cubeâs triad oriented correctly when top/front/etc. changes

Incorrect selection color for wide lines

Letavp.ENABLE_INLINE_WORKERbe changed at run time

LMV-3783:viewer.clearSelectionno longer fires an event when nothing is selected

Version 6.2.3

Release Date: 2018-11-26

Fixed

Issue in 6.1 and later where incompatible libraries caused 2D sheets to render black. URLs for dependencies are now set to load matching versions.

Version 6.2.2

Release Date: 2018-10-17

Fixed

LMV-3726 WebVR extension not working

Version 6.2.1

Release Date: 2018-10-12

Fixed

LMV-3809 DWFx embedded images have low resolution

Version 6.2.0

Release Date: 2018-09-12

Added

Probing

ExtensionAutodesk.OMVfor On Machine Verification flows.

Display of measurement/probe points

Setting confetti diameter

Changed

Split Screen Extension

Support for up to 4 views in SplitScreenExt

Split Screen Extension - up to 4 linked views

Fixed

BLMV-2463: Unable to close sub-menu. (Centers toolbar only with text-align: center)

Incorrectly named property - RenderContext.getConfig().clearColorBottom

BLMV-2458: Viewer runs out of memory when loading large textures

LMV-3703:  Model Browser becomes empty after unloading a non-primary model

Version 6.1.2

Release Date: 2018-11-26

Fixed

Issue in 6.1 and later where incompatible libraries caused 2D sheets to render black. URLs for dependencies are now set to load matching versions.

Version 6.1.1

Release Date: 2018-08-21

Fixed

LMV-3689 - Selection not working correctly

Version 6.1.0

Release Date: 2018-08-21

Changed

MEASUREMENT_CHANGED_EVENTto containtype&id

Added

Handling new paper transform for 2d files.

Support for png based leaflets

Functionviewer.getVisibleModels()

Allow meta keys (CMD) to be used on mac. Applies to Markupâs copy/paste/undo/redo commands. All tools benefit from this change, too.

Removed

Global variableLMV_RESOURCE_VERSION

Fixed

zoomWindowTool issue on window resize

Markupâs text input height when zooming

iOS10 device keyboard now hides after editing a text markup

Top right area is now clickable when viewcube is disabled (ex: 2D documents)

âCalibration requiredâ dialog displays as expected

Path to markups output files in string replace

Editing markup in IE11 (update canvg third party to address)

Environment Background image visiblity while in 2D file compare

Visibility of measuring axes on mobile devices

Camera view when loading Navisworks saved views

Bump map heuristics overwriting the specified bumpScale /âgeneric_bump_amountâin certain cases.

Measure button behavior when pressing for the second time

Duplication of focal length and edit frame elements when changing sheets

3D section missing capping in the view saved with a pushpin

Text markup jumps after finishing editing on iOS

World up tool (roll) for extensionAutodesk.SplitScreen

BimWalk guide missing title: Run

Zoom tool whenAutodesk.SplitScreenextension is active.

Version 6.0.2

Release Date: 2018-08-13

Fixed

Filter functions for extensionAutodesk.SplitScreen

Version 6.0.1

Release Date: 2018-07-25

Fixed

Avoid dispatching events whenviewer.getScreenShot()is invoked.

Version 6.0.0

Release Date: 2018-07-24

NOTE:This release includes breaking changes described below.  As a workaround, affected users may include a version number to the CDN url. Please visitBasicspage for details.

Changed

Screenshots

BREAKING CHANGE:getScreenShotBuffer()has been removed.

getScreenShot(width,height,onComplete)has been improved to allow arbitrary sized screenshots.  In addtion, the parameters are now optional (defaults to the canvas size)

Viewer Canvas  (350px x 400px)

getScreenShot ()  (350px x 400px)

getScreenShot (3500,4000)

Blow-up of getScreenShot(3500,4000)

Other Changes

Several performance improvements for loading PDF and 2D models.

Added

API endpoints for EMEA (eu) Data Center Support

Note that in some cases you may wish to determine if the bucketKey is from EMEA or US.
Start by base64 decoding the URN, then check if it containsurn:adsk.wipemea:xxx(for EMEA) orurn:adsk.wipprod:xxx(for US).
Read more in the blog aboutEuropean data center support.

SplitScreen Extension

AddedAutodesk.SplitScreenextension

Added optional params to facilitate multi-viewport rendering.

Vertex array objects default to false on mobile devices to save memory

Autodesk.BIM360.Extension.PushPinextension

Panning with middle button when editing markup is now allowed

Added layerOrder support

Addedviewer.impl.cancelLeafletScreenshot()to cancel time-consuming PDF screenshots

More render settings can be controlled via metadata:renderEnvironmentDisplayEdges,renderEnvironmentDisplayPointsand additional parameters forrenderEnvironmentAmbientShadows.

Removed

Removedviewer.getScreenShotBuffer(). Please useviewer.getScreenShot(), instead.

window.Hammerremoved in favor ofAutodesk.Viewing.Hammer

Fixed

Fixed ray intersection fixes aggregated views

fragmentList.getOriginalWorldBounds()no longer crashes in 2D

AGD/Scalaris files without stress data are now handled properly

Issue with text markup being cut after saving

Issue with callbacks when ending markup creation on mobile.

getCameraUpVector()case where up and direction vectors are colinear

Issues with Moldflow visualization extension seen inEdge/IE11

Inability to load certain files frommodelderivative/v2/endpoint.

```
executeUserFunction(function userFunction(pdb) {
     var dbId = 1;
     pdb.enumObjectProperties(dbId, function(propId, valueId) {
           // do stuff
     });
})

```

```
var extName = 'Autodesk.CrossFadeEffects';
NOP_VIEWER.loadExtension(extName);

function setCameraToRoom() {
    var cam = {
       fov:          53.13010235415598,
       isPerspective:true,
       orthoScale:   6.442020414517138,
       position:     {x:-23.63091853857176, y: 0.9033896546012906, z:-4.261154219883789},
       target:       {x:-20.871083468967406, y: 6.520671770079398, z:-5.787286273399167},
       up:           {x:0.10446560472788749, y: 0.21262602957092375, z:0.9715333802694284}
    };
    NOP_VIEWER.impl.setViewFromCamera(cam, true);
}

function fadeExample() {

    // apply fade transition
    var viewer = NOP_VIEWER;
    var ext = viewer.getExtension(extName);
    ext.fadeToViewerState(setCameraToRoom, 1.5);
}

```

```
// Create Viewer instance and load PDF file on page 1
    Autodesk.Viewing.Initializer(options, function() {
        var viewer = new Autodesk.Viewing.Viewer3D(div,config3d);
        viewer.start()
        viewer.loadExtension('Autodesk.PDF').then(function() {
            // URL parameter `page` will override value passed to loadModel
            viewer.loadModel('path/to/file.pdf', { page: 1 });
        });
    });

```


---

# V5 Changelog

V5 Changelog

Version 5.0.0

Release Date: 2018-06-19

Changed

Refactored to incorporate forked changes. Some breaking changes were introduced and identified (see below). If there are additional breaking changes we didnât spot, please let us know!

three.min.jsandthree.jsare no longer required. These libraries are now bundled intoviewer3D.min.jsandviewer3D.jsrespectively.

Improved display and sizing of Settings Panel

Reflectivity is reduced at grazing angles in phong shader for some Protein materials.

Can now zoom more than 100% in PNG/JPG image files

default value is now false forapplyRefPointoption

ReplacedAutodesk.Viewing.theHotkeyManagerwithviewer.getHotkeyManager()

ReplacedHotkeyManager.KEYCODESwithAutodesk.Viewing.KeyCode

IFC tranlsations are treated as AEC models

Added

Added monochrome mode for 2D models:viewer.setGrayscale(true)

Added AEC ExtensionThis submission is an initial file dump, and adaptation will be needed to SectionTool and BlendShader to make the extensions fully functional.It also shows how to build an LMV extension using modern JavaScript and package it with webpack.

This submission is an initial file dump, and adaptation will be needed to SectionTool and BlendShader to make the extensions fully functional.

It also shows how to build an LMV extension using modern JavaScript and package it with webpack.

Adding various cross-fade logic used by view transitions

Added option to disable node box caching

Added preference valuewheelSetsPivotalong withNavigationmethods

Added edge color/opacity for ghosted shapes

Add spatial filter support to RenderContext and blend_frag.glsl

Localization strings for recently added IBLs and for Scalaris extension

Exposeconfig3d.modelBrowserExcludeRootto configure whether the Model Browser will display the modelâs root node or not (default is to not display it)

Exposeconfig3d.modelBrowserStartCollapsedto configure whether the Model Browser will have the topmost node collapsed or not (default is no, aka: expanded)

Added version to Settings Panel, bottom right

Fixed

A360 Preview tab images are now loaded

Pressing the ESC key in the LMV window no longer confuses which state the icons are in

Choosing specific environments now forces âEnvironment Image Visibleâ to enabled or disabled

After enabling the zoom tool holding the ALT key now enables the orbit tool as expected

Property Panel now shows the root-node properties when nothing is selected.

Search is no longer shown for PDF bubble

Selected object is now highlighted properly

2D and 3D selection color settings are decoupled

Fixed loading problem with models that use memory optimized mode

Fixed loading problem with Animation extension

Prevent renamingwindow.nameto âuser_infoâ

Screen is no longer temporarily black at startup

Fixed missing highlight

Removed

Removed Comments and Billboard extensions

Removed code that was only used for debugging

Removed in-viewer search extension

Removed old First Person tool toggle.


---

# V4 Changelog

V4 Changelog

Version 4.2.7

Release Date: 2018-06-22

Fixed

Avoid crashing when attempting to use an undefined material id.

Version 4.2.6

Release Date: 2018-05-29

Fixed

Translation update from localization build.

Version 4.2.5

Release Date: 2018-05-09

Fixed

Fixed Scalaris Extension localization strings.

Version 4.2.4

Release Date: 2018-05-07

Fixed

Fixed problem with Animation activate() and deactivate().

Version 4.2.2

Release Date: 2018-04-19

Fixed

Fixed problem with Fit-to-View in 2D models on iOS devices.

Version 4.2.1

Release Date: 2018-04-17

Added

MoldFlow Extension

This release adds an extension to LMV that enables a legend for MoldFlow files.

Version 4.1.0

Release Date: 2018-04-02

Added

Glazing Materials

Glazing materials are now supported.

Fixed

Fixed problem with initialization of viewer with multi-model.

Fixed size of first person panel in Spanish language.

Hidden properties are now skipped when evaluating instance_of relationships.

Viewer no longer fails with jQuery slim.

Default text is now provided for null selection in model properties.

cloneMaterial() now copies disableEnvMap property.

Model browser no longer switches node positions

Changed

Settings UX Redesign

The viewer Settings dialog has been redesigned for improved ease of use.

Settings are now presented in a modal dialog featuring better functional grouping of settings and detailed new descriptions of each viewer option.  The dialog for 3D models comprises four tabsâPerformance, Navigation, Appearance, and Environment.  For 2D sheets there are three tabsâPerformance, Navigation, and Appearance.

(Table 1) 3D Settings Panel

Existing 3D Settings (4.0.1 and earlier)

New 3D Settings (4.1)

(Table 2) 2D Settings Panel

Existing 2D Settings (4.0.1 and earlier)

New 2D Settings (4.1)

Known Issues

On IOS, Fit to view fails for 2D models (Issue LMV-3154)

WebVR extension fails in 4.0.x and 4.1.0 (issue LMV-3203)

Version 4.0.1

Release Date: 2018-02-21

Fixed

Fixed âReferenceError WGS is not defined.â The WGS global variable that was used by LMV was not defined. The fix was to change the output format of the Rollup build of WGS from UMD to IIFE.

Version 4.0.0

Release Date: 2018-01-25

Changed

UI Themes

ALERT!Changes to UI themes in version 4.0 may break applications developed using 3.3.5 and earlier.
Light and Dark UI themes are now available.

Existing UI theme (3.3.5 and earlier)

string = âdark-themeâ

string = âlight-themeâ

API Reference

Viewer configuration option

Set theme method

Enhanced Search Results

Search now yields results in a more intuitive results summary.

Existing search (3.3.5 and earlier)

Improved version 4.0 behavior

Toolbar API

ADDED new toolbar API.

Each tool in the toolbar should be considered an extension.  Likewise, each extension may be queried and activated in the toolbar as described below.

API Reference

Optimized Prism materials performance

We no longer copy data structures such as matrices, vectors, and colors every frame for every PRISM material.

Added

Autodesk Forge Viewer Usage Limitations Disclaimer

The Autodesk Forge viewer can only be used to view files generated by Autodesk Forge services. The Autodesk Forge Viewer JavaScript must be delivered from an Autodesk hosted URL.

Multi-model support

UI behavior has been updated to allow multiple models. In addition, model names may now be overridden in the Model Browser.

FragmentList visibility flags

Initial visibility flags for fragments are now supported.

Measure, Markup and Hyperlinks

Measure, Markup and Hyperlinks are now external extensions

Material Tiling Patterns

Protein Materials tiling patterns (Revit 2019) are now supported.

Swedish language localization

Localized Swedish language âsvâ is now supported.

Fixed

Fixed minor problem with selection of dimension markup.

Fixed problem with Fit to View not working for all models.

Fixed selection highlight issue when using non-photoreal rendering styles.

Viewer no longer refreshes needlessly in specific cases.

Textures now work in Prism materials coming from Revit.

Loading of large raster images has been optimized.

Isolation is no longer cleared when measuring.

Pivot point can now be predictably changed in orthographic projection.

Zoom Window no longer leaves artifacts over selected objects.

Known Issues

Localization is incomplete in the Settings panel, where titles âNavigationâ and âPerformanceâ remain printed in English.

```
activateExtension(extensionID, mode);  // Activates the extension based on the extensionID and mode given.
                                       // By default uses the first available mode in getExtensionModes()

deactivateExtension(extensionID);      // Deactivates the extension based on the extensionID specified.

IsExtensionActive(extensionID);        // Check if the extension is active or not by passing the extensionID.

IsExtensionLoaded(extensionID);        // Check if the extension is loaded or not by passing the extensionID.

getLoadedExtensions();                 // Get a list of all the extensions that are currently loaded.

getExtensionModes(extensionID);        // Get a list of all the modes that are available for the given extensionID.
                                       // For example, "Autodesk.Measure" has modes: "distance", "area", "angle", "calibrate"

```


---

# V3 Changelog

V3 Changelog

Version 3.3.5

Release Date: 2017-12-15

Fixed

Fix a conflict in Angular zone.js promise polyfill.

Version 3.3.4

Release Date: 2017-11-29

Added

Non-Photorealistic (NPR) Rendering Styles

Several styles of non-photorealistic rendering (NPR) are now available.

NPR is often used for artistic expression or as a way to suggest that a view is to be interpreted as a work in progress.

This is done as a post process. For desktops and laptops the cost is negligible; for mobile devices the cost is some drop in frame rate, due to a lack of multiple-render target support on these devices.

API Reference

Optional:

The âgraphiteâ and âpencilâ styles require textures, so there may be a slight delay upon first launch while textures are cached. You can preload all textures or instead pass an individual style string to initialize only a single style. (If not called, the first call to setPostProcessParameter which sets a style will load the textures.)

All NPR parameters are set with a combination of string and value.  See additional descriptions below.

ââ (or âoffâ)

âedgingâ

âcelâ

âgraphiteâ

âpencilâ

None (value = ââ or âoffâ)

None (value = ââ or âoffâ)

value = âedgingâ

value = âedgingâ

value = âcelâ

value = âcelâ

value = âgraphiteâ

value = âgraphiteâ

value = âpencilâ

value = âpencilâ

Example Code

Selection and highlight can be turned off individually using a new API

By default, the viewer changes the color of an object when you hover the mouse over it, and you can select objects by clicking them in the view or Model Browser.  This highlighting is useful when selecting and interacting with the model, but can be a distraction when you prefer a presentation mode. You can now toggle these behaviors.

API Reference

Example Code

Toggle highlight and selection

Layers defined in 3D files now can accessed through the Layers Panel

The Layer Manager control now works for 3D files.  Click the Layer Manager icon to open the Layers panel, where you can toggle visibility of layers.

Dutch language supported

See existing API Reference forAutodesk.Viewing.Initializer.

Set stringoptions.languageto ânlâ to enable Dutch.

Fixed

Hyperlinks pointing to invalid locations are no longer displayed

Fit to View âfâ hotkey now works consistently

Ambient shadows now work on mobile devices

Measure Tool is more accurate when measuring large drawings

Interaction is no longer blocked in the ViewCube area when ViewCube is disableddiv.viewcubeUIno longer blocks interaction when the ViewCube is disabled

div.viewcubeUIno longer blocks interaction when the ViewCube is disabled

Version 3.2.1

Release Date: 2017-10-25

Changed

Model Browser look and feel

The Model Browser has been improved for more consistent appearance and behavior. Object visibility is now explicitly indicated by the eye icon to the right of each element. Object selection behavior has changed.

Toggle visibility by clicking the eye icon to the right of the element

Left-click a listed name to select an element and automatically focus the view on it

Right-click a selected object to bring up the full context menu (Isolate, Hide selected, Show all objects, Focus, Clear selection)

Before

Now

Measure Angle tool

Measurement of angles will now require selecting 3 points instead of choosing 2 lines.

Animated example:

Added

Viewer version display

Viewer version is now displayed at the very top of viewer3D.min.js

URL

https://developer.api.autodesk.com/modelderivative/v2/viewers/viewer3D.min.js?v=3.2

Content

Camera transition event

Event

Autodesk.Viewing.CAMERA_TRANSITION_COMPLETED

Usage

// Hook the eventviewer.addEventListener(Autodesk.Viewing.CAMERA_TRANSITION_COMPLETED,function(){console.log('camera is no longer moving');});// Trigger an action that will move the camera and fire the eventviewer.fitToView();

Transition types

The event will fire at the end of these operations:

Go Home transition

Focus / Fit to View transition (example above)

Restore State transition

Named Views transition

Any other camera transitions

New tool method: getPriority()

Tools that are registered into theToolControllerwill now be able to specify their own priority. The priority is used by theToolControllerto sort the tools in it. By default all tools have a priority value of 0.

The higher the numeric value returned, the higher priority on the tool stack. Tools with a higher priority have the opportunity to handle events first.

Fixed

The Freehand Markup is now smoother and more performant.

Fixed issue where SVG icon on toolbar buttons didnât work on IE11

Fixed issue with the New First Person tool which locked the camera when the initial view was pointing directly down or up

Fixed issues with touch gestures on IE11 running on Windows Surface devices.

Improved memory handling on iOS for models that referenced multiple textures

Version 3.1.3

Release Date: 2017-10-02

Fixed

Fix issue where the eventAutodesk.Viewing.GEOMETRY_LOADED_EVENTwas not getting fired after loading a 2D model in Chrome for iPhone.

Version 3.1.2

Release Date: 2017-09-21

Fixed

Fix issue where ESC button would enable the measure toolbar.

Version 3.1.1

Release Date: 2017-09-15

Changed

Semantic Versioning

Starting now, current and future versions of the Viewer will be following theSemantic Versioningconvention.

Breaking Changes

A few API methods have been relocated:

Before

Now

method

Autodesk.Viewing.setApiEndpoint

Autodesk.Viewing.endpoint.setApiEndpoint

method

Autodesk.Viewing.getEndpointAndApi

Autodesk.Viewing.endpoint.getApiEndpoint

object

Autodesk.Viewing.HTTP_REQUEST_HEADERS

Autodesk.Viewing.endpoint.HTTP_REQUEST_HEADERS

Model Browser

In our previous release, the Model Browser internals were changed to reduce the memory consumption, which was a big issue with BIM models.

In this occasion, the Model Browser is getting some behavior improvements.

Tree-Node Selection

Clicking to select a node in the Model Browser will now trigger a selection and a focus operation on the model canvas.

Additionally, the selection will display on top of occluding objects.

Viewer Selection

To keep the experience consistent, the selection on the viewer will get reflected on the Model Browser.

The Model Browser will automatically scroll to the selected item.

Context Menu

Right clicking to open the Context Menu will no longer perform a selection action as part of the operation.

Same rule applies when clicking away to close the Context Menu.

Upcoming changes

The Model Browser will receive UI changes in the upcoming release.

Measure Tool Redesign

Accessing the measure tool is still done through a button on the toolbar

After clicking on the button, the toolbar will expand to reveal additional measuring tools

Measure simple distance

Click 2 points and get their distance.

For 2D models:

For 3D models:

Measure angle

Click 2 lines and get the angle between them.

For 2D models:

For 3D models:

Measure area

Define a closed area composed of line segments to get the total area within. Availableonly in 2D models.

Calibration

Is the documentâs default measurement inaccurate? Then use the calibration tool to specify a known distance,
and have all the other measurements performed on the document adjusted accordingly.

Settings

Accessing measurement unit type and precision is now done through the measureâs Settings panel

Multiple measurements

It is now possible to have more than one measurement on the screen at once!

Modify measurement

After a measurement has been performed, users are able to adjust it by dragging the blue knobs.

```
preloadPostProcessStyle();        //OPTIONAL: loads all textures needed, for all styles.
preloadPostProcessStyle(string);  //OPTIONAL: use style string to initialize textures for a single style

```

```
setPostProcessParameter(string, value);  //string options and value ranges are described in the reference below

```

```
// Optional call, do this some time before using a style so that the required textures are loaded before the style is used.
// Not doing so may give a bad render or two while the textures are being loaded. In particular, Graphite will look black.
// This loads all textures needed, for all styles. You can instead pass an individual style string to initialize only it.
// Currently only the graphite and pencil styles require textures. If not called, the first call to setPostProcessParameter
// which sets a style will load the textures.
viewer.impl.preloadPostProcessStyle();

// Turn on a style. Styles are passed in as strings, for the "value" parameter:
// "" - turn off the style; back to normal, no post-process is done.
// "edging" - turn on image-based edging system
// "cel" - cartoon ("posterized") style, with edges
// "graphite" - black pencil style
// "pencil" - colored pencil and paper
var value = "graphite";
viewer.impl.setPostProcessParameter( "style", value );

// make the image have no edges:
viewer.impl.setPostProcessParameter( "edges", false);

// turn up brightness a bit:
viewer.impl.setPostProcessParameter( "brightness", 0.4);

```

```
disableHighlight(boolean); //true to disable highlight, false to show highlight (defaults to false)
disableSelection(boolean); //true to disable selection, false to allow selection (defaults to false)

```

```
// Disable highlight when cursor hovers over an object
disableHighlight(true);

// Enable highlight when cursor hovers over an object
disableHighlight(false);

// Disable selection when clicking an object in the view or Model Browser
disableSelection(true);

// Enable selection when clicking an object in the view or Model Browser
disableSelection(false);

```

```
// Hook the event
viewer.addEventListener(Autodesk.Viewing.CAMERA_TRANSITION_COMPLETED, function(){
    console.log('camera is no longer moving');
});

// Trigger an action that will move the camera and fire the event
viewer.fitToView();

```

```
// Default implementation
this.getPriority = function() {
   return 0;
};

```

```
// Tool with high priority
function MyAwesomeTool() {
  Autodesk.Viewing.ToolInterface.call(this);
  this.names = ['my-awesome-tool'];

    this.getPriority = function() {
       return 1000; // Default is 0, higher numerical value results in higher priority.
    };
};

// Tool with default priority
function MyRegularTool() {
    Autodesk.Viewing.ToolInterface.call(this);
    this.names = ['my-regular-tool'];
};

// Register them to the Viewer instance (no matter the order)
viewer.toolController.registerTool(new MyAwesomeTool());
viewer.toolController.registerTool(new MyRegularTool());

// Activate tools
viewer.toolController.activateTool('my-awesome-tool'); // MyAwesomeTool gets all events because it is being activated
viewer.toolController.activateTool('my-regular-tool'); // MyAwesomeTool STILL gets all events first because it has the highest priority.

```


---

# V2 Changelog

V2 Changelog

Version 2.17

Release Date: 2017-08-22

Changed

Default Memory Management

We introducted the memory management options feature in Viewer v2.15 where we allowed users to specify a memory budget for the Viewer to work with in order to address the problem with browser crashing when it doesnât have enough memory access to allocate for BIM 360 construction models containing too much geometry data.

This release includes a default memory limit.

How it works?

By default, the memory limit for the Viewer is set to:

Desktop

600 MB

Mobile

195 MB

Developers can override these values:

varconfig3d={memory:{limit:1024// in MB}};varviewer=newAutodesk.Viewing.Viewer3D(container,config3d);viewer.loadModel(modelUrl);

In addition, we are exposing a URL parameter that overrides all other memory limit settings:

Usage

http://lmv.ninja.autodesk.com/?viewermemory=200

Use theviewer.getMemoryInfo()method to check whether the Viewer makes use of the memory limit.

If it returnsnull, the specified memory limit is enough to contain all the geometry data in the memory. Otherwise, it will return an object with additional memory data, such as:

{"limit":20,"effectiveLimit":22.238370895385742"loaded":24.898095417022706}

Model Browser UI

The look and feel of the Model Browser remains the same. However, changes have been made under the hood.

Reduced Memory Consumption

This change aims at reducing memory consumption on very large models.

Hereâs an example of a model that has 1,582,736 nodes available on the Model Browser.

Before

Now

Memory Consumption

212 MB

3 MB

Image

UX Changes

Clicking on nodes in the Model Browser now produces different results.

Before

Now

Isolation

Isolation

SelectionFocus

Selection

Focus

You can still get Isolation by right clicking anywhere on
the canvas to open the Context Menu, then select Isolate.

Some other changes include:

Removed the root node of the Model Browser.To access properties of the root node, open the Property Panel without any selection.

To access properties of the root node, open the Property Panel without any selection.

Opening the Context Menu retains everything you select. Clicking outside the Context Menu closes the menu but retains everything you select.

Fixed

Fixed issue where Fusion 360 background color would not propagate correctly to the Viewer.

Fixed issue where the Properties Panel would not update its content after changing model selection.

Fixed issue where measurement precision was incorrectly rounding up.

Reduce excessive analytics requests during model initialization.

Version 2.16

Release Date: 2017-07-26

Changed

Removed Reliance on Browser Cookies to Authenticate Requests

The Viewer will no longer rely on browser cookies when authenticating with Forge API REST endpoints.
This change was implemented to protect against CSRF attacks on the Forge platform. No changes are necessary to the code.

However, developers might encounter a potential thumbnail problem if they initialize an<img>tag with asrcvalue that points to a thumbnail (PNG/JPEG/JPG) generated by the Model Derivative service. The cookie change included in this release will prevent those images from loading the thumbnail, resulting in a 401 Unauthorized error.

Solution to this problem

The first step is to identify whether this change will affect you.
Sinceversion 2.7, the Viewer exposes a global variablewindow.LMV_THIRD_PARTY_COOKIEwhich when set tofalsewill avoid setting and leveraging the browser cookie for authentication with Forge API endpoints.

You will need to fetch images usingAjax.

Populating HTML Images

The usual method of displaying images retrieved from the Model Derivative service is to create an HTML Image element and set its src property to the URL of the image you want to display. The browser handles making the request to retrieve the image. The problem is that there is no way to tell the browser to add an authorization header. This approach only works if the cookie is defined.

The solution is to make an XHR request from JavaScript to retrieve the image as a blob and then usecreateObjectUrlto create a URL that refers to the image in memory. Finally use that URL as the src of the image. You need to be careful to make sure that you callrevokeObjectUrlafter the image has been loaded otherwise you end up with a resource leak.

If youâre using a UI framework like Angular, there are modules that you can include that wrap this pattern in an easy to use form. For example,angular-img-http-src.

Integrate the module, then all you need to do is change the code so that the image URL is assigned to thehttp-srcproperty instead of thesrcproperty. Behind the scenes the image will be loaded using the Angularhttp_service, which you will already have configured to add to the authorization header for any request.

Take a look atthis exampleto see these strategies in action. Note that you need to generate an access token for this example.

See thisStack Overflow questionfor more information about how to use Angular to call images with custom headers.

Decoupled MarkupsCore Extension from the Main Bundle

In our previous release notes for Viewer v2.15, we introduced a change to decouple some of the extension code from the main build artifact (viewer3D.min.js) into their own ones.
With Viewer v2.16, theMarkupsCoreextension is supported with independent build artifact.

Note, code using the MarkupsCore extension will have to be updated to accommodate this change.

Before

varresult=viewer.loadExtension('Autodesk.Viewing.MarkupsCore');if(result===true){varextension=viewer.getExtension('Autodesk.Viewing.MarkupsCore');console.log('MarkupsCore extension is ready to be used!');}

Now

varpromise=viewer.loadExtension('Autodesk.Viewing.MarkupsCore');// async fetch from serverpromise.then(function(extension){console.log('MarkupsCore extension is ready to be used!');});

Added

New First Person Walk Experience

This release includes a new version of the First Person Walking tool called the New First Person Walking tool.

The New First Person Walking tool has additional features such as, floor detection, navigation between floors, teleportation (use double-click) and a new UI to display changes in speed.

How to use it

The New First Person Walking tool can be enabled by end users through the Navigation Settings checkbox:

The checkbox settings will persist across sessions.

From there, the same Toolbar icon will now enable the New First Person Walking tool. The tooltip will be different:

On first usage, end users will be prompted with a navigation guide to them get started:

You can access the guide any time by pressing the top right info button while theNewFirstPersonWalk tool is active:

Markup Editing API

In an effort to continue supporting BIM Docs, the Markup extension API has been extended to support editing of loaded markups.

How it works

The MarkupsCore extension exposes theenterEditMode()method, which has been enhanced to allow editing a layer that contains loaded markups.

// string with markups data generated with markupsExt.generateData()varmodelMarkups='...';// Load the markups extensionviewer.loadExtension('Autodesk.Viewing.MarkupsCore').then(function(markupsExt){markupsExt.show();markupsExt.loadMarkups(modelMarkups,"layerA");// Load markups onto "layerA"markupsExt.enterEditMode("layerA");// Allow editing of markups in "layerA"})Show More

With this change, an end user will be able to modify markups!

Developers can get the modified markups data by doing the following:

varmodifiedMarkups=markupsExt.generateData();markupsExt.leaveEditMode();// Prevent further modifications to the markups onscreen

You can revert all the changes done to the loaded set of markups using themarkupsExt.revertLayer("layerA");method

markupsExt.revertLayer("layerA");// Restores markups from "layerA" to their loaded state

ViewCube Triad

A new method has been added to the the ViewCube, to display labeled axis lines. This code is available at the GuiViewer3D level:

viewer.showViewCubeTriad(true);

ViewCube Reflects Camera Projection

The ViewCube will get rendered using the same camera projection as the Viewer

Pivot Customization

Whenever a user orbits (rotates) the camera, it is centered at a point called the âpivot pointâ.
This pivot point is displayed as a green dot (small sphere) while the rotation is taking place.
With Viewer v2.16, new functions have been added to customize the pivot point.

Customization

Code

Notes

Size

viewer.utilities.setPivotSize(2)

A size of 1 maps to the default size.

Color

viewer.utilities.setPivotColor(0xFF0000, 1)

Separate arguments for RGB-color and opacity

Below is an image comparing the default pivot with a customized pivot using the functions mentioned above.

Before

Now

Added Support for Run-time Loaded Locale Files

A new function is being exposed, to allow 3rd party extensions to add additional localization strings for the Viewer to use.
You can make use of this functionextendLocalization()in your extension code.

Usage

// Create a custom extensionfunctionMyAwesomeExtension(viewer,options){Autodesk.Viewing.Extension.call(this,viewer,options);}MyAwesomeExtension.prototype=Object.create(Autodesk.Viewing.Extension.prototype);MyAwesomeExtension.prototype.constructor=MyAwesomeExtension;// Define what are the localization strings to add...varlocales={en:{"Hello":"Hello!",},es:{"Hello":"Hola!",},};// Add locales during extension's loading phaseMyAwesomeExtension.prototype.load=function(){this.extendLocalization(locales);returntrue;};Show More

Fixed

Fixed some issues with z-fighting

Fixed missing info button.

Fixed navigation issue where a pan command would result in very big jumps.

Fixed issue with sectioning where the 3D UI would incorrectly change size.

Fixed issue where some transparent objects disappear on zoom.

Fixed issue where some transparent objects would display as opaque right after loading the model.

Fixed issue in iOS where rotating the phone while in Fullscreen mode would result in an inconsistent state.

Fixed issue where turning ambient shadows on would result in some faraway geometry to disappear.

Fixed some rendering issues related to ambient occlusion.

Version 2.15

Release Date: 2017-06-08

Changed

Extension Decoupling

Up until now all extensions were bundled with the main build artifact: viewer3D.min.js. We have begun to decouple extension code from the main build artifcact, starting with theInViewerSearch.min.jsextension. We will decouple more extensions for future releases.

Note that as a result of this change, theviewer.loadExtension()function now returns a promise instead of a boolean value.

Before

varresult=viewer.loadExtension('Autodesk.InViewerSearch');if(result===true){varextension=viewer.getExtension('Autodesk.InViewerSearch');console.log('Extension loaded: '+extension.id);}

Now

varpromise=viewer.loadExtension('Autodesk.InViewerSearch');// async fetch from serverpromise.then(function(extension){console.log('Extension loaded: '+extension.id);});

Note that we have not changed theviewer.getExtension()andviewer.unloadExtension()methods.

New Default Lighting for AEC Models

BIM 360 models now have a new default lighting.

Before

Now / New!

Added

Memory Management Options

You can set your browser to allocate enough memory for displaying all the 3D geometry for a 3D design.   s online so that all the 3D geometry.

Note that this feature is disabled by default.

Hereâs how to enable the feature:

Usage

varconfig3d={memory:{limit:400// in MB}};varviewer=newAutodesk.Viewing.Viewer3D(container,config3d);viewer.loadModel(modelUrl);

Another way of enabling the feature on a per-design basis, is to append aviewermemory=<value>string parameter to the browserâs URL.

Example

https://mywebsite.com/viewer/document-id-here?viewermemory=400

Note that the query string parameter will override memory limitations you define in the code.

You can check if the feature is active or not, using the newviewer.getMemoryInfo()method, that is available in the Viewer instance.

varmemInfo=viewer.getMemoryInfo();console.log(memInfo.limit);// == 400 MBconsole.log(memInfo.effectiveLimit);// >= 400 MBconsole.log(memInfo.loaded);// <= 400 MB

This method will returnnullwhen the feature is not enabled.

ViewingApplication Enhancements

The ViewingApplication class is a utility class that we recommend using when initializing the Viewer from a manifest (converted file).

This version includes 3 enhancements:

setDocument() - new method

You can now pass a plain JavaScript object to theViewingApplication:setDocument()method to initialize the Viewer, rather than using a URN.

Usage

// Fetch JSON from https://developer.api.autodesk.com/modelderivative/v2/designdata/:urn/manifest// and store it as an objectvarmanifestObject={...};// After Autodesk.Viewing.Initializer() succeedsviewerApp=newAutodesk.Viewing.ViewingApplication('MyViewerDiv');viewerApp.registerViewer(viewerApp.k3D,Autodesk.Viewing.Private.GuiViewer3D);viewerApp.setDocument(manifestObject);// Not an async method!varviewables=viewerApp.bubble.search({'type':'geometry'})viewerApp.selectItem(viewables[0].data,onItemLoadSuccess,onItemLoadFail);Show More

selectItem() - enhancement

selectItem() now supports BubbleNode objects.

Usage

varviewables=viewerApp.bubble.search({'type':'geometry'});viewerApp.selectItem(viewables[0],onItemLoadSuccess,onItemLoadFail);

getNamedViews() - new method

This helper method can be used to get all the named views from a 3D viewable. Named views are obtained from the documentâs manifest which contains camera information and a string identifier.

Usage

varnamedViews=viewerApp.getNamedViews(viewables[0].data);alert('Selecting named view: '+namedViews[0].data.name);viewerApp.selectItem(namedViews[0],onItemLoadSuccess);

Hereâs how named views shows up in the manifest:

Edge Rendering

Theviewer.setDisplayEdges(true)method renders all the edge-related parts of the model, such as borders and frames.

Fixed

Fixed decal rendering issues.

Fixed issue affecting rendering of arcs and circles in 2D models.

Fixed full screen issues that were occuring in several browsers.

Fixed issue where end users would sometimes be unable to select transparent objects.

The Measure, calibration dialog now closes when you press the ESC key.

Fixed issue where environment background would flip orientation when reflections were turned on.

Fixed issue where a rectangle markup would render in the wrong place when created from a snapped location.

Fixed issue whereviewer.search()would not work on 2D Models with properties.

Updated WebVR polyfill to comply with latest Chrome version.

Fixed iOS issue where a pinch gesture would result in a full page zoom.

Fixed issue where the CSS rule .header would affect the functionality of the Properties panel.

Version 2.14

Release Date: 2017-05-28

Changed

Improved Time To First Pixel for Fusion Models

Fusion models typically contain topology data that is used for precise measuring and snapping.
A new method (viewer.model.fetchTopology()) has been added to themodelobject, which delays downloading topology data until after the measure tool opens. This enables end users to perform non-topology related measurements while they are waiting for the topology data to download, and speeds up the process of downloading the model to the Viewer.

It is invoked by the measure extension.

Note that you can use theviewer.model.hasTopology()method to verify whether the topology data is available in the Viewer.

Added

Model Derivative API Support

Developers can now set up the Viewer to communicate directly with theModel Derivative API.

Example:

The following code snippet is an example of setting a secure proxy.

Why should you use it?

Since the Model Derivative API supports loading models referenced by theData Management API, developers do not need to add the following request headers when the Viewer retrieves referenced model data.

Fixed

Fixed issue whereconfig.wantInfoButtonhad no effect.

Fixed issue where the measure snapper and the markup snapper (green big dot) would snap to the Viewerâs edges.

Fixed issue with consolidated geometry where point and line primitive types didnât render correctly.

Fixed null pointer reference issue when unloading a model.

Fixed issue where a section plane would remain visible when isolation was active.

Fixed issue in the measure panel where the measurementâs precision would sometimes not match the one specified.

Fixed first person drag mode dialog message.

Fixed issue with setting âReverse mouse zoom directionâ.

Fixed issue where undoing an arrow markup would invert its direction.

Fixed issue where loading theAutodesk.Viewing.ZoomWindowextension would result in having 2 Zoom buttons in the toolbar UI.

Fixed issue where reflections would render partially when âProgressive model displayâ settings option was active.

Fixed issue with theAutodesk.Viewing.ZoomWindowextension where it would incorrectly zoom when there was no geometry at the rectangleâs center point.

Fixed issue with the measure panel where the cursor changed to a text icon when hovering over UI elements.

Fixed issue in IE11 where the exact position on the animation timeline was not selectable.

Version 2.13

Release Date: 2017-02-07

Changed

WebVR Extension

The VR extension is now narrowing down its support for mobile cardboard usage. As such, we will no longer fully support Vive and Oculus headsets. However, given that the extension uses the browserâs webVR API, those devices may still benefit from the extensionâs functionality.

The VR extension was renamed fromAutodesk.Viewing.webVRtoAutodesk.Viewing.WebVR.

The extension will now automatically download the WebVR polyfill when needed. The downloaded polyfill is hosted along with the Viewer.

Added

Supported Configuration Values

To help developers customize the Viewer new static methods have been added that show which configuration options are available.

The following shows the default values for those configurations:

Method

Autodesk.Viewing.createInitializerOptions()

Usage Example

// Get a default objectvarinitOptions=Autodesk.Viewing.createInitializerOptions();// Customize it!initOptions.env='AutodeskProduction';initOptions.language='es';initOptions.getAccessToken=myAccessTokenFunction;// And use itAutodesk.Viewing.Initialize(initOptions,onInitCallback);Show More

ObjectinitOptions

{env:"AutodeskProduction",getAccessToken:undefined,language:undefined,webGLHelpLink:null}

Method

Autodesk.Viewing.createViewerConfig()

Usage Example

// Get default Viewer3D configvarconfig=Autodesk.Viewing.createViewerConfig();// Customize it!config.extensions.push('MyAwesomeExtension');config.startOnInitialize=true;config.experimental.push('webVR_orbitModel');// And use itvarviewer=newAutodesk.Viewing.Private.GuiViewer3D(container,config);Show More

Objectconfig

{canvasConfig:undefined,disabledExtensions:{hyperlink:false,measure:false,section:false},experimental:[],inViewerSearchConfig:{},sharedPropertyDbPath:undefined,startOnInitialize:true,wantInfoButton:true}Show More

WebVR Extension Experimental Feature Orbit

The experimental flag enables the VR extension to change behavior so that moving the cardboard goggles will result in the VR camera orbiting around the model.

How to use

How to use

varconfig={extensions:['Autodesk.Viewing.WebVR'],experimental:['webVR_orbitModel']};varviewer=newAutodesk.Viewing.Viewer3D(container,config);

Default VR experience

WithwebVR_orbitModelflag enabled

Usability Warning

This experimental feature may result in a negative experience for end users, given that the real world head motion will not match the virtual one.

Support

We may drop support for the experimental flag in upcoming versions, in favor of a non-experimental mechanism to enable it.

Measure Calibration

The Calibration feature allows you to specify the exact distance between two points. Subsequent measurements get adjusted based on the specified calibration.

Calibration Button

You can find it in the panel that opens when selecting the Measure button.

You can find it in the panel that opens when selecting the Measure button.

Usage

In this example a user measures a distance between two points that measures 100mm.
However, the user knows that the actual distance is 50cm.
The user can use the calibration tool to specify the correct value.

In this example a user measures a distance between two points that measures 100mm.
However, the user knows that the actual distance is 50cm.
The user can use the calibration tool to specify the correct value.

Support

This feature is available for 2D and 3D models.

Limitations

Calibration is only available with the Measure tool.

Multi-Model Fast Show/Hide

New methods have been added to fully hide/show a model in the scene.
This is specially useful in multi-model scenarios.

This feature removes the need to invokeviewer.hide()to every node in the model.

Others

PROGRESS_UPDATE_EVENThas a new attribute,state, with a value fromAutodesk.Viewing.ProgressState

SHOW_EVENTandHIDE_EVENThave a new attribute,model, useful for multi-model scenarios.

Fixed

General

Fixed crash on Microsoft Edge browser.

Fixed issue where viewing a 3D model from the bottom when ground reflections is active resulted in ghosted objects not rendering.

Fixed issue where reflections would disappear when the 3D model was viewed from certain angles.

Fixed issue in the circular orbit UI where the camera roll operation was incorrect.

Fixed issue where fit-to-view operations would get delayed soon after changing between orthographic and perspective cameras.

Fixed issues with fit-to-view in 2D models.

Fixed issue where materials would not get loaded/rendered when loading a model hosted in AWS S3 (or similar static hosting).

Mobile

Fixed issue whereviewer.model.isLoadDone()would never return true, even after the model was fully loaded.

Fixed issue where transparent objects would render incorrect dark reflections.

Fixed issue where the ViewCube would get rendered while the model was being loaded.

Version 2.12

Release Date: 2017-08-10

Changed

TheFit-To-Viewaction has been changed to make 2D models cover more canvas surface area.

Before

Now

Added

WebVR Extension

With the webVR extension, users will be able to visualize 3D models in a virtual reality scene from their desktop and mobile browsers.

To use, developers will have to load the extensionAutodesk.Viewing.webVR.

Example:

HTML running in browsers that have not yet conformed to thewebVR specwill have to include apolyfill.

For mobile VR usage, the minimum recommended devices are:

iPhone 5s

Samsung Galaxy S6

Click the VR button on the toolbarâ¦

â¦then change phone orientation to landscape.

Though technically the VR extension can be enabled on any loaded model, the framerate and overall user experience will degrade when visualizing very big models, specially on mobile devices.

Consider using desktop VR solutions for big model VR experiences.

Finally, check out our next new feature,Model Consolidation, which brings performance enhancements that also apply to VR!

Model Consolidation

Example:

Limitations with model consolidation include:

It requires a significant amount of extra memory (CPU-side and GPU-side).

Consolidation will be turned off automatically when playing animations or exploding the model.

Currently, per-fragment modifications, such as ghosting and theming only work with a simple fallback. We use normal (unoptimized) rendering if any special per-fragment customization is applied.

Consolidation reduces the granularity of the scene, which conflicts with existing techniques like progressive rendering, fine-grained frustum culling, and sorting (e.g., for transparency). Although we try to achieve a good trade-off here, we cannot preserve everything 100%.

Focus in 2D Models

This feature is now available and can be used by either:

Double-clicking the element

Using the keyboard hotkeyF

Using the toolbar buttonFocus

Before

Now

Notice that in previous versions, attempting to focus on a 2D element would result in a full-model focus operation.

Model.getBulkProperties()can be configured to ignore hidden properties

Developers arenot requiredto make changes to code that uses thegetBulkProperties()function.

Example:

Fixed

Fixed issue where texts in a 2D model were drawn as an outline without fill color.

Focus will now work when loading more than one model into the scene.

Shift-clicking on empty 3D canvas will no longer clear accumulated selection.

Fixed Animation UI glitch in IE11.

Fixed issue in IE11 where the Measure PanelâsUnitTypedropdown would display âUnknownâ.

Fixed issue in IE11 where Setting PanelâsResetSettingsbutton would not be displayed.

Version 2.11

Release Date: 2016-09-27

Changed

This release contains no breaking changes.

viewer.getProperties()will now return bothattributeNameanddisplayName(if available).
TheattributeNamecan be use as a filter forviewer.search()calls.

Added

Markup Snapping:ExtensionAutodesk.Viewing.MarkupsCorehas been enhanced with snapping functionality when used to markup 2D models.
The featureâs behavior is similar to the snapping currently available in theAutodesk.Measureextension.

While mouse-hovering over geometry, a green indicator will appear over snapped geometry.

Key snapping locations include
- the two edge points along a segment
- the segmentâs mid point
- all other points along the segment

From there, a user can start drawing a markup.

TheArrow markuphas been enhanced to be drawnparallelorperpendicularto the segment being snapped.

Snapping can be applied to segments with aslope.

TheRectanglemarkup has also been enhanced with segment awareness.

ThePolyLinemarkup also benefits from snapping.

FreeHandmarkup will not snap to geometry.

Fixed

viewer.restoreState()will no longer re-render the scene when is not necessary.

Fixed issue where hotkeys would no longer work after the Viewer was initialized a second time.

Settings optionSwitch sheet color white to blackwill now work in 2D sheets where it previously didnât.

Version 2.10

Release Date: 2016-08-17

Changed

The Toolbar settings button no longer displays a popup on click.

Background and lightingdropdown andDisplay linescheckbox are now available in thePerformance and AppearanceTab in Settings Panel.

ThePerformance and AppearanceTab in Settings Panel has been redesigned:

Models loaded into the scene that specify a variation of an environment and lighting preset will now be displayed in the dropdown as a new entry:(modelsettings). This avoids confusing users that switch environments after loading a model that forces the Viewer to use specific render settings.

Added

New Hyperlink User Experience.

Geometry tagged for hyperlinking will now receive a specialized visual treatment.

For 2d sheets, geometry that contains hyperlinks will get highlighted in a light blue box.

Clicking on an hyperlink that links to another sheet will present a popup with a thumbnail of the referenced sheet.

Open the hyperlinked sheet by clicking theViewbutton. The Viewer will unload the current sheet and load the linked one.
When a model gets loaded due to an hyperlink, aBackbutton will get added to the Viewerâs top left. Click on it to navigate back to the previous sheet.
The button can be dismissed with thexbutton next to it.

Hyperlinks to external web resources will also show up in the popup. Click onViewto have your browser open a new tab to the linked resource.

New Extension:Autodesk.InViewerSearch

Extension must be explicitly loaded by developers.
Extension will add a button to the toolbar.

Click on the button to open the Search Panel. The panel may include previously searched strings.

Search results are placed into tabsThisViewandThisItem.

ThisViewrefers to the currently loaded model.ThisItemwill display results across all viewables from the loaded Document (requires usage ofViewingApplication).

Click on a search result to have its corresponding node isolated in the Viewer. The Properties Panel will show up, as well.

Additional configuration options can be specified throughinViewerSearchConfig:

config3dneeds to be passed intoviewerApp.registerViewer.

Refer toBasic ViewerStep-by-Step tutorial for more information onviewerApp.registerViewer.

Fixed

Fix issue where ghosted objects disappeared when changing a setting until some action is performed in the canvas.

Fix issue where an isolation operation triggered through Model Browser item would fail on some files.

Fix issue where some model files may never finish loading (the progress bar would never go away).

Fix issue where the Property Panel would stop working after switching sheets.

Fix issue whereAutodesk.Viewing.SELECTION_CHANGED_EVENTwould get fired twice after clearing current selection.

Minor text fixes.

Version 2.9

Release Date: 2017-08-10

Changed

API CHANGE:viewer.getScreenShot()must always receive the 3rd argument, a callback function, and no longer returns a string. See Fixes section below on why this change was required.

So far, developers would get a url to a non-resized image of the Viewer the following way:

Now in 2.9 the same can be achieved as follows:

Added

When available, render settings from loaded model will override default and user-defined preferences, in order to provide an initial load that is consistent throughout sessions.

Developers can bypass this behavior with the following code in an Extensionâsload()method:

Render settings applied from loaded model file will now have a distinctive appearance in Settings Panel:

An error message will be displayed when loading an empty SVF.

Add extension ZoomWindow, which allows to zoom into a region of the canvas by drawing a rectangular area. Extension is not loaded by default, developers must do so explicitly.

A button will get added to the toolbar whenAutodesk.Viewing.ZoomWindowextension is loaded:

It will allow a user to draw a rectangular region (click, drag, release):

On release, the camera will change focus to the rectangular region drawn:

Fixed

API CHANGE:viewer.getScreenShot()no longer returns a vertically-flipped image in Safari.

Image Based Lighting (IBL) looks different on load than on selection of same IBL.

Some models that used to have their Model Browsers empty, will now have it populated.

Isolation was not reflected in the model browser when isolating before open it.

Model Properties of Chinese (and other Unicode) characters would render incorrectly.

Version 2.8

Release Date: 2016-06-06

Changed

None

Added

Add node coloring APIs. Can be used with 2D and 3D dbIds

Swap background color of a 2D sheet from white to black; activated in Settings, Performance and appearance Tab

Fixed

[Mobile] Drop down menu arrow of the viewcube is not visible

[Mobile] Improved performance when âSmooth Navigationâ option is active on devices such as Samsung S5

Fix issue where Ground shadows were not rendered for a particular combination of settings

Some arcs were missing in 2D drawings

IE11: Show/hide this layer didnât work after you hide then show the layer once

Property Panel would sometimes not display any data

Version 2.7

Release Date: 2016-04-25

Changed

API CHANGE: Removed file extensions/MarkupsCore.min.js

API CHANGE: Removed file extensions/CommentsExt.min.js

API CHANGE: viewer3D.min.js will now include the content from
MarkupsCore.min and CommentsExt.min.js.  There is no longer need to download those two files separately.

POTENTIAL BREAKING CHANGEAvoid ultra-long frames by spreading initialization over several frames â this makes the loading animation smoother and there is no two second frame blockage. In particular, notice that:
- UI creation is delayed
- extension loading is delayed
- ViewCube initialization is delayed
- shared buffer initialization is delayed

WebSocket logger has been turned off

We now kick off data loading before WebGL initialization, so that data loading happens in parallel with the renderer initialization.

Hyperlinks pointing to another viewable within the Document will now display the Label instead of the guid whenever possible

Buttons no longer fire click event when disabled

Added

Hyperlink support

Support hosting app to instantiate multiple viewers, each with different ACM namespace

Poli-Line Markup

Poli-Cloud Markup

Measuring time to first pixel

Add ViewCube API
- It is now possible to change camera orientation through code in the same way users are able to by clicking on the ViewCubeâs faces, edges and corners.

LMV will now only write error logs into the console by default
- Developers can customize theerror levelused by LMV:

The ViewCube can now be used when using a Viewer3D instance

viewerWebView now uses non-UI lmv library (firefly.js instead of viewer3D.js) to reduce memory footprint and javascript parsing time.

Use cache.manifest in native mobile integration HTML for faster load times.

viewer.search()will now take into account property databaseâs display value in addition to the key string.

Addviewer.model.getDocumentNode()which returns a typed object wrapping manifest definition for the loaded model.

Increased Markup hit areas for easier mobile usage

Fixed

Improved Cloud Markup graphics and behaviour

Fixed Text Markup glitches in Firefox

Fixed some issues with MarkupâsrenderToCanvas()

Fix toolbar alignment when leaving markup mode

Z depth computation for orthographic view

Improved Ambient Occlusion (SSAO) on very large models

Disabled Camera Roll when drawing Markups in mobile

Improve line selection of 2d models in mobile

Fixed assert in IE when switching from zoom to pan tool

First Person tool - MessageBox not showing key control directions

2D measure: Fix selection when 2 lines were overlapping the same pixel

No longer sends âfpsâ data to ADP before it collects enough samples

OrbiDollyPanTool is no longer added twice to ToolControllerâs tool stack

Performance and Navigation Settings Panel is no longer empty when more than one viewer is present

The first time an object is selected in the canvas, it was not selected in the model browser

SAO support in Firefox 45

Removed warnings due to upgraded ADP 1.0.1 usage

Ghosted nodes no longer disappear after isolating a node while reflections are active

Double tap was not recognized as a double click in Firefox when using markups

FixedInvalid CSS property declarationin Safari

Memory management enhancements for Web mobile and Native mobile

SAO working on iOS / most-android

Transparent materials

Fix ACM usage in native iOS integration

Fusion drawings with animation crash on low end IOS

Fix an undefined reference problem in model iterator and correct removeOverlayScene on selection2d

Known issues

As of Chrome 50, multiple WebGL warning are being flushed into the browserâs console. This happens with this version of the viewer, and previous ones as well.

Drawing an Arrow Markup (or similar) using a finger swipe-up gesture in Firefox for Windows on a Surface Pro 3 triggers a browser-scroll operation instead of actually drawing the markup. We suggest using another browser to work around this limitation

```
var config3d = {
    memory: {
        limit: 1024 // in MB
    }
};
var viewer = new Autodesk.Viewing.Viewer3D(container, config3d);
viewer.loadModel( modelUrl );

```

```
{
    "limit": 20,
    "effectiveLimit": 22.238370895385742
    "loaded": 24.898095417022706
}

```

```
var result = viewer.loadExtension('Autodesk.Viewing.MarkupsCore');
if (result === true) {
    var extension = viewer.getExtension('Autodesk.Viewing.MarkupsCore');
    console.log('MarkupsCore extension is ready to be used!');
}

```

```
var promise = viewer.loadExtension('Autodesk.Viewing.MarkupsCore'); // async fetch from server
promise.then(function(extension){
   console.log('MarkupsCore extension is ready to be used!');
});

```

```
// string with markups data generated with markupsExt.generateData()
var modelMarkups = '...';

// Load the markups extension
viewer.loadExtension('Autodesk.Viewing.MarkupsCore').then(function(markupsExt){
    markupsExt.show();
    markupsExt.loadMarkups(modelMarkups, "layerA"); // Load markups onto "layerA"
    markupsExt.enterEditMode("layerA");             // Allow editing of markups in "layerA"
})

```

```
var modifiedMarkups = markupsExt.generateData();
markupsExt.leaveEditMode(); // Prevent further modifications to the markups onscreen

```

```
markupsExt.revertLayer("layerA"); // Restores markups from "layerA" to their loaded state

```

```
viewer.showViewCubeTriad(true);

```

```
// Create a custom extension
function MyAwesomeExtension(viewer, options) {
    Autodesk.Viewing.Extension.call(this, viewer, options);
}
MyAwesomeExtension.prototype = Object.create(Autodesk.Viewing.Extension.prototype);
MyAwesomeExtension.prototype.constructor = MyAwesomeExtension;

// Define what are the localization strings to add...
var locales = {

    en: {
        "Hello": "Hello!",
    },
    es: {
        "Hello": "Hola!",
    },
};

// Add locales during extension's loading phase
MyAwesomeExtension.prototype.load = function() {

    this.extendLocalization(locales);
    return true;
};

```

```
var result = viewer.loadExtension('Autodesk.InViewerSearch');
if (result === true) {
    var extension = viewer.getExtension('Autodesk.InViewerSearch');
    console.log('Extension loaded: ' + extension.id);
}

```

```
var promise = viewer.loadExtension('Autodesk.InViewerSearch'); // async fetch from server
promise.then(function(extension){
   console.log('Extension loaded: ' + extension.id);
});

```

```
var config3d = {
    memory: {
        limit: 400// in MB
    }
};
var viewer = new Autodesk.Viewing.Viewer3D(container, config3d);
viewer.loadModel( modelUrl );

```

```
var memInfo = viewer.getMemoryInfo();
console.log(memInfo.limit);          // == 400 MB
console.log(memInfo.effectiveLimit); // >= 400 MB
console.log(memInfo.loaded);         // <= 400 MB

```

```
// Fetch JSON from https://developer.api.autodesk.com/modelderivative/v2/designdata/:urn/manifest
// and store it as an object
var manifestObject = {...};

// After Autodesk.Viewing.Initializer() succeeds
viewerApp = new Autodesk.Viewing.ViewingApplication('MyViewerDiv');
viewerApp.registerViewer(viewerApp.k3D, Autodesk.Viewing.Private.GuiViewer3D);
viewerApp.setDocument(manifestObject); // Not an async method!
var viewables = viewerApp.bubble.search({'type':'geometry'})
viewerApp.selectItem(viewables[0].data, onItemLoadSuccess, onItemLoadFail);

```

```
var viewables = viewerApp.bubble.search({'type':'geometry'});
viewerApp.selectItem(viewables[0], onItemLoadSuccess, onItemLoadFail);

```

```
var namedViews = viewerApp.getNamedViews(viewables[0].data);
alert('Selecting named view: ' + namedViews[0].data.name);
viewerApp.selectItem(namedViews[0], onItemLoadSuccess);

```

```
// returns a promise that resolves when the topology data is available in memory
viewer.model.fetchTopology();

```

```
var initOptions = Autodesk.Viewing.createInitializerOptions();
initOptions.api = 'modelDerivativeV2';
Autodesk.Viewing.Initialize( initOptions.api, onSuccess );

```

```
var initOptions = Autodesk.Viewing.createInitializerOptions();
initOptions.api = 'modelDerivativeV2';
initOptions.endpoint = window.location.origin + '/lmv-proxy';
Autodesk.Viewing.Initialize( initOptions.api, onSuccess );

```

```
// no longer needed for accessing models referenced by the Data Management API.
Autodesk.Viewing.HTTP_REQUEST_HEADERS['x-ads-acm-namespace'] = 'WIPDM';
Autodesk.Viewing.HTTP_REQUEST_HEADERS['x-ads-acm-check-groups'] = 'true';

```

```
Autodesk.Viewing.createInitializerOptions()

```

```
// Get a default object
var initOptions = Autodesk.Viewing.createInitializerOptions();

// Customize it!
initOptions.env = 'AutodeskProduction';
initOptions.language = 'es';
initOptions.getAccessToken = myAccessTokenFunction;

// And use it
Autodesk.Viewing.Initialize( initOptions, onInitCallback );

```

```
{
 env: "AutodeskProduction",
 getAccessToken: undefined,
 language: undefined,
 webGLHelpLink: null
}

```

```
Autodesk.Viewing.createViewerConfig()

```

```
// Get default Viewer3D config
var config = Autodesk.Viewing.createViewerConfig();

// Customize it!
config.extensions.push('MyAwesomeExtension');
config.startOnInitialize = true;
config.experimental.push('webVR_orbitModel');

// And use it
var viewer = new Autodesk.Viewing.Private.GuiViewer3D(container, config);

```

```
{
   canvasConfig: undefined,
   disabledExtensions: {
     hyperlink: false,
     measure: false,
     section: false
   },
   experimental: [],
   inViewerSearchConfig: {},
   sharedPropertyDbPath: undefined,
   startOnInitialize: true,
   wantInfoButton: true
}

```

```
var config = {
   extensions: [ 'Autodesk.Viewing.WebVR' ],
   experimental: [ 'webVR_orbitModel' ]
};

 var viewer = new Autodesk.Viewing.Viewer3D( container, config );

```

```
// Hide model using id
viewer.hideModel( model.id );

// Show model using id
viewer.showModel( model.id );

```

```
var initializerOptions = {
    env: 'AutodeskProduction',
    extensions: [ 'Autodesk.Viewing.webVR' ]
}
Autodesk.Viewing.Initializer( initializerOptions, function() {
    // ...
});

```

```
var initializerOptions = {
    env: 'AutodeskProduction',
    useConsolidation: true,
    consolidationMemoryLimit: 150 * 1024 * 1024 // 150MB - Optional, defaults to 100 MB
}
Autodesk.Viewing.Initializer( initializerOptions, function() {
    // ...
});

```

```
var dbIds = [1, 2, 3];
var propFilter = ['name', 'dimensions'];

// Before, and still supported in 2.12 //
viewer.model.getBulkProperties( dbIds, propFilter, onSuccessCallback, onFailureCallback );

// Now as of 2.12 //
var options = {
    propFilter: propFilter,
    ignoreHidden: true
}
viewer.model.getBulkProperties( dbIds, options, onSuccessCallback, onFailureCallback );

```

```
config3d.inViewerSearchConfig = {
    relatedItemsTab:{
        enabled: true,  //if false we hide the tab
        displayName: 'This Item',
        pageSize: 20
    },
    loadedModelTab: {
        enabled: true,  //if false we hide the tab
        displayName: 'This View',
        pageSize: 50
    }
}

```

```
viewerApp.registerViewer(viewerApp.k3D, Autodesk.Viewing.Private.GuiViewer3D, config3d);

```

```
// old way, up until 2.8
var blobUrl = viewer.getScreenShot();
window.open(blobUrl);

```

```
// new way as of 2.9
var currentWidth = viewer.container.clientWidth;
var currentHeight= viewer.container.clientHeight;
viewer.getScreenShot(currentWidth, currentHeight, onImageReady);
function onImageReady(blobUrl) {
    window.open(blobUrl);
}

```

```
this.viewer.prefs.tag('ignore-producer');

```

```
viewer.loadExtension('Autodesk.Viewing.ZoomWindow');

```

```
// Set color
var ids = [1,2,3]; // Array of dbIds
var color = new THREE.Vector4(1,0,0,1); // r, g, b, intensity
viewer.setThemingColor(ids, color);

// Reset colors
viewer.clearThemingColors();

```

```
// format is "[front/back], [top/bottom], [left/right]"
viewer.setViewCube(['front']);
viewer.setViewCube(['top, right']);
viewer.setViewCube(['back, bottom, left']);

```

```
Autodesk.Viewing.Initializer( options, function() {
   var avp = Autodesk.Viewing.Private;
   avp.logger.setLevel( avp.LogLevels.NONE );
   // or
   avp.logger.setLevel( avp.LogLevels.DEBUG );
   // avp.LogLevels has additional constants
});

```


---
