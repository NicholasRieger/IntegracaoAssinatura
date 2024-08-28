from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
from email.mime.text import MIMEText
import base64

# Caminho para o arquivo de chave JSON da sua conta de serviço (anonymizado)
ARQUIVO_CONTA_SERVICO = '/caminho/para/seu-arquivo-conta-servico.json'

# Escopos necessários para acessar as configurações do Gmail e Google Sheets
ESCOPOS = ['https://www.googleapis.com/auth/gmail.settings.basic',
           'https://www.googleapis.com/auth/gmail.settings.sharing',
           'https://www.googleapis.com/auth/spreadsheets.readonly',
           'https://www.googleapis.com/auth/gmail.send']

# ID da planilha do Google Sheets (anonymizado)
ID_PLANILHA = 'id-da-sua-planilha'
# Nome da aba dentro da planilha
NOME_FAIXA = 'Planilha1!A:E'  # ajuste o intervalo conforme necessário

# Carrega as credenciais da conta de serviço
credenciais = service_account.Credentials.from_service_account_file(
        ARQUIVO_CONTA_SERVICO, scopes=ESCOPOS)

# Cria o serviço para acessar a API do Google Sheets
servico_planilhas = build('sheets', 'v4', credentials=credenciais)

# Lê os dados da planilha
planilha = servico_planilhas.spreadsheets()
resultado = planilha.values().get(spreadsheetId=ID_PLANILHA,
                                  range=NOME_FAIXA).execute()
valores = resultado.get('values', [])

# Converte os dados para um DataFrame do pandas para facilitar a manipulação
df = pd.DataFrame(valores[1:], columns=valores[0])

try:
    for index, row in df.iterrows():
        nome = row['Apelido'].strip()
        ramal = row.get('Ramal', '').strip() if row.get('Ramal') else ''
        cargo = row['Cargo'].strip()
        email = row['E-mail-Corporativo'].strip()
        setor = row['Setor'].strip()

        # Cria a assinatura personalizada
        assinatura = f"""
            <table width="600px" style="border-spacing: 0;">
                <tr>
                    <td width="135" valign="center" style="padding: 0;">
                        <img src="https://seu-link-imagem.com/gif" alt="Logo da Empresa" style="width:150px; height: 70px; display: block;">
                    </td>
                    <td valign="top" style="padding-left: 6.5px; padding: 3;">
                        <img src="https://seu-link-imagem.com/linha" alt="Linha" style="width:17px; height: auto; float: left; margin-right: 6px; display: block;">
                        <div style="margin-left: 17px;">
                            <p style="font-size: 14px; margin: 5px;"><strong>{nome}</strong></p>
                            <p style="font-size: 12.5px; margin: 6px;">{cargo}</p>
                            <p style="font-size: 12.5px; margin: 6px;"><strong>Setor {setor}</strong></p>
                            <p style="font-size: 12.5px; margin: 6px;">(11) 99999-9999 {ramal}</p>
                        </div>
                        <div style="margin-top: 10px;">
                            <a href="https://seu-site-empresa.com" style="text-decoration: none;"><img src="https://seu-link-imagem.com/logo" alt="Logo da Empresa" style="width:34px; height: auto; margin-right: 14px; display: inline-block;"></a>
                            <a href="https://www.linkedin.com/company/sua-empresa" target="_blank" style="text-decoration: none;"><img src="https://seu-link-imagem.com/linkedin" alt="LinkedIn" style="width:34px; height: auto; margin-right: 12px; margin-top: 1.75px; display: inline-block;"></a>
                            <a href="https://www.instagram.com/sua-empresa/" target="_blank" style="text-decoration: none;"><img src="https://seu-link-imagem.com/instagram" alt="Instagram" style="width:34px; height: auto; margin-right: 7px; display: inline-block;"></a>
                        </div>
                    </td>
                </tr>
            </table>"""

        # Autentica para o usuário específico
        credenciais_delegadas = credenciais.with_subject(email)

        # Cria o serviço para acessar a API do Gmail
        servico_gmail = build('gmail', 'v1', credentials=credenciais_delegadas)

        # Define a assinatura para o usuário
        servico_gmail.users().settings().sendAs().patch(
            userId=email,
            sendAsEmail=email,
            body={'signature': assinatura}
        ).execute()

        print(f"Assinatura atualizada para {email}")

    # Enviar e-mail de confirmação
    def criar_mensagem(destinatario, assunto, texto_mensagem):
        mensagem = MIMEText(texto_mensagem)
        mensagem['to'] = destinatario
        mensagem['subject'] = assunto
        bruto = base64.urlsafe_b64encode(mensagem.as_bytes())
        return {'raw': bruto.decode()}

    # Credenciais para enviar o e-mail de notificação
    servico_notificacao = build('gmail', 'v1', credentials=credenciais)
    
    # Criando a mensagem
    mensagem_email = criar_mensagem(
        destinatario="notificacao@sua-empresa.com",
        assunto="Integração das assinaturas concluída",
        texto_mensagem="A integração foi concluída com sucesso e as assinaturas foram atualizadas."
    )
    
    # Enviando o e-mail
    credenciais_delegadas = credenciais.with_subject('integracao@sua-empresa.com')

    servico_gmail = build('gmail', 'v1', credentials=credenciais_delegadas)
    servico_gmail.users().messages().send(
        userId='integracao@sua-empresa.com',
        body=mensagem_email
    ).execute()

    print("E-mail de notificação enviado para notificacao@sua-empresa.com")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
