
import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("oes.db")

with sqlite3.connect(DB) as con:
    con.execute("""
        INSERT OR IGNORE INTO noticias
        (titulo, institucion, categoria, fuente, fecha, url, resumen)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        "SUNEDU realiza supervisión diagnóstica en la Universidad Nacional Autónoma de Tayacaja ante la amenaza del fenómeno El Niño",
        "SUNEDU",
        "Ente rector",
        "Portal oficial de SUNEDU",
        "2026-11-05",
        "https://www.gob.pe/institucion/sunedu/noticias/1470459-sunedu-realiza-supervision-diagnostica-en-la-universidad-nacional-autonoma-de-tayacaja-ante-la-amenaza-del-fenomeno-el-nino",
        "Noticia sobre una supervisión diagnóstica de SUNEDU en la Universidad Nacional Autónoma de Tayacaja ante la amenaza del fenómeno El Niño. Resumen provisional basado en el título."
    ))

print("Noticia registrada correctamente")
