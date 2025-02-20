# Create a custom Component

So far, your **Hello World system** successfully creates a sphere. However, there is a **critical issue:**

- ❌ The sphere is created **globally in every scene**.
- ✅ The goal is to **create it only in specific scenes**.

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

:::hint{type="info"}
ℹ️  **Info**

Without a component, the engine has no way to determine when to create the sphere. The current implementation lacks a trigger to tell the system when to execute.
:::

## The solution: Locking the sphere behind a component

You need to define a **custom component** that controls when and where the sphere is created.

To restrict the sphere’s execution, you need to:

1. **Define a custom component** to track when the sphere should appear.
2. **Use a query** to execute logic only when an entity has this component.
3. **Ensure the system only runs under the right conditions**.

By following this approach, your system will only create the sphere when needed rather than running globally.

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

Right now, this component does nothing on its own. You will connect it to your system in the next step.

### What does this do?

| **Property** | **Description**                                                      |
| :----------- | :------------------------------------------------------------------- |
| `name`       | A unique identifier for the component.                               |
| `jsonID`     | An internal identifier used by the engine.                           |
| `onInit`     | Defines the default state of the component (initialized as `false`). |

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
💡 **State management in ECS**

Component states must be managed through `getMutableComponent()` to ensure proper updates.
:::

:::hint{type="success"}
📝  **Checkpoint**

At this point, you have a component that stores an initialization state.
:::

Next, modify the system to **only execute when this component is present**.

***

## Step 3: Restrict execution using a query

Modify the system so that it **only runs for entities that have the** `HelloComponent`. This prevents the sphere from being created in every scene.

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

### How does this fix the issue?

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

## Confirming the changes

To verify your system is now **scene-specific**:

1. Run the project in iR Engine.
2. Open the "**hello-final**"** **scene (pre-configured to include `HelloComponent`).
3. ✅ The **sphere should appear in the scene**.
4. Switch to another scene (e.g., `default-project/apartment`).
5. ✅ **The sphere should not appear** in unrelated scenes.

If both conditions are met, your system is now correctly **scene-specific**.

:::hint{type="success"}
🎉 You have successfully restricted the system’s execution using components!
:::

## ➡️  Next steps

Now that the sphere creation is **locked behind a component**, let’s optimize execution using **queries**.

📌  Continue to [Define a Query](./05_query.md).
