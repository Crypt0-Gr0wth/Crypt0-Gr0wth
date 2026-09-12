# Carte de recherche

Ce dépôt relie quatre axes complémentaires : preuves succinctes, calcul chiffré, infrastructure Base et exécution Hyperliquid/HyperEVM. Cette carte sert à transformer une lecture de code en hypothèse vérifiable.

## Chaîne d'analyse

Source primaire → observation dans le code → invariant attendu → menace étudiée → décision documentée.

## Axes

- **STARK et SNARK** : suivre la trace d'exécution, les contraintes, le transcript et les hypothèses du vérificateur. L'objectif est d'identifier précisément ce qui est prouvé et ce qui reste une hypothèse de confiance.
- **FHE** : distinguer les opérations sur chiffrés, le budget de bruit, la compilation et la frontière de confiance autour des clés.
- **Base** : examiner la provenance des données, l'autorité des agents, les listes d'actions autorisées et l'approbation avant transaction dans un environnement OP Stack.
- **Hyperliquid et HyperEVM** : vérifier signatures, nonce, import de blocs, fraîcheur des oracles et réconciliation entre événements et état local.

## Limites

Ce document décrit une méthode de recherche et ne constitue ni un audit cryptographique ni une garantie de production. Les prototypes associés restent autonomes, sans dépendance ni accès réseau ; aucune installation, compilation ou exécution n'est revendiquée pour cette contribution.
