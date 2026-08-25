import flet as ft
    # lista de emojis que irão aparecer no app
    # essa lista pode ser ampliada , o aplicativo
EMOJIS =[ "a","b","c","d","e",]





IDX = 0 

def main(page:  ft.Page):
        # ------configurações da página
        #editar a titulo  da janela/aba do navegador/nome do app
        page.title = 'EmojiApp' 
        # alinha verticalmente o elemento (control) que foi inserido na página
        # ft.MainAxisAlignment.Center -> centralizada  o conteúdo verticalmente
        page.vertical_alignment = ft.MainAxisAlingnment.Center

        # ----- meus elementos (controls)
        # ft,.Text -> Elemento textual
        # parametro value deste  objeto contém o valor mostrado na tela
        input = ft.Text(value=EMOJIS[0], size=30)

# ----- função aninhada na main
        # Esta é  afunção que  é executada ao clicar em "btn"
        # A função é a  aninhada à main para que ela consiga acessar as variáveis
        # declaradas na função main (ex, variavel input).
        # A função acresce o valor de IDX para mostrar o próximo emoji da lista
        # O parâmetro "e" da função carrega informações sobre o evento.
        # é possivcel acessar a partir de "e" o elemento que sofreu o evento.
        def refresh_click(e):
            global IDX
            # Incrmento circular :
            #    * Acesce IDX em 1
            #   * Se IDX > tamanho de EMOJIS
            #     
            btn = e.contrl
            if btn.icon == ft.Icons.ARROW_RIGHT_SHARP:
                IDX = IDX + 1
            else:
                 IDX = IDX - 1




            IDX = (IDX + 1 ) % len(EMOJIS)

            input.value = EMOJIS[IDX]

        btn_left = ft.IconButton(ft.Icons.ARROW_LEFT_SHARP , on_click = refresh_click)
        btn_right = ft.IconButton(ft.Icons.ARROW_RIGHT_SHARP , on_click = refresh_click)

        row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                btn_left,
                input,
                btn_right,
            ]
        )
if __name__ == '__name__':

    ft.run(main)


        