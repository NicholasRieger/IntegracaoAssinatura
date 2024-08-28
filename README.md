# Gerador de Assinaturas de E-mail Automatizadas

Este projeto automatiza a criação e configuração de assinaturas de e-mail personalizadas para usuários em uma organização. Ele utiliza a API do Gmail e do Google Sheets para aplicar assinaturas em contas de e-mail a partir de dados fornecidos em uma planilha do Google Sheets.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens:

- **Python 3.x instalado**
- **Bibliotecas necessárias instaladas**:

  ```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas

+ Uma conta de serviço Google com as permissões necessárias para acessar as configurações do Gmail e do Google Sheets
+ Configuração de delegação em todo o domínio para permitir que a conta de serviço gerencie as configurações de e-mail dos usuários
+ Um arquivo de chave JSON para a conta de serviço
+ Acesso a uma planilha do Google Sheets contendo as informações de nome, e-mail, cargo, setor e ramal dos usuários

# Estrutura do Projeto

O projeto é composto por dois arquivos principais:


1. **HTML para Assinatura de E-mail**
   
Este arquivo define o modelo de assinatura de e-mail em HTML. O HTML deve ser configurado com placeholders que serão substituídos pelas informações específicas de cada usuário. Os placeholders são:

```
{nome}: Nome completo do usuário
{cargo}: Cargo do usuário
{setor}: Setor do usuário
{ramal}: Ramal do usuário
```

Exemplo de placeholders no HTML:

```
<p style="font-size: 14px; margin: 5px;"><strong>{nome}</strong></p>
<p style="font-size: 12.5px; margin: 6px;">{cargo}</p>
<p style="font-size: 12.5px; margin: 6px;"><strong>{setor}</strong></p>
<p style="font-size: 12.5px; margin: 6px;">{ramal}</p>
```

2. **Script Python**

Este script lê os dados de uma planilha do Google Sheets e utiliza a API do Gmail para aplicar as assinaturas personalizadas.

**Principais funções**:

- Leitura da Planilha: Lê as informações de nome, cargo, setor, e-mail e ramal dos usuários.
- Criação da Assinatura: Gera o HTML da assinatura para cada usuário substituindo os placeholders pelas informações reais.
- Autenticação e Aplicação: Autentica na conta de e-mail do usuário e aplica a assinatura gerada.
- Notificação por E-mail: Envia um e-mail de confirmação quando a integração é concluída.

## Configuração

1. Configuração do Ambiente
Instale as dependências necessárias com:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```
2. Modificar o Script
- Substitua ARQUIVO_CONTA_SERVICO pelo caminho do seu arquivo de chave JSON.
- Substitua ID_PLANILHA pelo ID da sua planilha do Google Sheets.
- Substitua NOME_FAIXA pelo nome da aba e intervalo de células na sua planilha do Google Sheets (por exemplo, 'Planilha1!A:E').
- No HTML da assinatura, substitua os placeholders ({nome}, {cargo}, {setor}, {ramal}) pelos valores apropriados ou mantenha-os como estão se forem substituídos pelo script.

3. Executar o Script
Rode o script Python para aplicar as assinaturas:

```
python script.py
````

Ou use a extensão Code Runner no VSCode para executar o script.

# Notificação por E-mail

Após a conclusão da atualização das assinaturas, um e-mail de notificação é enviado para o endereço especificado (notificacao@sua-empresa.com). Este e-mail confirma que a integração foi realizada com sucesso e que todas as assinaturas foram atualizadas conforme o esperado.

**Configuração do Envio de E-mail**:

- Credenciais de Envio: Certifique-se de que as credenciais de autenticação usadas no script para enviar e-mails estão configuradas corretamente.

- Destinatário: O e-mail de notificação é enviado para notificacao@sua-empresa.com. Substitua este endereço conforme necessário para o seu caso.

- Conteúdo do E-mail: A mensagem de e-mail confirma que a integração foi realizada e pode ser ajustada conforme suas necessidades.

# Observações
- Certifique-se de que a conta de serviço tenha as permissões necessárias para modificar as configurações do Gmail dos usuários.
- Personalize o HTML conforme necessário para atender aos padrões visuais da sua organização.
- Verifique as configurações de delegação em todo o domínio para garantir que a conta de serviço tenha acesso para gerenciar as assinaturas de e-mail dos usuários.
  
# Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
