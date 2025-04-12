import flet as ft

def main(pagina):
    titulo=ft.Text("Oi Napô")
    pagina.add(titulo)


ft.app(main,view=ft.WEB_BROWSER)