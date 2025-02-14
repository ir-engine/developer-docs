# Define a system

So far, you have learned how to create **entities** and attach **components** in iR Engine. However, your project **does not yet include any logic**.

In this guide, you will define a **system**, which is responsible for executing logic in the **Entity-Component-System (ECS)** architecture.

---

## Why do you need a system?

A **system** executes logic on entities that contain specific components. Without a system, your project would **only define data** (components) but lack **behavior**.

### **What systems do in ECS**

✅ **Process** entities based on their components.  
✅ **Run automatically** based on engine timing.  
✅ **Execute logic globally** or based on conditions.  

---

## Step 1: Move logic into a function

Currently, your **entity creation logic** runs immediately when the project loads.

📌 To follow **best practices**, move it into a function.

```typescript
let initialized = false // Track execution state

function createHelloWorldEntity() {
  if (initialized) return
  initialized = true // Prevent multiple executions

  const entity = ECS.createEntity()
  ECS.setComponent(entity, NameComponent, 'hello-world')
  ECS.setComponent(entity, VisibleComponent)
  ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
  ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
}
```

**Why move logic into a function?**  
- Ensures **controlled execution**.  
- Prevents **duplicate entities**.  
- Allows **execution only when needed**.

---

## Step 2: Define a system

Now, **wrap your function inside a system**.

📌 **A system must include:**

1. A **unique identifier** (`uuid`).
2. A **function to execute**.
3. **An execution order** (e.g., after `PhysicsSystem`).

```typescript
export const HelloWorldSystem = ECS.defineSystem({
  uuid: 'helloworld.system',
  execute: createHelloWorldEntity,
  insert: { after: PhysicsSystem }
})
```

### How does this improve execution?

| **Issue** | **Before** | **Now** |
|-----------|-----------|---------|
| Logic runs **immediately** | Hard to control | Runs **when the system executes** |
| No execution control | Runs on project load | Now follows **engine timing** |
| Entities created globally | No restrictions | Can be **controlled via queries** later |

---

## Step 3: Final implementation

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

// Track execution state
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

---

## Step 4: Confirm the changes

To verify that the system executes correctly:

1. **Restart the engine** (`Ctrl + C`, then `npm run dev`).  
2. Open **Studio** at [https://localhost:3000/studio](https://localhost:3000/studio).  
3. Open the **ir-tutorial-hello** project.  
4. Create a **new scene**.  
5. ✅ **A white sphere should appear**, created by the system.

:::hint{style="success"}
🎉 **Success!**  
Your entity is now managed by a system rather than executing globally.
:::

---

## Next steps

Now that your project follows best practices with a **system**, the next step is to **control execution more effectively** using **custom components**.

📌 **Proceed to** [Create a custom component](./05_create_component.md).
