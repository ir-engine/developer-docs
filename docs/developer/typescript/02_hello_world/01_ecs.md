# The ECS pattern

iR Engine uses the **Entity-Component-System (ECS) pattern**, a **high-performance** architecture that organizes game logic into **three main parts**:

- **Entities** – Identifiers that group components.  
- **Components** – Data containers that store attributes but have no logic.  
- **Systems** – Logic processors that modify components and control behavior.

---

## Understanding ECS

Unlike **traditional object-oriented programming (OOP)**, ECS separates **data (components)** from **behavior (systems)**.

### **How ECS works**

- **Entities** are **empty containers** that hold **components**.  
- **Components** store **data** (e.g., position, appearance).  
- **Systems** apply **logic** to entities **that match specific components**.  

## Step 1: Create an entity

Creating an entity is as simple as calling the `createEntity()` function from iR Engine’s `ECS`.

```typescript
const entity = ECS.createEntity()
```

:::hint{type="info"}
**What happens here?**

- `createEntity()` generates a **unique ID**.  
- The entity itself does **not store data**—it only holds **components**. 
:::

## Step 2: Attach components

Components store data and have no behavior or unique identifiers.
To attach components to an entity, use the `setComponent` function from iR Engine’s `ECS`.

:::hint{type="info"}
The `setComponent` function does not return a value, but it:

- Adds the specified component to the entity.
- Stores the component’s data in the ECS, making it accessible through the API (e.g., `getComponent` and similar functions).
:::

### Essential components for rendering

To display an entity in iR Engine, it must have specific components:

| Component | Purpose |
|--------------|------------|
| `NameComponent` | Assigns a human-readable name. |
| `VisibleComponent` | Makes the entity visible in the scene. |
| `TransformComponent` | Defines the entity’s **position** in 3D space. |
| `PrimitiveGeometryComponent` | Assigns a **primitive shape** to the entity. |

```typescript
ECS.setComponent(entity, NameComponent, 'hello-world')
ECS.setComponent(entity, VisibleComponent)
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

:::hint{type="info"}
**Why does this work?**  

- The **entity itself does nothing**—it only holds **components**.  
- The **renderer** detects components like `VisibleComponent` and `PrimitiveGeometryComponent`, then **renders the entity**.  
:::

The following section explains how to use them.

**NameComponent**:

A `NameComponent` provides a human-readable identifier for an entity.
The assigned name appears in the **Studio** and the **debugger**, making it easier to manage entities.

```typescript
ECS.setComponent(entity, NameComponent, 'hello-world')
```

:::hint{type="info"}
An entity is an identifier, yet we assign it a `NameComponent`.
Internally, every entity is identified by a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier), which is not human-readable.
A `NameComponent` provides a readable name while keeping the UUID unchanged.
:::

**VisibleComponent**:

A `VisibleComponent` makes an entity visible on the screen. Entities without this component are ignored by the renderer.

```typescript
ECS.setComponent(entity, VisibleComponent)
```

**TransformComponent**:

A `TransformComponent` gives an entity a **position** in 3D space. Without this component, the entity cannot be placed in the world.

```typescript
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
```

:::hint{type="info"}
In technical terms, a `TransformComponent` allows an entity to be affected by [linear transformations](https://en.wikipedia.org/wiki/Linear_transformation).
:::

**PrimitiveGeometryComponent**:

A `PrimitiveGeometryComponent` assigns a **primitive shape** to an entity. Without this component, the entity lacks a [3D geometry](https://en.wikipedia.org/wiki/Polygon_mesh) and will not be rendered.

```typescript
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

:::hint{type="info"}
The `1` here represents a [`SphereGeometry`](https://github.com/ir-engine/ir-engine/blob/dev/packages/engine/src/scene/constants/GeometryTypeEnum.ts#L28) object.
In the next section, we will use a more readable name to create this component.
:::

## Step 3: Understand system logic

A **system** is responsible for processing logic on entities **that contain specific components**.

🚀 **Example:** A physics system might process **only entities with `RigidBodyComponent`**.  

You will define a **system** in the next guide.

---

## Summary

| **ECS Concept** | **Definition** |
|----------------|---------------|
| **Entity** | A unique identifier that holds components. |
| **Component** | A data container (no behavior). |
| **System** | A function that modifies components and executes logic. |

---

## What’s next?

Now that you understand **how ECS organizes logic**, it’s time to **modify an entity in iR Engine**.

📌 **Proceed to** [Work in the engine](./03_work_in_engine.md).
