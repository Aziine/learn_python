import math

def main_function():
    def calc(k):

        functions = ['sin', 'cos', 'tan', 'sqrt', 'pi']

        for i in functions:
            if i in k.lower():
                withmath = 'math.' + i
                k = k.replace(i, withmath)

                try:
                    k = eval(k)
                    
