# Shirakami Evidence Contract Profile v0.1

Status: draft / review required  
Date: 2026-10-05  
Parent: `docs/CANONICAL_MODEL_MAP_v0.1.md`

## Purpose

Define the guarantees that the current Shirakami Evidence layer can claim, and explicitly separate them from guarantees that remain unresolved.

This profile is intentionally conservative. An Evidence record is not a decision, an authority grant, or a semantic truth claim merely because it exists or can be replayed.

## 1. Guaranteed properties

### 1.1 Immutability

Once recorded, an EvidenceRecord is treated as immutable. Later processing must create a new record or a derived state rather than silently rewriting the original record.

### 1.2 Non-authority

Evidence does not grant authority. Evidence may support analysis, candidate generation, review, replay, or verification, but it cannot substitute for Human Gate authorization.

### 1.3 Replayability

Recorded Evidence can be replayed to reconstruct the corresponding Landscape state through the Runtime replay path.

### 1.4 Deterministic replay for an identical ordered sequence

Given the same ordered Evidence sequence and the same replay rules, replay is expected to produce the same reconstructed state/fingerprint.

This does **not** imply that arbitrary reordering of Evidence is semantically equivalent.

### 1.5 Fingerprintability

Replayable execution and reconstructed Landscape state can be fingerprinted for comparison and verification.

### 1.6 Human-Gated promotion

Promotion of Evidence into an accepted/authoritative state requires the designated Human Gate. Technical success, API success, comparative agreement, or AI output does not itself constitute authorization.

## 2. Explicit non-guarantees

The following are **not yet canonical guarantees**:

- globally unique event identity;
- universal timestamp semantics;
- causal parentage for every Evidence record;
- complete temporal ordering semantics;
- concurrency semantics;
- commutativity under Evidence reordering;
- automatic conflict resolution;
- automatic merge semantics;
- complete reconstruction of the historical Landscape independent of stored ordering;
- semantic truth of an Evidence record solely because it was recorded.

These are open specification/research questions, not assumptions.

## 3. Core distinction

```text
Immutable
   ≠
Causally complete

Replayable
   ≠
Order-independent

Recorded
   ≠
True

Verified
   ≠
Human-authorized

Technical success
   ≠
Decision authority
```

These distinctions are part of the current Shirakami model and should not be collapsed for convenience.

## 4. Evidence lifecycle

```text
Observation
   ↓
EvidenceRecord
   ↓
Analysis / Candidate generation
   ↓
Human Gate
   ↓
Accepted / authorized transition
   ↓
Runtime execution
   ↓
Verification
   ↓
New EvidenceRecord
```

A failed or uncertain verification result remains evidence of an observed state; it does not become an authorization signal merely because it is stored.

## 5. Provenance profile

Current provenance is sufficient for the present replay/audit model but is not declared causally complete.

Future provenance fields such as:

- `event_id`
- `parent_evidence_id`
- `sequence_number`
- `timestamp`
- `landscape_version`
- causal relation identifiers

must not be added merely by convention. They should be introduced only when a required guarantee—such as replay independence, causal reconstruction, auditability, concurrency handling, or conflict detection—has been explicitly identified.

## 6. Conflict and ordering

For the current contract, ordering is treated as potentially meaningful. The system must not silently claim:

```text
A → B == B → A
```

unless a specific invariant and test establish that equivalence.

Where conflicting Evidence exists, the correct next step is to preserve the conflict as observable state and define the required resolution semantics through specification and Human Gate, rather than silently converting conflict into authority.

## 7. Verification requirements

A future Evidence-contract test suite should separately verify:

1. immutability;
2. non-authority;
3. Human Gate enforcement;
4. deterministic replay of identical ordered sequences;
5. fingerprint stability;
6. mismatch preservation;
7. behavior under reversed Evidence ordering;
8. duplicate Evidence handling;
9. concurrent/conflicting Evidence behavior;
10. provenance sufficiency for whatever guarantees are ultimately claimed.

## 8. Relationship to Canonical Model

This profile establishes Evidence as a **Core mechanism** while keeping unresolved temporal/causal semantics outside the current normative guarantee set.

The Canonical Model Map should reference this profile whenever Evidence is described as immutable, replayable, or authoritative/non-authoritative.

## Human Gate

Required: true  
Decision: pending  
Status: draft / review required
