# Define a Query

Queries are a core feature of the **Entity Component System (ECS)** pattern in iR Engine.

A **query** allows you to retrieve **all entities that contain a specific set of components**.
This provides a dynamic way to access entities instead of manually tracking them.

## How queries work

Queries are essential when working with the engine. In essence, a query:

1. Accepts a **list of components** as input.
2. Returns **a function** that retrieves all entities containing those components.
3. Can be used anywhere in your code to fetch **matching entities**.

### Important rules

When using queries, consider the following:

- The query **only matches entities that have ALL the specified components**.
- Even if you are searching for **one component**, you must pass it inside an **array**.
- The query **does not create entities**; it only retrieves existing ones.

Queries return a **JavaScript Generator**, which efficiently fetches matching entities without creating unnecessary objects.

To learn more, see [JavaScript Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#generator_functions).

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

## Step 2: Using queries to process entities

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

Queries return a **JavaScript Generator**, which improves performance by retrieving entities dynamically instead of storing them all at once in memory.

To learn more, see [JavaScript Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#generator_functions).

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

### Why does this matter?

Using a generator instead of an array provides several benefits:

- **Performance** – Entities are retrieved **only when needed**, reducing memory usage.
- **Efficiency** – ECS ensures that **only relevant entities** are processed.
- **Scalability** – The engine handles thousands of entities without loading them all at once.

## Step 3: Update the system definition

Now, modify the system to execute the updated function.

```typescript
export const HelloSystem = ECS.defineSystem({
  uuid: 'ee.tutorial.HelloSystem',
  execute: hello,
  insert: { after: PhysicsSystem }
})

```

### How does this solve the problem?

| **Issue**                 | **Before**            | **Now**                                            |
| :------------------------ | :-------------------- | :------------------------------------------------- |
| Entities created manually | Used `createEntity()` | Now retrieved dynamically via `defineQuery()`      |
| Code ran globally         | Executed every time   | Now runs **only for specific entities**            |
| No filtering mechanism    | Affected all scenes   | Now **restricted to entities with HelloComponent** |

## Step 4: Loading the component

For the system to process the entity, the `HelloComponent` must be present in the scene. The `hello-final` scene in the `ir-tutorial-hello` project already includes this component, so the system can recognize and process the correct entity.

### Scene setup

The `hello-final` scene includes:

- An entity with **HelloComponent**.
- A saved scene file that ensures the entity is available when the project runs.

With this setup, the system runs only inside `hello-final`, preventing unwanted behavior in other scenes.

## Step 5: Confirm the implementation

Follow these steps to verify that queries and components are working correctly:

1. **Run the project** and open the `hello-final` scene.
   ✅ The sphere should appear in the scene.
2. **Switch to another scene** (e.g., `default-project/apartment`).
   ✅ The sphere should not appear.

If everything works as expected, the system is correctly filtering and processing entities based on their components.

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

