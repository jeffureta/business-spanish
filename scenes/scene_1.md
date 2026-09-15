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

# Escena 1: Solicitud de Información sobre Vehículos de Flotilla

<div id="audio-bar" style="position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; background: #ffffff; padding: 10px 0; border-top: 1px solid #d0d7de; box-shadow: 0 -2px 10px rgba(0,0,0,0.08); transition: background 0.2s ease;">
  <div style="max-width: 860px; margin: 0 auto; padding: 0 24px;">
    <audio controls style="width: 100%; height: 38px;">
      <source src="../audios/escena_1.mp3" type="audio/mpeg">
      Tu navegador no soporta la reproducción de audio.
    </audio>
  </div>
</div>

---

## 1. Vocabulario y Expresiones Profesionales

| Término / Expresión          | Categoría        | Traducción al inglés            | Frase de muestra del diálogo                                         |
| :----------------------------- | :---------------- | :-------------------------------- | :-------------------------------------------------------------------- |
| **Flotilla**             | Sustantivo        | Fleet                             | *"...precios para flotillas comerciales."*                          |
| **Camioneta de carga**   | Sustantivo        | Cargo van                         | *"...anuncio sobre las camionetas de carga Ford Transit 250..."*    |
| **Adquirir**             | Verbo             | To acquire / purchase             | *"...hemos estado buscando adquirir media docena de vehículos..."* |
| **Llamar la atención**  | Frase verbal      | To catch someone's eye / interest | *"...su oferta nos llamó la atención."*                           |
| **Ficha técnica**       | Sustantivo        | Spec sheet / data sheet           | *"...enviar por correo electrónico nuestras fichas técnicas..."*  |
| **Sala de exhibición**  | Sustantivo        | Showroom                          | *"...pasar por su sala de exhibición esta tarde..."*               |
| **Revisar los números** | Frase idiomática | To run through the numbers        | *"...para que podamos revisar los números en persona."*            |
| **Concesionario**        | Sustantivo        | Dealership                        | *"Sé exactamente dónde queda su concesionario..."*                |

---

## 2. Guión Interactivo

Haz clic en **"Ver traducción"** debajo de cada intervención para comprobar tu comprensión auditiva y lectora.

**Maureen Simmons (Summit Commercial Fleet Group):**

> "Buenos días, Summit Commercial Fleet Group, habla Maureen. ¿En qué le puedo ayudar?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Good morning, Summit Commercial Fleet Group. Maureen speaking. How can I help you?</em>
</details>

<br>

**Sr. Lewis (Cascade Technologies):**

> "Buenos días. Mi nombre es Alan Lewis. Acabo de ver su anuncio sobre las camionetas de carga Ford Transit 250 disponibles con precios para flotillas comerciales. Desde hace un tiempo hemos estado buscando adquirir media docena de vehículos de servicio a un buen precio, y su oferta nos llamó la atención."

<details>
<summary>🔍 Ver traducción</summary>
<em>Good morning. My name is Alan Lewis. I just saw your ad for the Ford Transit 250 cargo vans available with commercial fleet pricing. We’ve been looking to pick up a half-dozen service vehicles at the right price for a while now, and your offer caught our eye.</em>
</details>

<br>

**Maureen Simmons:**

> "Excelente. ¿Le gustaría que le envíe por correo electrónico nuestras fichas técnicas y paquetes de financiamiento?"

<details>
<summary>🔍 Ver traducción</summary>
<em>Wonderful. Would you like me to email you our spec sheets and financing packages?</em>
</details>

<br>

**Sr. Lewis:**

> "No, gracias. En realidad preferiría pasar por su sala de exhibición esta tarde con un compañero de trabajo para que podamos revisar los números en persona."

<details>
<summary>🔍 Ver traducción</summary>
<em>No, thank you. I’d actually prefer to head over to your showroom this afternoon with a coworker so we can run through the numbers in person.</em>
</details>

<br>

**Maureen Simmons:**

> "No hay ningún problema, señor. Mi nombre es Maureen Simmons y estaré disponible a partir de las 2:30 p. m. ¿Podría confirmarme su nombre completo y el de su empresa, por favor?"

<details>
<summary>🔍 Ver traducción</summary>
<em>No problem at all, sir. My name is Maureen Simmons, and I’ll be available starting at 2:30 PM. Could you confirm your full name and company name for me, please?</em>
</details>

<br>

**Sr. Lewis:**

> "Por supuesto. Es Alan Lewis, de Cascade Technologies. Sé exactamente dónde queda su concesionario, así que nos vemos a las 2:30. Gracias, hasta luego."

<details>
<summary>🔍 Ver traducción</summary>
<em>Of course. It’s Alan Lewis with Cascade Technologies. I know right where your dealership is located, so we’ll see you at 2:30. Thanks, bye.</em>
</details>

<br>

**Maureen Simmons:**

> "¡Me parece muy bien, Sr. Lewis! ¡Será un gusto conocerlo entonces"

<details>
<summary>🔍 Ver traducción</summary>
<em>Sounds great, Mr. Lewis. Looking forward to meeting you then!</em>
</details>

---

## 3. Extracción de Información Clave

Intenta responder las siguientes preguntas de memoria antes de desplegar la solución:

1. **¿Quién llama y a qué empresa representa?**

<details>
<summary>Mostrar respuesta</summary>
Alan Lewis, de <strong>Cascade Technologies</strong>.
</details>

2. **¿Con quién se comunica y qué empresa atiende la llamada?**

<details>
<summary>Mostrar respuesta</summary>
Maureen Simmons, de <strong>Summit Commercial Fleet Group</strong>.
</details>

3. **¿Cuál es el motivo exacto de la llamada?**

<details>
<summary>Mostrar respuesta</summary>
Interés en adquirir media docena (6) de camionetas de carga Ford Transit 250 con precio de flotilla comercial.
</details>

4. **¿Acepta el cliente recibir las especificaciones por correo electrónico?**

<details>
<summary>Mostrar respuesta</summary>
No. Prefiere acudir en persona con un colega a la sala de exhibición para revisar los números.
</details>

5. **¿A qué hora y dónde se pactó el encuentro?**

<details>
<summary>Mostrar respuesta</summary>
A las <strong>2:30 p. m.</strong> en el concesionario de Summit Commercial Fleet Group.
</details>

---

<!-- Spacer to prevent the fixed bottom bar from covering content when scrolling -->

<div style="height: 80px;"></div>
