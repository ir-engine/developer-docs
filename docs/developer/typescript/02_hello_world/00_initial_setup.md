# Initial setup

In this tutorial, you will set up the **Hello World** project, which serves as your introduction to working with iR Engine.

---

## Prerequisites

Before proceeding, ensure that you have:

✅ Completed the **[Developer Quickstart](./../01_quickstart/index.md)**.  
✅ Installed iR Engine successfully on your system.  

:::hint{style="info"}
💡 **Important**  
Before continuing, stop any running instances of iR Engine by pressing **Ctrl + C** in your terminal.
:::

---

## Step 1: Install and run the tutorial project

To install and start the **Hello World** tutorial project, execute the following commands:

```bash
git clone -b Step0 https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
npm run dev
```

### **Verify installation**
1. Open **Studio** at [https://localhost:3000/studio](https://localhost:3000/studio).
2. Locate the **ir-tutorial-hello** project in the list.

:::hint{style="danger"}
⚠️ **Warning**  
This tutorial project is for **local development only**.  
**Do not install it in a remote deployment**.
:::

---

## Step 2: Confirm installation success

To verify that the project is running correctly:

1. Open the project in **Studio** by clicking on its card.  
2. Create a **new empty scene**.  
3. ✅ If installed correctly, a **white sphere** should appear in the center of the scene.

:::hint{style="info"}
💡 **Tip**  
You can enter the scene and control an avatar by pressing the **Play** button in the editor.
:::

---

## Next steps

Now that your tutorial project is running, proceed to **[Project overview](./01_project_overview.md)** to understand the basics of your cloned codebase.
