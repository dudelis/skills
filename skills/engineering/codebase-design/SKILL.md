---
name: codebase-design
description: Guide codebase architecture toward deep modules, stable interfaces, explicit seams, and local knowledge. Use when designing module boundaries, evaluating abstractions, planning test seams, or reviewing architecture.
---

# Codebase Design

Use this as shared vocabulary for architecture decisions. It is a reference skill, not a mandatory workflow stage, and may also be invoked directly.

## Vocabulary

- **Module**: behavior hidden behind a public interface.
- **Interface**: the smallest contract callers need.
- **Depth**: useful behavior provided relative to interface complexity.
- **Seam**: a public boundary where behavior can be substituted or observed.
- **Adapter**: an implementation placed behind a seam.
- **Leverage**: capability many callers gain from one implementation.
- **Locality**: keeping knowledge and changes near the concept that owns them.

## Design Heuristics

1. Prefer deep modules: substantial behavior behind small, stable interfaces.
2. Put seams around meaningful policy or external variability, not every function.
3. Keep domain rules independent from frameworks, transport, storage, and vendors.
4. Place adapters at system edges and translate into domain concepts once.
5. Keep related behavior and knowledge together; avoid changes that scatter for one reason.
6. Reuse an existing seam before adding another. Fewer coherent seams are easier to test and evolve.
7. Introduce an abstraction only for demonstrated complexity, duplication, or an established repository pattern.

## Applying The Guidance

Read the repository's context documents, ADRs, standards, and nearby implementation first. Describe proposed boundaries using domain language, identify the public interface and hidden decisions, then state the tradeoffs. Treat these heuristics as design prompts rather than universal rules; repository-specific decisions win.