import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        
        self.resultado = tk.StringVar()
        self.entrada = tk.Entry(
            master,
            textvariable=self.resultado,
            font=("Arial", 24),
            bd=10,
            insertwidth=2,
            width=14,
            borderwidth=4,
            justify='right'
        )
        self.entrada.grid(row=0, column=0, columnspan=4)
        
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]
        
        fila = 1
        col = 0
        for boton in botones:
            tk.Button(
                master, 
                text=boton,
                padx=20,
                pady=20,
                font=("Arial", 18),
                command=lambda b=boton: self.presionar_boton(b)
            ).grid(row=fila, column=col)
            col += 1
            if col > 3:
                col = 0
                fila += 1
        
        
        tk.Button(
            master,
            text='=',
            padx=20,
            pady=20,
            font=("Arial", 18),
            command=self.calcular
        ).grid(row=fila, column=0, columnspan=4)
        
        
        master.bind("<Key>", self.manejar_teclado)
        self.entrada.focus_set()
    
    def presionar_boton(self, caracter):
        if caracter == 'C':
            self.limpiar()
        else:
            posicion = self.entrada.index(tk.INSERT)
            self.entrada.insert(posicion, caracter)
        self.entrada.focus_set()
    
    def manejar_teclado(self, event):
        
        if event.char in '0123456789+-*/.':
            return 
            
        elif event.keysym == 'Return' or event.char == '=':
            self.calcular()
            
        elif event.keysym == 'Escape':
            self.limpiar()
            
        elif event.keysym == 'BackSpace':
            posicion = self.entrada.index(tk.INSERT)
            if posicion > 0:
                self.entrada.delete(posicion-1)
        
        self.entrada.focus_set()
        return "break"  
    
    def calcular(self):
        try:
            expresion = self.entrada.get()
            if expresion:
                resultado = str(eval(expresion))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Error")
        finally:
            self.entrada.focus_set()
    
    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.entrada.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
