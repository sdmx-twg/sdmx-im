# Cube

## Context

Some statistical systems create views of data based on a “cube”
structure. In essence, a cube is an n-dimensional object where the value
of each dimension can be derived from a hierarchical code list. The
utility of such cube systems is that it is possible to “roll up” or
“drill down” each of the hierarchy levels for each of the dimensions to
specify the level of granularity required to give a “view” of the data –
some dimensions may be rolled up, others may be drilled down. Such
systems give a dynamic view of the data, with aggregated values for
rolled up dimension positions. For example, the individual countries may
be rolled up into an economic region such as the EU, or a geographical
region such as Europe, whilst another dimension, such as “type of road”
may be drilled down to its lower level. The resulting measure (such as
“number of accidents”) would then be an aggregation of the value for
each individual country for the specific type of road.

Such cube systems rely, not on simple code lists, but on hierarchical
code sets (see Section [Hierarchy](./7_Hierarchy.md)).

## Support for the Cube in the Information Model

Data reported using a Data Structure Definition structure (where each
dimension value, if coded, is taken from a flat code list) can be
described by a cube definition and can be processed by cube aware
systems. The SDMX-IM supports the definition of such cubes in the
following way:

- The `Hierarchy` defines the (often complex) hierarchies of codes.
- If required:
    - The `StructureMap` can group `DataStructureDefinition` that describe
        the cube
    - The `HierarchyAssociation` can provide a mechanism to apply a
        `Hierarchy` to the `Code`s in the `Codelist`s used by the
        `DataStructureDefinition`, providing also the context of which the
        hierarchy applies (e.g., a `Dataflow`).