# 41. Décision fail-closed sur Base

Ce chapitre documente le refus sûr lorsqu’une donnée de contexte Base est absente, périmée ou incohérente, à partir de prototype/base_action_policy.py. La lecture distingue une décision explicitement refusée d’un état simplement inconnu.

## Point de départ

La politique doit examiner l’identité, l’action, le montant et le contexte avant toute émission. Une réponse vide ou ambiguë ne doit pas être transformée en permission implicite.

## Limite

Un refus local ne protège pas contre une autorité distante déjà compromise. Ce chapitre ne déclare ni test réussi, ni audit, ni aptitude au déploiement.

[Retour au sommaire](./README.md)
