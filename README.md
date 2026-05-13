# SDMX Information Model

This submodule contains the SDMX Information Model, Framework, Logical
Interfaces, and Technical Notes documentation components used within the
[`sdmx-docs`](https://github.com/sdmx-twg/sdmx-docs) unified documentation
site.

## Repository Structure

-   `docs/` — content pages, organised into four sub-folders:
    -   `docs/framework/`
    -   `docs/information_model/`
    -   `docs/logical_interfaces/`
    -   `docs/technical_notes/`

| File                            | Section served                 |
| ------------------------------- | ------------------------------ |
| `mkdocs_framework.yml`          | Section 1 — Framework          |
| `mkdocs_information_model.yml`  | Section 2 — Information Model  |
| `mkdocs_logical_interfaces.yml` | Section 5 — Logical Interfaces |
| `mkdocs_technical_notes.yml`    | Section 6 — Technical Notes    |

## Version Branches

Each minor release of this component is maintained on a dedicated documentation
branch following the naming convention `docs_vX.Y` (e.g., `docs_v2.1`,
`docs_v3.0`).

These branches exist solely to support the documentation website and are not
used for regular development. Changes to the specification continue to go
through the normal development and release process (via `develop`). Older
documentation branches may additionally require file reorganization and
formatting adaptations for MkDocs.

The branch tracked by the
[`sdmx-docs`](https://github.com/sdmx-twg/sdmx-docs) parent repository is
declared in `.gitmodules` at the root of that repo. Switching the tracked
branch in the parent repository is how a new version of this component is
published on the documentation site.

## Formatting Conventions

For Markdown and MkDocs formatting conventions that apply to content in `docs/`,
see the [`sdmx-docs` README](https://github.com/sdmx-twg/sdmx-docs#readme).
