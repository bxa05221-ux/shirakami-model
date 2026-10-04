# Human Gate Promotion Boundary Test v0.1

Status: draft / review required

## Purpose

This specification defines the negative test required before implementing automatic Core promotion.

The test must demonstrate that technical audit evidence cannot itself change the Human Gate decision state.

## Required invariant

Given:

    technical_audit = PASS
    human_gate_status = REVIEW_PENDING

then:

    core_promotion = false

must remain true until an explicit Human Gate decision is recorded.

## Forbidden transitions

The following inputs must not transition REVIEW_PENDING to APPROVED:

- CI success;
- all tests passing;
- AI recommendation;
- Runtime success;
- Verification success;
- pull-request mergeability;
- structural validation success.

## Positive transition

Only an explicit, attributable Human Gate decision may establish APPROVED, with scope and conditions recorded.

## Implementation note

This is intentionally a specification before implementation. The model must not infer a mechanism merely because the desired behavior is clear.

A future deterministic test should cover at least:

1. PASS evidence exists;
2. status remains REVIEW_PENDING;
3. no automation path can set APPROVED;
4. an explicit Human Gate record is required for APPROVED.

## Acceptance boundary

A passing implementation test proves the boundary is implemented. It does not itself constitute the Human Gate decision for C-01 through C-10.
