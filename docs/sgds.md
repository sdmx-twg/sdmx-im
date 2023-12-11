This is a sample SGDS UML diagram:

```mermaid
---
title: SGDS
---
classDiagram
class MaintainableArtefact
class PubLocation
class Endpoint
  MaintainableArtefact <|-- Endpoint
  MaintainableArtefact <|-- PubLocation
  PubLocation "0..*"-->"0..*" Endpoint : targets
```
