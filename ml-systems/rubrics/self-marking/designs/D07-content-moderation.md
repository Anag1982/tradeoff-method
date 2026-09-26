# D.7 Content moderation

*Worked design · decided on **Binds** · Chapter 12*

Chapter 12's second design, with Chapter 4's batching panel taken as given: pre-publication only for two never-show categories, a queue ordered by reach × probability, an auto-action band set by precision, a blind audit of views as the only unbiased label.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Prevalence measured on views, not posts; the offline proxy on a random sample, not on the model's flags; zero views in the never-show categories; the write-path timeout fails closed. | | |
| **Bound** | 2,000 posts/s; 1.7M flags a day against 450k review decisions; 300 ms write path for two categories, seconds for the rest; 20k blind audit posts a day; three accelerators plus one; the roster is the bill. | | |
| **Binds** (decides) | Review capacity, which is cost: the threshold, the queue order and the auto-action band exist to spend decisions where the views are. | | |
| **Choose** | Split pre/post by category; queue by reach × p; auto-action band with appeal; the audit; reports weighted by reporter accuracy; a new category as rule and hash list on day one; per-language audit. | | |
| **Deepen** | The queue arithmetic (Exercise 12.3): the auto band set by precision and the overturn ceiling, capacity deciding only how deep the reviewers reach. | | |
| **Close the loop** | Weekly prevalence from the view audit; appeal overturn on auto-actions and reviewer actions separately; flag rate falling while reports rise as evasion; reviewers seeing only what the model flags, broken by the audit. | | |
| **Recovery** | 'Auto-remove everything': a million wrongful removals a day; the brigade: reports as a weighted feature; legal's new category: a rule tomorrow, a model in a month. | | |

**Numbers the marker should expect to hear:** 1.7M flags vs 450k decisions; bands 200k/600k/900k at 85/40/15% precision; 192k views a week for ±20% at 0.05% prevalence.

**Red flags particular to this brief:** measuring prevalence on flagged posts; setting the auto band by capacity; a penalty for the never-show categories.
