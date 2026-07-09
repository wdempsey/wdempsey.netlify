# Lab evaluation automation

`n8n-quarterly-checkin.json` is an importable n8n workflow that runs the quarterly check-in loop. Import it once UM ITS approves the Slack + n8n setup (n8n → Workflows → Import from File).

## What it does

1. **Kickoff** — 9am on Jan 1 / Apr 1 / Jul 1 / Oct 1: DMs every active lab member the quarterly check-in PDF link and logs a row in a tracking sheet.
2. **Submission watcher** — a new file landing in the *Quarterly Check-Ins* Drive folder marks that person as submitted and DMs Walter a receipt.
3. **Weekly sweep** — Mondays 9am: students outstanding ≥5 days get a friendly Slack reminder; anyone outstanding ≥14 days gets rolled into an escalation DM to Walter.

## One-time setup

1. **Google Sheet** (any name) with two tabs:
   - `Roster`: columns `Name`, `SlackUserId`, `Email`, `Active` (TRUE/FALSE). `Name` should be the student's lastname, lowercase, matching the filename convention.
   - `Tracking`: columns `Name`, `Quarter`, `PingedAt`, `Submitted`, `SubmittedAt`. Leave empty; the workflow fills it.
2. **Drive folder** named *Quarterly Check-Ins*, shared with the lab (edit access).
3. In the imported workflow, replace:
   - `YOUR_TRACKING_SHEET_ID` → the sheet's document ID (3 nodes)
   - `YOUR_DRIVE_FOLDER_ID` → the Drive folder ID (1 node)
   - `WALTER_SLACK_ID` → your Slack member ID (2 nodes; Slack profile → ⋯ → Copy member ID)
4. Attach credentials: Google Sheets OAuth, Google Drive OAuth, Slack (bot token with `chat:write` and `im:write`).
5. Activate the workflow.

## Filename convention

Students upload completed PDFs as `lastname_2026Q3.pdf`. The watcher parses the first token and matches it against `Roster.Name`. Off-convention filenames still trigger a receipt DM but won't auto-match — check the tracking sheet if a name looks stuck.

## Annual reviews

The annual forms are not automated (once a year, and the scheduling conversation is personal). Suggested rhythm: send the form 2 weeks before the review meeting, student returns it 3 days ahead, advisor sections completed during/after the meeting, signed copy filed in the student's Drive folder.

## Forms

Hosted on the site: [PhD annual](https://wdempsey.netlify.app/assets/pdf/annual-review-phd.pdf) · [Postdoc annual](https://wdempsey.netlify.app/assets/pdf/annual-review-postdoc.pdf) · [Quarterly check-in](https://wdempsey.netlify.app/assets/pdf/quarterly-checkin.pdf). To regenerate after edits: `python3 build_forms.py` (in this folder; requires `reportlab`), then copy the PDFs to `assets/pdf/`.
