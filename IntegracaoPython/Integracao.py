import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Caminho para o arquivo de chave JSON da sua conta de serviço
SERVICE_ACCOUNT_FILE = 'CAMINHO_PARA_ARQUIVO_JSON'

# Escopos necessários para acessar as configurações do Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic',
          'https://www.googleapis.com/auth/gmail.settings.sharing']

# Carrega as credenciais da conta de serviço
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Lê o CSV com as informações de email, nome e função
with open("CAMINHO_PARA_ARQUIVO_CSV", mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        email = row['Email'].strip()
        nome = row['Nome'].strip()
        cargo = row['Cargo'].strip()
        setor = row['Setor'].strip()
        ramal = row['Ramal'].strip()

        # Cria a assinatura personalizada
        signature = f"""
            <table width="100%">
                <tr>
                    <td width="135" valign="center">
                        <img src="LINK_PARA_IMAGEM_DO_LOGO" alt="Gif Liceu Jardim" style="width:175px; min-height: 70px;">
                    </td>
                    <td valign="top" style="padding-left: 5px;">
                        <img src="LINK_PARA_IMAGEM_DECORATIVA" alt="Linhas" style="width:16px; float: left; margin-right: 9.5px;">
                        <div>
                            <p style="font-size: 14px; margin: 5px;"><strong>{nome}</strong></p>
                            <p style="font-size: 12.5px; margin: 5px;">{cargo}</p>
                            <p style="font-size: 12.5px; margin: 5px;"><strong>Setor {setor}</strong></p>
                            <p style="font-size: 12.5px; margin: 5px;">(11) 4993-5200 {ramal}</p>
                        </div>
                        <a href="LINK_PARA_SITE_DA_EMPRESA"><img src="LINK_PARA_LOGO_SITE" alt="Logo Empresa" style="width:34px; margin-right: 12px;" ></a>
                        <a href="LINK_PARA_LINKEDIN" target="_blank" style="text-decoration: none;"><img src="LINK_PARA_LOGO_LINKEDIN" alt="LinkedIn" style="width:34px; margin-right: 12px; margin-top: 1.75px"></a>
                        <a href="LINK_PARA_INSTAGRAM" target="_blank" style="text-decoration: none;"><img src="LINK_PARA_LOGO_INSTAGRAM" alt="Instagram" style="width:34px; margin-right: 7px;"></a>
                    </td>
                </tr>
            </table>"""


        # Autentica para o usuário específico
        delegated_credentials = credentials.with_subject(email)

        # Cria o serviço para acessar a API do Gmail
        service = build('gmail', 'v1', credentials=delegated_credentials)

        # Define a assinatura para o usuário
        service.users().settings().sendAs().patch(
            userId=email,
            sendAsEmail=email,
            body={'signature': signature}
        ).execute()

        print(f"Assinatura atualizada para {email}")
