# Capivara 🦫

Um chatbot interativo construído com Python, Streamlit e a API da OpenAI. Este projeto demonstra como integrar modelos de linguagem em uma interface web simples e gerenciar o histórico de conversas usando o estado de sessão (`session_state`) do Streamlit.

## 🚀 Funcionalidades

* Interface de chat limpa e amigável.
* Integração direta com a API da OpenAI.
* Retenção de histórico de mensagens durante a sessão do usuário.
* Estrutura segura para ocultação de chaves de API.

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)** - Linguagem principal.
* **[Streamlit](https://streamlit.io/)** - Framework para criação da interface web.
* **[OpenAI API](https://platform.openai.com/)** - Integração com o modelo de inteligência artificial.

## 📋 Pré-requisitos

Antes de começar, você precisará ter o Python instalado na sua máquina (versão 3.8 ou superior) e uma conta na OpenAI para gerar a sua própria API Key.

## 🔧 Como rodar o projeto localmente

1. **Clone este repositório**
2. **Crie um ambiente virtual (Opcional, mas recomendado)**:
     python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
3. **Instale as dependências**: pip install streamlit openai
4. **Configure a sua Chave da API (OpenAI)**
   
   * Por questões de segurança, a API Key não está inclusa no código. Para o app funcionar, você precisa configurar a sua própria chave:
    1. Crie uma pasta oculta chamada .streamlit na raiz do projeto.
    2. Dentro dela, crie um arquivo chamado secrets.toml.
    3. Adicione a sua chave no arquivo seguindo o modelo abaixo:
    4. OPENAI_API_KEY = "sk-sua-chave-api-aqui"
5. **Execute a aplicação**: streamlit run IA.py
