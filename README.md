# Crypt0-Gr0wth

Researching proof systems, confidential computation and high-integrity blockchain infrastructure.

I publish source-grounded technical paths that make protocol architecture, trust assumptions and failure modes easier to review. The work is documentary: every security limit is explicit, and no audit or production-readiness claim is implied.

## Parcours français

Le parcours documentaire français rassemble 40 chapitres sur les preuves ZK, la FHE, Base, HyperEVM et Hyperliquid. Consulter le [sommaire](docs/fr/README.md) pour suivre les contributions dans l’ordre.

## Current focus

- **Zero knowledge:** STARK execution and transcripts, universal-setup SNARKs and verifier assumptions.
- **Confidential computing:** FHE compilation, noise budgets and trusted boundaries.
- **Base:** OP Stack enclaves, agent security, data provenance and transaction approval.
- **Hyperliquid / HyperEVM:** signing, state reconciliation, block import and oracle integrity.

## Featured research paths

### Proof systems and privacy

- [STWO](https://github.com/Crypt0-Gr0wth/stwo/tree/dev/docs/fr) — Circle STARK, AIR, FRI and transcript review.
- [Marlin](https://github.com/Crypt0-Gr0wth/marlin/tree/master/docs/fr) — universal SRS, AHP and SNARK verification.
- [Concrete](https://github.com/Crypt0-Gr0wth/concrete/tree/main/docs/fr) — FHE compilation, noise propagation and trust boundaries.

### Base

- [OP Enclave](https://github.com/Crypt0-Gr0wth/op-enclave/tree/main/docs/fr) — Nitro attestation and OP Stack derivation.
- [Base Agent](https://github.com/Crypt0-Gr0wth/base-agent/tree/main/docs/fr) — tool-data provenance, session security, least privilege and explicit transaction approval.

### Hyperliquid and HyperEVM

- [Hyperliquid Rust SDK](https://github.com/Crypt0-Gr0wth/hyperliquid-rust-sdk/tree/master/docs/fr) — signing, order lifecycle and reconciliation.
- [HyperEVM Block Importer](https://github.com/Crypt0-Gr0wth/block-importer/tree/main/docs/fr) — replay, idempotence and state integrity.
- [HyperEVM Oracle](https://github.com/Crypt0-Gr0wth/hyperevm-oracle/tree/master/docs/fr) — source timestamps, Chainlink-interface semantics, keepers, EMA and defensive consumption.

## Method

Each path follows the repository source and separates observed behavior from inference. Important mechanisms receive their own chapter and commit so readers can review the reasoning incrementally. No dependencies are installed and no tests or deployments are claimed for these documentary contributions.
