# Project overview

Now that you have successfully set up your **Hello World** project in iR Engine, let’s review its structure before diving deeper.

This guide provides a high-level overview of the project’s code, so you can understand **how the engine processes your project**.

:::hint{type="info"}
💡 **Quick overview**
This is a **brief** introduction. You don’t need to understand everything now—the upcoming guides will explain each concept in detail.
:::

## Understanding the project structure

Your **Hello World** project contains the following key components:

1. **Project configuration file** (`xrengine.config.ts`) – Connects the project to the engine.
2. **Hello World script** (`src/Hello.ts`) – Defines the entity and components.
3. **Scenes and assets** – Stores all scene data.

## Reviewing the Hello World script

The core logic of your project is located in `src/Hello.ts`. This file initializes an **entity** with basic components.

:::codeblocktabs
src/Hello.ts

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'

const entity = ECS.createEntity()
ECS.setComponent(entity, NameComponent, 'hello-world')
ECS.setComponent(entity, VisibleComponent)
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```
:::

## Conceptual overview

At a high level, this script does the following:

✅ **Creates an entity** named hello-world.
✅ **Assigns a geometry component** to define its shape (a sphere).
✅ **Positions the entity** in 3D space.

## Technical overview

From a technical perspective, this script:

- **Imports iR Engine modules** to use ECS functions and components.
- **Uses the ECS pattern** to structure data and behavior.
- **Defines an entity and components** to create a visible object.
- **Registers the script with the engine** using the xrengine.config.ts file.

This connection happens in the project’s configuration file:

:::codeblocktabs
xrengine.config.ts

```typescript
worldInjection: () => import('./src/Hello') // Connects Hello.ts to the engine
```
:::

This ensures the engine loads and executes `Hello.ts` when the project starts.

## ➡️  Next steps

Your project is minimal but introduces critical engine concepts. Next, you will explore **how iR Engine structures data and logic using the ECS pattern**.

📌 Continue to [The ECS pattern](./01_ecs.md) to understand the engine’s core architecture.
