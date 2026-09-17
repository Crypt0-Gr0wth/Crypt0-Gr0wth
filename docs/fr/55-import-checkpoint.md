# 55. Checkpoint d’import

Ce chapitre examine préserver la reprise et la détection des trous à partir de prototype/hyperevm_import_idempotence.py, dans le parcours source-grounded de Crypt0-Gr0wth. Il sépare les comportements observables, les hypothèses et les conséquences possibles.

## Repères

La revue suit les entrées, les contrôles, l’état produit et les dépendances externes. Les exemples servent à rendre la lecture reproductible sans prétendre constituer un composant de production.

## Limite

un checkpoint doit représenter un état entièrement traité. Aucun test, audit ou déploiement n’est déclaré dans ce chapitre.

[Sommaire](./README.md)
