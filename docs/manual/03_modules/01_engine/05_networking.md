# Networking

This guide explains how networking works in iR Engine and how **users, peers, ownership,** and **authority** interact in a networked environment.&#x20;

## Networks

Networks are channels used to share data between peers. iR Engine supports two primary network types:

- **World networks:**
  - Tied to *location instances*.
  - Handle information about the environment, user positions, and world interactions.
- **Media networks**
  - Tied to *media instances*.
  - Handle audio or video streams and other media-related data.

Each network serves a distinct purpose, ensuring that only relevant data is broadcast to connected peers.

## Users and peers

A **user** is a unique account on an iR Engine deployment. Users can join multiple instances, potentially having several **peers**—one peer per active connection or device.

- **Users**
  - Represent the individual account or identity in the system.
  - Own avatars and maintain consistent identity across different sessions or devices.
- **Peers**
  - Represent active client connections (e.g., a user’s laptop, phone, or VR headset).
  - A single user can have multiple peers connected to different or the same instances simultaneously.

:::hint{type="info"}
ℹ️ **Note**:

Only a single avatar is loaded per user, but it can be controlled by any one of that user's peers.
:::

## Ownership and authority

**Ownership** and **authority** define how networked entities are managed and controlled across peers:

- **Ownership**
  - Indicates which user *owns* a particular entity (e.g., an avatar or object in the scene).
  - Cannot be transferred. If ownership must change, destroy the entity and recreate it under the new user.
- **Authority**
  - Indicates which peer can *actively control* the entity’s state (e.g., movement, interactions).
  - Can be transferred between peers via an authority request and an authority transfer action.
  - The owner peer decides whether to grant authority to another peer.

By separating ownership (long-term association) from authority (immediate control), iR Engine allows flexible handoffs of control without altering the underlying entity’s ownership.
