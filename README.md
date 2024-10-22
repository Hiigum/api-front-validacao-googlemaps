
# Validador de API Key do Google Maps 🌍🔑

Este projeto é uma aplicação web desenvolvida com **FastAPI** e **JavaScript**, que permite aos usuários validarem suas chaves da API do Google Maps. A validação é feita em tempo real, verificando se a chave fornecida é válida ou não.

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework Python moderno para construir APIs rápidas e eficientes.
- **Uvicorn**: Servidor ASGI leve e rápido, usado para rodar a aplicação FastAPI.
- **Requests**: Biblioteca HTTP Python para fazer requisições para a API do Google Maps.
- **Jinja2**: Motor de templates utilizado para renderizar HTML dinâmico no lado do servidor.
- **Pydantic**: Validação de dados para entradas e saídas, garantindo que as solicitações à API estejam no formato correto.
- **HTML/CSS**: Estrutura e estilização da interface do usuário.
- **JavaScript**: Usado para interações assíncronas com o backend e validação no frontend.

---

## 🚀 Funcionalidades

- ✅ Validação da chave da API do Google Maps.
- 📡 Comunicação assíncrona entre o frontend e o backend usando `fetch` API.
- 🎨 Interface simples e responsiva para uma melhor experiência do usuário.

---

## 👓 Verifique na Vercel

- [Vercel](https://api-front-validacao-googlemaps.vercel.app/)

---

## ⚙️ Como Rodar o Projeto Localmente

Siga estas etapas para rodar o projeto localmente:

### 1. Clonar o Repositório
```bash
git clone https://github.com/Hiigum/api-front-validacao-googlemaps.git
cd api-front-validacao-googlemaps
```

### 2. Configurar o Ambiente Virtual
Recomenda-se usar um ambiente virtual para gerenciar as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar Dependências
Certifique-se de que todas as dependências estejam instaladas, utilizando o arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Rodar o Servidor Localmente
Execute o servidor com o `uvicorn` para iniciar a aplicação:
```bash
uvicorn api.index:app --reload
```
A aplicação estará rodando em: `http://127.0.0.1:8000/`

---

## 🌍 Implantando na Vercel

Para implantar o projeto na [Vercel](https://vercel.com), siga estas instruções:

### 1. Configurar o Arquivo `vercel.json`
O arquivo `vercel.json` deve estar na raiz do projeto, contendo a seguinte configuração:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

### 2. Instalar a CLI da Vercel
Se ainda não tiver a Vercel CLI instalada, você pode instalar com o seguinte comando:
```bash
npm install -g vercel
```

### 3. Deploy
Dentro da pasta do seu projeto, execute:
```bash
vercel
```
Siga as instruções no terminal para completar o deploy.

---

## 📂 Estrutura do Projeto

```
/nome-do-repositorio
│
├── api/
│   ├── index.py               # Arquivo principal da API FastAPI
│   ├── requirements.txt       # Dependências do projeto
│   ├── static/                # Arquivos estáticos (CSS, JS)
│   ├── templates/             # Templates HTML
│
├── vercel.json                # Configurações da Vercel
├── README.md                  # Documentação do projeto
```

---

## 🔑 Como Funciona a Validação da Chave

A validação é realizada através de uma requisição para a API de Geocoding do Google Maps:

```python
def validar_chave_api(chave_api):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key={chave_api}"
    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        if 'error_message' in dados:
            return False, dados['error_message']
        return True, "Chave API válida!"
    else:
        return False, f"Erro na requisição: {resposta.status_code}"
```



