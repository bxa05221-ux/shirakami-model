# Shirakami Architecture — Provider Independence

Shirakami Architecture is defined independently of any particular AI model provider.

```text
                 Shirakami Architecture
                         │
              Runtime / Protocol Boundary
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
         GPT           Claude        Local Model
```

## Separation of responsibilities

| Layer | Responsibility |
|---|---|
| Architecture | Defines structure, boundaries, and invariants |
| Protocol | Defines permitted behavior and transitions |
| Runtime | Executes the protocol |
| Model Provider | Supplies model intelligence |
| Interface | Connects humans, machines, or physical media |

A provider may be replaced without redefining the Landscape, Dark Layer, Thread, Revisit, or Catch concepts.

## Why this matters

The architecture is intended to prevent the model from becoming the identity of the system. Model capability can improve, degrade, or change while the surrounding cognitive structure remains stable.

## Reference implementation

The SHBB API is a provider-neutral reference implementation. Its minimal Runtime can operate without an LLM, allowing the architectural boundary to be tested before attaching a specific model provider.

## Non-goal

Provider independence does not claim that all providers behave identically. Adapter behavior, capability differences, latency, context limits, and safety constraints remain implementation concerns.
