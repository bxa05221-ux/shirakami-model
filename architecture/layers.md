# Shirakami Architecture — Layers

```text
Human / Society
      │
      ▼
Human / Narrative Interface
      │
      ▼
┌──────────────────────────────┐
│     Shirakami Architecture   │
│                              │
│  Landscape                   │
│      ↕                       │
│  Observation                 │
│      ↕                       │
│  Dark Layer                 │
│      ↕                       │
│  Protocol                    │
│      ↕                       │
│  Runtime Boundary            │
└──────────────┬───────────────┘
               │
               ▼
        Model Provider(s)
```

## Landscape

The shared state in which observations, evidence, relations, unresolved questions, and history can accumulate.

## Observation

The operation of looking at the Landscape from one or more viewpoints.

## Dark Layer

The holding layer for questions and matters that are not ready for closure.

## Protocol

The rules governing how observation, retention, revisit, and catch are handled.

## Runtime Boundary

The exchange boundary between the architecture and its executable implementation.

## Model Provider

A replaceable source of model intelligence. It operates inside the boundary defined by the architecture and does not become the architecture itself.

## Interfaces

The architecture may be entered through multiple interfaces:

- Human / Narrative: novel, conversation, radio
- Machine: SHBB API
- Physical: member card, QR, NFC, novelty

These are different entrances to the same Landscape.
