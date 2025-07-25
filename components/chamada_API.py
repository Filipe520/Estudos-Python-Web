from flask import Flask, render_template
import os
import requests

# Caminho absoluto até a pasta 'templates'
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
templates_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir )

@app.route('/')
def chamada_API():
    try:
        # Fazendo a requisição GET
        url = "https://api.thecatapi.com/v1/images/search"
        resposta = requests.get(url)
        dados = resposta.json() # Converte o JSOM para dicionário
        imagem_url = dados[0]["url"] # Pega a URL da imagem
        
        return render_template("index.html", imagem_url=imagem_url)
    except Exception as erro:
        return f"<h1>Erro ao carregar imagem do gato 😿</h1><p>{erro}</p>"

if __name__ == '__main__':
    print(f"Caminho para templates: {templates_dir}")
    app.run(debug=True)