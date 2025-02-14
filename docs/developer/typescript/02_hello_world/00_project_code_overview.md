# Project overview

Now that you have installed the **Hello World** tutorial project, let’s examine its structure before diving deeper.

---

## Understanding the project

The [Developer Quickstart](./../01_quickstart/index.md) helped you install and run iR Engine.  
This section provides a **brief overview** of the tutorial project.

:::hint{style="info"}
💡 **Info**  
This is a **high-level preview**. Do not worry about understanding every detail—each concept will be explained in upcoming sections.
:::

---

## Reviewing the project code

Your cloned **Hello World** project includes the following code:

```typescript title="ir-tutorial-hello/src/Hello.ts"
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

This file (`Hello.ts`) contains the **core logic** of the tutorial project.

---

## Conceptual overview

This example project performs the following actions:

✅ **Creates an entity** named `hello-world`.  
✅ **Assigns a primitive geometry component** (a sphere) to the entity.  
✅ **Positions the sphere** in the scene at coordinates `(0,1,0)`.  

---

## Technical overview

From a **technical** perspective, the code:

✅ **Imports iR Engine's TypeScript modules**.  
✅ **Uses the Entity-Component-System (ECS) pattern**.  
✅ **Creates an entity and assigns multiple components**.  
✅ **Connects the script to the engine via `xrengine.config.ts`**.

This line in `xrengine.config.ts` integrates the script with iR Engine:

```typescript
worldInjection: () => import('./src/Hello') // Connects Hello.ts to the engine
```

---

## What’s next?

This project is as minimal as possible, but it already introduces **core concepts**.

Next, we will **break down how each part of the code works** and start programming in iR Engine.

✅ **Proceed to [The ECS pattern](./02_ecs_pattern.md)** to learn how iR Engine structures logic. 🚀
