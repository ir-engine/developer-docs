# State Management

This guide introduces **state**, explains how it works in iR Engine, and covers different approaches to managing local and global state.

## Introduction

State management is a fundamental concept in programming, allowing applications to store and modify data over time. In iR Engine, managing state efficiently ensures components interact smoothly and maintain consistent behavior.

***

## Understanding state

State allows applications to store and update data dynamically, ensuring that components can react to changes over time. Let's explore what state is and how it works in iR Engine.

### What is state?

[State](https://en.wikipedia.org/wiki/State_\(computer_science\)) refers to information that a program retains and updates as it runs. It allows the application to **remember** past actions and maintain continuity.

For example, to track elapsed time in an application, we could store a variable that updates every second:

```ts
let seconds = 0;
```

This variable acts as **state**, representing the number of seconds elapsed. Naming it descriptively, such as `clockSeconds`, improves readability.

A common example in iR Engine is using a state variable like `initialized` to ensure some code runs only once:

```ts
let initialized = false;

function hello() {
  if (initialized) return;
  initialized = true;
  // Initialization logic
}
```

### Local vs. global state

State can be categorized as **local** or **global**, depending on its accessibility. The table below outlines the differences:

| **Type of state** | **Description**                                          |
| :---------------- | :------------------------------------------------------- |
| **Local state**   | Exists only within a specific component or module.       |
| **Global state**  | Can be accessed and modified across multiple components. |

***

## Local state in iR Engine

Local state exists within a single component or module and is not shared across different parts of the application. Understanding scope is key to using local state effectively.

### Scope and module-local variables

[Scope](https://en.wikipedia.org/wiki/Scope_\(computer_science\)) defines where a variable is accessible in a program.

- **Module scope**: A variable is only available within the file it is declared in.
- **Component scope**: A variable is accessible inside a component where it is defined.

Initially, we used **module scope** in the [Hello World tutorial](./../02_hello_world/index.md):

```ts
let initialized = false;
function hello() {
  if (initialized) return;
}
```

Later, we moved the variable into a **component**:

```ts
export const HelloComponent = defineComponent({
  onInit: () => ({ initialized: false }),
});
```

This change made `initialized` **local to the component** instead of the module.

***

## Global state in iR Engine

Global state allows multiple parts of an application to share and modify the same data, making it useful for complex applications. Unlike local state, it persists beyond a single module or component.

### What is global state?

Global state allows multiple parts of an application to **share and modify the same data**. This eliminates **prop drilling**—the practice of passing data through multiple components.

### Managing global state in React

React provides the [Context API](https://react.dev/learn/passing-data-deeply-with-context) for managing global state. However, iR Engine introduces **Hyperflux**, which is optimized for handling state in real-time applications.

***

## State management approaches in iR Engine

iR Engine provides several ways to manage state, each suited for different use cases. The table below outlines the main approaches:

| **Method**                     | **Use case**                                                     |
| :----------------------------- | :--------------------------------------------------------------- |
| **Local variables**            | Suitable for tracking state within a single module or component. |
| **Hyperflux**                  | The preferred method for managing global state in iR Engine.     |
| **Reactors (**`useEffect`**)** | Used to trigger updates when state changes.                      |

### Using local variables

Local variables allow components to store data internally. However, they have **limitations**:

- Their scope determines accessibility.
- They do not persist across component unmounts.
- They require manual updates.

***

## Hyperflux: iR Engine’s state management system

Hyperflux is a powerful state management system in iR Engine, allowing applications to handle real-time updates efficiently. It is designed to manage **asynchronous state changes** across different components.

### Hookstate: A simplified state management tool

[Hookstate](https://hookstate.js.org/) is a lightweight state management library used in React applications. iR Engine leverages Hookstate for managing state efficiently.

A **Hookstate variable** is created using `useState`:

```ts
const myState = useState(0);
```

Hookstate variables have:

1. `get()`: Reads the current value.
2. `set()`: Updates the value.
3. `merge()`: Combines new data with the existing state.

### Defining state with Hyperflux

Hyperflux provides a structured way to manage **global state** in iR Engine. The following example defines a global state for tracking spawned and destroyed entities:

```ts
const BasicState = defineState({
  name: 'ee.basic.BasicState', // Unique identifier for this state

  initial: {} as Record<EntityUUID, {}>, // Initial state: an empty object that maps entity UUIDs to their state

  receptors: {
    onSpawnAction: BasicActions.spawnAction.receive((action) => {
      const state = getMutableState(BasicState); // Access global state
      state[action.entityUUID].merge({}); // Initialize state for the new entity
    }),

    onDestroyObject: WorldNetworkAction.destroyObject.receive((action) => {
      const state = getMutableState(BasicState); // Access global state
      state[action.entityUUID].set(none); // Remove state for the destroyed entity
    })
  }
});
```

### How it works:

- **Global state definition**: `defineState` creates a global state container accessible throughout the application.
- **State initialization**: The `initial` property starts as an empty object, mapping **entity UUIDs** to their respective states.
- **Receptors handle updates**:
  - `onSpawnAction` listens for entity spawns and initializes their state.
  - `onDestroyObject` listens for entity destruction and removes them from state.

This approach ensures **efficient state tracking** by dynamically updating global state based on entity events, reducing the need for manual state management.

### Reactors and `useEffect`

Reactors are used in iR Engine to track and respond to state changes, similar to React’s [`useEffect`](https://react.dev/reference/react/useEffect) hook.

`useEffect` executes **side effects** when a component:

1. Renders.
2. Mounts for the first time.
3. Reacts to a dependency change.

In iR Engine, **reactor mounts** serve a similar function, ensuring state updates are handled efficiently.

***

## ➡️  Next steps

***

