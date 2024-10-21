import flet as ft
import os

# Cabecera con el logo e imagen de texto (texto o imagen)
logo = ft.Image(src=os.path.abspath("logo.png"), width=300)
header_text = ft.Text("Bienvenido a la app de lista de compras", size=20)

# Lista global para almacenar las tareas
tasks = []
selected_task = None  # Variable para almacenar la tarea seleccionada

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista de Compras"

    # Agregar el header a la parte superior de la página
    page.add(header)

    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)

    # botones de "Agregar", "Modificar" y "Eliminar"
    add_button = ft.ElevatedButton("Agregar", on_click=lambda e: add_clicked(e, new_task, page))
    modify_button = ft.ElevatedButton("Modificar", on_click=lambda e: modify_clicked(e, new_task))
    delete_button = ft.ElevatedButton("Eliminar", on_click=lambda e: delete_clicked(e, page))

    # Agregar los botones a la página en una fila
    page.add(ft.Row([new_task, add_button, modify_button, delete_button]))

def add_clicked(e, new_task, page):
    """Función para agregar o modificar una tarea."""
    global selected_task

    if selected_task:
        # Si hay una tarea seleccionada, modificar su texto
        selected_task.label = new_task.value  # Cambiar el texto del checkbox
        selected_task.update()  # Actualizar el checkbox
        selected_task = None  # Deseleccionar la tarea después de modificar
    else:
        # Si no hay tarea seleccionada, se agrega una nueva tarea
        new_task_value = new_task.value
        if new_task_value:
            # Crear una nueva tarea como un checkbox
            checkbox = ft.Checkbox(label=new_task_value, value=False)
            tasks.append(checkbox)  # Añadir a la lista de tareas
            page.add(checkbox)  # Añadir el checkbox a la página

    # Limpiar y actualizar el campo de texto después de agregar/modificar
    new_task.value = ""
    new_task.update()

def modify_clicked(e, new_task):
    """Función para seleccionar una tarea y copiar su texto al campo de texto."""
    global selected_task

    # Buscar la tarea seleccionada (marcada)
    for task in tasks:
        if task.value:  # Si el checkbox está marcado
            selected_task = task  # Guardar la tarea seleccionada
            new_task.value = task.label  # Copiar el texto de la tarea al campo de texto
            new_task.update()  # Actualizar el campo de texto
            break

def delete_clicked(e, page):
    """Función para eliminar tareas seleccionadas."""
    global selected_task
    tasks_to_remove = [task for task in tasks if task.value]
    for task in tasks_to_remove:
        page.controls.remove(task)  # Eliminar de la página
        tasks.remove(task)  # Eliminar de la lista global
    page.update()  # Actualizar la página después de eliminar

    selected_task = None  # Deseleccionar la tarea si es eliminada

# Se organiza la cabecera en una columna
header = ft.Column(
    [
        logo,
        header_text
    ],
    alignment=ft.MainAxisAlignment.CENTER,  # Centra verticalmente
    horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centra horizontalmente
)

# Ejecutar la aplicación
ft.app(main)