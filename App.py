import flet as ft
import Modules.llm as llm
import json

jsonContent = {
  "title": "SAP ist cool!",
  "student": "Patrick",
  "firma": "SIT",
  "gliederung": ["Einleitung", "Was ist SAP?", "Geschichte", "HANA", "UI5", "Meins Meinung"]
}
bachelorTestJson = json.dumps(jsonContent)

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    llmText = ft.Text(value="", text_align=ft.TextAlign.CENTER, width=500)

    def getLlmModel(e):
        llmText.value = llm.analyzeJson(bachelorTestJson)
        page.update()

    page.add(
        llmText,
        ft.IconButton(ft.icons.SEARCH_ROUNDED, on_click=getLlmModel)
    )

ft.app(main)