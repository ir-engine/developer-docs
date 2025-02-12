# The ECS Pattern

# The ECS pattern

The [Entity-Component-System (ECS)](https://en.wikipedia.org/wiki/Entity_component_system) is a software architecture pattern used to structure code efficiently.

In this pattern:

- **Logic** is represented as `systems`, which define the application's behavior.
- **Data** is stored in `components`, which do not have behavior or identifiers.
- **Entities** are identifiers that group components together.

:::hint{type="info"}
**How this works**:

- The ECS pattern represents [objects](https://en.wikipedia.org/wiki/Object_\(computer_science\)) by attaching components (data) to an entity (identifier) without behavior
- Application behavior is controlled by separate systems (logic) that process that data.
- Systems do not need to know where data comes from—they only operate on the components available to them.
:::

## Creating an entity

Creating an entity is as simple as calling the `createEntity()` function from iR Engine’s `ECS`.
This function returns an identifier that allows grouping components into a unique object.

```typescript
const entity = ECS.createEntity()
```

## Adding components

Components store data and have no behavior or unique identifiers.
To attach components to an entity, use the `setComponent` function from iR Engine’s `ECS`.

:::hint{type="info"}
The `setComponent` function does not return a value, but it:

- Adds the specified component to the entity.
- Stores the component’s data in the ECS, making it accessible through the API (e.g., `getComponent` and similar functions).
:::

To display an entity in iR Engine, it must have specific components:

- **VisibleComponent**
- **TransformComponent**
- **PrimitiveGeometryComponent** or **MeshComponent**
- *(Optional)* **NameComponent**: Not required but recommended for better debugging.

### NameComponent

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

### VisibleComponent

A `VisibleComponent` makes an entity visible on the screen. Entities without this component are ignored by the renderer.

```typescript
ECS.setComponent(entity, VisibleComponent)
```

### TransformComponent

A `TransformComponent` gives an entity a **position** in 3D space. Without this component, the entity cannot be placed in the world.

```typescript
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
```

:::hint{type="info"}
In technical terms, a `TransformComponent` allows an entity to be affected by [linear transformations](https://en.wikipedia.org/wiki/Linear_transformation).
:::

### PrimitiveGeometryComponent

A `PrimitiveGeometryComponent` assigns a **primitive shape** to an entity. Without this component, the entity lacks a [3D geometry](https://en.wikipedia.org/wiki/Polygon_mesh) and will not be rendered.

```typescript
ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

:::hint{type="info"}
The `1` here represents a [`SphereGeometry`](https://github.com/ir-engine/ir-engine/blob/dev/packages/engine/src/scene/constants/GeometryTypeEnum.ts#L28) object.
In the next section, we will use a more readable name to create this component.
:::

