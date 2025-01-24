<!-- import UbuntuInstall from '../../../_partials/installUbuntu.md' -->
<!-- import DefaultProjects from '../../../_partials/defaultProjects.md' -->

# TypeScript Quickstart
This QuickStart guide will teach you the basics of iR Engine, and how to run the engine for the first time.  

## Installation
<!-- Start of partial: UbuntuInstall -->
:::important
Ethereal Engine is a web application.  
We are going to install and run a local version of the engine.  
But this setup might not reflect how you will use the engine on a day to day basis.  
:::

:::note
These installation instructions assume you are using Ubuntu Linux.  
You can find alternative _(and more advanced)_ installation instructions for [Windows](/manual/install/windowsWSL), [Mac](/manual/install/macOSX) and [Linux](/manual/install/linux) in the Manual.
:::

If you are on Ubuntu Linux, there is an automatic installation script to setup and run a local version of Ethereal Engine.  
Open a terminal window and run these two lines:  
> Make sure that you open the terminal in the folder where you want to install the engine
```bash
wget https://raw.githubusercontent.com/EtherealEngine/etherealengine/dev/scripts/ubuntu-install.sh && bash -i ./ubuntu-install.sh
npm run reinit && npm run dev
```
You can now open Ethereal Engine on your web browser by navigating to https://localhost:3000

<!-- End of partial: UbuntuInstall -->

## Projects
### Default Projects
<!-- Start of partial: DefaultProjects -->
Ethereal Engine has a few scenes that are installed by default.  
With the engine running, open the Studio by navigating to https://localhost:3000/studio, and you will see the engine's default project listed in that page.  

Lets give it a test run:
- Open the default project by clicking on its card
- Click on one of the scenes to open it
- Click on the `Play` button to enter the scene with an Avatar
- Move around the scene with `WASD` and/or clicking on the ground

<!-- End of partial: DefaultProjects -->

### Install and Run the tutorial project
Whether you installed the engine with method above, or with the installation instructions for your specific system, your next step will be to install the tutorial project.

:::danger
This `HelloWorld` project should never be installed in a remote deployment.  
A local version of the engine is required to follow this introductory tutorial.  
:::

The previous commands will have the engine running locally.  
Lets stop it by pressing `Ctrl+C`, and then run these commands to install and run the tutorial's template project:
```bash
git clone -b Step0 https://github.com/EtherealEngine/ee-tutorial-hello packages/projects/projects/ee-tutorial-hello
npm run dev
```

You should now be able to see the `ee-tutorial-hello` project listed in iR Engine's Studio by navigating to https://localhost:3000/studio.

## Confirm the installation
Lets make sure that our `hello world` code is running:
1. Open the project from the Studio by clicking on its card
2. Create a new empty scene

You will know that the code is running if you can see a white sphere in the middle of the scene.  

:::note
You can also enter the scene and move around with an avatar by pressing the `Play` button in the editor like we did before.  
:::
