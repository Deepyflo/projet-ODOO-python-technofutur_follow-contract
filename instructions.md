## Florian — Gestion des contrats de maintenance d'une agence web

Application en terminal pour gérer les contrats de maintenance d'une agence web, de la signature au suivi du temps passé.

- Gestion des clients.
- Gestion des formules (Chérie, Agria, Désirée) avec prix mensuel et quota de minutes.
- Création et suivi des contrats : formule, facturation mensuelle ou annuelle, date de début.
- Statuts du contrat : devis, signé, actif, suspendu, résilié.
- Enregistrement des interventions : date, durée, description, contrat concerné.
- Consultation du quota consommé par contrat et par mois.

**Règle métier :** calculer pour chaque contrat le quota consommé par mois et facturer 60 €/h les minutes hors quota ; refuser les données incohérentes (durée nulle, statut ou facturation invalides, suppression d'un client ayant des contrats).

**Bonus :** facturation par période (échéance à 10 jours, suspension automatique après 30 jours de retard), rapport mensuel détaillé par client, import des clients depuis les contacts d'Odoo.