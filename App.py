from typing import Any
import flet as ft
class main:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        activPage = "main"
        activFilter = []
        file_location = ""
        analyseMode = "Datei"

    def main_page(page: ft.Page):
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
            filter.update()
        
        def filterUpdate(e):
            activFilter[e.key] = {filterList[e.key]: e.value}

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

        # create activFilter list with all filters set to "False"
        for item in filterList:
            filterCheckbox = {item: False}
            activFilter.append(filterCheckbox)

        # create all Checkboxes into filterCheckboxList
        i = 0
        for item in filterList:
            filterCheckbox = {"key": i, "label": item}
            filterCheckboxList.append(filterCheckbox)
            print(f"Filter {i}: {item}")
            i += 1
        
        print("filterCheckBoxList: "+str(filterCheckboxList))
        print("filterList: "+str(filterList))
        print("activFilter: "+str(activFilter))

        def resetFilter():
            for item in activFilter:
                key = filterList[i]
                item[key] = False
            print("Filter zurückgesetzt!")
            page.update()

        # Button Analyse
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
            print(activFilter)
            print("Analyse beendet!")
            # page.clean()
            # main.update_page("result")
            page.go(main.result_page.route)
            page.update()

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
                ft.CrossAxisAlignment.CENTER,
                width="1000px",
            ),
            ft.Row(
                [
                ft.Text("Filter wählen: "),
                ]
            ),
            ft.Row(
                [
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

    def result_page(page: ft.Page):
        page.title = "PDF Extraction App"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.add(
            ft.Text("Wählen Sie aus, was sie analysieren wollen: "),
        )
            # ft.Column( 
            #     [
            #     ],
            #     ft.MainAxisAlignment.CENTER,
            # )
            # ft.Text = "Ergebnis Page"
            # # page.vertical_alignment = ft.MainAxisAlignment.CENTER

            # # Add content to the page
            # container.add(ft.Text("Ergebnis der Analyse:"))

            # # Add a button to go back to the main page
            # backButton = ft.ElevatedButton("Zurück zur Hauptseite",
            #     on_click=lambda _: page.go('/'))
            # page.add(backButton)

    def update_page(mode):
        if mode == "main":
            main.app.delete()
            main.app = ft.app(main.main_page)
        else:
            main.app.delete()
            main.app = ft.app(main.result_page)

    app = ft.app(main_page)