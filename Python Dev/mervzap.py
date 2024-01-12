# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


# produto = {
#     "nome": "iphone",
#     "preço": 6500,
#     "quantidade": 150    
# }

# produto["quantidade"]

import flet as ft

def main(pagina):
    titulo = ft.Text("Mervzap")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
       chat.controls.append(ft.Text(informacoes))
       pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"

        chat.controls.append(ft.Text(texto_campo_mensagem))

        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""
        pagina.update()    
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", 
                                  on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):

        popup.open = False

        pagina.remove(botao_enviar)

        pagina.add(chat)

        linha_mensagem = ft.Row(
            {campo_mensagem, botao_enviar}
        )
        pagina.add(linha_mensagem)

        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Mervzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )    
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_enviar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_enviar)

ft.app(main, view=ft.WEB_BROWSER)


    