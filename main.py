import requests
import pandas as pd

municipios = []

api_return = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome', timeout=2.50)

for city in api_return.json():
    # print(line)
    if city["microrregiao"]["mesorregiao"]["UF"]["sigla"] == "SC":
        municipios.append(
            (
                city["id"],
                city["nome"],
                city["microrregiao"]["mesorregiao"]["nome"],
                city["microrregiao"]["mesorregiao"]["UF"]["sigla"],
                city["microrregiao"]["mesorregiao"]["UF"]["nome"]
             ))

df = pd.DataFrame(municipios, columns=['UNIQUE_ID', 'NOME', 'REGIAO', 'UF', 'ESTADO'])
df.sort_values(by=['REGIAO'], inplace=True)
compression_opts = dict(method='zip', archive_name='out.csv')
df.to_csv('out.zip', index=False, compression=compression_opts)