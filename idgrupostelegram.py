from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Substitua pelos dados da sua conta do Telegram
api_id = 'api_id'         # Substitua pelo seu API ID
api_hash = 'api_hash'     # Substitua pelo seu API Hash
session_name = 'buscar_id' # Nome da sessão do Telethon

# ID do grupo ou canal que você quer pesquisar
group_id = '@clonefonh'  # Ou o ID numérico do grupo, por exemplo: 123456789

# Criação do cliente do Telethon
client = TelegramClient('session_name', api_id, api_hash)

# Função para buscar o grupo pelo ID
async def get_group_by_id(group_id):
    try:
        # Conectando ao cliente
        await client.start()

        # Buscando o grupo pelo ID
        group = await client.get_entity(group_id)
        
        # Exibindo as informações do grupo
        print(f'Grupo encontrado! Nome: {group.title}')
        print(f'ID do grupo: {group.id}')
        print(f'Link do grupo: {group.username if group.username else "Não tem username"}')
        
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Executando a função
with client:
    client.loop.run_until_complete(get_group_by_id(group_id))
