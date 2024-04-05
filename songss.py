import flet as ft

song1 = "https://github.com/karlaaariass/music/blob/main/Las%20Avispas.mp3?raw=true"
song2 = "https://github.com/karlaaariass/music/blob/main/Juan%20Luis%20Guerra%204.40%20-%20Vale%20la%20Pena%20(Live)%20(Video%20Oficial).mp3?raw=true"
song3 = "https://github.com/karlaaariass/music/blob/main/Juan%20Luis%20Guerra%204.40%20-%20Todo%20Tiene%20Su%20Hora.mp3?raw=true"
song4 = "https://github.com/karlaaariass/music/blob/main/Juan%20Luis%20Guerra%204.40%20-%20Mambo%2023%20(Video%20Oficial).mp3?raw=true"
song5 = "https://github.com/karlaaariass/music/blob/main/Juan%20Luis%20Guerra%204.40%20-%20El%20Niágara%20en%20Bicicleta%20(Live)%20(Audio%20Oficial).mp3?raw=true"

def main(page: ft.Page):
    page.title = "Music Player"

    las_avispas = ft.Audio(
        src=song1,
        autoplay=False,
    )
    page.overlay.append(las_avispas)

    vale_la_pena = ft.Audio(
        src=song2,
        autoplay=False,
    )
    page.overlay.append(vale_la_pena)

    todo_tiene_su_hora = ft.Audio(
        src=song3,
        autoplay=False,
    )
    page.overlay.append(todo_tiene_su_hora)

    mambo_23 = ft.Audio(
        src=song4,
        autoplay=False,
    )
    page.overlay.append(mambo_23)

    el_niagara_en_bicicleta = ft.Audio(
        src=song5,
        autoplay=False,
    )
    page.overlay.append(el_niagara_en_bicicleta) 

    def yes_click(e):
        page.window_destroy()  

    page.add(
        ft.ElevatedButton("Las Avispas", on_click=lambda _: las_avispas.play()),
        ft.ElevatedButton("Vale la Pena", on_click=lambda _: vale_la_pena.play()),
        ft.ElevatedButton("Todo Tiene su Hora", on_click=lambda _: todo_tiene_su_hora.play()),
        ft.ElevatedButton("Mambo 23", on_click=lambda _: mambo_23.play()),
        ft.ElevatedButton("El Niagara en Bicicleta", on_click=lambda _: el_niagara_en_bicicleta.play()),
        ft.ElevatedButton("Exit", color="red", on_click=yes_click)
    )

ft.app(target=main)
