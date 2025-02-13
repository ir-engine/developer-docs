---
pagination_next: developer/typescript/basics/recap/index
---
<!-- import { UnstyledDetails } from '@site/src/components/UnstyledDetails'; -->

# Recap and next steps

Congratulations! 🎉 You have just learned the minimal basics of working with iR Engine using TypeScript!

This was an introductory tutorial to teach you the core essentials of the engine as quickly as possible.  
But iR Engine has a lot of features to explore!

## Tutorial recap

The `Hello World` tutorial has taught us how to work with and create the most minimal iR Engine programming example possible. But, as we are about to learn, there is a lot more to explore!

With this project we accomplished the following:

- Imported some iR Engine's typescript modules in our file
- Created an entity, and gave it an `uuid` and a `name`
- Gave the entity the ability to:
  - Be visible on the screen with a `VisibleComponent`
  - Have Linear Transformations with a `TransformComponent`
- Defined the position of the sphere in the scene
- Gave the entity a `PrimitiveGeometryComponent` _(a Sphere)_
- Defined a Custom `Component` type
- Defined a `Query` to search for our Custom Component
- Locked our logic to only happen once with the `initialized` State variable contained inside our Custom Component.
- Defined a `System` and locked our logic behind its `execute` function
- Locked our logic to only trigger for the entities that match our `helloQuery` generator
- Added our project's code to the engine with the `xrengine.config.ts` configuration file

That's a lot!!!

## What to do next?

Your next step in your journey will be to expand on the knowledge you've acquired by running through the **iR Engine basics**.

In the continuation of this tutorial, we will add these features to the source code of our project:

- **Physics Properties**: Gravity, Collision, Friction, etc
- **Logic** that happens every frame at specific intervals _(eg: every fixed-frame or every visual-frame)_
- **State Management** _(eg: our `initialized` variable, but better)_
- **Input Management** _(keyboard, mouse, touchpad, etc)_
- **How to debug our code** to search for errors
- **Networked events and actions** that can be shared between multiple devices

And, at the end of the tutorial, we will put everything together into a complete mini-game!

Let's not wait any longer and get started by adding [`Physics`](../physics) to our project.

### Intermediate content

If you are feeling confident already, you could jump right into the intermediate tutorials.  
Just pick a topic that interests you in the sidebar and continue your journey from there.  
:::note[Intermediate Note]
Make sure to skim-read the basics section at least once, as it gives an overview of some important concepts that will be used all throughout the other guides.
:::

### Advanced knowledge

The [Technical manual](/manual) is where iR Engine is presented in all of its complexity, without any guard-rails or hand-holding.
You will also find the [Reference API](https://ir-engine-api.mt-int.theinfinitereality.io/) really useful when writing the code of your application.  
:::note[Advanced Note]
Make sure to read the `Mastery Toolkit` section at least once.  
It contains a list of important tools that you will need when working with advanced projects.
:::

<!-- TODO: Add a list of cool and interesting topics to read next here -->
