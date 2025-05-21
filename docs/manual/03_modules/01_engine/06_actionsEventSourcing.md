# Event sourcing

Learn how the engine uses actions to manage event sourcing.

## Overview

Event sourcing is a method for managing state changes by recording a series of discrete actions instead of directly modifying the application state. This approach ensures that all peers in a networked environment maintain a consistent and synchronized state.

:::hint{type="info"}
For an overview of state management and how event sourcing integrates with Hyperflux, refer to the [state management documentation](https://docs.ir.world/developers/state-management).
:::

## Actions definition

Actions are discrete units of change that represent** user or system intentions **and serve as the primary mechanism for handling state changes in event sourcing. They allow developers to control how data flows within the system, ensuring that changes are processed in a structured and predictable manner.

They can be dispatched, processed, and synchronized across different parts of an application.

Examples of actions include:

- Spawning an entity
- Switching an avatar
- Modifying a property

Actions are processed **asynchronously** and follow a structured lifecycle.

### When to use actions

Use **actions** when a state change requires **validation, synchronization, or tracking** across peers.

## Action lifecycle

Actions follow a structured lifecycle to ensure consistency and correct ordering.

### Dispatching actions

Actions are dispatched to **topics**, which determine how they are routed:

- If no topic is specified, the action is sent to the **default topic**.
- If the action belongs to a **networked topic**, it will be **sent to the appropriate peers** for synchronization.

Once dispatched, the action is added to the **incoming queue** for local processing. If networked, it is also added to the **outgoing queue**.

### Processing actions

Action processing follows a structured pipeline:

1. **Outgoing actions are dispatched at the end of the animation frame.**
   - If the **peer is the host**, the action is forwarded to all other peers.
   - If the **peer is not the host**, the action is sent only to the host.
2. **Incoming action queues are populated at the start of the next animation frame.**
   - Actions are processed in the order they were received.
   - Each action is handled by its respective system based on the order in which systems were registered.
3. **Optional: Targeted action forwarding.**
   - By default, networked actions are forwarded according to the topic rules.
   - The `$to` property can be specified to forward an action only to a particular user.

The following diagram illustrates the action flow:

![](./images/action-flow.png)

## Best practices

Following best practices ensures efficient and reliable event sourcing:

✅ **Use actions only when necessary**

- Define an action only if it **needs to be networked** or represents a **significant state change**.
- Avoid dispatching unnecessary actions that could overload the network.

✅ **Optimize data transmission**

- Pass **references or IDs** instead of large data payloads to reduce network traffic.

✅ **Maintain consistent state synchronization**

- Ensure **all receptors** process actions in the same order.
- Handle **out-of-order actions** correctly to prevent state desynchronization.

:::hint{type="info"}
For a deeper understanding of how actions integrate with state management, visit the [state management documentation](https://docs.ir.world/developers/state-management).
:::

##

