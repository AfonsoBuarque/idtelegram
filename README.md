# Telegram Group Cloner

Este script em Python utiliza a biblioteca [Telethon](https://github.com/LonamiWebs/Telethon) para clonar mensagens de texto e mídias de um grupo do Telegram para outro. Ele é ideal para quem deseja migrar ou fazer backup do conteúdo de grupos. 

## 🛠️ **Funcionalidades**

- Reenvia **mensagens de texto** de um grupo para outro.
- Faz o download de **mídias** (como fotos, vídeos e documentos) e as envia para o grupo de destino.
- Suporta grupos públicos e privados (desde que a conta tenha permissão de acesso).
- Inclui tratamento para evitar erros, como mensagens muito longas ou falta de permissão nos grupos.
- Adiciona um pequeno atraso entre os envios para evitar limitações de taxa (**rate limit**) do Telegram.
- Relatório final com o número total de mensagens e mídias processadas.

## 🚀 **Como Usar**

### **Pré-requisitos**
1. Python 3.7+ instalado.
2. Instale a biblioteca **Telethon**:
   ```bash
   pip install telethon
   ```
3. Crie suas credenciais de API no [my.telegram.org](https://my.telegram.org):
   - **API ID** e **API Hash**.

### **Configuração**
1. Adicione suas credenciais como variáveis de ambiente para maior segurança:
   ```bash
   export TELEGRAM_API_ID=seu_api_id
   export TELEGRAM_API_HASH=seu_api_hash
   ```
2. No script, configure os seguintes parâmetros:
   - **source_group**: ID ou username do grupo de origem.
   - **destination_group**: ID ou username do grupo de destino.

### **Execução**
Execute o script no terminal:
```bash
python nome_do_arquivo.py
```

## 🔍 **Detalhes Técnicos**

- **Diretório Temporário**: O script cria um diretório chamado `temp_midias` para salvar mídias temporariamente antes de enviá-las para o grupo de destino. Esse diretório é limpo automaticamente após o envio.
- **Mensagens Longas**: O Telegram tem um limite de 4096 caracteres por mensagem. O script ignora mensagens que excedem esse limite.
- **Rate Limit**: Para evitar bloqueios, o script adiciona um atraso de 0,5 segundos entre os envios.

## ⚠️ **Atenção**
- Certifique-se de que a conta utilizada no script tenha permissão para acessar ambos os grupos.
- Não compartilhe suas credenciais de API publicamente.
- O script foi projetado para uso pessoal ou com autorização. Certifique-se de cumprir as políticas de uso do Telegram.

## 📜 **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).
