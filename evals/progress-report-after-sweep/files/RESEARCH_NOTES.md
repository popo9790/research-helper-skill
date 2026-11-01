# Research notes

## Goal
Build a one-step diffusion super-resolution model whose perceptual quality beats RefSR-X on DIV2K-val and on a real-world test set.

## Current question
RefSR-X is ahead of us by about 0.45 on NIQE. It adds a small amount of white noise (c=0.02) before decoding. If we add noise before our decoder, does that close the NIQE gap?

## Decisions
- 2026-09-12 — Use the 20k-step checkpoint as the comparison point — it's the version the paper will report
- 2026-09-13 — Start two stage-2 loss A/B runs (see session_log)

## Open questions
- Is the piecewise schedule consistently better than cosine?
