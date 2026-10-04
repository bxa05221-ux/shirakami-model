# Shirakami Canonical Model Map v0.1

Status: draft / audit baseline  
Date: 2026-10-05  
Purpose: establish a traceable map from Shirakami concepts to architecture, specification, runtime, evidence, and verification.

> This document is a consolidation artifact. It does not replace human review, existing specifications, implementation evidence, or legal evaluation.

## 1. Canonical layering

```text
CORE MODEL
  ↓
ARCHITECTURE / COGNITIVE MODEL
  ↓
SPECIFICATION / NORMATIVE CONTRACT
  ↓
RUNTIME / IMPLEMENTATION
  ↓
EVIDENCE / VERIFICATION
  ↺
RESEARCH / DEVELOPMENT LANDSCAPE
```

The model layer defines what Shirakami is. Architecture describes the major interaction and observation structure. Specification defines normative boundaries. Runtime implements those boundaries. Evidence and verification establish what was actually observed. Research and development feed later iterations but do not automatically acquire authority.

## 2. Core concepts

| Concept | Canonical role | Architecture | Specification | Runtime | Evidence / Verification | Status |
|---|---|---|---|---|---|---|
| Human Authority | Final decision authority remains human | Human final judgment | Human Gate / approval invariants | Review boundary before execution/acceptance | Decision and authority state observable | CORE / established |
| Landscape | External/contextual field being observed | Landscape First | R0100 observation context | Observation boundary | Observation/Evidence | CORE / established |
| Observation | Input operation; not itself authority | Observation First | Observation event | observation/candidate path | Recorded observation | CORE / established |
| Context | State carried across work | Human Context First | Context Snapshot | API/context routing | Snapshot/provenance | CORE / established |
| Evidence | Immutable externalized record | Evidence separation | Evidence contract | EvidenceRecord / store | Replay, promotion, verification | CORE / established |
| Protocol | Structured executable intent | Language Protocol | Protocol Contract / Candidate | Protocol execution boundary | Candidate/accepted distinction | CORE / established |
| Human Gate | Authorization boundary | Human judgment | Mandatory approval before acceptance/execution | Review/approval boundary | Authority state | CORE / established |
| Runtime | Replaceable execution component | Runtime replaceable | Runtime contract | Shirakami OS / adapters | Execution results | CORE / established |
| Verification | Compare expected and observed result | Revisit / observation | Verification step | Runtime verification | Mismatch / verified evidence | CORE / established |
| Provenance | Trace origin and lineage | Context/evidence continuity | Lineage | Traceability paths | Evidence IDs / review provenance | CORE / established |
| Uncertainty | Preserve unresolved state | Dark Layer / preserve uncertainty | Failure / inconclusive states | Candidate state | Explicit mismatch/inconclusive evidence | CORE / established |

## 3. Collaboration layer

| Concept | Role | Canonical source candidate | Classification |
|---|---|---|---|
| Thread | Independent observation/context stream | `matome_yaml/shirakami-model-v3.2.yaml` | Collaboration model |
| 的目YAML | Semantic handoff/state compression artifact | `matome_yaml/` | Collaboration + protocol artifact |
| Semantic Handoff | Context/reference transfer without hidden authority | `shirakami-OS` audit/specification | Core mechanism |
| Presenter / スレゼンター | Cross-thread comparison/presentation | v3.2 model | Collaboration mechanism |
| Conference | Asynchronous multi-perspective coordination | v3.2 model | Collaboration mechanism |
| Optimization | Per-thread adaptation after comparison | v3.2 model | Collaboration mechanism |
| Re-observation / Revisit | Return to Landscape after interpretation/execution | Architecture + R0100 | Core loop mechanism |
| Catch | Human discovery/judgment residue | Architecture | Human cognition layer |

## 4. Normative execution loop

```text
Observation
  ↓
Evidence
  ↓
Analysis
  ↓
Protocol Candidate
  ↓
Human Gate
  ↓
Runtime / Adapter
  ↓
Observation / Result
  ↓
Verification
  ↓
Evidence
  ↺
```

Normative principle:

- Evidence may generate a candidate.
- AI may analyze and propose.
- Runtime may execute an approved protocol.
- AI, reviewer, HTTP success, comparative agreement, or Evidence alone must not acquire decision authority automatically.
- Human Gate remains the authorization boundary.

## 5. Cognitive / collaboration loop

```text
Landscape
  ↓
Observation
  ↓
Thread(s)
  ↓
Context / 的目YAML
  ↓
Presenter / Conference
  ↓
Optimization
  ↓
Re-observation
  ↺ Landscape
```

This loop is complementary to the normative execution loop. It should not be treated as a competing definition of the Runtime authority boundary.

## 6. Development loop

Shirakami is also developed through the same externalization, protocol, evidence, human-authorization, and verification principles it implements:

```text
Human observation / problem
  ↓
Conversation / exploration
  ↓
Externalization into protocol/schema/specification
  ↓
Runtime / API / adapter implementation
  ↓
Tests / CI / observable results
  ↓
Evidence / diff / documented residue
  ↓
Human review and acceptance
  ↓
Next development context
  ↺
```

This is self-referential, not self-authorizing.

## 7. Repository boundary map

| Repository / area | Primary responsibility | Not authoritative for |
|---|---|---|
| `shirakami-model` | Canonical conceptual model and architecture references | Runtime execution state |
| `shirakami-specification` | Stable normative specifications / protocol contracts | Automatic human decisions |
| `shirakami-OS` | Runtime, API, adapters, evidence and verification implementation | Domain truth / final human authority |
| `shirakami-research` | Experiments, hypotheses, exploratory artifacts | Stable normative contract until promoted |
| protected/private areas | Sensitive or unreleased implementation/material | Public canonical model |

## 8. Open reconciliation items

1. Freeze one canonical definition for `Context`, `Protocol`, `Evidence`, `Semantic Handoff`, `Verification`, and `Human Gate` across repositories.
2. Explicitly map `shirakami-model-v3.2` concepts to the R0100 normative loop.
3. Identify the exact Runtime files/tests implementing each normative boundary.
4. Mark historical, experimental, application-specific, and core concepts separately.
5. Establish which document is canonical when README, YAML, specification, and implementation wording diverge.
6. Complete the existing cross-layer audit and CI verification items before claiming implementation completeness.
7. Do not convert this map into a legal/patentability conclusion; keep technical evidence separate from legal conclusions.

## 9. Current assessment

The repository evidence indicates that Shirakami's core mechanisms are substantially present across model, specification, and runtime layers. The main remaining gap is not invention of additional mechanisms but canonicalization: making the relationships, terminology, source-of-truth rules, and verification links explicit enough that an external reviewer can trace a concept from model → specification → implementation → evidence without relying on personal interpretation.

## 10. Human Gate

Required: true  
Decision: pending  
Status: draft / review required
