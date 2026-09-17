# 24. Limitation de débit Base

Ce chapitre documente encadrer retries, quotas et état dégradé à partir de prototype/base_rate_limit.py. La lecture suit le code et les documents du dépôt Crypt0-Gr0wth, en distinguant les faits observables des interprétations.

## Point de départ

Le parcours identifie les entrées, les contrôles, l’état produit et les dépendances externes. Chaque conclusion doit pouvoir être rattachée au fichier source indiqué.

## Limite

refuser temporairement vaut mieux qu’agir sur une donnée inconnue. Ce chapitre ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Chapitre suivant](./25-base-provenance.md)
