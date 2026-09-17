# 50. Nonce et expiration

Ce chapitre examine combiner unicité et durée de validité à partir de prototype/hyperliquid_nonce_guard.py, dans le parcours source-grounded de Crypt0-Gr0wth. Il sépare les comportements observables, les hypothèses et les conséquences possibles.

## Repères

La revue suit les entrées, les contrôles, l’état produit et les dépendances externes. Les exemples servent à rendre la lecture reproductible sans prétendre constituer un composant de production.

## Limite

un nonce unique mais permanent élargit la fenêtre d’attaque. Aucun test, audit ou déploiement n’est déclaré dans ce chapitre.

[Sommaire](./README.md)
