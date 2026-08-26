# Nursery Resilience α1.0 Architecture

## 1. Core flow

```text
Child / Person
  ↓
Observation
  ↓
Individual Landscape
  ↓
Individual Plan
  ↓
Practice
  ↓
Outcome / Evidence
  ↓
Group Landscape
  ↓
Organization Landscape
  ↓
Next Plan
```

## 2. Reverse evaluation flow

```text
Organization Landscape
  ↓
Evidence
  ↓
Third-party evaluation
  ↓
Evaluation findings / recommendations
  ↓
Organization Landscape
  ↓
Improvement plan
  ↓
Practice
  ↓
New Evidence
```

Third-party evaluation is therefore a reverse-reading and feedback loop over the same Landscape/Evidence model, not a disconnected reporting application.

## 3. External Landscape

External information is an input to the Landscape, not an autonomous decision engine.

Initial sources/domains:

- weather and warnings
- disaster information
- wildlife / nuisance-animal alerts
- local public information
- transport / infrastructure disruptions where relevant

External information must be attributed to its source and timestamped. Human staff decide whether and how it changes childcare plans.

## 4. Anonymous internal reporting

Internal reports are treated as protected Signals.

```text
Anonymous / pseudonymous report
  ↓
Protected Signal
  ↓
Access-controlled review
  ↓
Evidence / organizational pattern
  ↓
Human decision
  ↓
Improvement
```

Reporter identity, if technically retained for safety or legal reasons, must remain separated from ordinary childcare Landscape data and exposed only under explicitly authorized conditions.

## 5. Domain portability

The nursery implementation is intentionally a reference implementation rather than a hard-coded ontology for all human-support domains.

Potential future domains:

- school support
- employment support
- elder care
- medical / care environments

Domain-specific professional judgments must remain in domain protocols rather than being embedded in the generic Runtime.
