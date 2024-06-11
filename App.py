import flet as ft
import json
import Modules.llm as llm
import Modules.extractor as extractor
import Modules.exporter as exporter

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # vvvvvv----------------------fill with real filters
    filterList = ["Titel", "Autor", "Seitenanzahl", "Firma", "Matrikelnummer"]
    # ^^^^^^----------------------fill with real filters
    filterCheckboxList = []
    activFilter = []
    # vvvvvv----------------------fill by backend
    resultList = [{"Title": "Test"}, {"Autor": "Test"}, {"Seitenanzahl": 10}, {"Firma": "Musterfirma"}, {"Matrikelnummer": 1234567}]
    # ^^^^^^----------------------fill by backend

    uploadText = ft.Text("Laden Sie eine Datei hoch:")
    uploadButton = ft.ElevatedButton("Datei auswählen",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["pdf"]))
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Abgebrochen!"
        )
        if e.files:
            global file_location 
            file_location = r"{}".format(e.files[0].path)
            print(f"File Location: {file_location}")
        selected_files.update()

    def pick_folder_result(e: ft.FilePickerResultEvent):
        selected_files.value = e.path if e.path else "Abgebrochen!"
        if e.path:
            global file_location
            file_location = r"{}".format(e.path)
            print(f"File Location: {file_location}")
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    pick_folder_dialog = ft.FilePicker(on_result=pick_folder_result)
    page.overlay.append(pick_files_dialog)
    page.overlay.append(pick_folder_dialog)

    selected_files = ft.Text()
    filterText = ft.Text()
    
    def mode_changed(e):
        modus = e.control.value
        print(f"neuer Modus: {modus}")
        global file_location
        if modus == "Datei":
            uploadText.value = "Laden Sie eine Datei hoch:"
            uploadButton.text = "Datei auswählen"
            selected_files.value = ""
            file_location = ""
            uploadButton.on_click = lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["pdf"])
        else:
            uploadText.value = "Laden Sie ein Verzeichnis hoch:"
            uploadButton.text = "Verzeichnis auswählen"
            selected_files.value = ""
            file_location = ""
            uploadButton.on_click = lambda _: pick_folder_dialog.get_directory_path()
    llmText = ft.Text(value="", text_align=ft.TextAlign.CENTER, width=500)

    modusWahl = ft.RadioGroup(value="Datei", content=ft.Column([
        ft.Radio(value="Datei", label="Datei"),
        ft.Radio(value="Ordner", label="Ordner")]), on_change=mode_changed)
    for item in filterList:
        filterCheckbox = {item: False}
        activFilter.append(filterCheckbox)

    i = 0
    for item in filterList:
        filterCheckbox = {"key": i, "label": item}
        filterCheckboxList.append(filterCheckbox)
        i += 1
    
    def filterUpdate(e):
        activFilter[e.key] = {filterList[e.key]: e.value}

    def analysieren(e):
        global file_location
        if (modusWahl.value == "Datei"):
            isFolder = False
            print("Analyse Datei...")
        else:
            isFolder = True
            print("Analyse Ordner...")
        print(f"Dateipfad: {file_location}")

        i = 0
        for item in activFilter:
            key = filterList[i]
            if item[key] == True:
                print(f"{key}: active")
            else:
                print(f"{key}: inactive")
            i += 1
        print("Filter: "+ str(activFilter))

        getTitle = bool(activFilter[0].get('Titel'))
        getAuthor = bool(activFilter[1].get('Autor'))
        getNumberOfPages = bool(activFilter[2].get('Seitenanzahl'))
        getCompany = bool(activFilter[3].get('Firma'))
        getMatNr = bool(activFilter[4].get('Matrikelnummer'))

        global objektJson
        objektJson = extractor.recieve(isFolder, file_location, getTitle, getAuthor, getNumberOfPages, getCompany, getMatNr)
        jsonData = objektJson['data'][0]
        print(jsonData)
        global resultList
        resultList = [{"Title": jsonData['title']}, {"Autor": jsonData['student']}, {"Seitenanzahl": jsonData['totalPages']}, {"Firma": jsonData['firma']}, {"Matrikelnummer": jsonData['matNr']}]
        print("Analyse beendet!")
        print(resultList)
        renderResultPage()
    
    mainPageList = []
    mainPageFistRow = ft.Row(
        [
            ft.Column( 
                [
                    ft.Text("Wählen Sie aus, was Sie analysieren wollen: "),
                    modusWahl,
                ],
                ft.MainAxisAlignment.CENTER,
            ),
            ft.Column(
                [
                    uploadText,
                    uploadButton,
                    selected_files,
                ],
                ft.MainAxisAlignment.CENTER,
            ),
        ],
        ft.MainAxisAlignment.SPACE_EVENLY,
        ft.CrossAxisAlignment.CENTER,
    )
    mainPageList.append(mainPageFistRow)

    mainPageSecondRow = ft.Container(
        ft.Row(
            [
                ft.Text("Filter wählen: ")
            ]
        ),
        padding = ft.padding.only(left=8),
    )
    mainPageList.append(mainPageSecondRow)

    mainPageThirdRow = ft.Row(
        [
            *[ft.Checkbox(key=item['key'],
                label=item['label'],
                value=False,
                on_change=lambda e: filterUpdate(e.control))
                for item in filterCheckboxList],
            filterText,
        ],
    )
    mainPageList.append(mainPageThirdRow)

    mainPageFourthRow = ft.Row(
        [
            ft.ElevatedButton(text="Analysieren", on_click=analysieren),
        ],
        ft.MainAxisAlignment.END,
    )
    mainPageList.append(mainPageFourthRow)

    def renderMainPage():
        page.clean()
        for item in mainPageList:
            page.add(item)

    resultPageList = []
    resultPageFistRow = ft.Row(
        [
            ft.Text("Result Page")
        ],
        ft.MainAxisAlignment.CENTER,
        ft.CrossAxisAlignment.CENTER,
    )
    resultPageList.append(resultPageFistRow)

    resultPageSecondRow = ft.Row(
        [
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Filter")),
                    ft.DataColumn(ft.Text("Ergebnis")),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(key)),
                            ft.DataCell(ft.Text(str(value))),
                        ]
                    ) for item in resultList for key, value in item.items()
                ]
            ),
        ],
        ft.MainAxisAlignment.CENTER,
    )
    resultPageList.append(resultPageSecondRow)

    resultPageThirdRow = ft.Row(
        [   
            ft.ElevatedButton(text="Lade CSV", on_click=lambda _: exporter.createCsvFromJson(json.JSONDecoder.jsonObject)),
            ft.ElevatedButton(text="Neue Analyse", on_click=lambda _: renderMainPage()),
        ],
        ft.MainAxisAlignment.END,
    )
    resultPageList.append(resultPageThirdRow)

    def renderResultPage():
        page.clean()
        for item in resultPageList:
            page.add(item)

    renderMainPage()
ft.app(main)