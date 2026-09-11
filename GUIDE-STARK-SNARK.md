# Parcours STARK et SNARK

## Question centrale

Un système de preuve permet à un prouveur de convaincre un vérificateur qu’un calcul respecte des contraintes, sans lui transmettre nécessairement toutes les données du calcul.

## Points à suivre

Pour un STARK, examiner la représentation AIR, le trace du calcul, les engagements, le protocole FRI et le transcript Fiat-Shamir. Pour un SNARK, distinguer circuit, witness, système de contraintes, clé de preuve et clé de vérification.

## Hypothèses

La documentation doit séparer la sécurité liée aux fonctions de hachage, aux engagements, à la randomisation et, lorsqu’elle existe, à un SRS ou à une cérémonie de génération de paramètres.

## Vérification

Un parcours utile relie chaque étape aux fichiers du dépôt et précise les entrées publiques, les données privées et les contrôles effectués par le vérificateur. Une preuve acceptée ne démontre pas à elle seule la disponibilité ou la sûreté de l’application qui l’utilise.

## Limites

Les performances, la toxicité éventuelle d’un paramètre et les hypothèses cryptographiques doivent être évaluées séparément. Ce document décrit une méthode de lecture et ne remplace pas un audit.
