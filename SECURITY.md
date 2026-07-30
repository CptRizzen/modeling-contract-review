# Security, Privacy, and Content Removal

This project ships no executable code — it is a markdown skill file read by AI assistants. The realistic risks are privacy, prompt content, and defamatory or inaccurate entries in the community report list. All three are covered below.

## Reporting a vulnerability

Email **shawn.schultz@gmail.com** with "SECURITY" in the subject. Please do not open a public issue for a live vulnerability.

Expect an acknowledgement within 3 business days and a resolution or status update within 14 days.

In scope:
- Prompt-injection paths — content in the skill that could cause an assistant to leak a user's contract, ignore its guardrails, or take unintended action
- Instructions in this repo that could cause a user to expose sensitive personal or financial data
- Anything that turns a contract review into a data-exfiltration path

Out of scope: vulnerabilities in Claude, ChatGPT, Cursor, or any other host tool — report those to the vendor.

## Your contract data

This repo never receives your contract. Everything happens between you and whichever AI tool you use.

Before pasting a contract anywhere, know that:
- Your contract text goes to the AI provider you chose and is subject to *their* privacy policy and retention terms.
- Free consumer tiers of some AI tools may use your input for model training. Check the provider's settings before pasting anything sensitive.
- Consider redacting your home address, date of birth, government ID numbers, and bank details — none of them are needed for a contract review.
- Never commit a real contract to this repository. `.gitignore` excludes `contracts/`, `*.pdf`, and `*.docx` as a backstop, not a guarantee.

## Community report list — corrections and removals

The community report list contains **unverified allegations** made by anonymous members of the public. It is not a finding of fact and is not an accusation by this project. Entries may be wrong, out of date, or refer to a different business with a similar name.

**If you are named and believe an entry is inaccurate:**

1. Open a [correction request](https://github.com/CptRizzen/modeling-contract-review/issues/new?template=list-correction.yml), or email **shawn.schultz@gmail.com** with "LIST CORRECTION" in the subject if you would rather not post publicly.
2. Say which entry and why it is inaccurate. You do not need a lawyer, and you do not need to prove a negative.
3. The entry is **suspended from the list while the request is reviewed** — it comes out first, and goes back only if the original report can be substantiated.
4. Expect a response within 5 business days.

Named individuals get priority handling. Any entry naming a private person is removed on request unless it is supported by a public, still-live source.

This process exists so the list stays useful as a safety tool and does not become a way to punish people.
