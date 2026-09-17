# 53. Oracle en mode dégradé

Ce chapitre examine définir stale, missing et outlier à partir de prototype/hyperevm_oracle_freshness.py, dans le parcours source-grounded de Crypt0-Gr0wth. Il sépare les comportements observables, les hypothèses et les conséquences possibles.

## Repères

La revue suit les entrées, les contrôles, l’état produit et les dépendances externes. Les exemples servent à rendre la lecture reproductible sans prétendre constituer un composant de production.

## Limite

continuer avec la dernière valeur peut amplifier une erreur. Aucun test, audit ou déploiement n’est déclaré dans ce chapitre.

[Sommaire](./README.md)
