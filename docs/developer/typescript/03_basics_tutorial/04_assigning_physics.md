# Add physics to an entity

This guide walks you through adding physics components to your entity, allowing it to behave like a real-world object.&#x20;

:::hint{type="info"}
ℹ️ **Complete** [Hello World tutorial](./../02_hello_world/index.md) **first**

This guide uses the Hello.ts file from the [Hello World tutorial](./../02_hello_world/index.md) project to teach you how to add physics to an entity. If you haven't completed such tutorial, you use the code snippet from the introduction as a reference to follow along with this guide.
:::

## Introduction

In iR Engine, entities do not have physics properties by default. If you want an entity to interact with forces like gravity, collisions, and movement, you need to explicitly define its physics behavior.&#x20;

For this excersice we'll work with the last implementation of the Hello.ts file from [Hello World tutorial](./../02_hello_world/index.md):

::::codedrawer{title="Hello.ts file"}
:::codeblocktabs-examples
```javascript
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
:::

:::codeblocktabs-responses
```javascript
```
:::
::::

***

## The problem: A static object

So far, we have **created an entity** and assigned it a **shape**. However, the entity does not interact with the world—it simply exists without movement or collision.

- **Issue**: The entity is **visible** but **does not respond to gravity or collisions**.
- **Expected behavior**: The entity should **fall, collide, and respond to forces** in the environment.

You can confirm this by running the scene and **walking into the sphere with your avatar**. Right now, the avatar **walks through the object** because it has no physics properties.

***

## Solution: Adding physics components

To fix this issue, you need to **assign physics properties** to the sphere by adding two key components:

1. `RigidBodyComponent` – Enables **physics simulation** (gravity, forces, movement).
2. `ColliderComponent` – Defines a **collision shape**, allowing objects to interact physically.

Additionally, you will adjust the **spawn height** of the sphere so it falls naturally due to gravity.

***

## Step 1: Import physics components

Physics components belong to the **spatial physics module** in iR Engine. Import them into your script:

```typescript
import { RigidBodyComponent } from '@ir-engine/packages/spatial/src/physics/components/RigidBodyComponent'
import { ColliderComponent } from '@ir-engine/packages/spatial/src/physics/components/ColliderComponent'
```

***

## Step 2: Assign physics properties

### 1. Enable rigid body physics

The **RigidBodyComponent** allows the sphere to move dynamically in response to forces and collisions. Set its **type** to `'dynamic'` so it responds to gravity and forces.

```typescript
ECS.setComponent(entity, RigidBodyComponent, { type: 'dynamic' })
```

**What this does:**

✅ The sphere **falls** to the ground.

✅ It can be **pushed by other objects**.

***

### 2. Define a collider shape

The **ColliderComponent** assigns a **collision shape** to the sphere, preventing other objects from passing through it. Use a **sphere collider** to match the shape of the entity.

```typescript
ECS.setComponent(entity, ColliderComponent, { shape: 'sphere' })
```

**What this does:**

- The sphere **collides** with other objects.
- The avatar **can no longer walk through it**.

***

### 3. Adjust the spawn position

Currently, the sphere spawns **at ground level**, making it difficult to observe physics effects. Move it **3 units above the ground** so you can see it fall.

```tsx
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 3, 0) })
```

**What this does:**

- The sphere starts **above the ground**.
- Gravity pulls it down **when the scene starts**.

***

## Step 3: Confirm physics interactions

Once you have added the physics components, **test the behavior** to ensure everything is working correctly.

### Expected behaviors:

✔ The sphere **falls** to the ground due to gravity.

✔ When the avatar walks into the sphere, **it moves instead of passing through**.

### If something is wrong:

⚠ If the sphere **doesn’t fall**, ensure the `RigidBodyComponent` is set to `type: 'dynamic'`.

⚠ If the avatar **still walks through the sphere**, double-check the `ColliderComponent`.

***

## Final implementation

After making these updates, your system definition should look like this:

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'
import { PhysicsSystem } from '@ir-engine/packages/spatial'

// Import physics components
import { RigidBodyComponent } from '@ir-engine/packages/spatial/src/physics/components/RigidBodyComponent'
import { ColliderComponent } from '@ir-engine/packages/spatial/src/physics/components/ColliderComponent'

// Define the custom component
export const PhysicsComponent = ECS.defineComponent({
  name: 'ir-engine.tutorial.PhysicsComponent',
  jsonID: 'IR_ENGINE_TUTORIAL_PHYSICS',
  onInit: () => ({ initialized: false })
})

// Define the query to find entities with PhysicsComponent
const physicsQuery = ECS.defineQuery([PhysicsComponent])

// Define the system to apply physics
export const PhysicsSystem = ECS.defineSystem({
  uuid: 'ir-engine.tutorial.PhysicsSystem',
  execute: () => {
    for (const entity of physicsQuery()) {
      let { initialized } = ECS.getMutableComponent(entity, PhysicsComponent)
      if (initialized.value) continue
      initialized.set(true)

      ECS.setComponent(entity, NameComponent, 'ir-engine.physics-entity')
      ECS.setComponent(entity, VisibleComponent)

      // Set initial position (3 units above ground)
      ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 3, 0) })

      // Assign primitive geometry
      ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })

      // Enable physics
      ECS.setComponent(entity, RigidBodyComponent, { type: 'dynamic' })
      ECS.setComponent(entity, ColliderComponent, { shape: 'sphere' })
    }
  },
  insert: { after: PhysicsSystem }
})
```

***

## Summary

✅ **Entities need physics components** to interact with forces like gravity.

✅ Use `RigidBodyComponent` to define movement and behavior.

✅ Use `ColliderComponent` to specify how an entity collides.

✅ Adjust the **spawn position** to test gravity and movement.

✅ The entity should now **fall** and **collide with the avatar** in the scene.

***

## ➡️  Next steps

[State Management](./05_state_management.md)&#x20;

