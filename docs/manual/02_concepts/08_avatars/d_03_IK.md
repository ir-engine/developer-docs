# Inverse Kinematics

## Overview

Inverse kinematics allow for procedural animations, where the avatar’s limb rotations will track the positions of networked IK targets. IK is enabled by default for immersive experiences to allow the avatar’s hands and feet to match the real-world user.

## Blend Weights

IK solves are blended into the avatar’s forward kinematic animations with blend weight values determined by the `AvatarIKTargetComponent` associated with each IK target entity. Blend weights are properties of the `AvatarIKTargetComponent`'s schema and are networked to all clients.