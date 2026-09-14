"""Minimal runnable HTTP interface for SHBB API v0.1.

This module deliberately keeps the Runtime provider-neutral.  The reference
implementation stores an in-memory Landscape and returns observations without
requiring an LLM.  A model provider can be attached later behind the same
runtime boundary.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

try:
    from fastapi import FastAPI
    from pydantic import BaseModel, Field
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("Install dependencies with: pip install -r requirements.txt") from exc


@dataclass
class Landscape:
    observations: list[dict[str, Any]] = field(default_factory=list)
    unresolved_questions: list[str] = field(default_factory=list)
    revisits: list[dict[str, Any]] = field(default_factory=list)
    catches: list[dict[str, Any]] = field(default_factory=list)

    def snapshot(self) -> dict[str, Any]:
        return asdict(self)


landscape = Landscape()
app = FastAPI(title="SHBB API", version="0.1.0")


class ObserveRequest(BaseModel):
    input: str = Field(min_length=1)
    mode: str = "normal"
    context: dict[str, Any] = Field(default_factory=dict)


class RevisitRequest(BaseModel):
    question: str = Field(min_length=1)
    mode: str = "normal"


class CatchRequest(BaseModel):
    content: str = Field(min_length=1)
    source_question: str | None = None


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "api": "shbb", "version": "0.1.0"}


@app.post("/observe")
def observe(req: ObserveRequest) -> dict[str, Any]:
    observation = {
        "timestamp": now(),
        "input": req.input,
        "mode": req.mode,
        "context": req.context,
    }
    landscape.observations.append(observation)

    # Contract-first reference behavior: preserve ambiguity rather than invent
    # an answer.  A provider adapter may enrich this result later.
    return {
        "observation": observation,
        "perspectives": [],
        "new_relations": [],
        "unresolved_questions": list(landscape.unresolved_questions),
        "next_observation": None,
    }


@app.get("/landscape")
def get_landscape() -> dict[str, Any]:
    return landscape.snapshot()


@app.get("/dark-layer")
def get_dark_layer() -> dict[str, Any]:
    return {
        "unresolved_questions": list(landscape.unresolved_questions),
        "revisits": list(landscape.revisits),
    }


@app.post("/revisit")
def revisit(req: RevisitRequest) -> dict[str, Any]:
    item = {"timestamp": now(), "question": req.question, "mode": req.mode}
    landscape.revisits.append(item)
    if req.question not in landscape.unresolved_questions:
        landscape.unresolved_questions.append(req.question)
    return {
        "revisit": item,
        "status": "held",
        "question": req.question,
    }


@app.post("/catch")
def catch(req: CatchRequest) -> dict[str, Any]:
    item = {
        "timestamp": now(),
        "content": req.content,
        "source_question": req.source_question,
    }
    landscape.catches.append(item)
    if req.source_question in landscape.unresolved_questions:
        landscape.unresolved_questions.remove(req.source_question)
    return {"catch": item, "status": "recorded"}
