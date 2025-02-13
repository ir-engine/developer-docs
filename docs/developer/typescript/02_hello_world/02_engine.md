# Start working in the engine

In this guide, you will finally get your hands on your first task to learn the engine by modifying a project's source code, importing components, setting up ECS, and modifying an object's geometry.

## Requirements and dependencies

In general, to start working on a project in the engine, you need to follow three key steps:

1. **Install iR Engine**
2. **Install or create a project**
3. **Modify and run the project’s source code**

:::hint{type="info"}
ℹ️    **Info**

For installation instructions, consult the [Installation]() section on the [Technical manual.]()
:::

**Additional requirements**

Throughout this guide, we frequently use `git` and `npm`. If you followed the [Developer quickstart](./../01_quickstart/index.md) or installed the iR Engine manually, you already have both tools installed.

## Installing and running projects

The iR Engine can be extended by using **projects**, which function similarly to projects in other game engines but are modular, just like `npm` packages. Projects, in fact, are `npm` packages, too.

:::hint{type="info"}
**ℹ️    Info**

Each project's source code is executed **globally**.
This will become an important concept later in this guide.
:::

### Projects directory

The engine automatically scans for projects inside the `/packages/projects/projects/` directory. This means that we can install and run new projects by executing the following commands inside our iR Engine installation folder:

```bash
git clone https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
npm run dev
```

:::hint{type="info"}
**ℹ️    Important**

Whenever you install a new project, you must stop and restart the engine for the changes to take effect.
:::

These commands perform the following actions:

1. Clone the project’s repository so iR Engine can load it.
2. Install all required `npm` packages.
3. Run a local development instance of iR Engine.

:::hint{type="success"}
📝    **Checkpoint**

- [ ] Did you clone the repository with no issues?



*If you run into any trouble with the commands above, consult the *[Troubleshooting](./../../../manual/01_install/050_advanced/07_troubleshooting.md)* guides for guidance.*
:::

This is also the recommended method for working with projects of your authoring–instead of starting from **Hello World**, you can use a pre-made template as a starting point.

:::hint{type="info"}
**ℹ️    Info**

In the [TypeScript Quickstart](./../index.md) document, we cloned only the `Step0` branch of the `ir-tutorial-hello` project instead of the entire repository.
This was done by using `-b Step0` in the `git clone` command:

```bash
git clone -b Step0 https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
```

For your own projects, this is not required, and you can clone without `-b Step0` on your command.
:::

## Configuring  projects

To integrate a project's source code with iR Engine, two critical steps are required:

1. **Importing iR Engine’s modules**
2. **Exporting the code so the engine can run it**

### Project configuration file

Every project includes an <a href="https://github.com/ir-engine/ir-tutorial-hello/xrengine.config.ts" target="_blank">xrengine.config.ts</a>  file, which defines how the project interacts with iR Engine.

The key part to note in this file is that our `src/Hello0.ts` file is connected to the engine through this configuration. See the code below:

```typescript
import type { ProjectConfigInterface } from '@ir-engine/packages/projects/ProjectConfigInterface'

const config: ProjectConfigInterface = {
  onEvent: undefined,
  thumbnail: '/static/ir-engine_thumbnail.jpg',
  routes: {},
  services: undefined,
  databaseSeed: undefined,
  // highlight-start
  worldInjection: () => import('./src/Hello0')  // Import our Hello World code
  // highlight-end
}

export default config
```

For now, it is enough to understand that this file connects your project’s code to the engine. More details will be covered in the [Beyond the Basics]() guide.

## Importing required modules

In this tutorial, we are adding a sphere primitive to the scene. This section explains the importing process.&#x20;

:::hint{type="info"}
ℹ️    **Tip**

For now, focus on understanding the concepts exclusively. We'll get hands-on experience with the project when we start modifying the source must also
:::

### Importing spatial components

Since the sphere is a **spatial** object, we must import several components from the [spatial engine module](https://github.com/ir-engine/ir-engine/tree/dev/packages/spatial), as well as our sphere from the [PrimitiveGeometry component](https://github.com/ir-engine/ir-engine/blob/dev/packages/engine/src/scene/components/PrimitiveGeometryComponent.ts) from the [components](https://github.com/ir-engine/ir-engine/tree/dev/packages/engine/src/scene/components) module.

```typescript
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
```

### Importing ECS utilities

Since we are working with the **ECS pattern**, we must also import the ECS management functions. iR Engine provides a way to import all ECS-related functions simultaneously via the `ECS` **namespace**.

```typescript
import { ECS } from '@ir-engine/packages/ecs'
```

## Modifying the source code

So far, we have only reviewed how our example works—we haven’t modified any source code yet. Let's start with a simple task: **modifying the sphere geometry**.

:::hint{type="info"}
ℹ️    **Info**

This guide follows a **project-based learning** approach.
From this point onward, you will actively modify the `ir-tutorial-hello` project as you progress.
:::

### Modifying the sphere geometry type

:::hint{type="success"}
📝    **Hands-on task**

Let's start with a simple change: replacing the hardcoded `1` in `PrimitiveGeometryComponent` with a readable **enum value**.&#x20;
:::

These are the instructions:

- [ ] Open the file `ir-tutorial-hello/src/Hello0.ts` in a text editor.
- [ ] Import `GeometryTypeEnum` from the `scene/constants/` submodule.
- [ ] Replace `1` with `GeometryTypeEnum.SphereGeometry`.

:::hint{type="info"}
✅    **Need help?**

You can jump straight to the [Outcome]() section to see the process in place or try implementing these changes on your own.&#x20;
:::

### Where is the enum?

If you’re unsure where the enum is located, use these hints:

```none
/ The full path to the GeometryTypeEnum:
'@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'

// Getting the ID number of a Sphere by its enum name:
GeometryTypeEnum.SphereGeometry

// To verify your changes, set the geometry to a cylinder instead:
GeometryTypeEnum.CylinderGeometry
```

:::hint{type="info"}
ℹ️    **Info**

You only need to restart the engine when **installing** a new project.
When modifying source code, simply **refresh the webpage** to see your changes.
:::

### Outcome

Once updated, the **import section** should look like this:

```typescript
// Other imports
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
// highlight-start
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'
// highlight-end
```

The **PrimitiveGeometryComponent** assignment should be updated as follows:

```typescript
const entity = ECS.createEntity()
// Other setComponent calls
// highlight-start
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
// highlight-end
```

### Confirming the changes

To see your new changes in place:

1. Open [http://localhost:3000/studio](http://localhost:3000/studio).
2. Open the **ir-tutorial-hello** project.
3. Create a new scene.
4. A **white sphere** should appear in the center.

:::hint{type="success"}
👏.   Congratulations!

You have had your first experience working in the engine. Now, let's learn to add logic through [Systems](./03_system.md).
:::



