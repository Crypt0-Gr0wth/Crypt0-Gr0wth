# Parcours FHE

## Promesse

Le chiffrement homomorphe permet d’exécuter certaines opérations sur des données chiffrées. L’analyse doit cependant suivre tout le cycle de vie des clés et des résultats.

## Compilation

Identifier le schéma utilisé, les opérations supportées, la représentation des circuits et les transformations appliquées par le compilateur. Les conversions implicites et les approximations doivent être rendues visibles.

## Budget de bruit

Chaque opération peut réduire la marge disponible avant déchiffrement. Documenter les paramètres, la profondeur multiplicative, les opérations de rafraîchissement et les conditions d’échec plutôt que de résumer le système par le seul mot « privé ».

## Frontières de confiance

Préciser qui génère les clés, qui peut déchiffrer, où s’effectue la gestion des clés et si les métadonnées, les tailles ou les erreurs révèlent des informations. La confidentialité du calcul ne garantit pas l’intégrité des entrées.

## Limites

Les résultats dépendent fortement des paramètres et du cas d’usage. Une lecture du code explique l’architecture déclarée, mais ne constitue ni une preuve de sécurité ni une mesure de performance.
