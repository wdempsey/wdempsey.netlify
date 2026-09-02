#!/usr/bin/env python3
"""Build fillable PDF evaluation forms for the Dempsey Lab."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

BLUE = HexColor("#00274C")   # UM blue
MAIZE = HexColor("#FFCB05")  # UM maize
GRAY = HexColor("#555555")
LIGHT = HexColor("#F4F6F8")
BORDER = HexColor("#9AA5B1")
W, H = letter
ML, MR, MT, MB = 50, 50, 50, 56
USABLE = W - ML - MR


class FormDoc:
    def __init__(self, path, title, subtitle, intro):
        self.c = canvas.Canvas(path, pagesize=letter)
        self.c.setTitle(title)
        self.c.setAuthor("Dempsey Lab, University of Michigan")
        self.title, self.subtitle = title, subtitle
        self.page = 0
        self.fid = 0
        self._first_page(intro)

    # ---------- pages ----------
    def _first_page(self, intro):
        self.page = 1
        c = self.c
        c.setFillColor(BLUE)
        c.rect(0, H - 88, W, 88, stroke=0, fill=1)
        c.setFillColor(MAIZE)
        c.rect(0, H - 92, W, 4, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(ML, H - 46, self.title)
        c.setFont("Helvetica", 11)
        c.drawString(ML, H - 66, self.subtitle)
        self.y = H - 112
        if intro:
            self.para(intro, size=9, color=GRAY, italic=True)
            self.y -= 4

    def new_page(self):
        c = self.c
        c.showPage()
        self.page += 1
        c.setFillColor(BLUE)
        c.rect(0, H - 30, W, 30, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica", 8)
        c.drawString(ML, H - 20, f"{self.title} — Dempsey Lab · University of Michigan")
        c.drawRightString(W - MR, H - 20, f"Page {self.page}")
        self.y = H - 52

    def ensure(self, h):
        if self.y - h < MB:
            self.new_page()

    def name(self, base):
        self.fid += 1
        return f"{base}_{self.fid}"

    # ---------- text ----------
    def para(self, text, size=9, color=black, bold=False, italic=False, gap=4):
        font = "Helvetica"
        if bold and italic:
            font = "Helvetica-BoldOblique"
        elif bold:
            font = "Helvetica-Bold"
        elif italic:
            font = "Helvetica-Oblique"
        lines = simpleSplit(text, font, size, USABLE)
        self.ensure(len(lines) * (size + 2) + gap)
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        for ln in lines:
            self.c.drawString(ML, self.y - size, ln)
            self.y -= size + 2
        self.y -= gap
        self.c.setFillColor(black)

    def section(self, text):
        self.ensure(46)
        self.y -= 6
        self.c.setFillColor(BLUE)
        self.c.rect(ML, self.y - 18, USABLE, 18, stroke=0, fill=1)
        self.c.setFillColor(MAIZE)
        self.c.rect(ML, self.y - 18, 4, 18, stroke=0, fill=1)
        self.c.setFillColor(white)
        self.c.setFont("Helvetica-Bold", 10.5)
        self.c.drawString(ML + 10, self.y - 13, text)
        self.c.setFillColor(black)
        self.y -= 26

    # ---------- fields ----------
    def box(self, label, height=70, hint=None):
        """Label + multiline text field."""
        lines = simpleSplit(label, "Helvetica-Bold", 9, USABLE)
        need = len(lines) * 11 + (11 if hint else 0) + height + 12
        self.ensure(need)
        self.c.setFont("Helvetica-Bold", 9)
        for ln in lines:
            self.c.drawString(ML, self.y - 9, ln)
            self.y -= 11
        if hint:
            self.c.setFont("Helvetica-Oblique", 8)
            self.c.setFillColor(GRAY)
            self.c.drawString(ML, self.y - 8, hint)
            self.c.setFillColor(black)
            self.y -= 11
        self.y -= 2
        self.c.acroForm.textfield(
            name=self.name("f"), tooltip=label[:100],
            x=ML, y=self.y - height, width=USABLE, height=height,
            borderColor=BORDER, fillColor=LIGHT, textColor=black,
            fontName="Helvetica", fontSize=9, borderWidth=0.75,
            fieldFlags="multiline", maxlen=0, forceBorder=True)
        self.y -= height + 10

    def line(self, label, width=None, label_w=None):
        """Inline label + single-line field."""
        self.ensure(26)
        self.c.setFont("Helvetica-Bold", 9)
        lw = label_w or (self.c.stringWidth(label, "Helvetica-Bold", 9) + 8)
        self.c.drawString(ML, self.y - 12, label)
        fw = width or (USABLE - lw)
        self.c.acroForm.textfield(
            name=self.name("f"), tooltip=label[:100],
            x=ML + lw, y=self.y - 16, width=fw, height=16,
            borderColor=BORDER, fillColor=LIGHT, textColor=black,
            fontName="Helvetica", fontSize=9, borderWidth=0.75,
            maxlen=0,
            forceBorder=True)
        self.y -= 24

    def two_lines(self, l1, l2, split=0.5):
        """Two label+field pairs on one row."""
        self.ensure(26)
        col1 = USABLE * split
        self.c.setFont("Helvetica-Bold", 9)
        w1 = self.c.stringWidth(l1, "Helvetica-Bold", 9) + 8
        self.c.drawString(ML, self.y - 12, l1)
        self.c.acroForm.textfield(
            name=self.name("f"), tooltip=l1[:100],
            x=ML + w1, y=self.y - 16, width=col1 - w1 - 12, height=16,
            borderColor=BORDER, fillColor=LIGHT, textColor=black,
            fontName="Helvetica", fontSize=9, borderWidth=0.75,
            maxlen=0, forceBorder=True)
        x2 = ML + col1
        w2 = self.c.stringWidth(l2, "Helvetica-Bold", 9) + 8
        self.c.drawString(x2, self.y - 12, l2)
        self.c.acroForm.textfield(
            name=self.name("f"), tooltip=l2[:100],
            x=x2 + w2, y=self.y - 16, width=USABLE - col1 - w2, height=16,
            borderColor=BORDER, fillColor=LIGHT, textColor=black,
            fontName="Helvetica", fontSize=9, borderWidth=0.75,
            maxlen=0, forceBorder=True)
        self.y -= 24

    def checks(self, label, options, note=None):
        """Label followed by a row (or wrapped rows) of checkboxes."""
        self.ensure(30)
        x = ML
        if label:
            self.c.setFont("Helvetica-Bold", 9)
            self.c.drawString(ML, self.y - 12, label)
            x = ML + self.c.stringWidth(label, "Helvetica-Bold", 9) + 12
        self.c.setFont("Helvetica", 9)
        for opt in options:
            ow = 14 + self.c.stringWidth(opt, "Helvetica", 9) + 16
            if x + ow > W - MR:
                self.y -= 18
                self.ensure(20)
                x = ML + 16
            self.c.acroForm.checkbox(
                name=self.name("cb"), tooltip=opt,
                x=x, y=self.y - 14, size=11, buttonStyle="check",
                borderColor=BORDER, fillColor=white, borderWidth=1)
            self.c.setFont("Helvetica", 9)
            self.c.drawString(x + 15, self.y - 12, opt)
            x += ow
        self.y -= 20
        if note:
            self.para(note, size=8, color=GRAY, italic=True, gap=2)

    def rating_row(self, label, options=("Ahead", "On track", "Needs focus")):
        """Compact rubric row: label left, checkboxes right-aligned columns."""
        self.ensure(20)
        self.c.setFont("Helvetica", 9)
        self.c.drawString(ML + 4, self.y - 12, label)
        x = W - MR - 260
        for opt in options:
            self.c.acroForm.checkbox(
                name=self.name("cb"), tooltip=f"{label}: {opt}",
                x=x, y=self.y - 14, size=11, buttonStyle="check",
                borderColor=BORDER, fillColor=white, borderWidth=1)
            x += 88
        self.c.setStrokeColor(HexColor("#DDDDDD"))
        self.c.setLineWidth(0.5)
        self.c.line(ML, self.y - 17, W - MR, self.y - 17)
        self.y -= 20

    def rating_header(self, options=("Ahead", "On track", "Needs focus")):
        self.ensure(16)
        self.c.setFont("Helvetica-Bold", 8)
        x = W - MR - 260
        for opt in options:
            self.c.drawString(x - 2, self.y - 10, opt)
            x += 88
        self.y -= 14

    def signatures(self, roles=("Student", "Advisor")):
        self.ensure(60)
        self.y -= 8
        col = USABLE / 2
        for i, role in enumerate(roles):
            x = ML + i * col
            self.c.setStrokeColor(black)
            self.c.setLineWidth(0.75)
            self.c.line(x, self.y - 26, x + col - 40, self.y - 26)
            self.c.setFont("Helvetica", 8)
            self.c.drawString(x, self.y - 37, f"{role} signature")
            self.c.drawString(x, self.y - 48, "Date:")
            self.c.acroForm.textfield(
                name=self.name("date"), tooltip=f"{role} date",
                x=x + 30, y=self.y - 52, width=100, height=14,
                borderColor=BORDER, fillColor=LIGHT, textColor=black,
                fontName="Helvetica", fontSize=9, borderWidth=0.75,
                maxlen=0, forceBorder=True)
        self.y -= 60

    def save(self):
        self.c.save()


# =====================================================================
# 1. ANNUAL REVIEW — PhD STUDENT
# =====================================================================
d = FormDoc(
    "annual-review-phd.pdf",
    "Annual Review — PhD Student",
    "Dempsey Lab · University of Michigan",
    "Complete Parts 1–6 before our review meeting; Part 7 is finalized together during the "
    "meeting. Throughout, focus on what was learned, not what was worked on. Companion reading: "
    "the Lab Expectations page (DRI rubric).")

d.two_lines("Name:", "Year in program:", split=0.62)
d.two_lines("Program:", "Review period:", split=0.5)
d.two_lines("Advisor:  Walter Dempsey", "Date of review:", split=0.5)

d.section("Part 1 · Last Year's Goals — Accountability Loop")
d.para("Copy each goal from last year's review and record its outcome. First-year students: skip to Part 2.", size=8.5, color=GRAY, italic=True)
for i in range(1, 4):
    d.line(f"Goal {i}:")
    d.checks("Outcome:", ["Achieved", "Partially achieved", "Dropped / pivoted"])
d.box("If a goal was dropped or pivoted, what did we learn from that decision?",
      height=44, hint="Pivots are expected — research is a stochastic decision process. What matters is what the pivot taught us.")

d.section("Part 2 · Milestones & Thesis Progress")
d.checks("Completed to date:", ["Coursework", "Qualifying exams", "Candidacy / prelim", "Thesis proposal", "Defense scheduled"])
d.two_lines("Next milestone:", "Target date:", split=0.62)
d.box("Research progress this year: key results, theoretical developments, methods built, data applications.",
      height=110, hint="State findings, not activity: “the estimator is biased under informative cluster size” beats “ran simulations.”")
d.box("Publications, preprints & software (R/Python packages), with status: in preparation / submitted / accepted.",
      height=70)

d.section("Part 3 · DRI Self-Assessment")
d.para("Rate yourself relative to expectations for your year in program, per the Lab Expectations rubric. We will compare notes at the meeting.", size=8.5, color=GRAY, italic=True)
DRI_ROWS = [
    "Thoughtful implementation — 45%",
    "Troubleshooting & autonomy — 25%",
    "Tactical direction — 10%",
    "Strategic vision — 10%",
    "Clear communication — 5%",
    "Lab citizenship — 5%",
]
d.rating_header()
for row in DRI_ROWS:
    d.rating_row(row)
d.box("Where are you in the DRI handoff, and what is the next capability you want to own?", height=52)

d.section("Part 4 · Research Assistant Performance (if RA-funded this period)")
d.box("Main technical contributions to the lab or grant project.",
      height=56, hint="e.g., data pipeline curation, large-scale simulation studies, statistical modeling, package development.")
d.box("Collaboration & deliverables: deadlines, code sharing via GitHub, work with co-investigators or domain experts.",
      height=56)

d.section("Part 5 · GSI / Teaching Performance (if applicable)")
d.box("Instructional duties: lab sections, office hours, grading, designing problems.", height=48)
d.box("Pedagogical reflection: what went well, what to improve, summary of student feedback if available.", height=56)

d.section("Part 6 · Professional Development, Service & Career")
d.box("Dissemination: posters, department seminars, conference talks (JSM, ENAR, NeurIPS, ICML, ...).", height=44)
d.box("Service & community: departmental service, peer review, mentorship of undergrads or newer students.", height=44)
d.checks("Career direction:", ["Academia (research)", "Academia (teaching)", "Industry", "Government / nonprofit", "Undecided"])
d.line("One skill to develop next year for that path:")
d.box("What do you need from me or the lab?",
      height=52, hint="Meeting cadence, funding clarity, introductions, compute, faster feedback, co-author connections — be specific.")

d.section("Part 7 · Goals for the Coming Year (finalized together at the meeting)")
d.para("Good goals name a deliverable and a date. “Make progress on Chapter 2” is not a goal; “submit the Chapter 2 paper to ENAR by January 15” is.", size=8.5, color=GRAY, italic=True)
for i in range(1, 4):
    d.line(f"Goal {i}:")
    d.two_lines("Deliverable:", "Target date:", split=0.68)
d.line("Funding & appointment plan for next year:")
d.line("Target graduation timeline:")

d.section("Advisor Assessment")
d.checks("Progress vs. timeline:", ["Ahead", "On track", "Needs improvement — plan below"],
         note="Judged against the milestone timeline for the student's year in program, not against expectations in the abstract.")
d.para("Expectations, per DRI rubric (weights from the Lab Expectations page). Compare with the student's Part 3 self-assessment at the meeting.", size=8.5, color=GRAY, italic=True)
d.rating_header(("Exceeds", "Meets", "Needs focus"))
for row in DRI_ROWS:
    d.rating_row(row, ("Exceeds", "Meets", "Needs focus"))
d.checks("RA performance:", ["Exceeds", "Meets", "Needs improvement", "N/A"])
d.checks("GSI performance:", ["Exceeds", "Meets", "Needs improvement", "N/A"])
d.box("Strengths observed this year.", height=52)
d.box("Growth areas and, if needed, the specific improvement plan with checkpoints.", height=64)
d.signatures()
d.save()

# =====================================================================
# 2. ANNUAL REVIEW — POSTDOC
# =====================================================================
d = FormDoc(
    "annual-review-postdoc.pdf",
    "Annual Review — Postdoctoral Fellow",
    "Dempsey Lab · University of Michigan",
    "Complete Parts 1–6 before our review meeting; Part 7 is finalized together. The organizing "
    "question of a postdoc review is trajectory toward independence: your own research line, your "
    "own funding, your own students. Focus on what was learned, not what was worked on.")

d.two_lines("Name:", "Postdoc start date:", split=0.6)
d.two_lines("Review period:", "Funding source:", split=0.5)
d.two_lines("Mentor:  Walter Dempsey", "Date of review:", split=0.5)

d.section("Part 1 · Last Year's Goals — Accountability Loop")
d.para("Copy each goal from last year's review and record its outcome. First-year postdocs: skip to Part 2.", size=8.5, color=GRAY, italic=True)
for i in range(1, 4):
    d.line(f"Goal {i}:")
    d.checks("Outcome:", ["Achieved", "Partially achieved", "Dropped / pivoted"])

d.section("Part 2 · Research Program & Independence")
d.box("Research progress this year: key results, methods developed, applications.",
      height=100, hint="State findings, not activity.")
d.box("Your independent research line: what direction is distinctly yours, beyond ongoing lab projects? How did it advance this year?",
      height=70)
d.box("Publications, preprints & software, with status and your role (lead / senior / contributing).",
      height=70)

d.section("Part 3 · Funding & Fellowships")
d.box("Applications submitted or planned (K99/R00, F32, foundation awards, internal pilots), with status and dates.",
      height=56)
d.box("Contributions to lab grant writing (aims pages, preliminary data, budgets).", height=44)

d.section("Part 4 · Mentoring & Lab Leadership")
d.box("Students mentored and projects overseen; what did your mentees accomplish?",
      height=56, hint="Mentoring track record matters for faculty applications — be concrete.")
d.box("Contributions to lab infrastructure, onboarding, or shared resources.", height=40)

d.section("Part 5 · Career & Job Market")
d.checks("Target track:", ["Tenure-track (research)", "Teaching-focused", "Industry research", "Government / nonprofit", "Undecided"])
d.two_lines("Planned market cycle (e.g., Fall 2027):", "Applications target:", split=0.6)
d.checks("Materials status:", ["Research statement", "Teaching statement", "Job talk", "CV current", "References lined up"],
         note="Check items that are drafted or better.")
d.box("Visibility this year: invited talks, conference presentations, networking, reviewing/editorial work.", height=48)

d.section("Part 6 · Support Needed")
d.box("What do you need from me?",
      height=52, hint="Introductions, letter timelines, practice-talk audiences, protected time for your own line, grant mentorship.")

d.section("Part 7 · Goals for the Coming Year (finalized together at the meeting)")
for i in range(1, 4):
    d.line(f"Goal {i}:")
    d.two_lines("Deliverable:", "Target date:", split=0.68)
d.line("Appointment / renewal plan:")

d.section("Mentor Assessment")
d.checks("Progress vs. timeline:", ["Ahead", "On track", "Needs improvement — plan below"])
d.checks("Independence trajectory:", ["Ahead of schedule", "On schedule", "Needs acceleration"])
d.box("Strengths observed this year.", height=52)
d.box("Growth areas and agreed actions (with checkpoints).", height=64)
d.signatures(("Postdoc", "Mentor"))
d.save()

# =====================================================================
# 3. QUARTERLY CHECK-IN
# =====================================================================
d = FormDoc(
    "quarterly-checkin.pdf",
    "Quarterly Check-In",
    "Dempsey Lab · University of Michigan",
    "Ten minutes, tops — if it takes longer, you are writing too much. This references the goals "
    "we set at your annual review; we discuss it at our next 1:1. Focus on what was learned.")

d.two_lines("Name:", "Quarter (e.g., 2026 Q3):", split=0.55)
d.line("Date submitted:", width=140)

d.section("1 · Status Against Annual Goals")
d.checks("Overall:", ["On track", "At risk", "Blocked"],
         note="Same traffic light as the weekly updates. “At risk” or “Blocked” is information, not failure — flag it early.")
d.line("If at risk or blocked — which goal, and why:")

d.section("2 · Since Last Check-In")
d.box("What was learned or accomplished? Three bullets max.", height=64)

d.section("3 · Next Quarter")
d.box("Top priority: the step that attacks your biggest remaining uncertainty.", height=44)

d.section("4 · Blockers & Risks")
d.box("Anything slowing you down or worrying you — technical, logistical, or otherwise.", height=44)

d.section("5 · Reflection")
d.box("One thing going well; one thing you want to improve.", height=44)

d.section("6 · What Do You Need From Me?")
d.box("Be specific: a decision, an introduction, feedback on a draft, more or less meeting time.", height=44)

d.section("Discussion Notes (completed together at the 1:1)")
d.box("Agreed adjustments to goals, priorities, or support.", height=56)
d.save()

print("done")
