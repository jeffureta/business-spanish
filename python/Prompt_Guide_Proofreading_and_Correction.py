from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "Prompt_Guide_Proofreading_and_Correction.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor("#1A365D")   # Deep navy
secondary_color = colors.HexColor("#2B6CB0") # Slate blue
accent_bg = colors.HexColor("#F7FAFC")       # Light grey/blue
border_color = colors.HexColor("#CBD5E0")    # Border grey
dark_text = colors.HexColor("#2D3748")       # Body text

# Typography Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=primary_color,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=secondary_color,
    spaceAfter=15
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=primary_color,
    spaceBefore=12,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'BodyDark',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13.5,
    textColor=dark_text,
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    'BulletText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=dark_text,
    leftIndent=12,
    spaceAfter=4
)

prompt_box_style = ParagraphStyle(
    'PromptCode',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor("#1A202C")
)

label_bold = ParagraphStyle(
    'LabelBold',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13.5,
    textColor=primary_color
)

story = []

# Title & Header
story.append(Paragraph("PROMPT GUIDE: TEXT PROOFREADING & CORRECTION", title_style))
story.append(Paragraph("Standard Operating Prompt for Grammar, Punctuation, Accents, and Spelling Verification", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceBefore=0, spaceAfter=12))

# Overview
overview_text = (
    "This prompt guide defines an automated, high-precision review workflow for proofreading text. "
    "It enforces systematic correction across three linguistic pillars and mandates direct output of the "
    "final corrected text without conversational filler, explanations, or meta-announcements."
)
story.append(Paragraph(overview_text, body_style))
story.append(Spacer(1, 8))

# Master Prompt Box
story.append(Paragraph("1. Master Prompt Template", section_heading))

prompt_content = (
    "<b>[COPY & PASTE PROMPT]</b><br/><br/>"
    "You are an expert proofreader and editor. Review the submitted text and correct all errors following these rules strictly:<br/><br/>"
    "<b>1. Grammar:</b> Fix syntactic inconsistencies, verb agreement errors, pronoun mismatches, and incorrect clause structures.<br/>"
    "<b>2. Punctuation & Accents:</b> Correct missing, mismatched, or misplaced punctuation marks (including paired quotation marks, question marks [¿ ?], exclamation points [¡ !], commas, and em dashes). Restore all missing acute accents (tildes), umlauts, and diacritics.<br/>"
    "<b>3. Spelling:</b> Fix all typographical errors, misspellings, unneeded capitalizations, accidental word duplications, and non-target foreign language slips.<br/><br/>"
    "<b>OUTPUT ENFORCEMENT:</b><br/>"
    "Once checked, output ONLY the final corrected text. Do NOT include greetings, intro phrases, bulleted changelogs, or explanations. Start immediately with the first line of the corrected text."
)

prompt_table = Table(
    [[Paragraph(prompt_content, prompt_box_style)]],
    colWidths=[532]
)
prompt_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), accent_bg),
    ('BOX', (0, 0), (-1, -1), 1, secondary_color),
    ('PADDING', (0, 0), (-1, -1), 10),
]))
story.append(prompt_table)
story.append(Spacer(1, 10))

# 3-Point Check Matrix Table
story.append(Paragraph("2. Verification Checklist & Scope Matrix", section_heading))

matrix_data = [
    [
        Paragraph("<b>Check Category</b>", label_bold),
        Paragraph("<b>Verification Scope</b>", label_bold),
        Paragraph("<b>Common Target Issues</b>", label_bold)
    ],
    [
        Paragraph("<b>1. Grammatical Errors</b>", body_style),
        Paragraph("Subject-verb agreement, tense cohesion, gender/number concordance, and prepositions.", body_style),
        Paragraph("Mismatched plural verbs, wrong auxiliary combinations, broken comparative structures.", bullet_style)
    ],
    [
        Paragraph("<b>2. Punctuation & Accents</b>", body_style),
        Paragraph("Bilateral punctuation marks, accentuation rules (agudas, graves, esdrújulas), and quote symmetry.", body_style),
        Paragraph("Missing inverted marks (¿, ¡), omitted tildes on verbs/pronouns, unclosed speech quotes.", bullet_style)
    ],
    [
        Paragraph("<b>3. Spelling Errors</b>", body_style),
        Paragraph("Lexical accuracy, typo remediation, character transposition, and untranslated slips.", body_style),
        Paragraph("OCR artifacts, repeated characters, misspellings, phonetic confusions (b/v, c/s/z).", bullet_style)
    ],
    [
        Paragraph("<b>Output Directive</b>", label_bold),
        Paragraph("Zero explanation policy: Return raw corrected content immediately.", body_style),
        Paragraph("Suppression of introductory greetings, summary tables, and analytical notes.", bullet_style)
    ]
]

matrix_table = Table(matrix_data, colWidths=[120, 210, 202])
matrix_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E2E8F0")),
    ('BOX', (0, 0), (-1, -1), 0.5, border_color),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, border_color),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(matrix_table)
story.append(Spacer(1, 10))

# Best Practice & Deployment Rules
story.append(Paragraph("3. Execution Best Practices", section_heading))
story.append(Paragraph("• <b>Temperature Setting:</b> Set LLM temperature to 0.0 or 0.1 to eliminate hallucinations and preserve source fidelity.", bullet_style))
story.append(Paragraph("• <b>Formatting Preservation:</b> The prompt explicitly retains line breaks, speaker headers, markdown syntax, and indentation.", bullet_style))
story.append(Paragraph("• <b>Strict Minimal Output:</b> For automated pipelines, the output directive guarantees pure text payload suitable for direct piping or file generation.", bullet_style))

doc.build(story)
print("PDF generated successfully:", pdf_path)