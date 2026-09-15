from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.pdfgen import canvas
import pypdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        if self._pageNumber > 1:
            self.drawString(36, 756, "BUSINESS SPANISH REPOSITORY — LATIN AMERICAN SCRIPT PIPELINE")
            self.drawRightString(576, 756, "Workflow Guide: Script Simplification v4.0")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(36, 750, 576, 750)
            
        self.drawString(36, 25, "BUSINESS SPANISH REPOSITORY — LATIN AMERICAN SCRIPT PIPELINE")
        self.drawRightString(576, 25, f"Page {self._pageNumber} of {page_count}")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(36, 35, 576, 35)
        self.restoreState()

def build_pdf(filename="Script_Simplification_Workflow_Guide_v4.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor("#1A365D")
    secondary_color = colors.HexColor("#2B6CB0")
    dark_text = colors.HexColor("#2D3748")
    border_color = colors.HexColor("#CBD5E0")

    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13.5, leading=16, textColor=primary_color, spaceAfter=1)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=secondary_color, spaceAfter=3)
    meta_style = ParagraphStyle('DocMeta', parent=styles['Normal'], fontName='Helvetica', fontSize=6.8, leading=8.8, textColor=colors.HexColor("#4A5568"))
    sec_head = ParagraphStyle('SecHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.8, leading=11, textColor=primary_color, spaceBefore=3, spaceAfter=1.5)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=6.8, leading=8.8, textColor=dark_text, spaceAfter=2)
    rule_head = ParagraphStyle('RuleHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.3, leading=9.2, textColor=secondary_color, spaceBefore=2, spaceAfter=1)
    bullet_style = ParagraphStyle('BulletText', parent=styles['Normal'], fontName='Helvetica', fontSize=6.7, leading=8.5, textColor=dark_text, leftIndent=6, spaceAfter=1)
    th_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7, leading=8.8, textColor=primary_color)
    tb_style = ParagraphStyle('TB', parent=styles['Normal'], fontName='Helvetica', fontSize=6.5, leading=8.2, textColor=dark_text)
    tbb_style = ParagraphStyle('TBB', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=6.5, leading=8.2, textColor=dark_text)

    story = [
        Paragraph("Spanish Script Simplification: Workflow Guide & Protocol", title_style),
        Paragraph("Standard Operating Procedure for Converting Formal Dialogues & Scene Titles into High-Frequency Latin American Spanish (v4.0)", subtitle_style),
        Table([
            [Paragraph("<b>Project Domain:</b> Business Spanish Scene Transformation", meta_style), Paragraph("<b>Target Execution:</b> Script & Title Rewriting Pipeline", meta_style)],
            [Paragraph("<b>Target Dialect / Standard:</b> Neutral Latin-American Spanish (No Peninsular)", meta_style), Paragraph("<b>Header Standard:</b> [Escena número: título] in conversational phrasing", meta_style)]
        ], colWidths=[270, 270], style=[('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EDF2F7")), ('BOX', (0,0), (-1,-1), 0.5, border_color), ('PADDING', (0,0), (-1,-1), 3)]),
        Spacer(1, 2),
        Paragraph("1. Purpose & Workflow Architecture", sec_head),
        Paragraph("This standard operating procedure governs the scene simplification pipeline. Business textbooks often use stiff, gerund-heavy headers, academic Peninsular expressions, and complex subjunctive conjugations. This pipeline transforms both scene titles and dialogue scripts into natural, spoken Latin-American Spanish, enforcing standardized conversational title formatting: <b>[Escena número: título]</b> and systematic conjugation bypass strategies.", body_style),
        Paragraph("2. The 3-Step Execution Workflow", sec_head),
        Paragraph("• <b>Step 1 — Prompt Ingestion:</b> The user submits the raw scene title and dialogue from the source document.", bullet_style),
        Paragraph("• <b>Step 2 — Systematic Transformation Execution:</b> The AI converts the formal title into a punchy, spoken Latin-American heading formatted as <b>[Escena número: título]</b>. Then it rewrites the script using high-frequency verbs, modal shields, courtesy softeners, <b>passive/impersonal <i>se</i> bypasses</b>, and authentic Latin American lexicon.", bullet_style),
        Paragraph("• <b>Step 3 — Formatted Output Generation:</b> The AI outputs: (1) The Conversational Script with the standardized header, (2) Transformation Breakdown Ledger (including original vs. simplified titles), and (3) Core Patterns Used.", bullet_style),
        Paragraph("3. Script & Title Transformation Rules (Latin-American Standard)", sec_head),
        Paragraph("Rule A: Conversational Title Transformation & Standard Header Format", rule_head),
        Paragraph("Scene titles must be simplified and formatted strictly as: <b>[Escena número: título]</b>.", bullet_style),
        Paragraph("• <b>Eliminate Stiff Gerunds / Abstract Nouns:</b> Replace textbook gerunds (<i>Solicitando...</i>, <i>Realizando...</i>) and bureaucratic nouns (<i>Consulta de...</i>, <i>Confirmación de...</i>) with high-frequency infinitive actions (<i>Preguntar por...</i>, <i>Hacer un pedido...</i>, <i>Cambiar...</i>, <i>Avisar que...</i>).", bullet_style),
        Paragraph("• <b>Concrete Over Technical:</b> Specify everyday commercial terms (e.g., 'vehículos de flotilla' &rarr; 'camionetas para la empresa'; 'equipo' &rarr; 'una copiadora').", bullet_style),
        Paragraph("• <b>Drop Redundancies:</b> Omit redundant channel descriptors like 'por teléfono' or '(En persona)' unless strictly necessary for context.", bullet_style),
        Paragraph("Rule B: Mandatory Latin-American Standards & Peninsular Exclusions", rule_head),
        Paragraph("Strictly adhere to conversational Latin-American business Spanish and exclude Spain-specific constructs:", bullet_style),
        Paragraph("• <b>Pronouns:</b> Never use <i>vosotros / os / vuestro</i>. Always use <b>usted</b> (formal singular) and <b>ustedes</b> (plural).", bullet_style),
        Paragraph("• <b>No Leísmo:</b> Use direct object pronouns (<i>lo / la / los / las</i>) for masculine and feminine accusative objects.", bullet_style),
        Paragraph("• <b>Peninsular Bans:</b> Ban terms like <i>coche</i> (&rarr; carro / auto), <i>furgoneta</i> (&rarr; camioneta / van), <i>ordenador</i> (&rarr; computadora), <i>vale</i> (&rarr; de acuerdo / perfecto / está bien), <i>coger</i> (&rarr; tomar / recoger / agarrar), <i>aparcar</i> (&rarr; estacionar), <i>avería</i> (&rarr; falla / problema).", bullet_style),
        Paragraph("• <b>Latin Courtesy:</b> Prioritize customary greetings: <i>'Con gusto'</i>, <i>'¿En qué le puedo ayudar?'</i>, <i>'¿Con quién gusta hablar?'</i>, <i>'Páseme a...'</i>, <i>'Ahorita le mando...'</i>.", bullet_style),
        Paragraph("Rule C: High-Frequency Verb Substitution ('Everyday Verb Swap')", rule_head),
        Paragraph("Eliminate literary or stiff verbs in favor of core spoken verbs: <i>Consultar/Averiguar</i> &rarr; <b>Preguntar/Ver</b> | <i>Adquirir</i> &rarr; <b>Comprar</b> | <i>Solicitar/Requerir</i> &rarr; <b>Pedir</b> | <i>Remitir/Enviar</i> &rarr; <b>Mandar</b> | <i>Facilitar/Proporcionar</i> &rarr; <b>Dar/Pasar</b> | <i>Comunicarse con</i> &rarr; <b>Hablar con</b>.", bullet_style),
        Paragraph("Rule D: Modal Shields ('Auxiliary + Infinitive' Conjugation Bypass)", rule_head),
        Paragraph("Shield action verbs inside high-frequency helper verbs to keep the main action unconjugated: <b>Querer + Inf:</b> <i>Quiere / Queremos + [inf]</i> | <b>Tener que + Inf:</b> <i>Tengo que / Tiene que + [inf]</i> | <b>Ir a + Inf:</b> <i>Va a / Vamos a + [inf]</i> | <b>Hay que + Inf:</b> Impersonal necessity without personal conjugations.", bullet_style),
        Paragraph("Rule E: Politeness Softeners & Courtesy Conditionals", rule_head),
        Paragraph("Wrap requests in conversational softeners: <i>¿Me podría + Inf...?</i>, <i>Quisiera + Inf...</i>, <i>¿Sería posible + Inf...?</i>, <i>Me gustaría + Inf...</i>", bullet_style),
        Paragraph("Rule F: Conversational Shortcuts (Zero-Verb & Past-Tense Bypasses)", rule_head),
        Paragraph("• <b>Acaba de + Inf:</b> Bypasses preterites (<i>'La tarima acaba de llegar'</i>) | <b>Para + Inf:</b> Replaces subjunctive clauses | <b>No, mejor + Inf:</b> Decline shortcut | <b>Zero-Verb Shorthand:</b> Direct logistics (<i>'A las 2:30 en el concesionario'</i>).", bullet_style),
        Paragraph("Rule G: Passive & Impersonal 'Se' (Universal Conjugation Bypass)", rule_head),
        Paragraph("Eliminate complex personal conjugations, passive voice periphrases, and irregular subjunctive forms using invariant 3rd-person <b>passive <i>se</i></b> (<i>se + singular/plural verb</i>) and <b>impersonal <i>se</i></b> (<i>se + singular verb</i>):", bullet_style),
        Paragraph("• <b>¿Se puede / Se podrá + Infinitivo?:</b> Universal bypass for polite inquiries and requests without conjugating modal verbs across persons (e.g., <i>'¿Se puede hacer el cambio?'</i> instead of <i>'¿Podríamos nosotros modificar...?'</i>; <i>'¿Se podrá pedir reembolso?'</i> instead of <i>'¿Sería factible que obtuviéramos...?'</i>).", bullet_style),
        Paragraph("• <b>Se + 3rd Person Action (Status & Procedures):</b> Converts actions into natural procedure updates, eliminating passive participles (<i>ser + participio</i>) and subject declarations (e.g., <i>'Se cancela el primer pedido'</i> instead of <i>'Cancelamos nosotros el primer pedido'</i>; <i>'Ya se mandó la factura'</i>; <i>'Se armó la junta para el martes'</i>).", bullet_style),
        Paragraph("• <b>Se necesita / Se busca + Objeto / Infinitivo:</b> Impersonal corporate necessity that avoids declaring specific personal subjects (e.g., <i>'Se necesitan cuarenta hojas'</i> instead of <i>'Nosotros necesitamos que nos provea...'</i>; <i>'Se busca expandir la zona'</i>).", bullet_style),
        Paragraph("• <b>Se me complica / Se me hace:</b> Expresses personal schedule constraints or impressions effortlessly using impersonal datives (e.g., <i>'En la mañana se me complica'</i> instead of <i>'Tengo un compromiso que me impide...'</i>; <i>'Se me hace que va a quedar apretado'</i>).", bullet_style),
        PageBreak(),
        Paragraph("4. Scene Title Simplification Master Matrix", sec_head),
        Paragraph("The matrix below illustrates the transformation from textbook gerunds to conversational infinitive headers, incorporating modal shields, common Latin American lexicon, and passive/impersonal shortcuts:", body_style),
        Table([
            [Paragraph("<b>Original Formal/Textbook Title</b>", th_style), Paragraph("<b>Mandatory Output Header Format</b>", th_style), Paragraph("<b>Simplification Rationale & Bypass Pattern</b>", th_style)],
            [Paragraph("Solicitando información sobre vehículos de flotilla por teléfono", tb_style), Paragraph("<b>[Escena 1: Preguntar por camionetas para la empresa]</b>", tbb_style), Paragraph("Replaces gerund with direct infinitive action; clarifies commercial units (<i>camionetas</i>) and eliminates redundant channel descriptor.", tb_style)],
            [Paragraph("Consulta de ventas por teléfono", tb_style), Paragraph("<b>[Escena 2: Llamar para pedir precios]</b>", tbb_style), Paragraph("Replaces abstract bureaucratic noun (<i>consulta</i>) with purposive infinitive shortcut (<i>para pedir precios</i>).", tb_style)],
            [Paragraph("Realizando un pedido de madera por teléfono", tb_style), Paragraph("<b>[Escena 3: Hacer un pedido de triplay]</b>", tbb_style), Paragraph("Replaces gerund with direct infinitive; introduces common commercial Latin term (<i>triplay</i>).", tb_style)],
            [Paragraph("Modificando un pedido de equipo por teléfono", tb_style), Paragraph("<b>[Escena 4: Cambiar el pedido de una copiadora]</b>", tbb_style), Paragraph("Replaces <i>modificando</i> with everyday verb <i>cambiar</i>; names the specific office asset (<i>copiadora</i>).", tb_style)],
            [Paragraph("Modificando un pedido por teléfono", tb_style), Paragraph("<b>[Escena 5: Hacer un cambio en el pedido]</b>", tbb_style), Paragraph("Employs conversational warehouse collocation (<i>hacer un cambio</i>); sets up <b>passive <i>se</i></b> check (<i>¿se puede hacer el cambio?</i>).", tb_style)],
            [Paragraph("Confirmando la recepción de un pedido por teléfono", tb_style), Paragraph("<b>[Escena 6: Avisar que ya llegó el pedido]</b>", tbb_style), Paragraph("Replaces administrative noun with conversational shortcut <i>avisar que ya llegó</i>.", tb_style)],
            [Paragraph("Coordinando los próximos pasos con una empresa socia (En persona)", tb_style), Paragraph("<b>[Escena 27: Acordar los siguientes pasos de un proyecto]</b>", tbb_style), Paragraph("Eliminates gerund and channel tag; replaces vague corporate jargon with concrete action <i>acordar</i>.", tb_style)],
            [Paragraph("Presentando una propuesta en una oficina ejecutiva (En persona)", tb_style), Paragraph("<b>[Escena 28: Proponer adelantar un lanzamiento]</b>", tbb_style), Paragraph("Replaces gerund and spatial descriptor with high-frequency commercial proposal verbs (<i>proponer adelantar</i>).", tb_style)],
            [Paragraph("Explorando una colaboración comercial en sala de juntas (En persona)", tb_style), Paragraph("<b>[Escena 29: Ver una alianza para entrar a una licitación]</b>", tbb_style), Paragraph("Replaces literary <i>explorando</i> with core spoken verb <i>ver</i>, naming the tangible objective (<i>licitación</i>).", tb_style)],
            [Paragraph("Cancelando un vuelo en una agencia de viajes (En persona)", tb_style), Paragraph("<b>[Escena 30: Cancelar un vuelo y pedir reembolso]</b>", tbb_style), Paragraph("Replaces gerund with twin high-frequency infinitive actions; prepares <b>passive <i>se</i></b> refund inquiry (<i>¿se podrá pedir...?</i>).", tb_style)],
        ], colWidths=[175, 175, 190], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]),
        Spacer(1, 5),
        Paragraph("5. AI Execution Output Format", sec_head),
        Paragraph("Whenever a raw scene script is submitted, the AI engine must strictly produce the following standardized 3-part ledger:", body_style),
        Table([
            [Paragraph("<b>Section</b>", th_style), Paragraph("<b>Required Content & Formatting Specifications</b>", th_style)],
            [Paragraph("<b>1. Conversational Script (Latin-American Standard)</b>", tbb_style), Paragraph("Must lead immediately with the standardized header <b>[Escena número: título]</b> using the simplified conversational title. All speaker labels must be bolded on separate lines, dialogues wrapped in quotation marks, and free of Peninsular vocabulary, unshielded subjunctive forms, or passive participles.", tb_style)],
            [Paragraph("<b>2. Vocabulary & Verb Replacement Table</b>", tbb_style), Paragraph("Three-column structured Markdown table detailing: (1) <i>Frase / Verbo Original</i>, (2) <i>Sustitución Conversacional (LatAm)</i>, and (3) <i>Razón del Cambio y Regla Aplicada</i> (explicitly citing Rules A through G).", tb_style)],
            [Paragraph("<b>3. Core Conversational Patterns Used</b>", tbb_style), Paragraph("Itemized bullet points cataloging the exact linguistic engineering devices deployed: Modal Shields, Everyday Verb Swaps, Politeness Softeners, Conversational Shortcuts, and <b>Passive / Impersonal <i>Se</i> Bypasses</b>.", tb_style)],
        ], colWidths=[150, 390], style=[
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
            ('BOX', (0,0), (-1,-1), 0.5, border_color),
            ('INNERGRID', (0,0), (-1,-1), 0.5, border_color),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ])
    ]

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"File successfully created: {filename}")

if __name__ == "__main__":
    build_pdf()