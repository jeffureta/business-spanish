import asyncio
import edge_tts

dialogue = [
    (
        "es-MX-JorgeNeural",
        "Midwest Wholesale Supply, habla Mike. ¿En qué le puedo ayudar?",
    ),
    (
        "es-ES-ElviraNeural",
        "Buenos días, Mike. Habla Sarah Wilson, de Valley Market. Disculpe la molestia, pero hubo un error en nuestro pedido de la semana. ¿Sería posible hacer un cambio por teléfono?",
    ),
    (
        "es-MX-JorgeNeural",
        "Claro que sí, no hay problema, señora Wilson, nada más que no lleve cosas frescas de pedido especial. ¿Tiene a la mano el número de pedido?",
    ),
    (
        "es-ES-ElviraNeural",
        "Sí, es el pedido SCC-231. Lo hicimos hace tres días y son puros productos secos empaquetados. Queremos cancelar los refrescos y los cereales, y cambiarlos por quince cajas de toallas de papel. ¿Se puede hacer el cambio?",
    ),
    (
        "es-MX-JorgeNeural",
        "Permítame checar el sistema... Muy bien, aquí tengo su pedido y la factura. Podemos hacer el cambio sin problema antes de que vengan a recogerlo mañana; le tengo lista la nota actualizada. ¿Van a pagar al recoger?",
    ),
    (
        "es-ES-ElviraNeural",
        "Sí, con cheque de la empresa, como siempre. Le agradezco mucho su ayuda. ¡Nos vemos mañana!",
    ),
    (
        "es-MX-JorgeNeural",
        "¡Con mucho gusto, señora Wilson! Aquí le tenemos todo listo para cuando lleguen. ¡Que le vaya muy bien!",
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
    output_filename = "escena_5.mp3"
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
