<!-- Dark Mode Component (Works without JavaScript via CSS :has) -->

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

# Escena 2: Consulta de Ventas por Teléfono

<div id="audio-bar" style="position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; background: #ffffff; padding: 10px 0; border-top: 1px solid #d0d7de; box-shadow: 0 -2px 10px rgba(0,0,0,0.08); transition: background 0.2s ease;">
  <div style="max-width: 860px; margin: 0 auto; padding: 0 24px;">
    <audio controls style="width: 100%; height: 38px;">
      <source src="../audios/escena_2.mp3" type="audio/mpeg">
      Tu navegador no soporta la reproducción de audio.
    </audio>
  </div>
</div>

---

## 1. Vocabulario y Expresiones Profesionales

| Término / Expresión          | Categoría        | Traducción al inglés            | Frase de muestra del diálogo                                         |
| :----------------------------- | :---------------- | :-------------------------------- | :-------------------------------------------------------------------- |
| **Transferirme**             | Verbo             | To transfer me                    | *"...¿Podría transferirme al Departamento de Ventas...?"* |
| **Manejan**                  | Verbo             | To carry / to sell                | *"...consultar si manejan bombas de agua comerciales."*   |
| **Bombas de agua**           | Sustantivo        | Water pumps                       | *"...consultar si manejan bombas de agua comerciales."*   |
| **En existencia**            | Frase preposicional| In stock                          | *"...Tenemos en existencia unidades..."*                  |
| **Vigente**                  | Adjetivo          | Current / valid                   | *"...y su lista de precios vigente?"*                     |
| **Facilíteme**               | Verbo             | Give me / provide me              | *"Solo facilíteme su dirección de correo electrónico..."* |

---

## 2. Guión Interactivo

Haz clic en **"Ver traducción"** debajo de cada intervención para comprobar tu comprensión auditiva y lectora.

**Recepcionista (Midwest Pump & Equipment):**

> "Buenos días, Midwest Pump & Equipment. ¿Con quién desea comunicarse?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Good morning, Midwest Pump & Equipment. How can I direct your call?</em>
</details>

<br>

**James Davies (Liberty Mechanical):**

> "Buenos días. ¿Podría transferirme al Departamento de Ventas, por favor?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Good morning. Could you transfer me over to your Sales Department, please?</em>
</details>

<br>

**Recepcionista:**

> "Por supuesto. Un momento mientras le comunico."

<details>
<summary>🔍 Ver traducción</summary>
<em>Absolutely. One moment while I patch you through.</em>
</details>

<br>

**Departamento de Ventas (Greg):**

> "Ventas, le habla Greg. ¿En qué le puedo ayudar hoy?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Sales, this is Greg speaking. How can I help you today?</em>
</details>

<br>

**James Davies:**

> "Hola, Greg. Mi nombre es James Davies, de Liberty Mechanical. Llamo para consultar si manejan bombas de agua comerciales."

<details>
<summary>🔍 Ver traducción</summary>
<em>Hi Greg, my name is James Davies with Liberty Mechanical. I'm calling to check if you carry commercial water pumps.</em>
</details>

<br>

**Departamento de Ventas:**

> "Sí, claro que sí. Tenemos en existencia unidades tanto para uso comercial como residencial."

<details>
<summary>🔍 Ver traducción</summary>
<em>Yes, we sure do. We stock units for both commercial and residential use.</em>
</details>

<br>

**James Davies:**

> "Perfecto. ¿Podría enviarme una copia de su catálogo de productos y su lista de precios vigente?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Perfect. Would you be able to send over a copy of your product catalog and current price list?</em>
</details>

<br>

**Departamento de Ventas:**

> "Por supuesto. Solo facilíteme su dirección de correo electrónico y se la enviaremos hoy mismo más tarde."

<details>
<summary>🔍 Ver traducción</summary>
<em>Absolutely. Just give me your email address, and we'll get that right out to you later today.</em>
</details>

<br>

**James Davies:**

> "Me parece excelente. ¡Muchas gracias por su ayuda!"

<details>
<summary>🔍 Ver traducción</summary>
<em>Sounds great. Thanks for your help!</em>
</details>

<br>

**Departamento de Ventas:**

> "Con mucho gusto. ¡Que tenga un excelente día!"

<details>
<summary>🔍 Ver traducción</summary>
<em>Happy to help. Have a great day!</em>
</details>

---

## 3. Extracción de Información Clave

Intenta responder las siguientes preguntas de memoria antes de desplegar la solución:

1. **¿Quién llama y a qué empresa representa?**

<details>
<summary>Mostrar respuesta</summary>
James Davies, de <strong>Liberty Mechanical</strong>.
</details>

2. **¿Con quién se comunica al principio y a dónde pide ser transferido?**

<details>
<summary>Mostrar respuesta</summary>
Habla con la recepcionista de <strong>Midwest Pump & Equipment</strong> y pide ser transferido al <strong>Departamento de Ventas</strong>.
</details>

3. **¿Cuál es el motivo exacto de la llamada?**

<details>
<summary>Mostrar respuesta</summary>
Consultar si manejan <strong>bombas de agua comerciales</strong>.
</details>

4. **¿Qué documentos solicita el cliente que le envíen?**

<details>
<summary>Mostrar respuesta</summary>
Una copia del <strong>catálogo de productos</strong> y la <strong>lista de precios vigente</strong>.
</details>

5. **¿Por qué medio se acordó enviar la información solicitada?**

<details>
<summary>Mostrar respuesta</summary>
Por <strong>correo electrónico</strong> hoy mismo más tarde.
</details>

---

<!-- Spacer to prevent the fixed bottom bar from covering content when scrolling -->

<div style="height: 80px;"></div>