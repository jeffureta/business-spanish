import asyncio
import edge_tts

dialogue = [
    (
        "es-ES-ElviraNeural",
        "Keystone Lumber & Supply, habla Tracy. ¿A dónde desea que dirija su llamada?",
    ),
    (
        "es-ES-AlvaroNeural",
        "Buenos días. Quisiera hacer un pedido de madera contrachapada, por favor.",
    ),
    (
        "es-ES-ElviraNeural",
        "Con gusto, señor. Permítame transferirlo a nuestro Departamento de Maderas.",
    ),
    (
        "es-MX-JorgeNeural",
        "Departamento de Maderas, le habla Dave. ¿En qué le puedo ayudar hoy?",
    ),
    (
        "es-ES-AlvaroNeural",
        "Hola, Dave. Busco ordenar una cantidad bastante grande de madera contrachapada.",
    ),
    (
        "es-MX-JorgeNeural",
        "Por supuesto, señor. ¿Sabe qué grado necesita, o podría decirme qué va a construir?",
    ),
    (
        "es-ES-AlvaroNeural",
        "Es para estanterías comerciales, así que la madera debe ser lo suficientemente resistente para soportar colecciones pesadas de libros.",
    ),
    (
        "es-MX-JorgeNeural",
        "Entendido. Para ese tipo de carga, le recomendaría madera contrachapada de tres cuartos de pulgada para ebanistería, en láminas estándar de cuatro por ocho pies. ¿Cuántas láminas necesita?",
    ),
    (
        "es-ES-AlvaroNeural",
        "Necesitaré cuarenta láminas. ¿Ofrecen algún descuento por volumen para un pedido de ese tamaño?",
    ),
    (
        "es-MX-JorgeNeural",
        "Claro que sí. Ofrecemos descuentos escalonados para contratistas a partir de veinticinco láminas.",
    ),
    (
        "es-ES-AlvaroNeural",
        "Excelente. Le daré mi dirección de entrega para que me indique cuál sería la fecha de entrega más próxima y cuáles son las condiciones de facturación y pago.",
    ),
    (
        "es-MX-JorgeNeural",
        "Perfecto. En cuanto tenga a mano la dirección del lugar de entrega, lo incluiremos en el calendario de distribución y abriremos su cuenta.",
    ),
]


async def generate_line(voice: str, text: str, retries: int = 3):
    """Fetch audio chunks with automatic retry on dropped connections."""
    for attempt in range(1, retries + 1):
        try:
            audio_data = bytearray()
            communicate = edge_tts.Communicate(text, voice)
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_data.extend(chunk["data"])
            if audio_data:
                return audio_data
        except Exception as e:
            if attempt == retries:
                raise e
            await asyncio.sleep(2.0 * attempt)
    raise edge_tts.exceptions.NoAudioReceived(
        f"Failed to receive audio for voice '{voice}' after retries."
    )


async def generate_dialogue():
    output_filename = "escena_3.mp3"
    print(
        f"Iniciando generación de audio ({len(dialogue)} líneas de diálogo)..."
    )

    with open(output_filename, "wb") as outfile:
        for idx, (voice, text) in enumerate(dialogue, start=1):
            print(f"[{idx}/{len(dialogue)}] Procesando: {voice}...")
            audio_chunk = await generate_line(voice, text)
            outfile.write(audio_chunk)
            await asyncio.sleep(1.0)

    print(f"\nArchivo guardado con éxito: '{output_filename}'")


if __name__ == "__main__":
    asyncio.run(generate_dialogue())