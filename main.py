import customtkinter as ctk
from lib import calcular_soma, verificar_fibonacci, calcular_faturamento, calcular_percentual, inverter_string

# Configuração principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
largura = 800
altura = 600

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela / 2) - (largura / 2)
y = (altura_tela / 2) - (altura / 2)

app.geometry(f'{largura}x{altura}+{int(x)}+{int(y)}')

app.title("Desafio Target Sistemas")

# Funções para manipular botões
def mostrar_resultado(resultado):
    output_label.configure(text=resultado)

def executar_calcular_soma():
    resultado = calcular_soma()
    mostrar_resultado(resultado)

def executar_verificar_fibonacci():
    input_text = input_field.get()
    if input_text.isdigit():
        resultado = verificar_fibonacci(int(input_text))
    else:
        resultado = "Por favor, insira um número válido."
    mostrar_resultado(resultado)

def executar_calcular_faturamento():
    resultado = calcular_faturamento()
    mostrar_resultado(resultado)

def executar_calcular_percentual():
    resultado = calcular_percentual()
    mostrar_resultado(resultado)

def executar_inverter_string():
    input_text = input_field.get()
    if input_text.strip():
        resultado = inverter_string(input_text)
    else:
        resultado = "O campo de texto está vazio."
    mostrar_resultado(resultado)

# Layout principal
main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Menu lateral
menu_frame = ctk.CTkFrame(main_frame, width=200, corner_radius=10)
menu_frame.pack(side="left", fill="y", padx=10, pady=10)

menu_label = ctk.CTkLabel(menu_frame, text="Menu", font=("Arial", 18, "bold"))
menu_label.pack(pady=10)

btn_soma = ctk.CTkButton(menu_frame, text="Calcular Soma", command=executar_calcular_soma, width=150)
btn_soma.pack(pady=5)

btn_fibonacci = ctk.CTkButton(menu_frame, text="Verificar Fibonacci", command=executar_verificar_fibonacci, width=150)
btn_fibonacci.pack(pady=5)

btn_faturamento = ctk.CTkButton(menu_frame, text="Calcular Faturamento", command=executar_calcular_faturamento, width=150)
btn_faturamento.pack(pady=5)

btn_percentual = ctk.CTkButton(menu_frame, text="Calcular Percentual", command=executar_calcular_percentual, width=150)
btn_percentual.pack(pady=5)

btn_inverter = ctk.CTkButton(menu_frame, text="Inverter Texto", command=executar_inverter_string, width=150)
btn_inverter.pack(pady=5)

btn_sair = ctk.CTkButton(menu_frame, text="Sair", command=app.quit, fg_color="red", width=150)
btn_sair.pack(pady=100)

# Área principal
content_frame = ctk.CTkFrame(main_frame, corner_radius=10)
content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

header_label = ctk.CTkLabel(content_frame, text="Desafio Proposto", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

input_label = ctk.CTkLabel(content_frame, text="\nEntrada de Fibonacci e inverter texto\n\n escreva abaixo:", font=("Arial", 15))
input_label.pack(pady=5)

input_field = ctk.CTkEntry(content_frame, placeholder_text="Insira aqui...", font=("Arial", 15), width=400)
input_field.pack(pady=5)

output_label = ctk.CTkLabel(content_frame, text="", font=("Arial", 30), justify="left", wraplength=500)
output_label.pack(pady=40)

# Loop principal

if __name__ == "__main__":
   app.mainloop()
