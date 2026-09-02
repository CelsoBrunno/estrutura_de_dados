"""Aula 2 — PBL: reprodutor com lista duplamente encadeada."""


class Faixa:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None
        self.anterior = None


class ReprodutorStreaming:
    def __init__(self):
        self.faixa_atual = None

    def adicionar_na_fila(self, musica):
        nova = Faixa(musica)
        if self.faixa_atual is None:
            self.faixa_atual = nova
            print(f"Playlist iniciada: {musica}")
            return
        nova.anterior = self.faixa_atual
        nova.proximo = self.faixa_atual.proximo
        if self.faixa_atual.proximo:
            self.faixa_atual.proximo.anterior = nova
        self.faixa_atual.proximo = nova
        print(f"Faixa [{musica}] adicionada como próxima.")

    def proxima_faixa(self):
        if self.faixa_atual and self.faixa_atual.proximo:
            self.faixa_atual = self.faixa_atual.proximo
            print(f">> {self.faixa_atual.musica}")
        else:
            print(">> Fim da playlist.")

    def faixa_anterior(self):
        if self.faixa_atual and self.faixa_atual.anterior:
            self.faixa_atual = self.faixa_atual.anterior
            print(f"<< {self.faixa_atual.musica}")
        else:
            print("<< Início da playlist.")


if __name__ == "__main__":
    player = ReprodutorStreaming()
    player.adicionar_na_fila("Bohemian Rhapsody")
    player.adicionar_na_fila("Stairway to Heaven")
    player.adicionar_na_fila("Hotel California")
    player.proxima_faixa()
    player.proxima_faixa()
    player.proxima_faixa()
    player.faixa_anterior()
