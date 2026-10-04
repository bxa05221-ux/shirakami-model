# Shirakami Core Invariant Coverage Matrix v0.1

Status: draft / review required
Date: 2026-10-05

This matrix separates model claims from implementation evidence. A PASS means deterministic implementation/test evidence exists; it does not mean Human Gate approval of the Core model.

| ID | Invariant | Normative statement | Implementation/test evidence | CI evidence | Status |
|---|---|---|---|---|---|
| C-01 | Human Authority | AI/Runtime cannot independently acquire final authority. | Existing authority-boundary implementation/tests | Existing Core verification | PASS |
| C-02 | Evidence Non-Authority | Evidence informs authority but cannot become authority. | Evidence model + authority-boundary tests | Existing Core verification | PASS |
| C-03 | Candidate Non-Authority | Candidate remains proposal, not approval/execution authority. | Candidate authority/executable constraints + tests | Existing Core verification | PASS |
| C-04 | Context Non-Authority | Context/Handoff carries state but does not grant authority. | `runtime/test_core_invariants.py`: serialization, absent authority attributes, immutability | Run 37231397388: **12 passed** | PASS |
| C-05 | Uncertainty Preservation | Unresolved semantics remain explicit. | `runtime/test_evolution_bridge.py`: uncertainty preservation/non-authority | Verified CI: **9 passed**, commit `2540777a...` | PASS |
| C-06 | Structural/Semantic Separation | Structural validity does not establish domain truth. | Existing validation/model separation tests | Existing verification | PASS |
| C-07 | Verification Non-Authority | Verification does not authorize subsequent action. | Verification/candidate boundary tests | Existing Core verification | PASS |
| C-08 | Runtime Replaceability | Runtime/provider is replaceable and cannot redefine authority semantics. | `runtime/test_runtime_replaceability.py`, including EvidenceDrivenRuntime alternate runtime path | Verified CI: **3 passed**, commit `80a9ca23...` | PASS |
| C-09 | Evidence Replayability | Evidence remains usable for defined replay/reconstruction. | Existing evidence/replay implementation and tests | Existing verification | PASS |
| C-10 | Human Gate for Promotion | Promotion to authorized state requires Human Gate. | Existing Human Gate/promotion boundary implementation | Existing verification | PASS |

## Evidence levels

- **PASS**: implementation and deterministic test evidence identified.
- **PARTIAL**: implementation or tests exist, but the deterministic evidence chain is incomplete.
- **GAP**: normative claim exists without sufficient implementation/test evidence.
- **HUMAN REVIEW**: technical evidence exists, but model adoption remains pending Human Gate.

## Current assessment

Technical coverage of C-01 through C-10 is currently assessed as **PASS for implementation/test evidence** based on the audit record.

This is deliberately not equivalent to:

- semantic truth;
- production readiness;
- security certification;
- external validation;
- patentability;
- Human Gate approval.

The next audit should replace broad "Existing verification" labels with exact test paths and CI run/commit identifiers for C-01, C-02, C-03, C-06, C-07, C-09, and C-10. Until that refinement is complete, those rows are traceability references rather than newly re-executed evidence.

## Promotion rule

An invariant should be promoted from audit evidence to Core status only after:

1. normative wording is explicit;
2. implementation behavior is identified;
3. deterministic test is identified;
4. CI/evidence artifact is recorded;
5. Human Gate review is completed.

Human Gate decision: pending.
