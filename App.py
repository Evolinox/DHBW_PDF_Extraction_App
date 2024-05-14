import flet as ft
import Modules.llm as llm

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    llmText = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=500)

    def getLlmModel(e):
        llmText.value = llm.analyzeJson('Hey')

    page.add(
        llmText,
        ft.IconButton(ft.icons.AIRPLAY_ROUNDED, on_click=getLlmModel)
    )

ft.app(main)