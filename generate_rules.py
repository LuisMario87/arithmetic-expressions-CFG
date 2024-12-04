import openai
import json

# Configura tu clave API de OpenAI
openai.api_key = "private API"

# Prompt para generar las reglas
prompt = """
Generate Context-Free Grammar rules for arithmetic expressions in JSON format:
{
  "productions": {
    "expr": ["expr + term", "expr - term", "term"],
    "term": ["term * factor", "term / factor", "factor"],
    "factor": ["( expr )", "number", "identifier"]
  }
}
"""

# Solicita las reglas a la API de OpenAI
response = openai.ChatCompletion.create(
    model="01-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for creating grammars."},
        {"role": "user", "content": prompt}
    ]
)

# Extrae y guarda el contenido de la respuesta
rules = response["choices"][0]["message"]["content"]

# Guarda las reglas generadas en un archivo JSON
with open("C:\\Users\\luism\\OneDrive\\Documentos\\A. Tareas 7mo semestre\\Mat DIscretas\\ProyectoFinal\\generated_rules.json", "w") as file:
    json.dump(json.loads(rules), file)

print("Reglas generadas y guardadas en 'generated_rules.json'.")
