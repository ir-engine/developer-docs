# Coding style and best practices

Structure your code effectively to make it easier to read, maintain, and collaborate on.

## Code formatting and linting

Use automated formatting and linting tools to keep your code clean and consistent:

- <a href="https://prettier.io/docs/install" target="_blank">Prettier</a>: Automatically formats your code.
- <a href="https://www.npmjs.com/package/eslint" target="_blank">ESLint</a>: Analyzes your code and enforces best practices.

Ensure both tools are installed and enabled in your development environment.

***

## Naming conventions

Using clear and structured names helps you understand, navigate, and maintain your code. Follow these guidelines to name different elements correctly.

### Capitalization styles

Use these capitalization rules to keep your code consistent:

| Type                  | Convention     | Example           |
| :-------------------- | :------------- | :---------------- |
| Classes & definitions | `CapitalCase`  | `CapsuleGeometry` |
| Variables & functions | `camelCase`    | `createEntity()`  |
| Enums & namespaces    | `CAPITAL_CASE` | `ENTITY_TYPE`     |

### Component and system naming

Follow a **dot-separated format** when naming components and systems. This keeps them organized and easy to identify.

Each name should include:

- **Namespace**: The name of your organization or module.
- **Project**: The project to which the system belongs.
- **System name**: A meaningful identifier for the system.

📌 **Example:**

```plaintext
ir-engine.tutorial.HelloSystem
```

For multi-word names, avoid underscores and use camelCase within dot-separated segments:

```plaintext
ir-engine.multiwordexample.HelloSystem
```

### Component JSON identifiers (`jsonID`)

The `jsonID` field follows a different convention because iR Engine uses it for **glTF extensions**. Follow these rules:

- Use underscores (`_`) instead of dots (`.`).
- Write the namespace in uppercase (`IR_ENGINE`).
- Use lowercase with underscores for the project and component names.

📌 **Example:**

```plaintext
IR_ENGINE_TUTORIAL_HELLO
```

For multi-word names:

```plaintext
IR_ENGINE_MULTIWORD_EXAMPLE_HELLO
```

### Avoid unnecessary abbreviations or underscores

Keep names clear and easy to read:

✅ Use full words unless it's a common acronym (e.g., `HTTPRequest`).
✅ Avoid shortening words unnecessarily (`PlayerController`, not `PlrCtrl`).
✅ Use camelCase instead of underscores for variable names (`playerPosition`, not `player_position`).

Good naming makes your code easier to understand at a glance.

***

## TypeScript typing

Always use **explicit TypeScript types** for functions, variables, and objects. This prevents errors and makes your code easier to maintain.

***

## Use arrow functions

Arrow functions make your code more concise and readable. They are the preferred way to define functions inside objects or systems.

### Arrow function (recommended)

```typescript
const HelloSystem = ECS.defineSystem({
  uuid: 'ir-engine.tutorial.HelloSystem',
  execute: () => {
    console.log("Hello World")
  },
  insert: { after: PhysicsSystem }
})
```

### Regular function (less common in iR Engine)

```typescript
function sayHello() { console.log("Hello World") }

const HelloSystem = ECS.defineSystem({
  uuid: 'ir-engine.tutorial.HelloSystem',
  execute: sayHello,
  insert: { after: PhysicsSystem }
})
```

:::hint{type="info"}
ℹ️  **Why use arrow functions?**

- Makes your code **shorter** and **easier to read**.
- Matches the **style used across iR Engine’s codebase**.
- Works well for **defining system logic**.
:::

Use arrow functions whenever you define functions inside objects or systems.

***

## Apply best practices

Here’s an example of a properly structured system following all best practices.

```typescript
import { ECS } from '@ir-engine/packages/ecs'
import { PhysicsSystem } from '@ir-engine/packages/spatial/src/physics/PhysicsModule'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'

// Define a structured component name
export const HelloComponent = ECS.defineComponent({
  name: 'ir-engine.tutorial.HelloComponent',
  jsonID: 'IR_ENGINE_TUTORIAL_HELLO',
  onInit: () => ({ initialized: false })
})

// Define the query to find entities with HelloComponent
const helloQuery = ECS.defineQuery([HelloComponent])

// Define the system using arrow functions
export const HelloSystem = ECS.defineSystem({
  uuid: 'ir-engine.tutorial.HelloSystem',
  execute: () => {
    for (const entity of helloQuery()) {
      let { initialized } = ECS.getMutableComponent(entity, HelloComponent)
      if (initialized.value) continue
      initialized.set(true)

      ECS.setComponent(entity, NameComponent, 'ir-engine.hello-entity')
      ECS.setComponent(entity, VisibleComponent)
      ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 1, 0) })
      ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
    }
  },
  insert: { after: PhysicsSystem }
})
```

## ➡️  Next steps

Now that you’ve structured your code correctly, continue learning about [Custom Components](./02_custom_component.md).
