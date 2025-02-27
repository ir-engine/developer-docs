# Scene Management

This guide outlines the core concepts of scene management in iR Engine.

## Overview

A scene in iR Engine is a container for your **3D entities**, **assets**, **lighting**, and **environment** settings. It is the space where you import 3D models, define materials, place lights, and configure other properties.

### Scene hierarchy and panels

- **Hierarchy panel**: Shows all objects (entities) in your scene. Use it to select, parent, or rearrange items.
- **Assets panel**: Holds imported files, such as models, textures, and audio.
- **Properties panel**: Displays configurable attributes for the currently selected entity (e.g., transform, material settings, animations).

## Importing assets

iR Engine supports several file formats for 3D models, images, volumetric data, videos, and audio. You must import these assets before placing them in your scene.

### Supported file types

| **Type**       | **Formats**                |
| :------------- | :------------------------- |
| **3D models**  | `.glb`, `.gltf`            |
| **Images**     | `.png`, `.tiff`, `.jpeg`   |
| **Volumetric** | DRCS, UVOL, Manifest files |
| **Videos**     | `.mp4`, `.mkv`, `.avi`     |
| **Audio**      | `.mp3`, `.mpeg`, `.m4a`    |

***

## Material management

Materials define how objects appear in your scene. iR Engine uses **physically based rendering (PBR)** and supports **vertex colors** for realistic or stylized effects.

### Core material properties

- **Diffuse or base color map**
- **Metalness map**
- **Roughness map**
- **Normal map**
- **Ambient occlusion (AO) map**

Each texture increases draw calls, so only use those you need. To reduce file size, you can skip the diffuse map and use the engine’s built-in color selector.

### Accessing materials

All materials for an asset appear in the **Material Library** tab

```text
Material library
 └─ Asset Name
     ├─ material name
     ├─ material name
     └─ material name
```

### Material types

iR Engine supports several Three.js materials:

| **Material**                                                                                           | **Description**                                                                                         |
| :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| [**MeshBasicMaterial**](https://threejs.org/docs/?q=meshba#api/en/materials/MeshBasicMaterial)         | Not affected by lights; emits a constant color.                                                         |
| [**MeshStandardMaterial**](https://threejs.org/docs/?q=meshstan#api/en/materials/MeshStandardMaterial) | Standard physically based material using a Metallic-Roughness workflow.                                 |
| [**MeshPhysicalMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/MeshPhysicalMaterial)   | An extension of MeshStandardMaterial, adding clearcoat, advanced transparency, reflectivity, and sheen. |
| [**MeshMatcapMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/MeshMatcapMaterial)       | Uses a MatCap (lit sphere) texture for shading.                                                         |
| [**MeshLambertMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/MeshLambertMaterial)     | For non-shiny surfaces, without specular highlights.                                                    |
| [**MeshPhongMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/MeshPhongMaterial)         | For shiny surfaces with specular highlights.                                                            |
| [**MeshToonMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/MeshToonMaterial)           | Implements toon (cartoon-like) shading.                                                                 |
| [**ShaderMaterial**](https://threejs.org/docs/?q=shadermat#api/en/materials/ShaderMaterial)            | For custom GLSL shaders and advanced effects.                                                           |
| [**ShadowMaterial**](https://threejs.org/docs/?q=shadow#api/en/materials/ShadowMaterial)               | Receives shadows but is otherwise transparent.                                                          |

***

## Saving changes to models

You must save model changes (transform edits, normals, UVs, materials, or attributes) for them to persist:

1. **Select the model** in the **Hierarchy**.
2. In the **Properties** panel, scroll to the bottom and click **Save Changes**.
3. (Optional) To save under a new name, edit the file name at the end of the URL field before clicking **Save Changes** again.

A new or updated file (e.g., `myModel.glbl`) appears in the **Assets** panel.

:::hint{type="info"}
💡 **Tip**:&#x20;

Tip: You can convert `.gltf` or `.usdz` files to `.glb` by importing them, editing the file extension in the URL field to `.glb`, and clicking **Save Changes**.
:::

***

## Optimization and compression

iR Engine provides built-in tools to optimize your models. These tools help reduce file size and improve loading times.

### Accessing compression tools

1. **Select your model** in the **Hierarchy**.
2. **Open the properties panel**.
3. Expand the **Model Transform Properties** section to view the following options:

### glTF compression

- **Click optimize** to compress geometry and textures.
- **Image format**: Choose `.jpg`, `.ktx2`, or `.png`.
- **Max texture size**: Limit texture resolution (e.g., 1024×1024).

### Delete attributes

- Remove unnecessary attributes.
- List each attribute in the provided text field, separated by spaces.

### Bake to vertices

- Bake **diffuse**, **lightMap**, or **emissive** information into vertex colors.
- This eliminates the need for texture files if the model’s design is simple.

***

## Animations

### Avatars

Turn on animations for avatar models by using the **Loop Animation** tab:

1. **Select** the avatar model in the **Hierarchy**.
2. **Open** the Loop Animation tab in the **Properties** panel.
3. **Select** the animation track (e.g., `mixamo.com`).
4. **Enable** **Is Avatar** to use the engine’s built-in avatar animation features.

### Animated geometry

For non-avatar models, enable **Loop Animations** in the **Properties** panel to continuously play the motion tracks in the file.

***

## Skyboxes and cubemaps

Skyboxes surround your scene with a distant background. iR Engine supports **Color**, **Skybox** (cubemap), and **Equirectangular** (360° environment map).

1. **Click the skybox button** in the **Tools panel**.
2. **Choose a background type** (color, skybox, or equirectangular).
3. **Load the relevant images** or adjust the color settings.

:::hint{type="info"}
💡 **Tip**:&#x20;

Use HDR images from <a href="https://hdri-haven.com/" target="_blank">HDRi Haven</a> to achieve realistic lighting and reflections.
:::

***

## Additional conversion tools

If you must convert models before importing, use these tools:

- **Convert **`.gltf`** to **`.glb`** (browser)**
  - [glb-packer.glitch.me](https://glb-packer.glitch.me/)
  - [CartMagician](https://cartmagician.com/tools/3d-to-AR-converter) (paid)
- **Convert **`.fbx`** to **`.glb`** (app)**
  - [facebookincubator/FBX2glTF](https://github.com/facebookincubator/FBX2glTF)
- **Convert **`.usd`** to **`.gltf`** (browser)**
  - [GroupDocs USD to GLTF](https://products.groupdocs.app/conversion/usd-to-gltf)

:::hint{type="info"}
💡 **Tip**:&#x20;

Converting `.gltf` into `.glb` is recommended for easier importing.
:::

***

## Using standard materials

Use the [MeshStandardMaterial](https://threejs.org/docs/?q=meshstan#api/en/materials/MeshStandardMaterial) to simulate glass, plastic, glow, or metal by adjusting **metalness**, **roughness**, **emissive**, and **transparency**.

| **Glass**                                      | **Plastic**                                     | **Glow**                                     | **Metal**                     |
| :--------------------------------------------- | :---------------------------------------------- | :------------------------------------------- | :---------------------------- |
| High reflectivity, clearcoat, and transparency | Moderate roughness, minimal metallic properties | Emissive color and higher emissive intensity | High metalness, low roughness |

### Tips for basic materials

- It is not necessary to have a texture map for every object.
- Use **standard materials** frequently to reduce complexity.
- **Name** materials appropriately before exporting from your DCC or game engine. iR Engine inherits these names.
- Indicate which assets use standard materials before importing `.glb` files into iR Engine.

***

## Saving your scene

You can **Save Scene** or **Save As** from the **File menu** to store your scene file. Some scenes require extra time to finish saving.

:::hint{type="info"}
💡 **Thumbnail tip:**

Position your viewport camera before clicking Save. The engine will prompt you to create a thumbnail, which uses a screenshot of your current view.
:::

