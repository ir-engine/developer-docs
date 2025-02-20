# Defining components

Learn how to define custom components in iR Engine using `defineComponent()`, structure component data with `ComponentPartial`, and configure essential properties.

## Introduction

A **component** is a fundamental part of the **Entity Component System (ECS)** pattern in iR Engine. Components store data that describes **an entity’s properties and behaviors**, allowing systems to process and update them efficiently.

***

## Creating a component

To define a new component, use `defineComponent()`, which accepts a `ComponentPartial` object containing key configuration fields.

### Example: Defining a simple component

The following code creates a **HelloComponent** that tracks whether an entity has been initialized:

```tsx
const HelloComponent = ECS.defineComponent({
  name: 'ir-engine.tutorial.HelloComponent',
  jsonID: 'IR_ENGINE_TUTORIAL_HELLO',
  onInit: () => ({ initialized: false }) // Default state
})
```

This component assigns an `initialized` property to entities, allowing a system to determine whether an entity has already processed specific logic.

***

## Understanding `ComponentPartial`

The `defineComponent()` function accepts a **ComponentPartial** object, which provides flexible definitions for components.

:::hint{type="info"}
ℹ️  **What are TypeScript Partials?**

A **partial** in TypeScript means that some properties are optional during definition but are required when used.

📌 **Reference:** See [TypeScript.Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype) for more details.
:::

The `ComponentPartial` object includes several key properties that define how a component behaves.

***

## Core component properties

Below is a breakdown of the **most important properties** in `ComponentPartial` and how they affect component behavior.

### 1. `name` (Required)

The `name` property defines a **human-readable label** for the component. This name appears in **Studio, debugging tools, and logs**, making it easier to identify.

```tsx
name: 'ir-engine.tutorial.HelloComponent'
```

:::hint{type="info"}
📌 **Follow the naming conventions** outlined in [Coding style and best practices](./01_styling_code.md).
:::

***

### 2. `jsonID` (Optional, but recommended)

The `jsonID` property assigns an **internal identifier** used when **serializing components into JSON**. This is required for **glTF-based exports and scene persistence**.

```tsx
jsonID: 'IR_ENGINE_TUTORIAL_HELLO'
```

:::hint{type="info"}
📌 **Follow the required JSON naming format** outlined in [Coding Style and Best Practices](https://www.notion.so/styling#jsonid-naming-requirements).
:::

### 3. `onInit` (Optional, but commonly used)

The `onInit` property defines a function that executes **once** when the component is added to an entity. It sets the **initial state** of the component.

```tsx
onInit: () => ({ initialized: false })
```

This function **returns an object** that describes the component’s **runtime data structure**.

**How does **`onInit`** work?**

The `onInit` function returns the shape of the component’s runtime data, which has the type `Schema`.

```tsx
onInit?: (this: SoAComponentType<Schema>, entity: Entity) => ComponentType & OnInitValidateNotState<ComponentType>
// this    : `@internal` The component partial itself.
// entity  : The entity to which this Component is being assigned.
// returns : The `Schema` (aka shape) of the component's runtime data.
```

This means that `onInit` is responsible for defining **what kind of data the component holds**. You can use this to store **state variables, metadata, or any relevant information** about an entity.

***

## Additional component properties

While the properties above define the **basic functionality** of a component, `defineComponent()` supports several **advanced features**.

| **Property** | **Purpose**                                              |
| :----------- | :------------------------------------------------------- |
| `schema`     | Defines the **expected structure** of component data.    |
| `toJSON`     | **Serializes** the component’s data when saving a scene. |
| `onSet`      | Triggers when the component’s data updates.              |
| `onRemove`   | Triggers when the component is removed from an entity.   |
| `reactor`    | Defines **React-based side effects** for the component.  |
| `errors`     | Stores error-handling information.                       |

You don’t need to use these properties in every component. However, understanding them helps when creating more complex systems.

***

## Full `ComponentPartial` interface

The following is the full interface for `ComponentPartial`, as defined in <a href="https://github.com/ir-engine/ir-engine/blob/dev/packages/ecs/src/ComponentFunctions.ts" target="_blank">ComponentFunctions.ts</a>.

```tsx
{
  name: string
  jsonID?: string
  onInit?: (this: SoAComponentType<Schema>, entity: Entity) => ComponentType & OnInitValidateNotState<ComponentType>

  // Defines the expected structure of the component’s runtime data
  schema?: Schema

  // Converts component data to JSON format when saving a scene
  toJSON?: (entity: Entity, component: State<ComponentType>) => JSON

  // Handles updates to the component’s data
  onSet?: (entity: Entity, component: State<ComponentType>, json?: SetJSON) => void

  // Handles cleanup logic when the component is removed from an entity
  onRemove?: (entity: Entity, component: State<ComponentType>) => void | Promise<void>

  // Defines React-based logic related to this component
  reactor?: React.FC

  errors?: ErrorTypes[]
}
```

***

## ➡️  Next steps

Now that you know how to define a custom component, the next step is **using queries** to find and process entities dynamically.

📌 Continue to [Define a Query](./../02_hello_world/05_query.md).
