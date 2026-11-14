import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("oes.db")

with sqlite3.connect(DB) as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS noticias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            institucion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            fuente TEXT NOT NULL,
            fecha TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            resumen TEXT NOT NULL
        )
    """)

    datos = [
        ("Ejemplo: convocatoria de becas", "PRONABEC", "Ente rector",
         "Portal institucional (ejemplo)", "2026-11-06",
         "https://www.pronabec.gob.pe/",
         "Registro didáctico: verificar nota original."),

        ("Ejemplo: actividad de investigación", "UNMSM", "Universidad pública",
         "Portal institucional (ejemplo)", "2026-11-06",
         "https://www.unmsm.edu.pe/",
         "Registro didáctico: verificar noticia original."),

        ("Ejemplo: programa académico", "PUCP", "Universidad privada",
         "Portal institucional (ejemplo)", "2026-11-05",
         "https://www.pucp.edu.pe/",
         "Registro didáctico: verificar noticia original.")
    ]

    con.executemany("""
        INSERT OR IGNORE INTO noticias
        (titulo, institucion, categoria, fuente, fecha, url, resumen)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, datos)

print("Base creada:", DB)