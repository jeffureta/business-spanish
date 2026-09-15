<!-- scripts/scenes.md -->
<style>
  :root {
    --bg-canvas: #ffffff;
    --surface: #f6f8fa;
    --border-color: #d0d7de;
    --text-primary: #1f2328;
    --text-secondary: #656d76;
    --accent: #0969da;
    --blockquote-bg: #f8fafd;
    --dock-bg: #ffffff;
    --dock-border: #d0d7de;
    --summary-bg: #eaeef2;
  }

  body:has(#theme-toggle:checked) {
    --bg-canvas: #0d1117;
    --surface: #161b22;
    --border-color: #30363d;
    --text-primary: #c9d1d9;
    --text-secondary: #8b949e;
    --accent: #58a6ff;
    --blockquote-bg: #161b22;
    --dock-bg: #161b22;
    --dock-border: #30363d;
    --summary-bg: #21262d;
  }

  body {
    background-color: var(--bg-canvas);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
    line-height: 1.6;
    max-width: 880px;
    margin: 0 auto;
    padding: 24px 20px;
    transition: background-color 0.2s ease, color 0.2s ease;
  }

  /* Fixed Top-Right Theme Toggle */
  .theme-toggle-container {
    position: fixed;
    top: 16px;
    right: 20px;
    z-index: 100000;
  }

  #theme-toggle {
    display: none;
  }

  .theme-toggle-label {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 9999px;
    background-color: var(--surface);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    user-select: none;
    transition: all 0.2s ease;
  }

  .theme-toggle-label:hover {
    border-color: var(--accent);
  }

  .dark-text { display: none; }
  .light-text { display: inline; }

  body:has(#theme-toggle:checked) .dark-text { display: inline; }
  body:has(#theme-toggle:checked) .light-text { display: none; }

  /* Typography & Tables */
  h1, h2, h3 {
    color: var(--text-primary);
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 8px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
    display: table;
  }

  th, td {
    padding: 12px 14px;
    border: 1px solid var(--border-color);
    text-align: left;
  }

  th {
    background-color: var(--surface);
    color: var(--accent);
    font-weight: 600;
  }

  tr:nth-child(even) {
    background-color: var(--surface);
  }

  /* Interactive Script Blockquotes */
  .speaker-label {
    font-weight: 700;
    color: var(--accent);
    margin-top: 24px;
    margin-bottom: 6px;
    display: block;
    font-size: 15px;
  }

  blockquote.utterance {
    margin: 0 0 10px 0;
    padding: 12px 18px;
    background-color: var(--blockquote-bg);
    border-left: 4px solid var(--accent);
    border-radius: 0 6px 6px 0;
    color: var(--text-primary);
    font-size: 15px;
  }

  /* Progressive Disclosure Dropdowns */
  details.translation-widget {
    margin-bottom: 16px;
    background-color: var(--surface);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    overflow: hidden;
  }

  details.translation-widget summary {
    padding: 8px 14px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    background-color: var(--summary-bg);
    list-style: none;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  details.translation-widget summary::-webkit-details-marker {
    display: none;
  }

  details.translation-widget summary::before {
    content: "▶";
    font-size: 10px;
    transition: transform 0.2s ease;
  }

  details.translation-widget[open] summary::before {
    transform: rotate(90deg);
  }

  .translation-content {
    padding: 12px 16px;
    font-size: 14px;
    color: var(--text-secondary);
    font-style: italic;
  }

  /* Section 3 Assessment Cards */
  .assessment-card {
    background-color: var(--surface);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
  }

  .assessment-card h4 {
    margin-top: 0;
    color: var(--accent);
  }

  details.key-reveal {
    margin-top: 10px;
    border-top: 1px dashed var(--border-color);
    padding-top: 8px;
  }

  details.key-reveal summary {
    cursor: pointer;
    font-size: 13px;
    color: var(--accent);
    font-weight: 600;
  }

  .key-content {
    margin-top: 8px;
    padding: 10px;
    background-color: var(--bg-canvas);
    border-radius: 4px;
    border: 1px solid var(--border-color);
    font-size: 13px;
  }

  /* Bottom Audio Dock */
  .audio-dock {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: var(--dock-bg);
    border-top: 1px solid var(--dock-border);
    box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 12px 20px;
    box-sizing: border-box;
    z-index: 99999;
  }

  .audio-dock audio {
    width: 100%;
    max-width: 800px;
    height: 40px;
  }

  /* 80px Collision Spacer */
  .collision-spacer {
    height: 80px;
    width: 100%;
    clear: both;
  }
</style>

<!-- Zero-JS CSS:has Theme Switcher -->
<div class="theme-toggle-container">
  <input type="checkbox" id="theme-toggle" aria-label="Toggle dark mode">
  <label for="theme-toggle" class="theme-toggle-label">
    <span class="light-text">🌙 Modo oscuro</span>
    <span class="dark-text">☀️ Modo claro</span>
  </label>
</div>

# Escena 5: Hacer un cambio en el pedido
**Módulo Interactivo de Telefonía Comercial** | Midwest Wholesale Supply vs. Valley Market

---

## Sección 1: Vocabulario y Expresiones Profesionales

| Término / Expresión | Categoría | Traducción al inglés | Frase de muestra del diálogo |
| :--- | :--- | :--- | :--- |
| **Hacer un cambio** | Locución verbal | To modify / make an order change | *"¿Sería posible hacer un cambio por teléfono?"* |
| **Pedido especial** | Sustantivo masculino | Special-order item | *"nada más que no lleve cosas frescas de pedido especial."* |
| **Tener a la mano** | Locución verbal | To have on hand / readily available | *"¿Tiene a la mano el número de pedido?"* |
| **Productos secos** | Sustantivo masculino pl. | Packaged dry goods | *"Lo hicimos hace tres días y son puros productos secos empaquetados."* |
| **Empaquetado/a** | Adjetivo | Pre-packaged / boxed | *"son puros productos secos empaquetados."* |
| **Cajas** | Sustantivo femenino pl. | Bulk cases / boxes | *"cambiarlos por quince cajas de toallas de papel."* |
| **Checar el sistema** | Locución verbal | To check / pull up in the system | *"Permítame checar el sistema... Muy bien, aquí tengo su pedido y la factura."* |
| **Factura** | Sustantivo femenino | Commercial invoice | *"aquí tengo su pedido y la factura."* |
| **Recoger** | Verbo transitivo | To pick up / collect | *"Podemos hacer el cambio sin problema antes de que vengan a recogerlo mañana"* |
| **Nota actualizada** | Sustantivo femenino | Updated invoice / adjusted ticket | *"le tengo lista la nota actualizada."* |
| **Cheque de la empresa** | Sustantivo masculino | Corporate check | *"Sí, con cheque de la empresa, como siempre."* |
| **Tener todo listo** | Locución verbal | To stage / have everything ready | *"Aquí le tenemos todo listo para cuando lleguen."* |

---

## Sección 2: Guión Interactivo (Interactive Script)

<span class="speaker-label">Gerente de la tienda — Mike (Midwest Wholesale Supply):</span>
<blockquote class="utterance">
"Midwest Wholesale Supply, habla Mike. ¿En qué le puedo ayudar?"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Midwest Wholesale Supply, this is Mike speaking. How can I help you today?"
  </div>
</details>

<span class="speaker-label">Cliente — Sarah Wilson (Valley Market):</span>
<blockquote class="utterance">
"Buenos días, Mike. Habla Sarah Wilson, de Valley Market. Disculpe la molestia, pero hubo un error en nuestro pedido de la semana. ¿Sería posible hacer un cambio por teléfono?"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Good morning, Mike. This is Sarah Wilson from Valley Market. I apologize for the trouble, but my brother made a mistake on our weekly order. Would it be possible to modify it over the phone?"
  </div>
</details>

<span class="speaker-label">Gerente de la tienda — Mike (Midwest Wholesale Supply):</span>
<blockquote class="utterance">
"Claro que sí, no hay problema, señora Wilson, nada más que no lleve cosas frescas de pedido especial. ¿Tiene a la mano el número de pedido?"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Not a problem at all, Mrs. Wilson, as long as there aren't any special-order perishables involved. Do you have the order number handy?"
  </div>
</details>

<span class="speaker-label">Cliente — Sarah Wilson (Valley Market):</span>
<blockquote class="utterance">
"Sí, es el pedido SCC-231. Lo hicimos hace tres días y son puros productos secos empaquetados. Queremos cancelar los refrescos y los cereales, y cambiarlos por quince cajas de toallas de papel. ¿Se puede hacer el cambio?"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Yes, it's PO number SCC-231. We just submitted it three days ago, and it's entirely packaged dry goods. We'd like to cancel the sodas and the breakfast cereals, and replace them with fifteen bulk cases of paper towels instead. Would that be doable?"
  </div>
</details>

<span class="speaker-label">Gerente de la tienda — Mike (Midwest Wholesale Supply):</span>
<blockquote class="utterance">
"Permítame checar el sistema... Muy bien, aquí tengo su pedido y la factura. Podemos hacer el cambio sin problema antes de que vengan a recogerlo mañana; le tengo lista la nota actualizada. ¿Van a pagar al recoger?"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Let me pull that up on my screen... All right, I've got your order and the preliminary invoice right here. We can easily make that swap before your team swings by for pickup tomorrow, and I'll print out an updated invoice. Will you be paying at pickup?"
  </div>
</details>

<span class="speaker-label">Cliente — Sarah Wilson (Valley Market):</span>
<blockquote class="utterance">
"Sí, con cheque de la empresa, como siempre. Le agradezco mucho su ayuda. ¡Nos vemos mañana!"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "Yes, by company check, as usual. Thank you so much for your help. See you tomorrow!"
  </div>
</details>

<span class="speaker-label">Gerente de la tienda — Mike (Midwest Wholesale Supply):</span>
<blockquote class="utterance">
"¡Con mucho gusto, señora Wilson! Aquí le tenemos todo listo para cuando lleguen. ¡Que le vaya muy bien!"
</blockquote>
<details class="translation-widget">
  <summary>Show English Translation</summary>
  <div class="translation-content">
    "You're very welcome, Mrs. Wilson. We'll have everything staged and ready for you. Take care!"
  </div>
</details>

---

## Sección 3: Extracción de Información Clave

<div class="assessment-card">
  <p>1. ¿Quién llama para pedir el cambio y de qué negocio es?</p>
  <details class="key-reveal">
    <summary>Ver respuesta</summary>
    <div class="key-content">
      Sarah Wilson, de <em>Valley Market</em>.
    </div>
  </details>
</div>

<div class="assessment-card">
  <p>2. ¿Quién contesta la llamada y qué puesto tiene en la tienda?</p>
  <details class="key-reveal">
    <summary>Ver respuesta</summary>
    <div class="key-content">
      Mike, gerente de la tienda en <em>Midwest Wholesale Supply</em>.
    </div>
  </details>
</div>

<div class="assessment-card">
  <p>3. ¿Cuál es el número de pedido y qué cambios se van a hacer?</p>
  <details class="key-reveal">
    <summary>Ver respuesta</summary>
    <div class="key-content">
      Pedido <strong>SCC-231</strong> (se hizo hace tres días). Se cancelan los refrescos y los cereales, y se cambian por quince cajas de toallas de papel.
    </div>
  </details>
</div>

<div class="assessment-card">
  <p>4. ¿Qué condición se pide para hacer el cambio y cuándo se va a recoger el pedido?</p>
  <details class="key-reveal">
    <summary>Ver respuesta</summary>
    <div class="key-content">
      Se puede hacer el cambio nada más si no lleva cosas frescas de pedido especial. Se pasa a recoger mañana en la tienda.
    </div>
  </details>
</div>

<div class="assessment-card">
  <p>5. ¿Cómo se va a pagar el pedido?</p>
  <details class="key-reveal">
    <summary>Ver respuesta</summary>
    <div class="key-content">
      Se paga al recoger en la tienda, con cheque de la empresa.
    </div>
  </details>
</div>
<!-- Mandatory 80px Collision Buffer -->
<div class="collision-spacer"></div>

<!-- Viewport Pinned Bottom Audio Dock -->
<div class="audio-dock">
  <audio controls preload="metadata" src="../audios/escena_5.mp3">
    Tu navegador no soporta el elemento de audio HTML5.
  </audio>
</div>