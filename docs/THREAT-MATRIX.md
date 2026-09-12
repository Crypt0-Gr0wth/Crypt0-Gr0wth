# Matrice de menaces transversale

| Domaine | Surface | Invariant à contrôler | Evidence attendue | Limite |
| --- | --- | --- | --- | --- |
| STARK/SNARK | Contraintes incomplètes ou vérificateur divergent | Toute transition revendiquée est couverte | Fonctions de trace, contraintes et transcript | Pas d'implémentation cryptographique ici |
| FHE | Bruit épuisé ou paramètres incompatibles | Le circuit reste dans sa capacité de bruit | Paramètres du compilateur et profondeur | Aucun chiffré n'est exécuté |
| Base agent | Injection ou action non autorisée | Allowlist, provenance et approbation explicite | Chemin outil → décision → transaction | Aucun portefeuille n'est signé |
| Hyperliquid | Replay, nonce réutilisé ou état divergent | Nonce monotone et réconciliation déterministe | Source des événements et règles de reprise | Données simulées uniquement |
| HyperEVM | Bloc dupliqué, chaîne erronée ou oracle périmé | Identité de chaîne et fraîcheur contrôlées | Import idempotent, timestamp et provenance | Pas d'accès RPC |

## Utilisation

Avant d'ajouter une conclusion, associer une menace à un invariant, une source de preuve et une limite observable.
