import tkinter as tk

def calcular_hba1c():
    try:
        glicose = int(entrada_glicose.get())
        media = glicose + 46.7
        resultado = media / 28.7
        resultado_label.config(text=f"Sua HbA1c é: {resultado:.1f}")

        if resultado <= 5.6:
            avaliacao_label.config(text="Sua glicose encontra-se dentro da normalidade.")
        else:
            avaliacao_label.config(text="Você precisa controlar sua glicose.")
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor numérico válido.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de HbA1c")

# Rótulo para o campo de entrada
rotulo_glicose = tk.Label(janela, text="Digite a média da sua glicose:")
rotulo_glicose.pack()

# Campo de entrada para a glicose
entrada_glicose = tk.Entry(janela)
entrada_glicose.pack()

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular HbA1c", command=calcular_hba1c)
botao_calcular.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Rótulo para exibir a avaliação
avaliacao_label = tk.Label(janela, text="")
avaliacao_label.pack()

janela.mainloop()