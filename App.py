import flet as ft

def main(page: ft.Page):
    page.title = "PDF Extraction App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # functions
        # File Picker
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Abgebrochen!"
        )
        # Get file location
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


        # Modus Wahl
    uploadText = ft.Text("Laden Sie eine Datei hoch:")
    uploadTextButton = "Datei auswählen" # default text for button
    uploadButton = ft.ElevatedButton("Datei auswählen",
    icon=ft.icons.UPLOAD_FILE,
    on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["pdf"]))

    def radiogroup_changed(e):
        modus = e.control.value
        print(f"neuer Modus: {modus}")
        if modus == "Datei":
            uploadText.value = "Laden Sie eine Datei hoch:"
            uploadButton.text = "Datei auswählen"
            selected_files.value = ""
            uploadButton.on_click = lambda _: pick_files_dialog.pick_files(allow_multiple=False, allowed_extensions=["pdf"])
        else:
            uploadText.value = "Laden Sie ein Verzeichnis hoch:"
            uploadButton.text = "Verzeichnis auswählen"
            selected_files.value = ""
            uploadButton.on_click = lambda _: pick_folder_dialog.get_directory_path()
        page.update()
    
    def filterUpdate(e):
        # print(f"Filter {e.key} changed to {e.value}")
        activFilter[e.key] = {filterList[e.key]: e.value}
        print(f"Filter aktives: {activFilter}")

    # precreate scopable variables
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    pick_folder_dialog = ft.FilePicker(on_result=pick_folder_result)
    page.overlay.append(pick_files_dialog)
    page.overlay.append(pick_folder_dialog)

    selected_files = ft.Text()

    filterText = ft.Text()
    
    modusWahl = ft.RadioGroup(value="Datei", content=ft.Column([
        ft.Radio(value="Datei", label="Datei"),
        ft.Radio(value="Ordner", label="Ordner")]), on_change=radiogroup_changed)
    
    # Filter Wahl
    filterList = ["Titel", "Name", "Seitenanzahl", "Abbildungsverzeichnis"]
    filterCheckboxList = []
    activFilter = []
    file_location = ""

    # create activFilter list with all filters set to "False"
    for item in filterList:
        filterCheckbox = {item: False}
        activFilter.append(filterCheckbox)
    print(f"aktiv Filter: {activFilter}")

    # create all Checkboxes into filterCheckboxList
    i = 0
    for item in filterList:
        filterCheckbox = {"key": i, "label": item}
        filterCheckboxList.append(filterCheckbox)
        print(f"Filter {i}: {item}")
        i += 1

    print(f" filterCheckboxList: {filterCheckboxList}")
    
    # Button Analyse
    def analysieren(e):
        global file_location
        if (modusWahl.value == "Datei"):
            print("Analyse Datei...")
        else:
            print("Analyse Ordner...")
        print(f"Analyse Modus: {modusWahl.value}")
        datei = selected_files.value
        print(f"Dateipfad: {file_location}")

        i = 0
        for item in activFilter:
            key = filterList[i]
            if item[key] == True:
                print(f"{key}: active")
            else:
                print(f"{key}: inactive")
            i += 1
    
    page.add(
        ft.Row(
            [
                # Modus Wahl
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
            ft.CrossAxisAlignment.START,
        ),
        ft.Row(
            [
                ft.Text("Filter wählen: "),
                *[ft.Checkbox(key=item['key'], 
                    label=item['label'], 
                    value=False, 
                    on_change=lambda e: filterUpdate(e.control)) 
                    for item in filterCheckboxList],
                filterText,
            ],
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="Analysieren", on_click=analysieren),
            ],
            ft.MainAxisAlignment.END,
        )
    )

ft.app(main)