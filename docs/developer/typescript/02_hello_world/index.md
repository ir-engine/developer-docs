# Hello World in iR Engine

Welcome to the Hello World tutorial. This guide is aimed to be your first hands on experience with the engine. 
By the end of this guide, you will have accomplished the following:

- Imported iR Engine's typescript modules in a file
- Created an entity, and gave it an `uuid` and a `name`
- Gave the entity the ability to:
  - Be visible on the screen with `VisibleComponent`
  - Have Linear Transformations with `TransformComponent`
- Gave the entity a `PrimitiveGeometryComponent` _(a Sphere)_
- Defined the position of the sphere in the scene
- Defined a Custom `Component` type
- Defined a `Query` to search for our Custom Component
- Locked our logic to only happen once with the `initialized` State variable contained inside our Custom Component.
- Defined a `System` and locked our logic behind its `execute` function
- Locked our logic to only trigger for the entities that match our `helloQuery` generator
- Added our project's code to the engine with the `xrengine.config.ts` configuration file

## Next steps

After finishing the tutorial, continue your learning path in the **iR Engine basics** section. This tutorial covers the next steps to work with your code.

Now, withour much further ado, let's get started.

## Tutorial contents

(Tutorial navigation)
