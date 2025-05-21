# Locations

Locations in **iR Engine** serve as **instances of a scene**, enabling **real-time multi-user interactions**. They provide a structured way to manage **shared virtual environments**, supporting **scalability** and **session persistence**.

## **Understanding locations**

A **location** is a **persistent virtual environment** where multiple users can interact in **real time**.

Each location consists of **one or more instances**, which handle different types of data processing. This architecture allows **multiple users** to participate in scalable environments.

## Instances

An **instance** is a single session running at a **location**. Users in the same instance share the **same environment** and can see and interact with each other.

Adding a new location is done from the `/admin/locations` route, and live instances can be viewed from `/admin/instances`.

### Types of instances

There are two types of instances:

| Instance Type      | Functionality                                                                             |
| :----------------- | :---------------------------------------------------------------------------------------- |
| **World Instance** | Handles all **spatial interactions** within the scene (e.g., avatars, vehicles, objects). |
| **Media Instance** | Manages **real-time audio, video, and screen sharing**.                                   |

Media instances can either belong to a location or exist as ephemeral group calls, known as parties.

## Default locations

Every new iR Engine project includes three predefined locations:

| Location name | Description                            |
| :------------ | :------------------------------------- |
| `default`     | The default entry point for iR Engine. |
| `apartment`   | A sample indoor environment.           |
| `sky-station` | A sample outdoor environment.          |

You can modify these locations or create new ones based on your project’s needs.

## **Matchmaker functionalities**

iR Engine allows custom instance configuration using `matchmaker` rules. This feature provides flexibility in controlling how users join and interact within locations.
