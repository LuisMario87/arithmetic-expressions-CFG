from validate_expressions import validate_expression

# Lista de casos de prueba
test_cases = {
    "valid": ["3 + 5", "x * (y - z)", "(3 + 2) / 4", "a - b * c"],
    "invalid": ["3 +", "x * (y -", "( 3 + 2", "a + b -"]
}

# Ejecutar pruebas
for category, cases in test_cases.items():
    print(f"\n{category.upper()} CASES:")
    for expr in cases:
        result = "Válido" if validate_expression(expr) else "Inválido"
        print(f"{expr}: {result}")
