# scope local
# todo el cuerpo de la funcion
# solo son visibles desde el cuespor de la estrucutura

nombre="edwin"
def func():
    num=10
    def func2():
        num2=20
        print(num2)
        print(num)
        print(locals())
    func2()
func()

print(globals())

# scope global se puede acceder desde cualquier lugar
# scope por default se carga por defecto cuando ejecutamos python 