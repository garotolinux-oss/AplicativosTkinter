#importação
import flet as ft

#função principal
def main(page: ft.Page):
    page.title = "Flet Contador"    # nome do app
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # alinhamento vertical dos elementos

    #entrada
    input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    #funcoes
    def minus_click(e):
        input.value = str(int(input.value) - 1)

    def plus_click(e):
        input.value = str(int(input.value) + 1)

    #adicionar na página
    page.add(
        ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            controls=[ ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                      input,
                      ft.IconButton(ft.Icons.ADD, on_click=plus_click)
            ]
        )
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)