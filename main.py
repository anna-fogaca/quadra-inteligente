import sqlite3
# import tinker
# -------------------- LÓGICA DO DATABASE
conn = sqlite3.connect('quadra.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        placar_visitante INT,
        placar_casa INT,
        quantidade_luz INT,
        horario TIME
        dia_noite VARCHAR(50)
);
""")

conn.close()
# ---------------------- LÓGICA DO PYTHON ------------------------------------
print("SISTEMA DA QUADRA INTELIGENTE")
print("MENU - O QUE VOCÊ DESEJA? ")
opcao = input("1. PLACAR / 2. MARCAR HORÁRIO / 3. VERIFICAR QUANTIDADE DE LUZ: ")

if opcao == 1:
    # logica do placar
    print("")
elif opcao == 2:
    #logica de marcar horario
    print("")
elif opcao == 3:
    # verificar quantidade
    print("")

