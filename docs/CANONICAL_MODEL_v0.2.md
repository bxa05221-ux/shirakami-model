# Shirakami Canonical Model v0.2

Status: reviewed Core scope approved / supporting principles retained  
Date: 2026-10-05

This document integrates the current Canonical Model Map, Evidence Contract, Protocol Contract, Context/Handoff Contract, and Matome YAML traceability work into one model-level reference.

It is intentionally a **reference model**, not a single implementation schema. Runtime, representation, and provider-specific details remain replaceable.

## 1. Core proposition

Shirakami is a human-authoritative AI architecture in which AI and Runtime components may observe, analyze, propose, execute authorized protocols, and verify results, while final authority remains outside those components at the Human Gate.

> AI may increase the quality of reasoning without acquiring the right to decide.

## 2. Canonical layers

### L0 — Human Authority
Final authority, approval, rejection, revision, and authorization.

### L1 — Landscape
The relevant external/internal situation from which observations are made. Landscape is not synonymous with model state.

### L2 — Observation
A bounded representation of what has been observed. Observation must remain distinguishable from interpretation and authority.

### L3 — Evidence
Immutable, non-authoritative records retained for verification, replay, audit, and reconstruction. Evidence can inform authority but cannot become authority.

### L4 — Context / Handoff
State required to interpret and continue work across loop boundaries. `ContextSnapshot` is an immutable runtime representation. Semantic Handoff transfers context while preserving provenance, uncertainty, assumptions, and unresolved meaning.

### L5 — Protocol Candidate
A structured proposal derived from observations/context. Candidate status is explicitly non-authoritative and non-executable until Human Gate authorization.

### L6 — Human Gate
The authority boundary. Candidate/Protocol information may be reviewed, rejected, revised, or approved. No lower layer may silently create authority.

### L7 — Authorized Protocol
A protocol explicitly authorized through the Human Gate. Authorization is distinct from structural validity and from eventual execution correctness.

### L8 — Runtime / Adapter
Executes authorized Protocols using replaceable runtime/provider components. Runtime must not manufacture Human authority.

### L9 — Verification
Checks observed execution/results against the relevant Protocol, Evidence, and Context. Verification may produce mismatch/uncertainty Evidence but does not itself authorize the next action.

## 3. Canonical loop

```text
Landscape
   ↓
Observation
   ↓
Evidence / Context
   ↓
Protocol Candidate
   ↓
Human Gate
   ├── reject / revise ──→ Observation / Context
   └── approve
          ↓
   Authorized Protocol
          ↓
       Runtime
          ↓
       Result
          ↓
     Verification
          ↓
       Evidence
          ↺
```

## 4. Authority invariant

The following components are non-authoritative by default:

- AI Runtime;
- Evidence;
- ContextSnapshot;
- Semantic Handoff;
- Protocol Candidate;
- structural validation;
- Replay;
- Verification;
- API success/failure state.

Only the defined Human Gate path may grant decision/execution authority.

## 5. Four-way separation

Shirakami explicitly separates:

```text
Structural validity
        ≠
Semantic truth
        ≠
Human authorization
        ≠
Verified outcome
```

A valid representation is not necessarily true. A plausible interpretation is not approval. An approved protocol is not a verified outcome.

## 6. Evidence contract

Currently modeled guarantees:

- immutability;
- non-authority;
- Human-gated promotion;
- replayability;
- deterministic replay for the same ordered sequence and rules;
- fingerprintability;
- mismatch externalization.

Not currently canonical guarantees:

- universal event identity;
- complete causal lineage;
- universal timestamp ordering;
- order independence of conflicting Evidence;
- automatic conflict resolution;
- concurrent merge semantics.

Those properties require concrete requirements, implementation, deterministic tests, and Human Gate review before promotion into the Core model.

## 7. Protocol contract

A Protocol Candidate must remain:

```text
status = CANDIDATE
authority = false
executable = false
```

Candidate generation must not silently rank, select, prioritize, approve, promote, activate, mutate Landscape, invent domain facts, or convert uncertainty into certainty.

## 8. Context and Handoff contract

Context carries the state required to interpret or continue work. A Semantic Handoff must preserve, where available:

- source identity;
- Observation/Evidence references;
- relevant Landscape context;
- Protocol/Candidate identity;
- execution state;
- uncertainty;
- provenance;
- labeled assumptions;
- unresolved questions.

Context does not grant authority.

## 9. Representation boundary

The semantic contract is authoritative over any particular serialization format.

```text
Canonical semantics
       ↓
representation contract
       ↓
的目YAML / Protocol IR / other representation
       ↓
Runtime implementation
```

The current Matome YAML implementation is a compact Protocol IR and must not be mistaken for the complete v3.2 conceptual model.

## 10. Model v3.2 relationship

`shirakami-model-v3.2.yaml` remains valuable as the broader conceptual/collaboration architecture. Its Thread, Presenter, Conference, Optimization, RPG, education, organizational, and rendering concepts should not automatically become Core Runtime primitives.

The v0.2 Canonical Model therefore distinguishes:

- **Reviewed Core:** C-01, C-02, C-03, C-04, C-05, C-07, C-10;
- **Core Supporting Principles:** C-06, C-08, C-09;
- **Collaboration:** Thread, Presenter, Conference, optimization and related coordination constructs;
- **Application:** education, organization, RPG and domain profiles;
- **Representation:** 的目YAML and other serializations;
- **Research:** unresolved temporal, causal, conflict, concurrency, and provider-specific questions.

## 11. Traceability requirement

Every Core concept should eventually map to:

```text
Model definition
   ↓
Normative specification
   ↓
Runtime implementation
   ↓
Deterministic test
   ↓
Evidence / audit artifact
```

Missing links are reported as gaps rather than inferred.

## 12. Core invariant decision

The 2026-10-05 Human Gate decision promoted the following seven invariants to Reviewed Core:

- C-01 — Human Authority
- C-02 — Evidence Non-Authority
- C-03 — Candidate Non-Authority
- C-04 — Context Non-Authority
- C-05 — Uncertainty Preservation
- C-07 — Verification Non-Authority
- C-10 — Human Gate for Promotion

The following remain Core Supporting Principles rather than equivalent Reviewed Core invariants:

- C-06 — Structural/Semantic Separation
- C-08 — Runtime Replaceability
- C-09 — Evidence Replayability

Promotion is scoped. It does not mean semantic truth, production readiness, security certification, external validation, patentability, or universal interoperability.

## 13. Unified invariant audit evidence

A unified CI audit was executed against the C-01 through C-10 evidence test set on 2026-10-05.

- OS PR: #568 (draft, not merged)
- CI workflow: `Core Invariant Full Audit`
- CI run: **37232354912**
- Result: **48 passed in 0.68s**
- Audit commit: `cdba16e2471ead3aea74cd2e7cb97f8ecfb86363`

The unified result strengthens the implementation/test evidence chain. It does not constitute semantic truth, production certification, external validation, patentability, or universal interoperability. The separate Human Gate decision is recorded in `docs/HUMAN_GATE_DECISION_RECORD_v0.1.md`.

## 14. Open model questions

1. Canonical provenance fields across Evidence, ContextSnapshot, and Semantic Handoff.
2. Canonical 的目YAML schema, if one is ultimately required.
3. Temporal ordering and causal lineage semantics.
4. Conflict and concurrent merge semantics.
5. Exact normative mapping of all Core invariants to R0100/tests.
6. Criteria for moving a collaboration/application concept into Core.

These remain research/extension questions and are not silently promoted by this decision.

## 15. Promotion rule

No unresolved research question becomes a Core invariant merely because it appears useful. Promotion requires:

1. observed requirement;
2. explicit normative statement;
3. minimal implementation;
4. deterministic test;
5. Evidence/audit artifact;
6. Human Gate review.

## 16. Human Gate

Required: true  
Decision: APPROVED WITH SCOPE  
Status: reviewed Core scope approved  
Reviewed Core: C-01, C-02, C-03, C-04, C-05, C-07, C-10  
Supporting Principles: C-06, C-08, C-09  
Decision record: `docs/HUMAN_GATE_DECISION_RECORD_v0.1.md`
