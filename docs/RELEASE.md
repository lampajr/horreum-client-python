# Release

This document aims to describe how to perform a release of the Horreum python library.

The versioning pattern should follow the [Horreum](https://github.com/Hyperfoil/Horreum) 
versioning scheme to keep coherence among all Horreum-related projects versions.

## Procedure

### Tag a new version

Checkout to your branch, either a `stable` (e.g., `0.12.x`) or the `main` one.

```bash
git checkout origin/main
```

Update the project version:

```bash
poetry version patch
```

This will bump your version, from `0.12-dev` to `0.12`.

To double-check the version, run:
```bash
poetry version                                                                                                                                                      [15:55:39]
# horreum 0.12
```

Commit the changes and tag a new version:
```bash
git add .
git commit -m "Tag version 0.12"
git tag v0.12
```

Ensure the tag is in the form of `v$(poetry version)`.

Push changes and tag:
```bash
git push origin main
git push origin v0.12
```

If you are releasing a new patch from a _stable_ branch all previous operations must be performed
from _stable_ rather than from `main`.

### Create stable branch

> **NOTE**: If the _stable_ branch is already existing simply skip this step at all as this means 
> you already did the following steps.

To create a _stable_ branch from the `main` one, e.g., `0.12.x`, run the following commands.

```bash
git checkout origin/main
git checkout -b 0.12.x
git checkout origin/main
```

Update version to the next development one:
```bash
poetry version 0.13-dev
```

Commit the changes:
```bash
git add .
git commit -m "Next is 0.13"
```

Push changes:
```bash
git push origin 0.12.x
git push origin main
```

