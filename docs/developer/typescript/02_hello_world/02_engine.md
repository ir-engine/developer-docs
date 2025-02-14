# Work in the engine

Now that you understand the **project structure**, it’s time to start working with iR Engine by modifying a project’s source code.

## Requirements and dependencies

Before making modifications, ensure you have:

✅ **iR Engine installed** ([Developer Quickstart](./../01_quickstart/index.md)).  
✅ **The Hello World project cloned and running** ([Initial setup](./00_initial_setup.md)).  

Throughout this guide, you will use `git` and `npm` frequently. If you followed the **installation guide**, these tools are already installed.

:::hint{style="info"}
💡 **Need installation help?**  
Refer to the **[Technical Manual](./../../../manual/01_install/index.md)** for full installation instructions.
:::

## Installing and running projects

The iR Engine can be extended by using **projects**, which function similarly to projects in other game engines but are modular, just like `npm` packages. Projects, in fact, are `npm` packages, too.

:::hint{type="info"}
**ℹ️    Info**

Each project's source code is executed **globally**.
This will become an important concept later in this guide.
:::

### Projects directory

The engine automatically scans for projects in: 

```
/packages/projects/projects/
```

To install and run a project inside iR Engine, execute the following:

```bash
git clone https://github.com/ir-engine/ir-tutorial-hello packages/projects/projects/ir-tutorial-hello
npm run dev
```

:::hint{type="info"}
**ℹ️    Important**

If you install a new project, **restart the engine** for changes to take effect.
:::

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

## Configuring the project

To integrate a project's source code with iR Engine, two critical steps are required:

1. **Importing iR Engine’s modules**
2. **Exporting the code so the engine can run it**

### Project configuration file

Each project has an **`xrengine.config.ts`** file, which defines how the project interacts with iR Engine.

```typescript title="xrengine.config.ts"
import type { ProjectConfigInterface } from '@ir-engine/packages/projects/ProjectConfigInterface'

const config: ProjectConfigInterface = {
  onEvent: undefined,
  thumbnail: '/static/ir-engine_thumbnail.jpg',
  routes: {},
  services: undefined,
  databaseSeed: undefined,
  worldInjection: () => import('./src/Hello')  // Connects Hello.ts to the engine
}

export default config
```

📌 **This file registers the project with the engine, allowing it to execute custom logic.**  
You will explore this configuration further in the **Beyond the Basics** guide.

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

