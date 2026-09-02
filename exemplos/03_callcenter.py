"""Aula 3 — PBL: Call Center (fila + pilha)."""

from collections import deque


class CallCenter:
    def __init__(self):
        self.fila_espera = deque()  # Fila: quem chega
        self.historico_acoes = []  # Pilha: desfazer (Ctrl+Z)

    def novo_cliente(self, nome):
        self.fila_espera.append(nome)
        print(f"[Entrada] Cliente {nome} entrou na fila de espera.")

    def atender_proximo(self):
        if len(self.fila_espera) > 0:
            cliente_atendido = self.fila_espera.popleft()  # O(1) — remove do início
            self.historico_acoes.append(cliente_atendido)
            print(f"[Atendimento] Atendendo cliente: {cliente_atendido}")
        else:
            print("[Atendimento] A fila de espera está vazia.")

    def desfazer_encerramento(self):
        if len(self.historico_acoes) > 0:
            cliente_recuperado = self.historico_acoes.pop()  # O(1) — remove do fim
            self.fila_espera.appendleft(cliente_recuperado)
            print(f"[Desfazer] Erro! O cliente {cliente_recuperado} foi devolvido ao início da fila.")
        else:
            print("[Desfazer] Não há ações recentes para desfazer.")

    def mostrar_painel(self):
        print(f"\nPainel - Fila atual: {list(self.fila_espera)}")
        print("-" * 30)


if __name__ == "__main__":
    sistema = CallCenter()
    sistema.novo_cliente("João")
    sistema.novo_cliente("Maria")
    sistema.novo_cliente("Carlos")
    sistema.mostrar_painel()
    sistema.atender_proximo()
    sistema.atender_proximo()
    sistema.mostrar_painel()
    sistema.desfazer_encerramento()
    sistema.mostrar_painel()
    sistema.atender_proximo()
