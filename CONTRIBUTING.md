# Contributing

Thanks for helping make this safer for models. You do not need to be a developer to contribute — the most valuable contributions here are contract knowledge and firsthand experience, not code.

## Ways to contribute

| I want to... | Do this |
|---|---|
| Report an agency that scammed me or someone I know | [Open a community report](https://github.com/CptRizzen/modeling-contract-review/issues/new?template=agency-report.yml) |
| Dispute or correct an entry about me or my business | [Open a correction request](https://github.com/CptRizzen/modeling-contract-review/issues/new?template=list-correction.yml) — see [SECURITY.md](SECURITY.md) |
| Report that the skill missed a bad clause or flagged something wrong | [Open a review-quality issue](https://github.com/CptRizzen/modeling-contract-review/issues/new?template=review-quality.yml) |
| Suggest a feature or a new contract type | [Open a feature request](https://github.com/CptRizzen/modeling-contract-review/issues/new?template=feature-request.yml) |
| Ask a question or share how you used it | [Discussions](https://github.com/CptRizzen/modeling-contract-review/discussions) |
| Fix typos, improve wording, add a checklist item | Send a pull request |

## Ground rules for the community report list

The community report list is the part of this project with real-world consequences for real people and businesses. It is held to a stricter standard than anything else here.

1. **Allegations only, framed as allegations.** Nothing in this repo may state that a named business or person committed fraud, a crime, or any other wrongdoing. Entries describe what was *reported*, not what is *true*.
2. **No new named individuals without a public, linkable source.** Naming a private person carries real legal and personal risk. Agency and company names may be added from firsthand reports; individual people require a public source (news report, court record, agency safety notice, or a public post that is still live).
3. **Firsthand or clearly attributed.** "My friend's cousin heard" is not enough. Say what happened, when, and how you know.
4. **No dollar-amount accusations you cannot support**, no addresses, no phone numbers, no photos, no family members. Never post someone's private information.
5. **Removal requests are honored quickly.** If an entry is disputed and the reporter cannot substantiate it, the entry comes out while it is reviewed. Safety of the list's usefulness depends on it not being a place to settle scores.

Maintainers may decline or remove any entry at their discretion.

## Pull requests

1. Fork the repo and create a branch off `main` (`fix/commission-threshold`, `docs/typo-for-models`).
2. Make the change. Keep the diff focused — one topic per PR.
3. If you changed `skill.md`, test it against a real (or realistic) contract and paste the before/after behavior in the PR description. Redact anything identifying.
4. Update `CHANGELOG.md` under an `## [Unreleased]` heading.
5. Open the PR and fill in the template. CI runs automatically; it checks the `skill.md` frontmatter and looks for broken links.

There is no build step, no dependencies, and no test framework. It is markdown.

## Style

- Plain language. A model reading this on her phone outside an agency office is the target reader, not a lawyer and not a developer.
- Specific over general. "Commission above 25% is a red flag" beats "watch out for high commission."
- Every risk claim should carry what to *do* about it — the redline language, the question to ask, or the walk-away line.
- US law is the default. Label anything jurisdiction-specific.

## Scope

In scope: contract review logic, checklists, benchmarks, redline language, model-facing documentation, the community report list.

Out of scope: giving legal advice to individuals in issues, naming people without a public source, anything that turns the list into a harassment vector.

## Code of Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Reports: shawn.schultz@gmail.com.

## License

Contributions are licensed under the [MIT License](LICENSE), same as the project.
