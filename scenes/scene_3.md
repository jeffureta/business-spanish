<!-- Dark Mode Component (Works without JavaScript via CSS :has) -->
<!-- Note: This document is a clean production file. No citations, footnotes, or bracketed reference markers (such as) are included in this output. -->

<style>
  #theme-toggle { display: none; }
  
  .theme-toggle-btn {
    position: fixed;
    top: 16px;
    right: 20px;
    z-index: 100000;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 20px;
    cursor: pointer;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    font-weight: 600;
    background: #ffffff;
    color: #24292f;
    border: 1px solid #d0d7de;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    user-select: none;
    transition: all 0.2s ease;
  }
  .theme-toggle-btn:hover {
    background: #f3f4f6;
  }

  .icon-sun { display: none; }
  .icon-moon { display: inline; }

  /* Dark Mode styles when the checkbox is checked */
  body:has(#theme-toggle:checked) {
    background-color: #0d1117 !important;
    color: #c9d1d9 !important;
  }
  body:has(#theme-toggle:checked) h1,
  body:has(#theme-toggle:checked) h2,
  body:has(#theme-toggle:checked) h3 {
    color: #58a6ff !important;
    border-bottom-color: #30363d !important;
  }
  body:has(#theme-toggle:checked) hr {
    border-color: #30363d !important;
  }
  body:has(#theme-toggle:checked) table th {
    background-color: #161b22 !important;
    color: #f0f6fc !important;
    border-color: #30363d !important;
  }
  body:has(#theme-toggle:checked) table td {
    background-color: #0d1117 !important;
    border-color: #30363d !important;
    color: #c9d1d9 !important;
  }
  body:has(#theme-toggle:checked) blockquote {
    background: #161b22 !important;
    border-left-color: #1f6feb !important;
    color: #e6edf3 !important;
  }
  body:has(#theme-toggle:checked) details {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    color: #c9d1d9 !important;
    padding: 8px 12px;
    border-radius: 6px;
  }
  body:has(#theme-toggle:checked) summary {
    color: #58a6ff !important;
  }
  body:has(#theme-toggle:checked) #audio-bar {
    background: #161b22 !important;
    border-top-color: #30363d !important;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.4) !important;
  }
  body:has(#theme-toggle:checked) .theme-toggle-btn {
    background: #21262d;
    color: #f0f6fc;
    border-color: #58a6ff;
  }
  body:has(#theme-toggle:checked) .icon-sun { display: inline; }
  body:has(#theme-toggle:checked) .icon-moon { display: none; }
  body:has(#theme-toggle:checked) .mode-label::after {
    content: "Modo claro";
  }
  body:not(:has(#theme-toggle:checked)) .mode-label::after {
    content: "Modo oscuro";
  }
  
</style>

<input type="checkbox" id="theme-toggle">
<label for="theme-toggle" class="theme-toggle-btn">
  <span class="icon-moon">🌙</span>
  <span class="icon-sun">☀️</span>
  <span class="mode-label"></span>
</label>

# Escena 3: Realizando un Pedido de Madera por Teléfono

<div id="audio-bar" style="position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; background: #ffffff; padding: 10px 0; border-top: 1px solid #d0d7de; box-shadow: 0 -2px 10px rgba(0,0,0,0.08); transition: background 0.2s ease;">
  <div style="max-width: 860px; margin: 0 auto; padding: 0 24px;">
    <audio controls style="width: 100%; height: 38px;">
      <source src="../audios/escena_3.mp3" type="audio/mpeg">
      Tu navegador no soporta la reproducción de audio.
    </audio>
  </div>
</div>

---

## 1. Vocabulario y Expresiones Profesionales

| Término / Expresión          | Categoría        | Traducción al inglés            | Frase de muestra del diálogo                                         |
| :----------------------------- | :---------------- | :-------------------------------- | :-------------------------------------------------------------------- |
| **Madera contrachapada**     | Sustantivo        | Plywood                           | *"...Quisiera hacer un pedido de madera contrachapada, por favor."*  |
| **Estanterías comerciales**  | Sustantivo        | Commercial shelving               | *"Es para estanterías comerciales, así que la madera debe ser..."*   |
| **Resistente**               | Adjetivo          | Sturdy / strong                   | *"...lo suficientemente resistente para soportar colecciones..."*    |
| **Ebanistería**              | Sustantivo        | Cabinetry / cabinet-grade         | *"...madera contrachapada de tres cuartos de pulgada para ebanistería..."* |
| **Láminas**                  | Sustantivo        | Sheets                            | *"...en láminas estándar de cuatro por ocho pies."*                  |
| **Descuento por volumen**    | Sustantivo        | Volume discount                   | *"...¿Ofrecen algún descuento por volumen para un pedido de ese tamaño?"* |
| **Descuentos escalonados**   | Sustantivo        | Tiered discounts                  | *"Ofrecemos descuentos escalonados para contratistas..."*            |
| **Lugar de entrega**         | Sustantivo        | Job site / delivery location      | *"En cuanto tenga a mano la dirección del lugar de entrega..."*      |

---

## 2. Guión Interactivo

Haz clic en **"Ver traducción"** debajo de cada intervención para comprobar tu comprensión auditiva y lectora.

**Tracy (Keystone Lumber & Supply):**

> "Keystone Lumber & Supply, habla Tracy. ¿A dónde desea que dirija su llamada?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Keystone Lumber & Supply, Tracy speaking. How can I direct your call?</em>
</details>

<br>

**Cliente:**

> "Buenos días. Quisiera hacer un pedido de madera contrachapada, por favor."

<details>
<summary>🔍 Ver traducción</summary>
<em>Good morning. I'd like to place an order for some plywood, please.</em>
</details>

<br>

**Tracy:**

> "Con gusto, señor. Permítame transferirlo a nuestro Departamento de Maderas."

<details>
<summary>🔍 Ver traducción</summary>
<em>Certainly, sir. Let me transfer you over to our Lumber Department.</em>
</details>

<br>

**Dave (Departamento de Maderas):**

> "Departamento de Maderas, le habla Dave. ¿En qué le puedo ayudar hoy?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Lumber Department, this is Dave. How can I help you today?</em>
</details>

<br>

**Cliente:**

> "Hola, Dave. Busco ordenar una cantidad bastante grande de madera contrachapada."

<details>
<summary>🔍 Ver traducción</summary>
<em>Hi Dave. I'm looking to order a fairly large quantity of plywood.</em>
</details>

<br>

**Dave:**

> "Por supuesto, señor. ¿Sabe qué grado necesita, o podría decirme qué va a construir?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Certainly, sir. Do you know what grade you need, or could you tell me what you're building?</em>
</details>

<br>

**Cliente:**

> "Es para estanterías comerciales, así que la madera debe ser lo suficientemente resistente para soportar colecciones pesadas de libros."

<details>
<summary>🔍 Ver traducción</summary>
<em>It's for commercial shelving, so the wood needs to be sturdy enough to hold heavy sets of books.</em>
</details>

<br>

**Dave:**

> "Entendido. Para ese tipo de carga, le recomendaría madera contrachapada de tres cuartos de pulgada para ebanistería, en láminas estándar de cuatro por ocho pies. ¿Cuántas láminas necesita?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Understood. For that kind of load, I'd recommend three-quarter-inch cabinet-grade plywood in standard four-by-eight-foot sheets. How many sheets do you need?</em>
</details>

<br>

**Cliente:**

> "Necesitaré cuarenta láminas. ¿Ofrecen algún descuento por volumen para un pedido de ese tamaño?"

<details>
<summary>🔍 Ver traducción</summary>
<em>I'll need forty sheets. Do you offer a volume discount on an order of that size?</em>
</details>

<br>

**Dave:**

> "Claro que sí. Ofrecemos descuentos escalonados para contratistas a partir de veinticinco láminas."

<details>
<summary>🔍 Ver traducción</summary>
<em>We sure do. We offer tiered contractor discounts starting at twenty-five sheets.</em>
</details>

<br>

**Cliente:**

> "Excelente. Le daré mi dirección de entrega para que me indique cuál sería la fecha de entrega más próxima y cuáles son las condiciones de facturación y pago."

<details>
<summary>🔍 Ver traducción</summary>
<em>Excellent. I'll give you my delivery address, and you can let me know your earliest delivery window and what your billing and payment terms look like.</em>
</details>

<br>

**Dave:**

> "Perfecto. En cuanto tenga a mano la dirección del lugar de entrega, lo incluiremos en el calendario de distribución y abriremos su cuenta."

<details>
<summary>🔍 Ver traducción</summary>
<em>Perfect. Whenever you're ready with that job site address, we'll get you on the delivery schedule and set up your account.</em>
</details>

---

## 3. Extracción de Información Clave

Intenta responder las siguientes preguntas de memoria antes de desplegar la solución:

1. **¿Quién recibe la llamada al inicio y a qué empresa representa?**

<details>
<summary>Mostrar respuesta</summary>
Tracy, de <strong>Keystone Lumber & Supply</strong>.
</details>

2. **¿A qué departamento transfieren al cliente y quién lo atiende?**

<details>
<summary>Mostrar respuesta</summary>
Al <strong>Departamento de Maderas</strong>, atendido por <strong>Dave</strong>.
</details>

3. **¿Qué producto busca adquirir el cliente y qué uso le dará?**

<details>
<summary>Mostrar respuesta</summary>
<strong>Madera contrachapada</strong> (<em>plywood</em>) para construir <strong>estanterías comerciales</strong> capaces de soportar colecciones pesadas de libros.
</details>

4. **¿Qué especificaciones y cantidad exacta de material acuerdan?**

<details>
<summary>Mostrar respuesta</summary>
Madera contrachapada de <strong>3/4 de pulgada</strong> para ebanistería en láminas de <strong>4x8 pies</strong>, requiriendo un total de <strong>40 láminas</strong>.
</details>

5. **¿Cuáles son las condiciones del descuento por volumen mencionado?**

<details>
<summary>Mostrar respuesta</summary>
Ofrecen <strong>descuentos escalonados para contratistas</strong> aplicables a partir de <strong>25 láminas</strong>.
</details>

---

<!-- Spacer to prevent the fixed bottom bar from covering content when scrolling -->

<div style="height: 80px;"></div>