# Intégrité de Base et HyperEVM

## Provenance

Une analyse fiable suit la donnée depuis sa source jusqu’à la décision ou la transaction. Chaque étape doit préciser l’émetteur, le format, le timestamp et la validation appliquée.

## Base

Pour un flux OP Stack ou un agent, distinguer les données observées, les attestations, les outils appelés et l’autorisation finale. Une transaction ne devrait être approuvée qu’après vérification de son intention, de sa destination et de ses paramètres.

## HyperEVM

Pour l’import de blocs et les oracles, suivre les numéros de bloc, les timestamps, les replays, les revalorisations et la reprise après interruption. L’idempotence évite qu’une même entrée produise plusieurs effets.

## Contrôles

Documenter la gestion des nonces, la fraîcheur des données, les reorgs, les valeurs manquantes et les divergences d’état. Une interface compatible ne suffit pas à établir l’exactitude d’une source.

## Limites

Ce parcours décrit les points de revue visibles dans les sources. Il ne garantit pas la disponibilité, la résistance aux compromissions des dépendances ni la sûreté d’un déploiement réel.
