<!-- import { TechnicalNote } from '@site/src/components/TechnicalNote'; -->
<!-- import { UnstyledDetails } from '@site/src/components/UnstyledDetails'; -->

# Assigning Physics

So far we have learned how to create an `Entity`, and how to tell the engine what we want our entity to be. In simple terms, we told the engine how to **create** our sphere.  

## Our problem

We added some components to our sphere, so that the engine can draw the sphere into the screen and we can see it.  
But right now it is only an "empty shell" that sits there doing nothing.  
We cannot even move it or push it around! What a boring ball.  
Lets fix that.

## Our solution

We are going to add a Collider and a RigidBody to our sphere object.  

Physics properties are tricky to test, as they may not be readily visible.  
Lets get a point of reference of how our project currently behaves, so we can be certain that the changes we make to our code are working as we expect them.  
In order to do that, we are going to run our project from the studio and walk around the scene with an Avatar.  

These are the steps needed to accomplish that:

- Open the scene you created before, or click on `Create Scene` if you don't have it
- Press the `Play` button in the studio
- Move your Avatar around the scene by either:
  - Pressing `WASD` in your keyboard
  - Clicking anywhere on the ground with your mouse

You may notice that, if you try to hit the sphere with your avatar... you will instead walk right through it!  
This happens because our Sphere doesn't have any Physics properties yet, so it can be "seen" but not "collided against".

## Physics Properties

In order to correct our problem, we are now going to:

- Add a `RigidBodyComponent` of type `dynamic` to our entity
- Add a `ColliderComponent` with the shape of a `sphere`

Lets also change the position of ball so that it spawns some distance above the ground.  
Here are your hints for this tutorial:

```ts
// Both the RigidBody and Collider components are part of the `Spatial/physics` engine module
'@ir-engine/packages/spatial/src/physics/components/.....'
// We can specify the dynamic type with:
{ type: 'dynamic' }
// We can specify the shape with:
{ shape: 'sphere' }
// Make the ball spawn 3units above the ground
Vector3(/* X */,  /* Y */,  /* Z */)
```

You will know that your code is correct if:

- The ball has gravity and falls to the ground
- You try to go through the ball with the Avatar, but the engine stops you and you push the ball instead.

<TechnicalNote title="Solution">

```ts
// Import both components from the Spatial/physics module
import { RigidBodyComponent } from '@ir-engine/packages/spatial/src/physics/components/RigidBodyComponent'
import { ColliderComponent } from '@ir-engine/packages/spatial/src/physics/components/ColliderComponent'
```
```ts
// Set both components to our entity
ECS.setComponent(entity, RigidBodyComponent, { type: 'dynamic' })
ECS.setComponent(entity, ColliderComponent, { shape: 'sphere' })
```
```ts
// Make the ball spawn 3 units along the Y axis (aka 3u above the ground)
ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 3, 0) })
```

<UnstyledDetails title="Full Solution">

```ts title="ir-tutorial-basic/Step2.ts" showLineNumbers
import { ECS } from '@ir-engine/packages/ecs'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { Vector3 } from 'three'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'
import { PhysicsSystem } from '@ir-engine/packages/spatial'
// Import both components from the Spatial/physics module
//highlight-start
import { RigidBodyComponent } from '@ir-engine/packages/spatial/src/physics/components/RigidBodyComponent'
import { ColliderComponent } from '@ir-engine/packages/spatial/src/physics/components/ColliderComponent'
//highlight-end

export const BasicsComponent = ECS.defineComponent({
  name: 'ee.tutorial.BasicsComponent',
  jsonID: 'EE_tutorial_basics',
  onInit: () => { return { initialized: false } }
})

const basicsQuery = ECS.defineQuery([BasicsComponent])

export const BasicsSystem = ECS.defineSystem({
  uuid: 'ee.tutorial.BasicsSystem',
  execute: () => {
    for (const entity of basicsQuery()) {
      let { initialized } = ECS.getMutableComponent(entity, BasicsComponent)
      if (initialized.value) continue
      initialized.set(true)

      ECS.setComponent(entity, NameComponent, 'ee.tutorial.basics-entity')
      ECS.setComponent(entity, VisibleComponent)
      // Make the ball spawn 3 units along the Y axis (aka 3u above the ground)
      //highlight-start
      ECS.setComponent(entity, TransformComponent, { position: new Vector3(0, 3, 0) })
      //highlight-end
      ECS.setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
      // Set both components to our entity
      //highlight-start
      ECS.setComponent(entity, RigidBodyComponent, { type: 'dynamic' })
      ECS.setComponent(entity, ColliderComponent, { shape: 'sphere' })
      //highlight-end
    }
  },
  insert: { after: PhysicsSystem }
})
```

</UnstyledDetails>
<!-- Full Solution End -->
</TechnicalNote>
<!-- Solution End -->

