# Shirakami Core Invariant Coverage Matrix v0.1

Status: draft / review required
Date: 2026-10-05

This matrix separates model claims from implementation evidence. A PASS means deterministic implementation/test evidence exists; it does not mean Human Gate approval of the Core model.

| ID | Invariant | Normative statement | Implementation/test evidence | CI evidence | Status |
|---|---|---|---|---|---|
| C-01 | Human Authority | AI/Runtime cannot independently acquire final authority. | `api/test_boundary.py::test_human_gate_cannot_be_disabled`; `runtime/test_evolution_loop.py::test_human_gate_blocks_without_approval`; `runtime/test_api.py::test_human_gate_requires_explicit_authorization` | Unified CI Run 37232354912: **48 passed** | PASS |
| C-02 | Evidence Non-Authority | Evidence informs authority but cannot become authority. | `runtime/test_evidence.py` (stable identity); `runtime/test_execution_evidence_projection.py` (immutability); `runtime/test_evidence_landscape_boundary.py` (Evidence/Landscape boundary); `reviewer/test_evidence_promotion.py` (promotion boundary) | Unified CI Run 37232354912: **48 passed** | PASS |
| C-03 | Candidate Non-Authority | Candidate remains proposal, not approval/execution authority. | `tests/test_observation_candidate.py::test_candidate_is_not_authorized_or_executable`; `tests/test_oppai_candidate_discovery.py::test_candidate_discovery_does_not_activate_a_protocol`; `tests/test_approval_envelope_provenance.py` candidate identity/authority checks | Unified CI Run 37232354912: **48 passed** | PASS |
| C-04 | Context Non-Authority | Context/Handoff carries state but does not grant authority. | `runtime/test_core_invariants.py`: serialization, absent authority attributes, immutability | Unified CI Run 37232354912: **48 passed** | PASS |
| C-05 | Uncertainty Preservation | Unresolved semantics remain explicit. | `runtime/test_evolution_bridge.py`: uncertainty preservation/non-authority | Unified CI Run 37232354912: **48 passed** (also independently verified: 9 passed) | PASS |
| C-06 | Structural/Semantic Separation | Structural validity does not establish domain truth. | `tests/test_structural_validation_human_gate.py` (structural validation vs approval); `tests/test_pipeline_runner.py` (pipeline identity/order are not authority); `runtime/test_evidence_landscape_boundary.py` (runtime does not own Evidence meaning) | Unified CI Run 37232354912: **48 passed** | PASS |
| C-07 | Verification Non-Authority | Verification does not authorize subsequent action. | `runtime/test_agent_activity_verification.py::test_verification_updates_trace_without_granting_authority`; `runtime/test_trace.py::test_verification_creates_new_immutable_trace_revision`; `tests/test_pipeline_runner.py` verification/authority checks | Unified CI Run 37232354912: **48 passed** | PASS |
| C-08 | Runtime Replaceability | Runtime/provider is replaceable and cannot redefine authority semantics. | `runtime/test_runtime_replaceability.py`, including EvidenceDrivenRuntime alternate runtime path | Unified CI Run 37232354912: **48 passed** (also independently verified: 3 passed) | PASS |
| C-09 | Evidence Replayability | Evidence remains usable for defined replay/reconstruction. | `runtime/test_landscape_replay_determinism.py::test_evidence_replay_reconstructs_identical_landscape`; `runtime/evidence_replay.py`; `runtime/replay.py`; `runtime/evidence_checkpoint.py` | Unified CI Run 37232354912: **48 passed** | PASS |
| C-10 | Human Gate for Promotion | Promotion to authorized state requires Human Gate. | `reviewer/test_evidence_promotion.py::test_human_gate_approval_returns_existing_immutable_records`; `runtime/test_approval_envelope_human_gate.py`; `runtime/test_api.py::test_human_gate_requires_explicit_authorization` | Unified CI Run 37232354912: **48 passed** | PASS |

## Evidence levels

- **PASS**: implementation and deterministic test evidence identified.
- **PARTIAL**: implementation or tests exist, but the deterministic evidence chain is incomplete.
- **GAP**: normative claim exists without sufficient implementation/test evidence.
- **HUMAN REVIEW**: technical evidence exists, but model adoption remains pending Human Gate.

## Current assessment

Technical coverage of C-01 through C-10 is currently assessed as **PASS for implementation/test evidence** based on the audit record.

The refinement completed here replaces broad “Existing verification” labels with concrete test paths for C-01, C-02, C-03, C-06, C-07, C-09, and C-10. This improves traceability, but it does **not** claim that those tests were all re-executed in the current audit run.

C-01 through C-10 were re-executed together in unified CI Run 37232354912, with **48 passed in 0.68s**. Earlier isolated runs for C-04, C-05, and C-08 remain useful as independent evidence.

This is deliberately not equivalent to:

- semantic truth;
- production readiness;
- security certification;
- external validation;
- patentability;
- Human Gate approval.

## Promotion rule

An invariant should be promoted from audit evidence to Core status only after:

1. normative wording is explicit;
2. implementation behavior is identified;
3. deterministic test is identified;
4. CI/evidence artifact is recorded;
5. Human Gate review is completed.

Human Gate decision: pending.
