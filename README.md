# Gerador de Assinaturas de E-mail Automatizadas

Este projeto automatiza a criação e configuração de assinaturas de e-mail personalizadas para usuários em uma organização. Ele utiliza a API do Gmail para aplicar assinaturas em contas de e-mail a partir de dados fornecidos em um arquivo CSV.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens:

- Python 3.x instalado
- Biblioteca `google-auth` e `google-api-python-client` instaladas (`pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`)
- Uma conta de serviço Google com as permissões necessárias para acessar as configurações do Gmail
- **Configuração de delegação em todo o domínio para permitir que a conta de serviço gerencie as configurações de e-mail dos usuários**
- Um arquivo de chave JSON para a conta de serviço
- Um arquivo CSV contendo as informações de nome, e-mail, cargo, setor e ramal dos usuários

## Estrutura do Projeto

O projeto é composto por dois arquivos principais:

### 1. HTML para Assinatura de E-mail

Este arquivo define o modelo de assinatura de e-mail em HTML. Ele inclui placeholders que são substituídos por informações específicas de cada usuário (nome, cargo, setor, etc.). 

**Exemplo de uso:**
```html
<p style="font-size: 14px; margin: 5px;"><strong>{nome}</strong></p>
<p style="font-size: 12.5px; margin: 6px;">{cargo}</p>
<p style="font-size: 12.5px; margin: 6px;"><strong>Setor {setor}</strong></p>
<p style="font-size: 12.5px; margin: 6px;">(11) 4993-5200 {ramal}</p>
2. Script Python
Este script lê os dados de um arquivo CSV e utiliza a API do Gmail para aplicar as assinaturas personalizadas.

Principais funções:

Leitura do CSV: Lê as informações de nome, cargo, setor, e-mail e ramal dos usuários.
Criação da Assinatura: Gera o HTML da assinatura para cada usuário.
Autenticação e Aplicação: Autentica na conta de e-mail do usuário e aplica a assinatura gerada.

Configuração

Configuração do Ambiente:

Instale as dependências necessárias com:
bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Modificar o Script:

Substitua CAMINHO_PARA_ARQUIVO_JSON pelo caminho do seu arquivo de chave JSON.
Substitua CAMINHO_PARA_ARQUIVO_CSV pelo caminho do arquivo CSV com os dados dos usuários.
No HTML, substitua os placeholders (LINK_PARA_*, {nome}, {cargo}, etc.) pelos valores ou links apropriados.
Executar o Script:

Rode o script Python para aplicar as assinaturas:
python script.py

Ou use a extensão Code Runner no VSCode

Observações
Certifique-se de que a conta de serviço tenha as permissões necessárias para modificar as configurações do Gmail dos usuários.
Personalize o HTML conforme necessário para atender aos padrões visuais da sua organização.
Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.

Este README fornece uma visão geral básica de como configurar e utilizar o projeto. Para maiores detalhes, consulte a documentação oficial da API do Gmail.







