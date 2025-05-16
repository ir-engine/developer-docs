# Initial setup

In this tutorial, you will use the <a href="https://github.com/ir-engine/ir-tutorial-hello" target="_blank">Hello World project</a> to learn how to work with iR Engine. This project provides a minimal working example to help you explore the engine’s core concepts.

## Prerequisites

Before starting, ensure you have completed the [**Quickstart guide**]() and have iR Engine installed.

:::hint{type="warning"}
⚠️ **Stop any running instances of iR Engine**
Before proceeding, stop any active instances of iR Engine by pressing **Ctrl + C** in your terminal.
:::

## Step 1: Install and run the tutorial project

To install and run the tutorial project locally, execute the following commands inside your iR Engine installation folder:

```bash
npm run clone-project -- --url https://github.com/ir-engine/ir-tutorial-hello
npm run dev
```

Once the installation is complete, open [https://localhost:3000/studio](https://localhost:3000/studio) in your web browser. You should see the **ir-tutorial-hello** project listed.

:::hint{type="warning"}
⚠️ **Local installation only**
This tutorial project should only be installed locally. **Do not** install it in a remote deployment.
:::

## Step 2: Verify the installation

To confirm that the Hello World project is running correctly:

1. Open **Studio** and click on the **ir-tutorial-hello** project card.
2. Create a **new empty scene**.
3. If the installation was successful, a **white sphere** should appear in the center of the scene.

:::hint{type="info"}
💡 **Tip**
You can enter the scene and move around with an avatar by pressing the **Play** button in the editor.
:::

## ➡️  Next steps

Now that your tutorial project is running, proceed to the [Project overview](./00_project_code_overview.md) to understand the structure of your cloned codebase.
