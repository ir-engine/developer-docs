# 3. Start working in the engine

To start working on a project in the engine, you need to follow three key steps:

1. **Install iR Engine**
2. **Install or create a project**
3. **Modify and run the project’s source code**

For installation instructions, consult the [Installation](./../../../../manual/01_install/index.md) section on the [Technical manual](./../../../../manual/index.md)

## Requirements and dependencies

Throughout this guide, we frequently use `git` and `npm`. If you followed the [TypeScript Quickstart](./../index.md) guide or [installed](./../../../../manual/01_install/index.md) the iR Engine manually, you already have both tools installed.

## Installing and running projects

iR Engine can be extended by using **projects**, which function similarly to projects in other game engines but are modular, like `npm` packages. Projects are `npm` packages too.

:::hint{type="info"}
**ℹ️    Info**

Each project's source code is executed **globally**.
This will become an important concept later in this guide.
:::

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

This is also the recommended method for working with projects of your authoring–instead of starting from  **Hello World**, you can use a pre-made template as a starting point.

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

Every project includes an <a href="https://github.com/ir-engine/ir-tutorial-hello/xrengine.config.ts" target="_blank">`xrengine.config.ts`</a> file, which defines how the project interacts with iR Engine.

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

## **Importing required modules**

In this tutorial, we are adding a sphere primitive to the scene. This section explains the importing process.&#x20;

:::hint{type="info"}
ℹ️    **Tip**

For now, focus on understanding the concepts exclusively. We'll get hands on with the project in the <a href="" target="_blank">Modifying the source code</a> section in just a bit.
:::

### **Importing spatial components**

Since the sphere is a **spatial** object, we must import several components from the <a href="https://github.com/ir-engine/ir-engine/tree/dev/packages/spatial" target="_blank">spatial** **engine module</a>, as well as our sphere from the <a href="https://github.com/ir-engine/ir-engine/blob/dev/packages/engine/src/scene/components/PrimitiveGeometryComponent.ts" target="_blank">PrimitiveGeometry component </a>from the <a href="https://github.com/ir-engine/ir-engine/tree/dev/packages/engine/src/scene/components" target="_blank">components</a> module.

```typescript
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
```

### **Importing ECS utilities**

Since we are working with the **ECS pattern**, we also need to import the ECS management functions. iR Engine provides a way to import all ECS-related functions simultaneously via the `ECS` **namespace**.

```typescript
import { ECS } from '@ir-engine/packages/ecs'
```

## Modifying the source code

So far, we have only reviewed how our example works—we haven’t modified any source code yet.

:::hint{type="info"}
This guide follows a **project-based learning** approach.
From this point onward, you will actively modify the `ir-tutorial-hello` project as you progress.
:::

Let's start with a simple change: replacing the hardcoded `1` in `PrimitiveGeometryComponent` with a readable **enum value**.

### **Modifying the sphere geometry type**

1. Open the file `ir-tutorial-hello/src/Hello0.ts` in a text editor.
2. Import `GeometryTypeEnum` from the `scene/constants/` submodule.
3. Replace `1` with `GeometryTypeEnum.SphereGeometry`.

Try implementing these changes on your own before checking the solution. If you’re unsure where the enum is located, use these hints:

```none
/ The full path to the GeometryTypeEnum:
'@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'

// Getting the ID number of a Sphere by its enum name:
GeometryTypeEnum.SphereGeometry

// To verify your changes, set the geometry to a cylinder instead:
GeometryTypeEnum.CylinderGeometry
```

:::hint{type="info"}
You only need to restart the engine when **installing** a new project.
When modifying source code, simply **refresh the webpage** to see your changes.
:::

### Solution

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

### **Confirming the changes**

1. Open [http://localhost:3000/studio](http://localhost:3000/studio).
2. Open the **ir-tutorial-hello** project.
3. Create a new scene.
4. A **white sphere** should appear in the center.

