# Contributing

The OPTBOT engineering standards live in the organization's
[`.github` repository](https://github.com/OPTBOTAI/.github/blob/main/STANDARDS.md).
The short version:

1. **Branch from `main`** (or `develop` where the repo has one): `feat/<topic>`,
   `fix/<topic>`, `docs/<topic>`, `research/<topic>`, `chore/<topic>`.
2. **Commit messages** follow Conventional Commits: `feat(scope): what changed`.
3. **Open a pull request.** Fill in the template, link the issue, keep it small.
4. **Checks must pass** and a code owner must approve before merge.
5. **Squash-merge** into `main`, then delete the branch.

Never commit secrets, customer data or another company's code. Data lives
outside the repo; configs point at it.
