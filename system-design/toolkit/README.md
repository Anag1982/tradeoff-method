# Capacity toolkit

Two forms of the same calculators.

**`capacity_toolkit.xlsx`**: five tabs. *Unit prices* holds every price and per-node capacity the book uses, in blue input cells; the other tabs read from it. *Envelope* computes rate, stored, moved and cost from daily users, actions and sizes. *Latency budget* splits a budget across hops and computes the fan-out tail and chain availability. *Cost per thousand* prices compute, storage and egress per thousand requests and names the dominant term, with the people line beneath. *Backlog* computes queue depth, drain time and Little's law. Example values are the book's own (the notification service, the thumbnail service, the marketing burst); replace them.

**`capacity.py`**: the same calculators as functions, reading `prices.json`. `python capacity.py demo` reproduces the notification-service envelope. `build_toolkit.py` regenerates the spreadsheet.

Update prices in one place, `prices.json` or the *Unit prices* tab, when they move. The values are order-of-magnitude figures checked in September 2026.
