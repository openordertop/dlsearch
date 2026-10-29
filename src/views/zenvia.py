from flet import (
    View, AppBar,
    Container, Row, Column, ResponsiveRow,
    ScrollMode, ScrollMode,
    Clipboard, SharedPreferences, Share, value,
)
from components import ZenviaCopyContainer
from asyncio import create_task
from typing import Any

class ZenviaView(View):
    def __init__(self) -> None:
        super().__init__()
        self.prefs = SharedPreferences()
        self.name = ""
        self.route = "/zenvia"
        self.appbar = AppBar(
            title="Zenvia",
        )
        self.expand = True
        self.controls = [
            ResponsiveRow(
                controls=[
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "Hola, se me asignó tu conversación, a tus órdenes ¿En qué puedo ayudarte?",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "Hola, se me asignó tu conversación, a tus órdenes ¿En qué puedo ayudarte?",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "¿Qué productos necesitas que te cotice?",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "¿Tienes algún presupuesto para esta compra?",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "¿Le puedo ofrecer alguna recomendación?",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = """
Para avanzar con su cotización, me podría proporcionar los siguientes datos por favor:
 • Nombre(s), Apellido Materno y Paterno:
 • Correo Electrónico:
 • Número de teléfono Celular:
 • Domicilio (en caso de que requiera envío a domicilio):
 - Calle y número exterior
 - Número interior (en caso de ser necesario)
 - Colonia
 - Código postal
 - Referencias""",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "Para mantenimiento o servicio es directo en la sucursal de Chapalita y Plaza del Sol ahí se encuentra nuestro departamento de servicio técnico o puedes comunicarte al teléfono 3336300660 Ext. 4",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = """
Le comparto la documentación que se le solicitará para poder continuar con el proceso de su pedido una vez haya realizado su pago vía PayPal:
 - Foto de identificación oficial vigente y legible por ambos lados del titular de la tarjeta y/o cuenta de PAY PAL con la que se realizó la compra (IFE/INE o Pasaporte)
 - Foto de la tarjeta de Crédito/Débito utilizada en la compra, donde únicamente sean visibles los últimos cuatro dígitos del número de tarjeta (En caso de ser virtual, una captura de pantalla de la tarjeta virtual donde sean visibles los últimos cuatro dígitos), o la caratula de un estado de cuenta reciente de la tarjeta con la que se realizó la compra. 
 - Comprobante del domicilio de envío (Solo en caso de que la dirección de su INE no coincida con el domicilio de envío)
Es de vital importancia que recibamos los documentos solicitados tan pronto sea posible para continuar con su compra, las imágenes deben ser legibles y enviadas como respuesta al correo que recibió por parte de ventas.internet@digitalife.com.mx. También es importante mencionar que el plazo de entrega (2 a 8 días hábiles) comenzará a partir de haber recibido los documentos solicitados.
 "Te informamos que tus datos personales están protegidos según la Ley General de Protección de Datos Personales"
Le invitamos a que visitar nuestro Aviso de privacidad.""",
                    ),
                    ZenviaCopyContainer(
                        text = "Primer Contacto",
                        value = "Buen día, me comunico con usted para darle seguimiento a su pedido",
                    ),
                ],
                scroll = ScrollMode.AUTO,
                expand=True,
            ),
        ]

    def did_mount(self) -> None:
        create_task(self.get_clipboard())

    def will_unmount(self) -> None:
        pass

    async def get_clipboard(self) -> None:
        if await self.prefs.contains_key("name"):
            self.name: Any = await self.prefs.get("name")
        else:
            await self.prefs.set("name", "nombre")
        print(await self.prefs.get("name"))
