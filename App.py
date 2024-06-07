import flet as ft

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # vvvvvv----------------------fill with real filters
    filterList = ["Titel", "Name", "Seitenanzahl", "Abbildungsverzeichnis"]
    # ^^^^^^----------------------fill with real filters
    filterCheckboxList = []
    activFilter = []
    # vvvvvv----------------------fill by backend
    resultList = [{"Title": "Test"}, {"Name": "Test"}, {"Seitenanzahl": 10}, {"Abbildungsverzeichnis": True}]
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
            file_location = e.files[0].path
            print(f"File Location: {file_location}")
        selected_files.update()

    def pick_folder_result(e: ft.FilePickerResultEvent):
        selected_files.value = e.path if e.path else "Abgebrochen!"
        if e.path:
            global file_location
            file_location = e.path
            print(f"File Location: {file_location}")
        selected_files.update()

    # precreate scopable variables
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
        page.update()
    modusWahl = ft.RadioGroup(value="Datei", content=ft.Column([
        ft.Radio(value="Datei", label="Datei"),
        ft.Radio(value="Ordner", label="Ordner")]), on_change=mode_changed)

    # create activFilter list with all filters set to "False"
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
            print("Analyse Datei...")
        else:
            print("Analyse Ordner...")
        print(f"Analyse Modus: {modusWahl.value}")
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
        print("Analyse beendet!")
        renderResultPage()
    # asdas
    mainPageList = []
    mainPageFistRow = ft.Row(
        [
            ft.Column( 
                [
                    ft.Text("Wählen Sie aus, was sie analysieren wollen: "),
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
        ft.MainAxisAlignment.CENTER,
        ft.CrossAxisAlignment.CENTER,
    )
    mainPageList.append(mainPageFistRow)

    mainPageSecondRow = ft.Row(
        [
            ft.Text("Filter wählen: "),
        ]
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