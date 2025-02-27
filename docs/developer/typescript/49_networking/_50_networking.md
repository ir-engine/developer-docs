<!-- import { TechnicalNote } from '@site/src/components/TechnicalNote'; -->
<!-- import { UnstyledDetails } from '@site/src/components/UnstyledDetails'; -->

# Networking
We're going to add networking to the `basic` example from the previous section.  
Our goal is to deliver a shared and collaborative experience to many players at once.

## Actions
First we want to think through what kinds of actions we want in our game.  
For this tutorial we will allow the creation and destruction of simple objects over the network.

In our case we can cheat a bit since destroying objects is common enough that there is a built in world networking event for it, and also for creating objects we can extend the built in world spawning event.  

This means that we need to define an action for creation:
```ts
const spawnAction = defineAction({
  ...WorldNetworkAction.spawnObject.actionShape,
  prefab: 'ee.basic.ball',
  $topic: NetworkTopics.world
})
```

## State
iR Engine uses an 'event sourced state' paradigm for networking. That means that as a developer you publish an event and that event is performed by all instances simultaneously.

Typically actions are going to affect state. For this example we will declare that we're going to allow any number of objects, each with their own appearance. We define state in a React like way like so:

```ts
export const BasicState = defineState({
  name: 'ee.basic.BasicState',
  initial: {} as Record< EntityUUID, {} >,
  ...
```

### Receptors
Finally for this phase we want to define handlers or receptors to handle the event.   
These are by convention stored on the state itself:
```ts
  ...
  receptors: [
    [
      spawnAction,
      (state, action: typeof spawnAction.matches._TYPE) => {
        state[action.entityUUID].merge({})
      }
    ],
    [
      WorldNetworkAction.destroyObject,
      (state, action: typeof WorldNetworkAction.destroyObject.matches._TYPE) => {
        state[action.entityUUID].set(none)
      }
    ]
  ]
```

### Dispatching new events
We can spawn entities now like so at any time:

```ts
dispatchAction(spawnAction({ entityUUID:'my-entity' }))
```

### Rendering State

Once state is being networked we want to visualize that state. The react pattern is to allow state changes to occur and then 'react' to them - creating visual objects that reflect the state database:

```ts
const ArtifactReactor = ({ entityUUID }: { entityUUID: EntityUUID }) => {
  const basicState = useHookstate(getMutableState(BasicState)[entityUUID])
  useEffect(() => {
    const entity = UUIDComponent.getEntityByUUID(entityUUID)
    setComponent(entity, TransformComponent)
    setComponent(entity, VisibleComponent)
    setComponent(entity, NameComponent,'hello')
    setComponent(entity, PrimitiveGeometryComponent, { geometryType: 1 })
```

## Closing
This example is simple, but these are the building blocks and foundations for creating richer and more complex experiences.  
The source code for this example from https://github.com/ir-engine/ir-tutorial-basic




<TechnicalNote title="Solution">
<UnstyledDetails title="Full Solution">

```ts
import React, { useEffect } from 'react'

import {
  defineAction,
  defineState,
  dispatchAction,
  getMutableState,
  getState,
  none,
  useHookstate
} from '@ir-engine/packages/hyperflux'

import { EntityUUID } from '@ir-engine/packages/common/src/interfaces/EntityUUID'

import { NetworkTopics } from '@ir-engine/packages/spatial/src/networking/classes/Network'
import { WorldNetworkAction } from '@ir-engine/packages/spatial/src/networking/functions/WorldNetworkAction'

import { isClient } from '@ir-engine/packages/common/src/utils/getEnvironment'
import { PresentationSystemGroup, defineSystem, getComponent, setComponent } from '@ir-engine/packages/ecs'
import { ECSState } from '@ir-engine/packages/ecs/src/ECSState'
import { PrimitiveGeometryComponent } from '@ir-engine/packages/engine/src/scene/components/PrimitiveGeometryComponent'
import { GeometryTypeEnum } from '@ir-engine/packages/engine/src/scene/constants/GeometryTypeEnum'
import { NameComponent } from '@ir-engine/packages/spatial/src/common/NameComponent'
import { UUIDComponent } from '@ir-engine/packages/spatial/src/common/UUIDComponent'
import { NetworkState } from '@ir-engine/packages/spatial/src/networking/NetworkState'
import { ColliderComponent } from '@ir-engine/packages/spatial/src/physics/components/ColliderComponent'
import { RigidBodyComponent } from '@ir-engine/packages/spatial/src/physics/components/RigidBodyComponent'
import { VisibleComponent } from '@ir-engine/packages/spatial/src/renderer/components/VisibleComponent'
import { TransformComponent } from '@ir-engine/packages/spatial/src/transform/components/TransformComponent'
import { Vector3 } from 'three'

/**
 * Basic actions to spawn and destroy objects
 * This extends and naturally utilizes the functionality in EntityNetworkState
 */

const BasicActions = {
  spawnAction: defineAction(
    WorldNetworkAction.spawnObject.extend({
      type: 'ee.basic.SPAWN_BALL',
      $topic: NetworkTopics.world
    })
  )
}

/**
 * Global state that tracks locally spawned or destroyed artifacts by using action receptors
 */

const BasicState = defineState({
  name: 'ee.basic.BasicState',

  initial: {} as Record<EntityUUID, {}>,

  receptors: {
    onSpawnAction: BasicActions.spawnAction.receive((action) => {
      const state = getMutableState(BasicState)
      state[action.entityUUID].merge({})
    }),
    onDestroyObject: WorldNetworkAction.destroyObject.receive((action) => {
      const state = getMutableState(BasicState)
      state[action.entityUUID].set(none)
    })
  }
})

/**
 * A reactor such that each basic state record has an associated a visual artifact
 */

const ArtifactReactor = ({ entityUUID }: { entityUUID: EntityUUID }) => {
  /** Entity creation and destruction is handled by EntityNetworkState */
  const entity = UUIDComponent.useEntityByUUID(entityUUID)

  useEffect(() => {
    if (!entity) return

    setComponent(entity, TransformComponent, { scale: new Vector3(0.1, 0.1, 0.1) })
    setComponent(entity, VisibleComponent)
    setComponent(entity, NameComponent, entityUUID)
    setComponent(entity, PrimitiveGeometryComponent, { geometryType: GeometryTypeEnum.SphereGeometry })
    setComponent(entity, RigidBodyComponent, { type: 'dynamic' })
    setComponent(entity, ColliderComponent, { shape: 'sphere' })

    if (isClient) return

    const angle = Math.random() * Math.PI * 2
    const direction = new Vector3(Math.sin(angle), 0, Math.cos(angle))
    const velocity = 0.025 + Math.random() * 0.01
    getComponent(entity, RigidBodyComponent).body.applyImpulse(direction.multiplyScalar(velocity), true)
  }, [entity])

  return null
}

/**
 * Observe spawn events and create a sub-reactor for each entry in the basic state
 */

const reactor = () => {
  const basicState = useHookstate(getMutableState(BasicState))
  return (
    <>
      {basicState.keys.map((entityUUID: EntityUUID) => (
        <ArtifactReactor key={entityUUID} entityUUID={entityUUID} />
      ))}
    </>
  )
}

let counter = 0
const spawnRate = 3

/**
 * Spawn a new basic entity every 3 seconds
 */

const execute = () => {
  /** Only run this on the server */
  if (isClient || !NetworkState.worldNetwork) return

  const { deltaSeconds, elapsedSeconds } = getState(ECSState)

  counter += deltaSeconds

  if (counter < spawnRate) return
  counter = 0

  const entityUUID = `basic-${elapsedSeconds}` as EntityUUID
  const action = BasicActions.spawnAction({ entityUUID, position: new Vector3(Math.random(), 1, Math.random()) })
  dispatchAction(action)
}

/**
 * System to register the execute function and reactor
 */

export const BasicSystem = defineSystem({
  uuid: 'basic.system',
  reactor,
  execute,
  insert: { after: PresentationSystemGroup }
})
```
</UnstyledDetails>
</TechnicalNote>

