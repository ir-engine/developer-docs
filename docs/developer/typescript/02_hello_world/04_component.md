# Create a custom Component

Your **current implementation has a critical issue**:  
The sphere appears in **every scene**, instead of being controlled within a specific scene.

This happens because iR Engine **executes projects globally**, and you have not defined when the sphere should be created.

## Understanding the problem

Right now, your implementation does the following:

1. **Creates a file** (`src/Hello.ts`) that contains the code.
2. **Connects the code to the engine** using the project’s configuration file.
3. **Defines a system** using `defineSystem`.
4. **Creates the sphere directly** inside the system.
5. ❌ **Does not define the sphere as a component**.
6. ❌ **Does not associate the sphere with a specific scene**.

Because of **steps 5 and 6**, the sphere appears in **every project that runs in the engine**, which is not the expected behavior.

### Why does this happen?

iR Engine **runs projects globally**, but your sphere should only appear when explicitly needed in a scene.

To achieve this, you need to define a **custom component** that controls when and where the sphere is created.

:::hint{type="warning"}
⚠️    **Important**

Without a component, the engine has no way to determine when to create the sphere.

The current implementation lacks a trigger to tell the system when to execute.
:::

## The solution: Locking the sphere behind a component

To restrict the sphere’s execution, you need to:

1. **Define a custom component** to track when the sphere should appear.
2. **Use a query** to execute logic only when an entity has this component.
3. **Ensure the system only runs under the right conditions**.

By following this approach, your system will **only create the sphere when needed** rather than running globally.

***

## Step 1: Define a custom component

A **component** is a structured way to store information about an entity in the engine. For this example, define a new component that tracks whether the sphere has been initialized.

We'll call this component `HelloComponent`.

```typescript
export const HelloComponent = ECS.defineComponent({
  name: 'ee.tutorial.HelloComponent',
  jsonID: 'EE_tutorial_hello',
  onInit: () => ({ initialized: false }) // Default state
})
```

Right now, this component **does nothing on its own**. You will connect it to your system in the next step.

### What does this do?

| **Property** | **Description**                                                      |
| :----------- | :------------------------------------------------------------------- |
| `name`       | A unique identifier for the component.                               |
| `jsonID`     | An internal identifier used by the engine.                           |
| `onInit`     | Defines the default state of the component (initialized as `false`). |

The `name` and `jsonID` follow a specific convention, which will be explained in a later guide.

***

## Step 2: Store component state

To track whether the sphere has been created, retrieve and update the component’s state inside your system.

```typescript
let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
if (initialized.value) continue
initialized.set(true)  // Set initialized to true
```

### Why is this necessary?

- `initialized.value` retrieves the current value of the component.
- `initialized.set(true)` updates the component’s state in a way that is compatible with iR Engine.

Using `initialized.set(true)` ensures that state changes are properly managed within the ECS system.

:::hint{type="info"}
ℹ️    **Info**

You will learn more about State in the [State Management](./../03_basics_tutorial/05_state_management.md) guide on the [Engine basics tutorial](./../03_basics_tutorial/index.md).
:::

:::hint{type="success"}
📝    **Checkpoint**

At this point, you have a component that stores an initialization state.
:::

Next, modify the system to **only execute when this component is present**.

***

## Step 3: Restrict execution using a query

Modify the system so that it **only runs for entities that have the `HelloComponent`.

This prevents the sphere from being created in every scene.

```typescript
export const HelloWorldSystem = ECS.defineSystem({
  uuid: 'helloworld.system',
  query: { entities: [HelloComponent] }, // Run only when HelloComponent is present
  execute: ({ entities }) => {
    for (const entity of entities) {
      let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
      if (initialized.value) continue
      initialized.set(true)

      ECS.setComponent(entity, NameComponent, 'hello-world')
      ECS.setComponent(entity, VisibleComponent)
      ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
      ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
    }
  },
  insert: { after: PhysicsSystem }
})
```

### How does this solve the problem?

| **Issue**                     | **Before**                              | **Now**                                        |
| :---------------------------- | :-------------------------------------- | :--------------------------------------------- |
| Sphere appears in every scene | System runs globally                    | Runs **only for entities with HelloComponent** |
| No way to track state         | Used an external `initialized` variable | State is now inside the component              |
| Unrestricted execution        | System always executes                  | System only runs when needed                   |

Now, the sphere is only created when an entity **has the HelloComponent**, ensuring correct behavior.

***

## Final implementation

After making these changes, your `Hello.ts` file should look like this:

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { PhysicsSystem } from '@ir-engine/packages/spatial/src/physics/PhysicsModule'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'

// Define the custom component
export const HelloComponent = ECS.defineComponent({
  name: 'ee.tutorial.HelloComponent',
  jsonID: 'EE_tutorial_hello',
  onInit: () => ({ initialized: false })
})

// Define the system with a query for HelloComponent
export const HelloWorldSystem = ECS.defineSystem({
  uuid: 'helloworld.system',
  query: { entities: [HelloComponent] },
  execute: ({ entities }) => {
    for (const entity of entities) {
      let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
      if (initialized.value) continue
      initialized.set(true)

      ECS.setComponent(entity, NameComponent, 'hello-world')
      ECS.setComponent(entity, VisibleComponent)
      ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
      ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
    }
  },
  insert: { after: PhysicsSystem }
})
```

