# Migration rubric

For migrations, database splits, re-platforming, and any change to a system that is already running under load. The senior rows apply, with one row added and the anchors changed to reward reversibility.

| Row | Below the bar | At the bar | Above the bar | Minute |
|---|---|---|---|---|
| **Frame** | Accepts "migrate" as the objective. | Asks why, and gets a reason. | Turns the request into an objective with a date (headroom by when; independence measured how); asks what the cheap moves are before the expensive one. | |
| **Budget** | Budgets the new system's requests. | Budgets the data volume and the time to move it. | Budgets the primary's remaining capacity as the thing every step must not exceed; the backfill rate the source can give; the calendar; the cost of running two stores for the duration. | |
| **Axes** | Compares old and new engines. | Names the durability and consistency choices in the copy. | Names capture-from-the-log against dual writes with the loss rate of the dual write computed; names verification as a precision-against-cost choice with a stated threshold. | |
| **Commit** | Proposes a cutover date. | Proposes stages. | Proposes stages placed by reversibility, each leaving the system working and undone by a flag; rejects the dual write aloud; states the exit criterion of the verification stage as a number before it begins. | |
| **Deepen** | Describes the target system. | Works the backfill or the capture. | Works the mechanism that makes rollback possible (reverse capture; the old store kept current; the order of snapshot and capture that loses no change). | |
| **Reversibility** (added) | Has a step that cannot be undone early in the plan, or does not know which step it is. | Can name the irreversible step. | Names the irreversible step, places it last with a stated rollback window before it, and says what evidence must exist (weeks of shadow reads, a mismatch count) before it is taken. | |
| **Stress** | Attacks the target system. | Runs the four attacks. | Attacks the migration itself: what happens if the primary saturates during the backfill, if the capture falls behind, if a corruption is found a month into the window; answers each from the plan rather than improvising. | |

**The push every migration gets:** "a month in, you find a corrupting bug in the new store." A candidate whose plan has a reverse path answers in two sentences; one whose plan does not has to say "repair in place and hope."
