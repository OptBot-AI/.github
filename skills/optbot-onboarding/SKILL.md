---
name: optbot-onboarding
description: Use when someone says "onboard me to OPTBOT" or "onboard Jane Doe", or a new OPTBOT teammate needs GitHub, Slack, profile picture, reactions or Claude set up the OPTBOT way.
---

# OPTBOT onboarding

Gets a person to the OPTBOT standard in one sitting: the account name, an official robot picture, security, the OPTBOT reactions at their fingertips in GitHub and Slack, an OPTBOT status, and the Claude skills. The source of truth is `OptBot-AI/.github`: `ONBOARDING.md` and `STANDARDS.md`. Read them first; if they disagree with this file, they win.

Assets (public, no sign-in needed):
- Pictures: `https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/avatars/optbot-avatar-<name>.png` (list: `assets/avatars/index.json`)
- Reactions: `.../assets/reactions/optbot-<name>.gif` (24); GIF library: `.../assets/gifs/optbot-<name>.gif` (list: `assets/gifs/index.json`)

Identity rule: the robot is always white frame, black face, white eyes, on a transparent background (never a black square). No orange or any other color. The CEO edition is reserved for the CEO: never offer it to anyone else.

## Two modes

- **"Onboard me"**: the person is setting up their own accounts. Work in their browser (Claude in Chrome, already signed in as them).
- **"Onboard <name>"** said by an OPTBOT owner: do the owner-side steps (invites) from the owner's browser, then hand the person the message in step 8 so they (or their own Claude) do the rest.

Ask only what you can't find: the person's full name, role, @optbotai.com email, GitHub username, and whether they join the org as a member or as an outside collaborator (outside collaborators get repository access only, for example Max). Then go. Changing account settings, sending invites and uploading pictures change things on the person's accounts: say what you will change, and do it once they agree. They enter passwords and 2FA codes themselves.

## Steps

1. **GitHub profile** (github.com/settings/profile and /settings/admin): username `firstname-lastname-optbot`, name = real name, bio = role at OPTBOT, company `@OptBot-AI`, URL `https://www.optbotai.com`.
2. **Profile picture.** Show the 50 pictures by category (Faces, Headwear, Sports, Work, Fun) from `index.json`, or send them to the picker in `ONBOARDING.md#2`. Let them pick a name, or "surprise me" (pick one at random and show it). Download the PNG into the workspace, then on github.com/settings/profile find the hidden "Upload a photo" file input, upload the file to it, and click "Set new profile picture". Offer the same file for Slack (Profile → Edit → Upload image) and Google.
3. **Security:** check Settings → Password and authentication. If 2FA uses SMS only, tell them to add an authenticator app or passkey (they do it). Verify the @optbotai.com email and make it primary.
4. **GitHub saved replies** (github.com/settings/replies): the standard set is 66, titled `optbot <name>` so `Ctrl + .` then typing the name finds them: the 24 reactions (`assets/reactions/`) and the 42 non-classic GIFs (`assets/gifs/index.json`, every category except Classics; the two GIF names that clash are titled `optbot chef-hat` and `optbot ball-spin`). Body: `![<name>](https://raw.githubusercontent.com/OptBot-AI/.github/main/assets/<reactions|gifs>/optbot-<file>.gif)`. Skip titles that already exist. Quickest: on the replies page, post the page's own "Add a saved reply" form once per reply (copy the form's fields, set `title` and `body`). Typing into the fields drops characters; if you must type, set values with form_input, then click the field and press End, space, Backspace. Finish by counting the `optbot` titles on the page.
5. **Slack:** the `:optbot-<name>:` emoji are workspace-wide, so nothing to install. Show them how to react (hover a message → add reaction → type `optbot`) and set an OPTBOT status. The workspace's suggested statuses already use OPTBOT robots (In a meeting, Recharging, Heads down, On vacation, Out sick); the full list, with Lunch `:optbot-chef:`, Working remotely `:optbot-remote:`, Out of office `:optbot-golf:` and more, is in `ONBOARDING.md#5`. Typing `:optbot` in any emoji picker shows every robot; shortcuts like `:optbot-lgtm:`, `:optbot-brb:`, `:optbot-wfh:`, `:optbot-ooo:` and `:optbot-gg:` work too.
6. **Claude:** install the `optbot-design` skill (design-system repository, `skills/optbot-design`) and this skill (`OptBot-AI/.github`, `skills/optbot-onboarding`).
7. **Owner-side, only in "onboard <name>" mode:** invite them at github.com/orgs/OptBot-AI/people (member) or add them as an outside collaborator on the repositories they work on, and invite them to the Slack workspace with their @optbotai.com email.
8. **Wrap up** with this checklist, ticked:
   - [ ] Username `firstname-lastname-optbot`, real name, bio, company
   - [ ] Official OPTBOT picture on GitHub, Slack, Google
   - [ ] 2FA with an app or passkey, @optbotai.com email verified
   - [ ] 66 `optbot` saved replies (try: Ctrl + . in any comment box)
   - [ ] Reacted once in Slack with `:optbot-thumbs-up:`, OPTBOT status set
   - [ ] Commented `/optbot random` on an issue in an OPTBOT repository
   - [ ] Claude skills installed; read `STANDARDS.md`

Never put the robot on orange, never draw a new robot by hand, and never use stock emoji where an OPTBOT reaction fits.
