import json

# Cargar reglas manuales y generadas
with open("C:\\Users\\luism\\OneDrive\\Documentos\\A. Tareas 7mo semestre\\Mat DIscretas\\ProyectoFinal\\codigo\\manual_rules.json") as manual_file, open("C:\\Users\\luism\\OneDrive\\Documentos\\A. Tareas 7mo semestre\\Mat DIscretas\\ProyectoFinal\\codigo\\generated_rules.json") as ai_file:
    manual_rules = json.load(manual_file)
    ai_rules = json.load(ai_file)

# Función para comparar reglas
def compare_rules(manual, ai):
    if manual == ai:
        return "Las reglas coinciden."
    else:
        manual_set = set(str(manual["productions"]))
        ai_set = set(str(ai["productions"]))
        return f"Diferencias encontradas: {manual_set ^ ai_set}"

# Resultado
print(compare_rules(manual_rules, ai_rules))
