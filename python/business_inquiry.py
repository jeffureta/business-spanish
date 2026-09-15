import asyncio
import edge_tts

dialogue = [
    ("es-ES-ElviraNeural", "Buenos días. Robinson’s Motors."),
    ("es-ES-AlvaroNeural", "Hola, me llamo Lewis. Acabo de ver su anuncio sobre los Riva 25s disponibles en condiciones de flota. Llevamos un tiempo buscando media docena de vehículos a un precio adecuado y su oferta nos interesa."),
    ("es-ES-ElviraNeural", "Muy bien. ¿Quiere que le envíe más información?"),
    ("es-ES-AlvaroNeural", "No, gracias. Prefiero pasarme por su sala de ventas esta tarde con un compañero para comentar el asunto con usted."),
    ("es-ES-ElviraNeural", "No hay problema, señor. Me llamo Maureen Simmons y estaré disponible a partir de las 14:30. ¿Podría repetirme su nombre y el de su empresa, por favor?"),
    ("es-ES-AlvaroNeural", "Por supuesto. Soy Alan Lewis, de Stafford Electronics. Sé dónde está su oficina, así que estaremos allí a las 14:30. Hasta entonces, adiós."),
    ("es-ES-ElviraNeural", "Gracias, hasta luego.")
]

async def generate_dialogue():
    with open("dialogo_espanol.mp3", "wb") as outfile:
        for voice, text in dialogue:
            communicate = edge_tts.Communicate(text, voice)
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    outfile.write(chunk["data"])
    print("MP3 generated successfully as 'dialogo_espanol.mp3'")

asyncio.run(generate_dialogue())