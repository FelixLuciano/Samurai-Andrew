from .. import load_assets

# Escopo do módulo
__g = globals()

# Varrega os assets a partir do diretório atual
for __name, __asset in load_assets(__file__).items():

    # Registra os assets no escopo do módulo
    __g[__name] = __asset
