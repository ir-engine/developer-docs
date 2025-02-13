# Adding  Systems

So far, you have used the **Entity-Component-System (ECS)** pattern by:

- Creating an **entity**:
  ```typescript
  const entity = ECS.createEntity()
  ```
- Adding **components** to the entity:
  ```typescript
  ECS.setComponent(entity, NameComponent, 'hello-world')
  ECS.setComponent(entity, VisibleComponent)
  ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
  ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
  ```
- Running the project within iR Engine.

However, you **haven’t defined a system** yet.

## Why do you need a system?

In the [ECS pattern](), **systems** define the logic and behavior of an application.
For simplicity, the previous tutorial skipped this step, but the **best practice** is to organize ECS logic within a system.

:::hint{type="warning"}
⚠️    **Warning**

Directly modifying ECS data in the module's top-level scope is an **anti-pattern**.
Data mutation operations should occur inside a **controlled context**, such as a the&#x20;
:::

## Creating your first system

To correctly create and manage the **Hello World sphere**, follow these steps:

1. Move entity creation into a **function**.
2. Define a **system** to execute that function.
3. Insert the system into the engine to run after the `PhysicsSystem`.

## Step 1: Create a function

Move your entity creation logic into a function and ensure it runs **only once**.

```typescript
let initialized = false // Track if the function has already run

function createHelloWorldEntity() {
  if (initialized) return
  initialized = true // Mark as initialized

  const entity = ECS.createEntity()
  ECS.setComponent(entity, NameComponent, 'hello-world')
  ECS.setComponent(entity, VisibleComponent)
  ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
  ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
}
```

## Step 2: Define a system

A **system** runs a function within the ECS context.
Define your system using `defineSystem`, specifying:

- `uuid`: A unique system identifier.
- `execute`: The function to run (`createHelloWorldEntity`).
- `insert`: When to execute the system (after `PhysicsSystem`).

```typescript
export const HelloWorldSystem = ECS.defineSystem({
  uuid: 'helloworld.system',
  execute: createHelloWorldEntity,
  insert: { after: PhysicsSystem }
})
```

## Final implementation

After applying these changes, your full `Hello0.ts` file should look like this:

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { PhysicsSystem } from '@ir-engine/packages/spatial/src/physics/PhysicsModule'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'

// Track if the function has already executed
let initialized = false

// Function to create the entity
function createHelloWorldEntity() {
  if (initialized) return
  initialized = true

  const entity = ECS.createEntity()
  ECS.setComponent(entity, NameComponent, 'hello-world')
  ECS.setComponent(entity, VisibleComponent)
  ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
  ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
}

// Define the system to execute the function
export const HelloWorldSystem = ECS.defineSystem({
  uuid: 'helloworld.system',
  execute: createHelloWorldEntity,
  insert: { after: PhysicsSystem }
})
```

