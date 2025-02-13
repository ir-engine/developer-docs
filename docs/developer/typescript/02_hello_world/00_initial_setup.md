# Install the Tutorial Project

For this tutorial, you will use the introductory <a href="https://github.com/ir-engine/ir-tutorial-hello" target="_blank">**Hellow World project**</a> to learn your way around the engine.

## Prerequisites

Ensure you have completed the [Developer quickstart](./../01_quickstart/index.md) and that you have the engine installed.

:::hint{type="info"}
ℹ️    **Important**

Before you proceed, end any instances of the engine you might have running by pressing **Ctrl + C** on your terminal.
:::

## Step 1. Install and run the tutorial project

To install the tutorial project and run your local environment, execute the following commands.

1. Install the tutorial project by running:
   ```bash
   git clone -b Step0 https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
   npm run dev
   ```
2. Open [https://localhost:3000/studio](https://localhost:3000/studio), and you should see the **ir-tutorial-hello** project listed.

:::hint{type="danger"}
⚠️    **Warning **

This tutorial project should only be installed locally. Do not install it in a remote deployment.
:::

## Step 2. Verify the installation

To confirm that the Hello World project is running correctly, follow these steps:

1. Open the project in **Studio** by clicking on its card.
2. Create a new empty scene.
3. If the installation was successful, a white sphere should appear in the center of the scene.

:::hint{type="info"}
💡    **Tip**

You can also enter the scene and move around with an avatar by pressing the **Play** button in the editor.
:::

## Next steps

With your tutorial project running, proceed now to the Project code overview to understand the basics of your cloned codebase.
