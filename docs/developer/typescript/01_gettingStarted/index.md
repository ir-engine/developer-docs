# TypeScript quickstart

This guide walks you through the basics of iR Engine and how to install and run it for the first time.

## Installation

Before you begin, note that iR Engine is a web application. The following steps will help you install and run a local version, which may differ from how you use the engine in production.

:::hint{type="info"}
These instructions are for Ubuntu Linux. For Windows, macOS, or other Linux distributions, refer to the [installation manual]().
:::

### Install iR Engine on Ubuntu

To install and run a local version of iR Engine on Ubuntu, follow these steps:

1. Open a terminal in the directory where you want to install the engine.
2. Run the following command:
   ```bash
   wget https://raw.githubusercontent.com/ir-engine/ir-engine/dev/scripts/ubuntu-install.sh && bash -i ./ubuntu-install.sh
   npm run reinit && npm run dev
   ```
3. Once the installation is complete, open [https://localhost:3000](https://localhost:3000) in your web browser to access iR Engine.

## Projects

iR Engine includes default projects and scenes that are pre-installed. You can explore them through the Studio.

### Default projects

To access the default project and test its functionality:

1. Open the Studio by navigating to [https://localhost:3000/studio](https://localhost:3000/studio).
2. Click on the default project card.
3. Select a scene to open it.
4. Click the **Play** button to enter the scene with an avatar.
5. Move around using the **WASD** keys or by clicking on the ground.

### Install and run the tutorial project

To follow the introductory tutorial, you need to install the **Hello World** project. This project provides a step-by-step introduction to iR Engine’s features.

:::hint{type="danger"}
This tutorial project should only be installed locally. Do not install it in a remote deployment.
:::

1. Stop the running engine by pressing **Ctrl+C** in the terminal.
2. Install the tutorial project by running:
   ```bash
   git clone -b Step0 https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
   npm run dev
   ```
3. Open [https://localhost:3000/studio](https://localhost:3000/studio), and you should see the **ir-tutorial-hello** project listed.

## Verify the installation

To confirm that the Hello World project is running correctly, follow these steps:

1. Open the project in **Studio** by clicking on its card.
2. Create a new empty scene.
3. If the installation was successful, a white sphere should appear in the center of the scene.

:::hint{type="info"}
You can also enter the scene and move around with an avatar by pressing the **Play** button in the editor.
:::

