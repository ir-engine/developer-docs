# Define a Query

Now that you've **locked sphere creation behind a component**, it's time to optimize execution further using **queries**.

## What are queries in ECS?

A **query** allows you to retrieve **all entities that contain a specific set of components**.
This provides a dynamic way to access entities instead of manually tracking them.

### How queries work

A **query** does the following:

1. Accepts a **list of components** as input.
2. Returns **a function** that retrieves all entities containing those components.
3. Can be used anywhere in your code to fetch **matching entities**.

### Important rules

When using queries, consider the following:

- The query **only matches entities that have ALL the specified components**.
- Even if you are searching for **one component**, you must pass it inside an **array**.
- The query **does not create entities**; it only retrieves existing ones.

:::hint{type="info"}
ℹ️  **Info**

Queries return a **JavaScript Generator**, which efficiently fetches matching entities without creating unnecessary objects. To learn more, see [JavaScript Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#generator_functions).
:::

## Step 1: Define a query

Define a query using `defineQuery()`, specifying the **component(s)** you want to search for.

```typescript
// Define the query that will find all entities with HelloComponent
const helloQuery = ECS.defineQuery([HelloComponent])
```

This query **returns all entities** that have the `HelloComponent`.

### Understanding the query definition

Here's a table to help you understand the query:

| **Function**        | **Description**                                                   |
| :------------------ | :---------------------------------------------------------------- |
| defineQuery(\[...]) | Creates a query to filter entities based on components.           |
| \[HelloComponent]   | The query will match **only** entities containing this component. |
| helloQuery()        | When called, it returns **all matching entities**.                |

At this stage, the query **does not run automatically**. You need to integrate it into your system.

## Step 2: Use the  query in a system to process entities

Before integrating the query into a system, it's important to understand how to retrieve and process its results.

### Iterating over query results

Calling `helloQuery()` does not return an array of entities. Instead, it returns a **generator function** that dynamically **yields** each matching entity one at a time.

To process all entities returned by the query, use a `for...of` loop:

```typescript
for (const entity of helloQuery()) {
  // Process each entity
}
```

This loop retrieves **each entity that contains the HelloComponent**, one at a time. The engine handles this efficiently, ensuring that only relevant entities are returned.

Now, use the query in a system to retrieve and modify the correct entities.

```typescript
function hello() {
  for (const entity of helloQuery()) {
    // Check if the entity has already been initialized
    let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
    if (initialized.value) continue
    initialized.set(true)  // Mark as initialized

    // Add required components to the entity
    ECS.setComponent(entity, NameComponent, 'ee.tutorial.hello-entity')
    ECS.setComponent(entity, VisibleComponent)
    ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
    ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
  }
}
```

## Step 3: Integrate the query into the system

Now, modify the system to execute the **hello()** function.

```typescript
export const HelloSystem = ECS.defineSystem({
  uuid: 'ee.tutorial.HelloSystem',
  execute: hello,
  insert: { after: PhysicsSystem }
})
```

### **How does this improve the system?**

| **Problem**                      | **Before**                     | **Now**                                       |
| -------------------------------- | ------------------------------ | --------------------------------------------- |
| Entities were processed manually | Had to store entity references | Query retrieves matching entities dynamically |
| Inefficient execution            | System executed every frame    | Now only executes for relevant entities       |
| No filtering mechanism           | Processed all entities         | Now limited to entities with `HelloComponent` |

## Step 4: Load the component in a scene

For the system to process entities, **the **`HelloComponent`** must exist** in a scene.

The `hello-final` scene (inside `ir-tutorial-hello`) is already **pre-configured** to include `HelloComponent`.

When this scene is loaded, the query will **automatically retrieve the correct entity**.

***

## Step 5: Confirm the changes

To verify that queries and components are working:

1. **Run the project** and open the `hello-final` scene.
   ✅ The sphere **should appear** in the scene.
2. **Switch to another scene** (e.g., `default-project/apartment`).
   ✅ The sphere **should not appear**.

If both conditions are met, the query is **correctly filtering entities**.

🎉 **You have successfully optimized execution using queries!**

***

## Final implementation

After making these updates, your `Hello.ts` file should look like this:

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'
import { PhysicsSystem } from '@ir-engine/packages/spatial'

// Define the custom component
export const HelloComponent = ECS.defineComponent({
  name: 'ee.tutorial.HelloComponent',
  jsonID: 'EE_tutorial_hello',
  onInit: () => ({ initialized: false })
})

// Define the query to find entities with HelloComponent
const helloQuery = ECS.defineQuery([HelloComponent])

// Define the function to execute
const hello = () => {
  for (const entity of helloQuery()) {
    let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
    if (initialized.value) continue
    initialized.set(true)

    ECS.setComponent(entity, NameComponent, 'ee.tutorial.hello-entity')
    ECS.setComponent(entity, VisibleComponent)
    ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
    ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
  }
}

// Define the system
export const HelloSystem = ECS.defineSystem({
  uuid: 'ee.tutorial.HelloSystem',
  execute: hello,
  insert: { after: PhysicsSystem }
})
```

## Summary

:::hint{type="success"}
✅    **You have now successfully implemented queries in iR Engine!**

By using `defineQuery()`, your system now **retrieves entities dynamically instead of creating them manually**.
:::

### Key takeaways

- Queries **find existing entities** based on components.
- Systems **process only matching entities**, reducing unnecessary execution.
- The sphere now **only appears in the correct scene**, rather than globally.
- Using **JavaScript Generators** improves performance by avoiding unnecessary data storage.

***

## ➡️  Next steps

Now that you have structured **entities, components, systems, and queries**, it's time to **recap what you've learned and move forward**.

📌 Continue to [Recap and next steps](./90_recap.md) .
