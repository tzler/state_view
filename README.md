# lab-trace viewer

A single static page that walks a project kept the [lab-trace](https://github.com/tzler/state) way.
Paste a GitHub repository; every commit that changed `STATE.md` becomes a point on a timeline; step with ← →
and read what the project believed at that moment (left) and why (right, `REASONING.md`, newest first),
with the figures as they were at that commit. `[Dxx]` links jump to the entry. Tabs show `RESOURCES.md`,
the `states/` snapshots, and the `agent/` files.

**Use it:** https://tzler.github.io/lab-trace-viewer/ — or open `index.html` locally.
Deep link: `…/#owner/repo@sha7`.

Public repos need nothing. Private repos: paste a fine-grained personal access token with *Contents: read*
on that repo (it stays in your browser's localStorage). Unauthenticated use is limited to 60 GitHub API
requests per hour; each state costs about three.

No server, no build: one HTML file, `marked` from cdnjs, the GitHub REST API.
