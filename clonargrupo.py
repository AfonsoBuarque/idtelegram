from telethon import TelegramClient
import os
import asyncio

# Credenciais da API do Telegram (obtenha em my.telegram.org)
api_id = 'api_id'         # Substitua pelo seu API ID
api_hash = 'api_hash'     # Substitua pelo seu API Hash
session_name = 'session_name' # Nome da sessão do Telethon

# Grupos de origem e destino
source_group = 'grupo de origem'    # Username ou ID do grupo de origem
destination_group = 'grupo de destino'  # Username ou ID do grupo de destino

# Diretório temporário para salvar mídias
temp_dir = 'temp_midias'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Função principal
async def clone_group():
    # Conecta ao cliente Telegram
    async with TelegramClient(session_name, api_id, api_hash) as client:
        print("✅ Conectado ao Telegram!")

        # Acesso aos grupos de origem e destino
        try:
            source_entity = await client.get_entity(source_group)
            dest_entity = await client.get_entity(destination_group)
            print(f"✅ Conectado ao grupo de origem: {source_group}")
            print(f"✅ Conectado ao grupo de destino: {destination_group}")
        except Exception as e:
            print(f"❌ Erro ao acessar os grupos: {e}")
            return
        
        print(f"📥 Clonando mensagens e mídias de '{source_group}' para '{destination_group}'...\n")

        # Contadores para progresso
        total_messages = 0
        total_media = 0

        # Itera sobre as mensagens do grupo de origem
        async for message in client.iter_messages(source_entity, reverse=True):
            try:
                total_messages += 1

                # Reenvia mensagens de texto
                if message.text:
                    if len(message.text) > 4096:
                        print(f"⚠️ Mensagem {message.id} é muito longa e será ignorada.")
                        continue
                    print(f"💬 Reenviando mensagem de texto {message.id}...")
                    await client.send_message(dest_entity, message.text)
                    await asyncio.sleep(0.5)  # Adicionando atraso para evitar rate limit

                # Reenvia mídias
                if message.media:
                    total_media += 1
                    print(f"📁 Reenviando mídia {total_media} da mensagem {message.id}...")
                    file_path = await message.download_media(file=temp_dir)  # Baixa a mídia temporariamente
                    await client.send_file(dest_entity, file_path)  # Envia a mídia ao grupo de destino
                    os.remove(file_path)  # Remove a mídia temporária após o envio
                    await asyncio.sleep(0.5)  # Adicionando atraso para evitar rate limit

            except Exception as e:
                print(f"❌ Erro ao processar mensagem {message.id}: {e}")

        # Relatório final
        print("\n🎉 Clonagem concluída!")
        print(f"🔢 Total de mensagens processadas: {total_messages}")
        print(f"📦 Total de mídias copiadas: {total_media}")

# Execução do script
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(clone_group())
