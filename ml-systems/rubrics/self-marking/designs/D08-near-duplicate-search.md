# D.8 Visual near-duplicate search

*Worked design · decided on **Choose** · Chapter 12*

Chapter 12's third design, worked from scratch: no label — pairs made by transformation; the model is a distance and the decision is a threshold; a hash in front, a quantised embedding in a cluster index, exact verification of twenty, a reviewed whitelist.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | 'The model is the embedding and the decision is the threshold'; recall on a transformation suite at a false-match ceiling; a meme removed because it resembles a removed meme, never — the whitelist. | | |
| **Bound** | 2B images; 5M uploads/day; 200 ms with ~30 used; 1 TB full precision on disk, 64 GB quantised, 70 GB with a cluster index; embedding the backfill a thousand accelerator-hours, so the model is frozen. | | |
| **Binds** | Quality in two parts: index recall at two billion (bought with memory) and the threshold's false-match rate at two billion candidates. | | |
| **Choose** (decides) | Hash then embedding; 128 dims quantised to 32 bytes; cluster index; verify the top twenty against full vectors so the ceiling is met over twenty pairs rather than two billion; whitelist; hot path for the last hour. | | |
| **Deepen** | The false-match arithmetic (Exercise 12.5): 10⁻¹⁴ per pair without verification, 10⁻⁶ with — 'the index's job is to put the true copy in the twenty; the verifier's is to be right about twenty.' | | |
| **Close the loop** | Index recall against brute force daily; re-upload rate from the audit; the adversary's new transformation answered by a small second model against the 50M known-bad set until the yearly re-embed; the whitelist guarded. | | |
| **Recovery** | 'Why not a hash?': kept in front, misses crops and overlays; the meme: a match is not an action; a new transformation in week two: mask it, or a small model on the hot path. | | |

**Numbers the marker should expect to hear:** 2B × 128 dims; 512 B / 256 GB / 64 GB; 96 GB budget fits the cluster index; 100 wrongful matches a day → 10⁻⁶ per pair over 20.

**Red flags particular to this brief:** a threshold on the approximate distance; removing every match; a model that is retrained monthly with a 2B re-embed.
