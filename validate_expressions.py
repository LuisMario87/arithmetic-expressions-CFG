import json

# Cargar las reglas CFG
with open("C:\\Users\\luism\\OneDrive\\Documentos\\A. Tareas 7mo semestre\\Mat DIscretas\\ProyectoFinal\\codigo\\manual_rules.json") as rules_file:
    rules = json.load(rules_file)

productions = rules["productions"]

# Función para validar un token contra una producción
def validate(tokens, rule):
    if not tokens:
        return False, tokens

    if rule == "expr":
        valid, tokens = validate(tokens, "term")
        while tokens and tokens[0] in ["+", "-"]:
            tokens.pop(0)  # Consume el operador
            valid, tokens = validate(tokens, "term")
        return valid, tokens

    elif rule == "term":
        valid, tokens = validate(tokens, "factor")
        while tokens and tokens[0] in ["*", "/"]:
            tokens.pop(0)  # Consume el operador
            valid, tokens = validate(tokens, "factor")
        return valid, tokens

    elif rule == "factor":
        token = tokens.pop(0) if tokens else None
        if token == "(":
            valid, tokens = validate(tokens, "expr")
            if tokens and tokens[0] == ")":
                tokens.pop(0)  # Consume el paréntesis
                return valid, tokens
            return False, tokens
        elif token.isdigit() or token.isalnum():  # Número o identificador
            return True, tokens
        return False, tokens

    return False, tokens

# Función principal para validar expresiones
def validate_expression(expr):
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    valid, remaining_tokens = validate(tokens, "expr")
    return valid and not remaining_tokens
