import tkinter as tk
import tkintermapview
from tkinter import ttk
import json
from ubicaciones import Ubicacion

def left_click_event(coordinates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)
    
root = tk.Tk()

root.title("Comida Rapida")
root.geometry("600x500")
root.iconbitmap('icon-principal.ico')

frame_mapa = ttk.Frame(root)
frame_mapa.grid(row=0,column=0)
frame_lista = ttk.Frame(root)
frame_lista.grid(row=0,column=1)
# create map widget
map_widget = tkintermapview.TkinterMapView(frame_mapa, width=800, height=600, corner_radius=0)
map_widget.set_position(-24.781101151703105, -65.42685626078968)  # Paris, France
map_widget.set_zoom(13)
map_widget.add_left_click_map_command(left_click_event)
map_widget.pack()

#lista ubicaciones
lista_ubicaciones = tk.Listbox(frame_lista)
lista_ubicaciones.pack()

with open('Ubicacion.json','r') as file:
    datas = json.load(file)

for data in datas:
    ubicacion = Ubicacion.from_json(data)
    map_widget.set_marker(ubicacion.coordenadas[0],ubicacion.coordenadas[1], text=ubicacion.nombre)
    lista_ubicaciones.insert(tk.END,ubicacion.nombre)

with open('Eventos.json','r') as file:
    datas = json.load(file)

for data in datas:
    lista_ubicaciones.insert(tk.END,ubicacion.nombre)

root.mainloop()


    
