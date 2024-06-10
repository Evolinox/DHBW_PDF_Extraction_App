import json
import flet as ft
import Modules.llm as llm
import Modules.extractor as extractor
import Modules.exporter as exporter

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 540
    page.window_resizable = False

    def onFilePicked(e: ft.FilePickerResultEvent):
        global dataLocation
        global isDirectory
        if e.files:
            selectedFileOrDirectory.value = e.files[0].name
            dataLocation = e.files[0].name
            isDirectory = False
            print(e.files[0].name)
        elif e.path:
            selectedFileOrDirectory.value = e.path
            dataLocation = e.path
            isDirectory = True
            print(e.path)
        page.update()

    def updateFilter(e):
        activeFilter[e.key] = {filterList[e.key]: e.value}

    def analyzeData(e):
        global dataLocation
        global isDirectory
        global extractionData

        if (isDirectory):
            return
        else:
            extractionData = extractor.runExtraction(dataLocation)
            jsonData = json.loads(extractionData)
            resultRowText.value = "Ergebnisse:"
            fileTitle.value = "Titel: " + jsonData['title']
            fileAuthor.value = "Student: " + jsonData['student']
            fileMatNr.value = "Matrikelnummer: " + jsonData['matNr']
            fileCompany.value = "Firma: " + jsonData['firma']
            filePages.value = "Seitenanzahl: " + str(jsonData['totalPages'])

        page.update()

    def exportCsvFile(e):
        global extractionData
        page.dialog = csvInfoDialog
        csvInfoDialog.open = True
        page.update()
        exporter.createCsvFromJson(extractionData)

    # Text Objects
    selectedFileOrDirectory = ft.Text(value="keine Datei ausgewhält...", text_align=ft.TextAlign.LEFT, italic=True)
    fileUploaderText = ft.Text(value="Wähle eine Datei oder einen Ordner:", text_align=ft.TextAlign.LEFT, size=20, width=500)
    filterRowText = ft.Text(value="Wähle Filter aus:", text_align=ft.TextAlign.LEFT, size=20, width=500)
    resultRowText = ft.Text(value="", text_align=ft.TextAlign.LEFT, size=20, width=500)
    fileTitle = ft.Text(value="", width=500)
    fileAuthor = ft.Text(value="", width=500)
    fileMatNr = ft.Text(value="", width=500)
    fileCompany = ft.Text(value="", width=500)
    filePages = ft.Text(value="", width=500)

    # Toast
    csvInfoDialog = ft.AlertDialog(
        title=ft.Text("CSV successfully exported!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    # Filters
    filterList = ["Titel", "Name", "Matrikelnummer", "Seitenanzahl"]
    filtersChecked = []
    activeFilter = []

    for item in filterList:
        filter = {item: False}
        activeFilter.append(filter)

    i = 0
    for item in filterList:
        filter = {"key": i, "label": item}
        filtersChecked.append(filter)
        i += 1

    # File Picker
    pickFilesDialog = ft.FilePicker(on_result = onFilePicked)
    page.overlay.append(pickFilesDialog)

    # Upload Button
    fileUploaderButton = ft.ElevatedButton("Auswählen",
        icon = ft.icons.UPLOAD_FILE,
        on_click = lambda f: pickFilesDialog.pick_files(allow_multiple=False, allowed_extensions=["pdf"]))

    # Homepage Layout
    fileUploaderRow = ft.Column(
        [
            fileUploaderText,
            ft.Row(
                [
                    fileUploaderButton,
                    selectedFileOrDirectory
                ]
            )
        ]
    )

    filterRow = ft.Column(
        [
            filterRowText,
            ft.Row(
                [
                    *[ft.Checkbox(key=item['key'],
                        label=item['label'],
                        value=False,
                        on_change=lambda e: updateFilter(e.control))
                        for item in filtersChecked]
                ]
            )
        ]
    )

    analyzedDataRow = ft.Container(
        content = ft.Column(
            [
                resultRowText,
                fileTitle,
                fileAuthor,
                fileMatNr,
                fileCompany,
                filePages
            ]
        ),
        height=200,
        width=500
    )
    
    buttonRow = ft.Row(
        [
            ft.ElevatedButton("CSV-Datei exportieren",
                icon=ft.icons.IMPORT_EXPORT,
                on_click = exportCsvFile),
            ft.ElevatedButton("Datei/en analysieren",
                icon=ft.icons.SEARCH_ROUNDED,
                on_click = analyzeData)
        ]
    )

    def createHomePage():
        page.clean()
        page.add(
            fileUploaderRow,
            ft.Divider(),
            filterRow,
            ft.Divider(),
            analyzedDataRow,
            ft.Divider(),
            buttonRow
        )

    createHomePage()

ft.app(main)