# The ECS pattern

Now that your Hello World project is set up, it is time to understand the most crucial concept of the engine: **The ECS pattern.**

This guide provides an overview of how ECS **organizes** **entities, components, and systems** to define behavior.

***

## What is the ECS pattern?

The **Entity-Component-System (ECS) pattern** is a **data-driven architecture** that separates **objects**, **their properties**, and **their behavior**.

| **Concept**   | **Definition**                                                       |
| :------------ | :------------------------------------------------------------------- |
| **Entity**    | A unique identifier that groups components together.                 |
| **Component** | Stores **data** (no behavior). Multiple components define an entity. |
| **System**    | Defines **logic** and modifies entities with specific components.    |

***

## How ECS works

1. **Entities** are just **IDs** (e.g., `entity_123`).
2. **Components** hold **data** (e.g., `MediaComponent`, `CameraSettingsComponent`).
3. **Systems** process entities with **matching components** (e.g., `PhysicsSystem` updates entities with `CollisionComponent`).

This separation allows for **efficient, modular, and reusable** code.

:::hint{type="info"}
💡 **Why ECS?**

Unlike traditional object-oriented programming, ECS avoids deep inheritance hierarchies. Instead, it **stores data separately** and **applies logic only when needed**, improving performance.
:::

***

## Creating an entity

To create an entity, use the `createEntity()` function:

```typescript
const entity = ECS.createEntity()
```

This **generates a unique ID** for an entity.

***

## Adding components

Components define **what an entity is**, not what it does. Components store **data only** and have no behavior.

To attach components to an entity, use `setComponent()`:

```typescript
ECS.setComponent(entity, NameComponent, 'hello-world')
ECS.setComponent(entity, VisibleComponent)
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

***

### Essential components in iR Engine

To display an entity in a scene, iR Engine requires specific components:

| **Component**                                      | **Purpose**                                                  |
| :------------------------------------------------- | :----------------------------------------------------------- |
| `NameComponent`                                    | Assigns a human-readable name to the entity.                 |
| `VisibleComponent`                                 | Ensures the entity is **visible** in the scene.              |
| `TransformComponent`                               | Defines the **position, rotation, and scale** of the entity. |
| `PrimitiveGeometryComponent` or a  `MeshComponent` | Assigns a **basic 3D shape** or a **mesh **to the entity.    |

See more details about these components in the following section.

***

## Using each component

### NameComponent

Defines a readable identifier:

```typescript
ECS.setComponent(entity, NameComponent, 'hello-world')
```

Entities internally use **UUIDs**. A `NameComponent` provides a human-readable name for debugging.

***

### VisibleComponent

Ensures the entity **renders in the scene**:

```typescript
ECS.setComponent(entity, VisibleComponent)
```

Without this component, the entity **exists in memory** but will **not be displayed**.

***

### TransformComponent

Defines **position, rotation, and scale**:

```typescript
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
```

This determines **where** the entity appears in the scene.

:::hint{type="info"}
💡 **Technical note**

`TransformComponent` uses [transformation matrices](https://en.wikipedia.org/wiki/Transformation_matrix) to control positioning.
:::

***

### PrimitiveGeometryComponent

Assigns a **basic 3D shape**:

```tsx
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

The number `1` represents a [`SphereGeometry`](https://github.com/ir-engine/ir-engine/blob/dev/packages/engine/src/scene/constants/GeometryTypeEnum.ts#L28).

***

## Understand system logic

A **system** is responsible for processing logic on entities **that contain specific components**.

:::hint{type="info"}
🚀  **Example**&#x20;

A physics system might process **only entities with **`RigidBodyComponent`.
:::

You will define a **system** in the following guides.

***

## Summary

| **ECS Concept** | **Definition**                                          |
| :-------------- | :------------------------------------------------------ |
| **Entity**      | A unique identifier that holds components.              |
| **Component**   | A data container (no behavior).                         |
| **System**      | A function that modifies components and executes logic. |

***

## ➡️  Next steps

Now that you understand **ECS**, it’s time to start your first task, **modify an entity in iR Engine**.&#x20;

Continue to [Work in the engine](./02_engine.md) to modify your project’s source code**,** and start interacting with the application.
