import time

#criando o decorator
def medir_tempo_execucao(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"o TEMPO TOTAL DA FUNCAO FOI: {total_time}")
        return result
    return wrapper

@medir_tempo_execucao
def tarefa_1():
    print("Rodando a funcao...")
    time.sleep(3)
    print("Funcao finalizada")

@medir_tempo_execucao
def tarefa_2():
    print("Rodando a funcao...")
    time.sleep(2)
    print("Funcao finalizada")

tarefa_1()

tarefa_2()