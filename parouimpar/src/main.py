import flet as ft


def main(page: ft.Page):
    # --- eventlistner
    def colose_dialog(e):
        page.pop_dialog(),
        page.update(),
    
    def on_click_send(e):
        value = input_txt.value
        try:
            int_value= int(value)
            output_txt = ft.Text(value ='')
            if(int_value % 2 == 0):
                output_txt.value = (f'{int_value} é par')
                
            else:
                output_txt.value = (f'{int_value} é impar')
            output_col.controls.append(output_txt)
        
        except ValueError:
            if(value.strip() == ''):
                dialog.content.value = 'O campo esta vazio.'
            else:
                dialog.content.value = f'"{value}" não é um valor inteiro'    
            page.show_dialog(dialog)
        input_txt.value = ''
        page.update
    # ----Widgets 
    dialog = ft.AlertDialog(
        title=ft.Text('Erro'),
        content=ft.Text('Mensagem erro'),
        actions=[
            ft.TextButon('Fechar')
        ]
    )
    input_txt = ft. TextField(
        expand=True,
        hint_text='Digite um numero.....')
    
    input_btn= ft.IconButton( 
        icon=ft.Icons.SEND,
        on_click = on_click_send)


    output_txt = ft.Text(value = '')

    # ----- Layout
    input_row = ft.Row(
        controls=[input_txt, input_btn]
    )

    output_col = ft.Column(
        expand=True,
        horizontal_aligmnts = ft.CrossAxisAlignment.STRETCH,
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        controls= []
    )

    main_col = ft.Column(
        controls = [input_row, output_col]
    )
  
    # ----- Página
    page.title = 'ParOuImparApp ' 
    page.add(main_col)

if __name__ == "__main__":
    ft.run(main)
