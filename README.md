

# Gráfico de Sensor de Altura

Este projeto mostra os valores de um sensor de altura ao longo do tempo. <br>
Ele será utilizado para o evento Handson do Instituto Mauá de Tecnologia (IMT). <br>
Siga as instruções abaixo para configurar e executar o programa localmente.

## 1. Clonar o repositório

Primeiro, clone o repositório em sua máquina local:

```bash
git clone https://github.com/MatCMartins/handson.git
```

Navegue até o diretório do projeto:

```bash
cd diretorio
```

## 2. Criar um ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/MacOS**:
  ```bash
  source venv/bin/activate
  ```

## 3. Baixar bibliotecas necessárias

Com o ambiente virtual ativado, instale as bibliotecas necessárias a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Inserir variáveis de ambiente

Adicione as variáveis de ambiente necessárias. Crie um arquivo `.env` no diretório raiz do projeto e adicione suas chaves, como no exemplo abaixo:

```env
URL_IMAGEM=www.exemploimagem.com
TIPO_IMAGEM=jpeg
```

## 5. Iniciar o programa

Agora você pode iniciar o programa com o seguinte comando:

```bash
python main.py
```

Certifique-se de que o ambiente virtual esteja ativo sempre que for executar o programa.

