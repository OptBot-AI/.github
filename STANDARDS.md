# OPTBOT engineering standards

How every OPTBOT repository, account and contribution looks. Short on purpose; follow it exactly. New members start with [ONBOARDING.md](ONBOARDING.md).

## 1. Names

| Thing | Format | Example |
|---|---|---|
| GitHub username | `firstname-lastname-optbot` | `griffin-thompson-optbot` |
| Display name | Real name | Griffin Thompson |
| Profile picture | One of the official OPTBOT robots ([ONBOARDING.md](ONBOARDING.md#2-profile-picture-pick-one-of-the-official-optbot-robots)) | `optbot-avatar-wave` |
| Commit email | Your @optbotai.com address, verified | griffin@optbotai.com |
| Repository | lowercase, hyphens, a noun | `design-system`, `superhead` |
| Branch | `<type>/<short-topic>` with type `feat`, `fix`, `docs`, `chore`, `research` | `feat/kitchen-supply-pack` |
| Commit message | Conventional Commits: `<type>(<scope>): <what changed>` | `fix(loop): keep the holdout out of tuning` |
| Release tag | `vMAJOR.MINOR.PATCH` | `v1.1.0` |
| Files and folders | lowercase, hyphens; Python modules use underscores | `brand-guidelines.md`, `quote_heads.py` |
| Issue and PR titles | Sentence case, no trailing period | Add kitchen-supply starter pack |

The company name is always **OPTBOT**, in capitals. The product is **OPTBOT Core**.

## 2. Every repository has

`README.md` (what it is, how to run it, layout), `LICENSE` (proprietary), `CLAUDE.md` (how Claude should work in it), `CONTRIBUTING.md`, `.github/CODEOWNERS`, a CI workflow, and the PR and issue templates. A topic list on GitHub that includes `optbot`.

## 3. How work flows

1. One issue per piece of work. Branch from `main` (or `develop` where it exists).
2. Small pull requests, one change each. Fill in the template.
3. CI green and one code-owner approval before merge. **Squash-merge**, then delete the branch.
4. `main` is always releasable. Nobody pushes to it directly.

## 4. Security

- 2FA required for every member, with an authenticator app or passkey (not SMS).
- No secrets, tokens, customer data or other companies' code in any repository. Data lives outside the repo; configs point at it.
- Outside collaborators get access to only the repositories they work on.

## 5. Culture: OPTBOT reactions, not emoji

We react with our own robot, everywhere. Every robot is the white frame and black face on a transparent background: no black squares, no other colors.

**Where they live**

| Place | How |
|---|---|
| Slack | Workspace emoji `:optbot-<name>:`, usable as reactions and statuses. Search `:optbot` in the picker. |
| GitHub comments | Saved replies titled `optbot <name>` (**Ctrl + .** in any comment box), or paste the markdown below. |
| GitHub bot | `/optbot <name>`, `/optbot random`, `/optbot list` in any issue or PR comment. The bot also reacts to new issues, PRs, approvals, merges and commits on `main` (`[skip optbot]` to silence). One shared workflow: `.github/workflows/optbot-reactions.yml` in this repository. |
| Docs, decks, READMEs | The files in `assets/` here, or `exports/` in the design-system repository. |

**Reactions** (the 24 with a meaning; use these in reviews and threads)

| | Name | Means | Slack | GitHub markdown |
|---|---|---|---|---|
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-thumbs-up.gif" height="44"> | `thumbs-up` | Approve, looks good | `:optbot-thumbs-up:` | `![thumbs-up](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-thumbs-up.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-ship-it.gif" height="44"> | `ship-it` | Done, merged, shipped | `:optbot-ship-it:` | `![ship-it](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-ship-it.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-party.gif" height="44"> | `party` | Celebrate a win | `:optbot-party:` | `![party](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-party.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-trophy.gif" height="44"> | `trophy` | A result, a milestone | `:optbot-trophy:` | `![trophy](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-trophy.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-chart.gif" height="44"> | `chart` | The numbers are up | `:optbot-chart:` | `![chart](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-chart.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-love.gif" height="44"> | `love` | Love it | `:optbot-love:` | `![love](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-love.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-laugh.gif" height="44"> | `laugh` | That's funny | `:optbot-laugh:` | `![laugh](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-laugh.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-thinking.gif" height="44"> | `thinking` | Thinking about it | `:optbot-thinking:` | `![thinking](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-thinking.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-idea.gif" height="44"> | `idea` | Good idea | `:optbot-idea:` | `![idea](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-idea.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-shrug.gif" height="44"> | `shrug` | Not sure, need data | `:optbot-shrug:` | `![shrug](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-shrug.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-facepalm.gif" height="44"> | `facepalm` | Oops | `:optbot-facepalm:` | `![facepalm](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-facepalm.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-eyes.gif" height="44"> | `eyes` | Looking into it | `:optbot-eyes:` | `![eyes](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-eyes.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-on-it.gif" height="44"> | `on-it` | Working on it | `:optbot-on-it:` | `![on-it](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-on-it.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-bug.gif" height="44"> | `bug` | Something broke | `:optbot-bug:` | `![bug](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-bug.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-waiting.gif" height="44"> | `waiting` | Blocked, waiting | `:optbot-waiting:` | `![waiting](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-waiting.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-coffee.gif" height="44"> | `coffee` | Break | `:optbot-coffee:` | `![coffee](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-coffee.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-wave.gif" height="44"> | `wave` | Hello | `:optbot-wave:` | `![wave](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-wave.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-sleep.gif" height="44"> | `sleep` | Away, offline, brb | `:optbot-sleep:` | `![sleep](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-sleep.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-hockey.gif" height="44"> | `hockey` | CIN, hockey | `:optbot-hockey:` | `![hockey](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-hockey.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-golf.gif" height="44"> | `golf` | Nice shot, great work | `:optbot-golf:` | `![golf](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-golf.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-ping-pong.gif" height="44"> | `ping-pong` | Back and forth, your turn | `:optbot-ping-pong:` | `![ping-pong](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-ping-pong.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-chef.gif" height="44"> | `chef` | Cooking something up | `:optbot-chef:` | `![chef](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-chef.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-basketball.gif" height="44"> | `basketball` | Nailed it | `:optbot-basketball:` | `![basketball](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-basketball.gif)` |
| <img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-gym.gif" height="44"> | `gym` | Putting in the work | `:optbot-gym:` | `![gym](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/reactions/optbot-gym.gif)` |

**The GIF library** (one per profile picture, status robots for Slack, and Max's classics: 87 in all). In Slack: `:optbot-<name>:` (two renamed to avoid clashes: `:optbot-chef-hat:`, `:optbot-ball-spin:`). In markdown: `![name](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-<name>.gif)`.

**Faces**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-classic.gif" width="64" alt="classic"><br><code>classic</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-blink.gif" width="64" alt="blink"><br><code>blink</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-wink.gif" width="64" alt="wink"><br><code>wink</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-happy.gif" width="64" alt="happy"><br><code>happy</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-side-eye.gif" width="64" alt="side-eye"><br><code>side-eye</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-focused.gif" width="64" alt="focused"><br><code>focused</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-shades.gif" width="64" alt="shades"><br><code>shades</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-heart-eyes.gif" width="64" alt="heart-eyes"><br><code>heart-eyes</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-star-eyes.gif" width="64" alt="star-eyes"><br><code>star-eyes</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-dizzy.gif" width="64" alt="dizzy"><br><code>dizzy</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sleepy.gif" width="64" alt="sleepy"><br><code>sleepy</code></td></tr>
</table>

**Headwear**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-cap.gif" width="64" alt="cap"><br><code>cap</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-beanie.gif" width="64" alt="beanie"><br><code>beanie</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-crown.gif" width="64" alt="crown"><br><code>crown</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-top-hat.gif" width="64" alt="top-hat"><br><code>top-hat</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-headphones.gif" width="64" alt="headphones"><br><code>headphones</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-chef.gif" width="64" alt="chef"><br><code>chef</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-party-hat.gif" width="64" alt="party-hat"><br><code>party-hat</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-wizard.gif" width="64" alt="wizard"><br><code>wizard</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-grad.gif" width="64" alt="grad"><br><code>grad</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-halo.gif" width="64" alt="halo"><br><code>halo</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-antenna.gif" width="64" alt="antenna"><br><code>antenna</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-cowboy.gif" width="64" alt="cowboy"><br><code>cowboy</code></td></tr>
</table>

**Sports**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-hockey.gif" width="64" alt="hockey"><br><code>hockey</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-hockey-celly.gif" width="64" alt="hockey-celly"><br><code>hockey-celly</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-golf-swing.gif" width="64" alt="golf-swing"><br><code>golf-swing</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-golf-putt.gif" width="64" alt="golf-putt"><br><code>golf-putt</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-basketball.gif" width="64" alt="basketball"><br><code>basketball</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-soccer.gif" width="64" alt="soccer"><br><code>soccer</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-tennis.gif" width="64" alt="tennis"><br><code>tennis</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-gym.gif" width="64" alt="gym"><br><code>gym</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-skate.gif" width="64" alt="skate"><br><code>skate</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-trophy.gif" width="64" alt="trophy"><br><code>trophy</code></td></tr>
</table>

**Work**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-laptop.gif" width="64" alt="laptop"><br><code>laptop</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-coffee.gif" width="64" alt="coffee"><br><code>coffee</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-chart.gif" width="64" alt="chart"><br><code>chart</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-detective.gif" width="64" alt="detective"><br><code>detective</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-idea.gif" width="64" alt="idea"><br><code>idea</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-launch.gif" width="64" alt="launch"><br><code>launch</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-support.gif" width="64" alt="support"><br><code>support</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-clipboard.gif" width="64" alt="clipboard"><br><code>clipboard</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-briefcase.gif" width="64" alt="briefcase"><br><code>briefcase</code></td></tr>
</table>

**Fun**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-wave.gif" width="64" alt="wave"><br><code>wave</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-thumbs-up.gif" width="64" alt="thumbs-up"><br><code>thumbs-up</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-guitar.gif" width="64" alt="guitar"><br><code>guitar</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-gamer.gif" width="64" alt="gamer"><br><code>gamer</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-zen.gif" width="64" alt="zen"><br><code>zen</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-balloon.gif" width="64" alt="balloon"><br><code>balloon</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-love.gif" width="64" alt="love"><br><code>love</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-music.gif" width="64" alt="music"><br><code>music</code></td></tr>
</table>

**Status**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-meeting.gif" width="64" alt="meeting"><br><code>meeting</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-recharge.gif" width="64" alt="recharge"><br><code>recharge</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-remote.gif" width="64" alt="remote"><br><code>remote</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sick.gif" width="64" alt="sick"><br><code>sick</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-vacation.gif" width="64" alt="vacation"><br><code>vacation</code></td></tr>
</table>

**Classics**

<table>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-look.gif" width="64" alt="look"><br><code>look</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-cursor.gif" width="64" alt="cursor"><br><code>cursor</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-no.gif" width="64" alt="no"><br><code>no</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-yes.gif" width="64" alt="yes"><br><code>yes</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-boot.gif" width="64" alt="boot"><br><code>boot</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-scan.gif" width="64" alt="scan"><br><code>scan</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-glitch.gif" width="64" alt="glitch"><br><code>glitch</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sad.gif" width="64" alt="sad"><br><code>sad</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-angry.gif" width="64" alt="angry"><br><code>angry</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-excited.gif" width="64" alt="excited"><br><code>excited</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-loading.gif" width="64" alt="loading"><br><code>loading</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-walk.gif" width="64" alt="walk"><br><code>walk</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sit.gif" width="64" alt="sit"><br><code>sit</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sit-down.gif" width="64" alt="sit-down"><br><code>sit-down</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-hop.gif" width="64" alt="hop"><br><code>hop</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-jump.gif" width="64" alt="jump"><br><code>jump</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-dance.gif" width="64" alt="dance"><br><code>dance</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-forecast.gif" width="64" alt="forecast"><br><code>forecast</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-point.gif" width="64" alt="point"><br><code>point</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-peek.gif" width="64" alt="peek"><br><code>peek</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-turn.gif" width="64" alt="turn"><br><code>turn</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-look-back.gif" width="64" alt="look-back"><br><code>look-back</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-chase.gif" width="64" alt="chase"><br><code>chase</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-throw.gif" width="64" alt="throw"><br><code>throw</code></td></tr>
<tr><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-flip.gif" width="64" alt="flip"><br><code>flip</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-shoot.gif" width="64" alt="shoot"><br><code>shoot</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-trip.gif" width="64" alt="trip"><br><code>trip</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-cry.gif" width="64" alt="cry"><br><code>cry</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-surprised.gif" width="64" alt="surprised"><br><code>surprised</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-success.gif" width="64" alt="success"><br><code>success</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-read.gif" width="64" alt="read"><br><code>read</code></td><td align="center"><img src="https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/gifs/optbot-sort.gif" width="64" alt="sort"><br><code>sort</code></td></tr>
</table>

**Slack statuses:** see [ONBOARDING.md](ONBOARDING.md#5-slack-status).

Brand rules for everything else: the `design-system` repository.
