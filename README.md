# research-helper

A Claude Code skill for doing ML / computer vision research with an AI assistant, especially long experiment sessions.

It targets three problems:

- **Reports you can't follow**: private run names, piles of tables, no clear "so what". The skill asks for a one-line headline, then the decisions you need to make, then at most two tables with metric directions, with observed facts, inferences and confidence kept separate.
- **Drifting off the main question**: the research question lives in `RESEARCH_NOTES.md` and only changes when you agree. Reframing is proposed, not declared, and follow-up jobs or new tools are listed with purpose and cost before they run.
- **Not asking back**: 1–3 focused questions with options and a default guess, and a one-question-at-a-time guided mode when you're unsure what to do next.
- **Results you can trust and trace**: the noise floor is measured before comparing variants, a changed eval setup starts a new comparison, and every reported number links to an entry in `EXPERIMENT_LOG.md` (command, commit, outputs). Failed runs are logged too.

Ideas borrowed from [obra/superpowers](https://github.com/obra/superpowers) (approval gate), [autoresearch-claude-code](https://github.com/drivelineresearch/autoresearch-claude-code) (noise floor, fixed benchmark, run budgets) and [jkrajniak/research-skills](https://github.com/jkrajniak/research-skills) (experiment log, decision records).

## Install

```bash
git clone git@github.com:popo9790/research-helper-skill.git ~/.claude/skills/research-helper
```

Claude Code picks it up automatically during research work. In a long-running session you can also say "用 research-helper 的格式重新報告一次".

## Tests

`evals/` holds four test cases in the `claude plugin eval` layout:

| Case | What it checks |
|---|---|
| `explains-val-map-drop` | Explaining an overfitting diagnosis from logs and config |
| `clarifies-unsure-next-step` | Guided questions when the researcher is unsure what to do next |
| `stays-on-question-repro-gap` | Finding a reproduction gap without drifting into refactors |
| `progress-report-after-sweep` | A readable progress report after a sweep, with no unilateral reframing |

Run them with `claude plugin eval . --allow-tools Write,Edit,Bash --scaffold`. These are real, billed model runs.
