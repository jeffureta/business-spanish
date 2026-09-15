import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

pdf_path = "Business_Spanish_Training_Module_PRD.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=46,
    rightMargin=46,
    topMargin=48,
    bottomMargin=48,
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor("#0969da")
dark_neutral = colors.HexColor("#24292f")
light_bg = colors.HexColor("#f6f8fa")
border_color = colors.HexColor("#d0d7de")

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=22,
    textColor=colors.HexColor("#1f2328"),
    spaceAfter=3,
)

subtitle_style = ParagraphStyle(
    "DocSubtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor("#57606a"),
    spaceAfter=8,
)

h1_style = ParagraphStyle(
    "SectionH1",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=11.5,
    leading=15,
    textColor=primary_color,
    spaceBefore=9,
    spaceAfter=4,
    keepWithNext=True,
)

h2_style = ParagraphStyle(
    "SectionH2",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=9.5,
    leading=13,
    textColor=dark_neutral,
    spaceBefore=6,
    spaceAfter=2,
    keepWithNext=True,
)

body_style = ParagraphStyle(
    "BodyTextCustom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=dark_neutral,
    spaceAfter=4,
)

bullet_style = ParagraphStyle(
    "BulletCustom",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=dark_neutral,
    leftIndent=10,
    firstLineIndent=-7,
    spaceAfter=2.5,
)

table_header_style = ParagraphStyle(
    "TH",
    fontName="Helvetica-Bold",
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor("#24292f"),
)
table_cell_style = ParagraphStyle(
    "TD",
    fontName="Helvetica",
    fontSize=7.5,
    leading=10,
    textColor=dark_neutral,
)
table_cell_code = ParagraphStyle(
    "TDCode",
    fontName="Courier",
    fontSize=7,
    leading=9,
    textColor=colors.HexColor("#0969da"),
)


class NumberedCanvas(canvas.Canvas):

  def __init__(self, *args, **kwargs):
    super(NumberedCanvas, self).__init__(*args, **kwargs)
    self._saved_page_states = []

  def showPage(self):
    self._saved_page_states.append(dict(self.__dict__))
    self._startPage()

  def save(self):
    num_pages = len(self._saved_page_states)
    for state in self._saved_page_states:
      self.__dict__.update(state)
      self.draw_page_decorations(num_pages)
      canvas.Canvas.showPage(self)
    canvas.Canvas.save(self)

  def draw_page_decorations(self, page_count):
    self.saveState()
    self.setFont("Helvetica", 7.5)
    self.setFillColor(colors.HexColor("#57606a"))

    if self._pageNumber > 1:
      self.drawString(
          46,
          755,
          "Product Requirements Document (PRD) — Interactive Business Spanish"
          " Module",
      )
      self.drawRightString(566, 755, "v1.0 | Core Specification")
      self.setStrokeColor(colors.HexColor("#d0d7de"))
      self.setLineWidth(0.5)
      self.line(46, 748, 566, 748)

    text = f"Page {self._pageNumber} of {page_count}"
    self.drawRightString(566, 30, text)
    self.drawString(
        46,
        30,
        "BUSINESS SPANISH LEARNING REPOSITORY — LOCAL CLIENT SPECIFICATION",
    )
    self.setStrokeColor(colors.HexColor("#d0d7de"))
    self.setLineWidth(0.5)
    self.line(46, 38, 566, 38)
    self.restoreState()


story = []

# Header & Metadata
story.append(Paragraph("Product Requirements Document (PRD)", title_style))
story.append(
    Paragraph(
        "Interactive Business Spanish Telephony Training Module",
        subtitle_style,
    )
)
story.append(
    HRFlowable(
        width="100%",
        thickness=1,
        color=primary_color,
        spaceBefore=0,
        spaceAfter=6,
    )
)

meta_data = [
    [
        Paragraph("<b>Document Version:</b> 1.0", table_cell_style),
        Paragraph(
            "<b>Target Environment:</b> Google Chrome (macOS / Local)",
            table_cell_style,
        ),
    ],
    [
        Paragraph(
            "<b>Product Area:</b> Business Spanish Telephony", table_cell_style
        ),
        Paragraph(
            "<b>Audio Engine:</b> Microsoft Edge TTS (Python edge-tts)",
            table_cell_style,
        ),
    ],
    [
        Paragraph(
            "<b>Document Status:</b> Approved Specification", table_cell_style
        ),
        Paragraph(
            "<b>Reference Source:</b> Scene 1 (Summit Fleet vs. Cascade)",
            table_cell_style,
        ),
    ],
]
t_meta = Table(meta_data, colWidths=[260, 260])
t_meta.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), light_bg),
        ("BOX", (0, 0), (-1, -1), 0.5, border_color),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ])
)
story.append(t_meta)
story.append(Spacer(1, 6))

# Section 1
story.append(
    Paragraph("1. Executive Summary & Core Objectives", h1_style)
)
story.append(
    Paragraph(
        "This PRD defines the architectural, pedagogical, and user interface"
        " requirements for the Interactive Business Spanish Training Module."
        " The product converts static corporate telephone dialogues into"
        " high-utility, browser-executable study artifacts. Operating entirely"
        " offline via local file execution, the system targets functional"
        " auditory comprehension, domain-specific vocabulary acquisition,"
        " active dialogue decoding, and transactional data extraction without"
        " requiring external server dependencies.",
        body_style,
    )
)
story.append(Paragraph("<b>Strategic Value Drivers:</b>", body_style))
story.append(
    Paragraph(
        "&bull; <b>Synchronized Auditory Immersion:</b> Integrated bottom-docked"
        " audio player enables continuous, distraction-free listening while"
        " navigating scripts.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Contextual Lexical Priming:</b> Pre-dialogue tabular"
        " breakdowns establish essential commercial and technical vocabulary.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Progressive Disclosure:</b> Collapsible translations"
        " encourage active cognitive retrieval before verification.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Zero-JS Ergonomics:</b> State toggling (theme switching and"
        " disclosure) functions seamlessly without external script runtimes.",
        bullet_style,
    )
)

# Section 2
story.append(
    Paragraph("2. Target Audience & Operational Workflow", h1_style)
)
story.append(
    Paragraph(
        "<b>Target Learner:</b> Intermediate corporate professionals,"
        " healthcare educators, logistics coordinators, and account managers"
        " seeking communicative fluency in formal Spanish telephone"
        " environments.",
        body_style,
    )
)
story.append(
    Paragraph(
        "<b>Primary User Workflow:</b> The user initiates audio playback via"
        " the fixed bottom dock, listens to authentic dialogue pacing, verifies"
        " technical terms in the vocabulary ledger, performs line-by-line"
        " shadowing with hidden translations, completes key information"
        " extraction tasks, and alternates between light and dark modes"
        " according to ambient lighting.",
        body_style,
    )
)

# Section 3
story.append(Paragraph("3. Functional Component Specifications", h1_style))

story.append(
    Paragraph(
        "3.1 Fixed Bottom Audio Player Dock (Conversation MP3)", h2_style
    )
)
story.append(
    Paragraph(
        "A viewport-anchored audio bar providing persistent auditory playback"
        " controls across lengthy transcripts.",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Source Audio:</b> Generated via Python <code>edge-tts</code>"
        " using bilingual/regional voices (e.g., <code>es-ES-ElviraNeural</code>,"
        " <code>es-ES-AlvaroNeural</code>) saved locally at"
        " <code>../audios/escena_1.mp3</code>.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Dock Positioning:</b> Viewport pinned (<code>position: fixed;"
        " bottom: 0; left: 0; width: 100%</code>) with high z-index"
        " (<code>99999</code>) and elevation drop-shadow.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Collision Buffer:</b> A mandatory <code>80px</code> bottom"
        " spacer preventing fixed bar overlap with final document content.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Controls:</b> Full native browser controls: Play/Pause,"
        " Scrubber, Volume Slider, and Playback Rate adjustments.",
        bullet_style,
    )
)

story.append(
    Paragraph(
        "3.2 Section 1: Vocabulario y Expresiones Profesionales", h2_style
    )
)
story.append(
    Paragraph(
        "A four-column lexical matrix designed for pre-dialogue priming,"
        " isolating technical corporate terminology.",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Mandatory Schema:</b> Four columns: <i>T&eacute;rmino /"
        " Expresi&oacute;n</i> (Bold Spanish), <i>Categor&iacute;a</i>"
        " (Grammatical Part of Speech), <i>Traducci&oacute;n al ingl&eacute;s</i>"
        " (English Equivalent), and <i>Frase de muestra del di&aacute;logo</i>"
        " (Verbatim contextual sentence).",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Lexical Scope:</b> Covers technical fleet purchasing terms"
        " (<i>flotilla</i>, <i>camioneta de carga</i>), procurement verbs"
        " (<i>adquirir</i>), commercial idioms (<i>llamar la atenci&oacute;n</i>,"
        " <i>revisar los n&uacute;meros</i>), technical documentation (<i>ficha"
        " t&eacute;cnica</i>), and facilities (<i>sala de exhibici&oacute;n</i>,"
        " <i>concesionario</i>).",
        bullet_style,
    )
)

story.append(
    Paragraph(
        "3.3 Section 2: Gui&oacute;n Interactivo (Interactive Script)", h2_style
    )
)
story.append(
    Paragraph(
        "A full-fidelity dialogue transcript structured for active auditory"
        " decoding and progressive translation checking.",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Speaker Attribution:</b> Clear caller and recipient labels"
        " including corporate entities (e.g., <i>Maureen Simmons (Summit"
        " Commercial Fleet Group)</i> vs. <i>Sr. Lewis (Cascade"
        " Technologies)</i>).",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Visual Encapsulation:</b> Spanish speech rendered in distinct"
        " blockquotes with colored left border indicators.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Progressive Reveal Widgets:</b> Semantic HTML5"
        " <code>&lt;details&gt;</code> and <code>&lt;summary&gt;</code>"
        " dropdowns placed directly below each utterance, concealing English"
        " translations until toggled.",
        bullet_style,
    )
)

story.append(
    Paragraph(
        "3.4 Section 3: Extracci&oacute;n de Informaci&oacute;n Clave (Key Data"
        " Extraction)",
        h2_style,
    )
)
story.append(
    Paragraph(
        "A comprehension assessment suite validating logistical, commercial,"
        " and administrative variables.",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Core Extraction Dimensions:</b> (1) Caller Name & Company,"
        " (2) Callee Name & Company, (3) Commercial Intent / Specific Models"
        " (Ford Transit 250), (4) Delivery / Communication Preference"
        " (declining email specs, opting for in-person review), and (5) Meeting"
        " Time & Venue (2:30 p.m. at dealership).",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Interactive Architecture:</b> Expandable disclosure reveals"
        " or embedded input elements verifying student answers against"
        " normalized keyword targets.",
        bullet_style,
    )
)

story.append(
    Paragraph(
        "3.5 Section 4 / Global UI: Zero-JavaScript Dark Mode Toggle", h2_style
    )
)
story.append(
    Paragraph(
        "An accessible theme toggle operating independently of JavaScript"
        " engines via modern CSS selectors.",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>CSS Pseudo-Class Engine:</b> Leverages"
        " <code>body:has(#theme-toggle:checked)</code> to dynamically recolor"
        " typography, tables, details widgets, blockquotes, and the audio"
        " dock.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Control Interface:</b> Fixed pill-shaped trigger at top-right"
        " (<code>top: 16px; right: 20px</code>) with dual-state moon/sun"
        " iconography and dynamic text indicator (<i>Modo oscuro / Modo"
        " claro</i>).",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Color Palette:</b> Dark Canvas: <code>#0d1117</code>; Surface"
        " Container: <code>#161b22</code>; Border Neutral: <code>#30363d</code>;"
        " Primary Accent: <code>#58a6ff</code>; Body Text: <code>#c9d1d9</code>.",
        bullet_style,
    )
)

# Section 4
story.append(
    Paragraph(
        "4. Technical Architecture & File Directory Structure", h1_style
    )
)
story.append(
    Paragraph(
        "The product requires a standardized relative directory structure to"
        " preserve local asset resolution when launched in Google Chrome on"
        " macOS:",
        body_style,
    )
)

arch_data = [
    [
        Paragraph("<b>Directory / File Path</b>", table_header_style),
        Paragraph("<b>Format / Type</b>", table_header_style),
        Paragraph("<b>Operational Function</b>", table_header_style),
    ],
    [
        Paragraph("<code>business-spanish/</code>", table_cell_code),
        Paragraph("Directory", table_cell_style),
        Paragraph("Project root directory.", table_cell_style),
    ],
    [
        Paragraph("<code>├── audios/escena_1.mp3</code>", table_cell_code),
        Paragraph("MPEG-3 Audio", table_cell_style),
        Paragraph(
            "Dual-voice composite audio generated via edge-tts.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("<code>├── scripts/scenes.md</code>", table_cell_code),
        Paragraph("Markdown / HTML5", table_cell_style),
        Paragraph(
            "Primary client-facing interactive training module.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("<code>├── text_to_speech.py</code>", table_cell_code),
        Paragraph("Python 3.11+", table_cell_style),
        Paragraph(
            "Async pipeline generating concatenated MP3 dialogues.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("<code>└── .venv/</code>", table_cell_code),
        Paragraph("Python Virtual Env", table_cell_style),
        Paragraph(
            "Isolated package dependencies (edge-tts, certifi).",
            table_cell_style,
        ),
    ],
]
t_arch = Table(arch_data, colWidths=[150, 80, 290])
t_arch.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), light_bg),
        ("BOX", (0, 0), (-1, -1), 0.5, border_color),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ])
)
story.append(t_arch)

# Section 5
story.append(
    Paragraph(
        "5. Non-Functional Requirements & Acceptance Standards", h1_style
    )
)

qa_data = [
    [
        Paragraph("<b>Evaluation Category</b>", table_header_style),
        Paragraph("<b>Acceptance Standard</b>", table_header_style),
        Paragraph("<b>Validation Procedure</b>", table_header_style),
    ],
    [
        Paragraph("Offline Self-Containment", table_cell_style),
        Paragraph(
            "Zero external network requests; all styling inline.",
            table_cell_style,
        ),
        Paragraph(
            "Disconnect Wi-Fi; launch in Chrome; verify all modules.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("Zero-JS Theme Toggle", table_cell_style),
        Paragraph(
            "CSS :has toggle functions even when JS is blocked.",
            table_cell_style,
        ),
        Paragraph(
            "Disable JS in Chrome settings; click theme pill toggle.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("Dock Scroll Margin", table_cell_style),
        Paragraph(
            "Bottom text must never be hidden behind audio dock.",
            table_cell_style,
        ),
        Paragraph(
            "Scroll to absolute bottom; verify 80px spacer clearance.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("Contrast Compliance", table_cell_style),
        Paragraph(
            "WCAG 2.1 AA compliant text contrast in both modes.",
            table_cell_style,
        ),
        Paragraph(
            "Audit text nodes using Chrome DevTools Lighthouse audit.",
            table_cell_style,
        ),
    ],
    [
        Paragraph("Audio Codec Support", table_cell_style),
        Paragraph(
            "MP3 bitrate compatible with native HTML5 audio tags.",
            table_cell_style,
        ),
        Paragraph(
            "Verify clean playback on Safari, Chrome, and Firefox.",
            table_cell_style,
        ),
    ],
]
t_qa = Table(qa_data, colWidths=[110, 195, 215])
t_qa.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), light_bg),
        ("BOX", (0, 0), (-1, -1), 0.5, border_color),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ])
)
story.append(t_qa)

# Section 6
story.append(
    Paragraph("6. Scalability & NotebookLM / Anki Integration", h1_style)
)
story.append(
    Paragraph(
        "To expand this module into a multi-scenario curriculum (Scenes 2"
        " through 32), the architecture standardizes three integration"
        " endpoints:",
        body_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Semantic Fact Extraction (NotebookLM):</b> Standardized"
        " scene metadata tags facilitate bulk ingesting into Google NotebookLM"
        " for generating automated role-play quizzes and cross-scenario"
        " queries.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Automated Anki Flashcard Pipeline:</b> The four-column"
        " vocabulary table schema exports directly into comma-separated value"
        " (CSV) formats for instant flashcard deck generation with contextual"
        " sentence triggers.",
        bullet_style,
    )
)
story.append(
    Paragraph(
        "&bull; <b>Multi-Speaker TTS Batching:</b> The asynchronous Python"
        " <code>edge-tts</code> script scales to support multiple localized"
        " accents (Spain, Mexico, Colombia) mapped dynamically to individual"
        " speaker personas.",
        bullet_style,
    )
)

doc.build(story, canvasmaker=NumberedCanvas)
print("Saved successfully to:", os.path.abspath(pdf_path))