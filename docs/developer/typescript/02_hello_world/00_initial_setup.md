# 1. Initial setup

The [TypeScript Quickstart](./../index.md) guide helped us create a project and run iR Engine for the first time. Now, let's review what we have before diving deeper.

:::hint{type="info"}
This is a brief overview. Skim through this page without focusing on details—the next sections will explain these concepts in depth.
:::

## Hello world code

At this stage, our project contains the following code:

:::codeblocktabs
ir-tutorial-hello/src/Hello0.ts

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

This example project performs the following actions:

- Creates an entity named `hello-world`.
- Assigns a **primitive geometry component** (a sphere) to the entity.
- Sets the sphere's **position** in the scene.

## Technical overview

From a technical perspective, this code:

- Imports **iR Engine's TypeScript modules**.
- Uses the **Entity-Component-System (ECS) pattern**.
- Creates an **entity**.
- Adds **components** to the entity.

This code is integrated into the engine via the <a href="https://github.com/ir-engine/ir-tutorial-hello/blob/dev/xrengine.config.ts" target="_blank">`xrengine.config.ts`</a> file, which contains the following line of code:

```typescript
worldInjection: () => import('./src/Hello') // Connects Hello.ts to the engine
```

## What’s next?

This project is as minimal as possible, but it already introduces key concepts.

Next, we'll break down how each part of the code works and begin programming with iR Engine. By the end of this guide, you will:

- Understand the fundamental concepts behind iR Engine.
- Write and modify code within an iR Engine project.
- Be prepared to continue learning through the **iR Engine: Basics** guide.

Let's get started! 🚀