# Release Helm Chart
<!-- TODO: Improve the formatting of this file -->
These are the steps that needs to be taken in order to update an iR Engine Helm charts repo:
> Pre-requisites:
> - Have a checked-out copy of https://github.com/ir-engine/ir-engine-helm  
>   set to the `gh-pages` branch
> - Have a checked-out copy of https://github.com/ir-engine/ir-engine-ops/  
>   set to the `master` branch
1. Set working directory to local `ir-engine-ops` folder: `cd ir-engine-ops`
2. Increase the version number in `ir-engine/Chart.yaml`
3. Run `helm package etherealengine`
4. Run `helm repo index --url https://helm.etherealengine.org .`
5. Copy `ir-engine-X.Y.Z.tgz` that's generated to the root of the `ir-engine-helm` repo, and make sure to `git add` it.
6. Open `index.yaml`. Under entries.xrengine, there should be an entry for the new version.
7. Copy that entry to `ir-engine-helm`'s `index.yaml`, making sure to put it under the right `entries` section; we've got `ir-engine-builder` and `ir-engine` in the same file, so pay attention to which one you're putting it in. Also make sure that the spacing/indentation matches the other entries.
8. Copy the `generated` line from `index.yaml` to `ir-engine-helm/index.yaml`, overwriting the `generated` line that's there.
9. Commit this, and push it to the `gh-pages` branch of `ir-engine-helm`. Within a couple of minutes, you should see the new version appear at https://helm.etherealengine.org/
