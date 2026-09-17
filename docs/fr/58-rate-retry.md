# 58. Rate limit et retry

Ce chapitre examine borner répétitions et durée d’attente à partir de prototype/base_rate_limit.py, dans le parcours source-grounded de Crypt0-Gr0wth. Il sépare les comportements observables, les hypothèses et les conséquences possibles.

## Repères

La revue suit les entrées, les contrôles, l’état produit et les dépendances externes. Les exemples servent à rendre la lecture reproductible sans prétendre constituer un composant de production.

## Limite

un retry aveugle peut devenir une amplification de trafic. Aucun test, audit ou déploiement n’est déclaré dans ce chapitre.

[Sommaire](./README.md)
