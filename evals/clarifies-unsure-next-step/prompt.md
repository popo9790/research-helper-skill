---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

我在做 few-shot segmentation，baseline (PFENet) 在 PASCAL-5i 1-shot 復現出來跟論文差不多。我自己加了一個 prototype refinement 的模組，但 mIoU 只多了 0.3，感覺好像沒什麼用...我現在有點不知道下一步要做什麼
