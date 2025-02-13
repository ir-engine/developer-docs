# Developer quickstart

Welcome to the developer quickstart. This guide prepares you for your first experience with the engine as a TypeScript developer. By the end of this guide, you will have:&#x20;

1. Installed the iR Engine in your local environment
2. Accessed the default projects to start developing
3. Get your first hands-on experience with the introduction of a tutorial project

## Installation

The iR Engine is a web application; the following steps will help you install and run a local version. Note that some steps of this tutorial may differ from how you use the engine in production.

:::hint{type="info"}
ℹ️    **Info**

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
3. Once the installation is complete, open [https://localhost:3000](https://localhost:3000) in your web browser to access the engine.

## Introduction to Projects

Projects are folders that contain all your custom code, assets, and scenes. Working with projects is the way you extend the engine's functionalities.&#x20;

These projects are hosted in the following directory:&#x20;

```shell
packages/projects/projects/
```

### Access default projects

iR Engine includes default projects and pre-installed scenes, which you can explore with Studio, the engine's editor and asset management interface.

**To access the default project:**

1. Open the Studio by navigating to [https://localhost:3000/studio](https://localhost:3000/studio).
2. Click on the default project card.
3. Select a scene to open it.

**To test the project's functionality:**

1. Click the **Play** button to enter the scene with an avatar.
2. Move around using the **WASD** keys or by clicking on the ground.

Your project is now ready for editing.

## Next steps

You can now start working with the engine and extend its functionality by following the ECS pattern. We suggest you run through the [Hello World tutorial](./02_hello/index.md)&#x20;

## Install and run the tutorial project

To learn the basics of the engine, you can start by cloning the introductory tutorial project, which we cover in the [Hello World in iR Engine](./02_hello/index.md) tutorial. This project provides a step-by-step introduction to iR Engine’s features.

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

### Verify the installation

To confirm that the Hello World project is running correctly, follow these steps:

1. Open the project in **Studio** by clicking on its card.
2. Create a new empty scene.
3. If the installation was successful, a white sphere should appear in the center of the scene.

:::hint{type="info"}
You can also enter the scene and move around with an avatar by pressing the **Play** button in the editor.
:::

## Next steps

With your tutorial project running, you can go through the [Hello World in iR Engine](./02_hello/index.md) tutorial to learn how the engine works and the basics of the ECS pattern. You will also create your first component and more.
