# Quickstart guide

Welcome to the developer quickstart. This guide prepares you for your first experience with the engine as a TypeScript developer. This guide prepares you to:

1. Install the iR Engine in your local environment
2. Access the default projects to test and develop
3. Introduce you to the **Hello world tutorial** for your first hands-on experience with the engine

## Initial setup

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

Projects are hosted in the following directory:&#x20;

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
