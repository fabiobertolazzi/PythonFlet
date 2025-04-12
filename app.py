import flet as ft
import sqlite3 as sql
import time

def main(pagina):
    titulo=ft.Text("Oi Napô")
    pagina.add(titulo)

    conn = sql.connect('banco.db')
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')
    conn.execute("INSERT INTO usuarios ( nome, idade) VALUES ('João',25)")
    conn.execute("INSERT INTO usuarios ( nome, idade) VALUES ('Fabio',49)")
    conn.execute("INSERT INTO usuarios ( nome, idade) VALUES ('Pedro',30)")
    conn.execute("INSERT INTO usuarios ( nome, idade) VALUES ('Carlos',27)")
    conn.execute("INSERT INTO usuarios ( nome, idade) VALUES ('Julia',16)")

    consulta = conn.execute("SELECT * FROM usuarios")

    for row in consulta:
        pagina.add(ft.Text(row))
        #print(row)

    # t = ft.Text()
    # pagina.add(t)
    # cidades = ["Belo Horizonte","Curitiba","São Paulo","Salvador","** fim **"]
    # for i in range(5):
    #     t.value = cidades[i]
    #     pagina.update()
    #     time.sleep(1)






ft.app(main,view=ft.WEB_BROWSER)