# Shirakami Model

**Language Protocol OS — a human-centered language processing environment for AI collaboration.**

Shirakami Model is an open model for strongly supporting **language Protocols**. It does not replace an LLM or make the underlying AI more capable. Instead, it provides a processing environment between human language and AI execution.

## What is Shirakami Model?

Shirakami Model organizes human prompts, expands them into forms that AI systems can process clearly, and treats the resulting structure as a computational target for task execution.

It can also observe language characteristics appearing in interaction — including wording, phrasing, and patterns of thought — and adapt the processing environment to the user's language Protocol.

The aim is not to make users adapt themselves to AI, but to make the AI interaction environment adaptable to the user.

## Human-led interaction

Shirakami Model reduces unnecessary verbosity that can obstruct understanding and presents options from multiple perspectives according to the user's current context.

This is designed to prevent AI from taking over task direction or decision-making.

When the user explicitly wants it, AI may provide supplementary guidance. The important distinction is that **the degree of AI guidance remains under the user's control**.

## Handling hallucination

Shirakami Model does not treat hallucination simply as something to eliminate.

Meaning deviations between AI output and confirmed Evidence can be recorded and, when appropriate, separated from confirmed information as speculative or creative material.

This makes it possible to distinguish among:

- confirmed information
- inference or speculation
- creative elements

AI's generative imagination can therefore be analyzed and presented without treating it as established fact.

## Protocol and GitHub

Shirakami Model externalizes AI instructions and processing procedures as **Protocols**, rather than treating every interaction as an isolated prompt.

Through GitHub integration, Protocols, Specifications, and user prompts stored in repositories can be processed through appropriate routes and applied to different tasks.

This enables a cycle of:

```text
Develop → Verify → Store → Reuse
```

for language Protocols.

The goal is to make high-quality language Protocols easier to develop, verify, accumulate, and reuse without tying them to a single AI vendor or runtime.

## What it changes

Using Shirakami Model does **not** increase the underlying performance of an AI model.

What changes is the environment around the AI:

```text
Human Language
      ↓
Prompt Organization
      ↓
Language Protocol
      ↓
Computational Task
      ↓
AI Runtime
      ↓
Evidence / Observation
      ↓
Human-readable Options
      ↓
Human Judgment
```

The intended result is a significant improvement in the user's experience of understanding and using AI, rather than a claim of increased model intelligence.

## Core principle

Shirakami Model does not aim to make AI smarter than humans or to delegate human decisions to AI.

It aims to create an environment in which people can understand, choose, and use AI according to their own intentions.

> **Do not make AI smarter. Make it possible for people to use AI on their own terms.**

## Related repositories

- [shirakami-OS](https://github.com/bxa05221-ux/shirakami-OS) — Foundation / Runtime / Implementation
- [shirakami-specification](https://github.com/bxa05221-ux/shirakami-specification) — Specifications
- [shirakami-research](https://github.com/bxa05221-ux/shirakami-research) — Research / Theory

## Status

🚧 **Prototype / β1.0 operational rollout**

The model is under active development. Prototype status does not imply theoretical or product completeness.

See the repository documentation and implementation repositories for current specifications and verification status.

## Japanese

[日本語版 README](README.ja.md)
