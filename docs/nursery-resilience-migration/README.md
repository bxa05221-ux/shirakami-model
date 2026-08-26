# Nursery Resilience α1.0 — Migration Staging

This directory stages the extraction of the Nursery Resilience reference implementation from Shirakami Model into a dedicated repository.

Target repository:

`bxa05221-ux/shirakami-nursery-resilience`

## Scope

- Individual Landscape
- Group / Organization Landscape
- Development observation and individualized childcare planning
- Childcare planning feedback loop
- Staffing / childcare load observation
- Safety, near-miss and incident records
- External Landscape (weather, disaster, wildlife / nuisance-animal information)
- Anonymous internal reporting with strict access separation
- Presenter / human review loop
- Evidence generation and third-party evaluation feedback loop

## Architecture principle

The nursery implementation is a domain reference implementation of a more general Human Support Runtime.

The domain-specific layer must remain separate from Shirakami OS Core concepts such as Landscape, Observation, Evidence, Signal, Protocol, Permission, Feedback and Audit.

## Important boundary

AI proposes, organizes and surfaces observations. It does not make professional childcare, safety, medical, legal, staffing, or evaluation decisions.

Human professionals retain decision authority.

## Extraction status

This branch is a staging point because the connected GitHub operations currently expose repository/file operations but not creation of a new top-level repository. Once the target repository exists, this directory can be migrated without changing the conceptual architecture.
